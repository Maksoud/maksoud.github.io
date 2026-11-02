"""Tutor de ITIL 4: RAG sobre as notas da pasta "ITIL 4" do vault.

Uso:
    pip install -r requirements.txt
    set ANTHROPIC_API_KEY=...        (Windows cmd)  |  $env:ANTHROPIC_API_KEY="..." (PowerShell)

    python tutor_itil.py indexar               # cria/atualiza o banco vetorial
    python tutor_itil.py perguntar "Quais são os princípios orientadores?"
    python tutor_itil.py simulado "service value chain" --n 3
    python tutor_itil.py avaliar --n 20        # testa contra o gabarito (arquivo de Q&A)
    python tutor_itil.py chat                  # modo interativo
"""
import argparse
import pathlib
import random
import re
import sys

import anthropic
import chromadb
from chromadb.utils import embedding_functions

AQUI = pathlib.Path(__file__).resolve().parent
PASTA_ITIL = AQUI.parents[2] / "ITIL 4"
GABARITO = "Q&A - ITIL 4 Foundation - Exam preparation.md"
MODELO_LLM = "claude-sonnet-5-5"
MODELO_EMB = "paraphrase-multilingual-MiniLM-L12-v2"

# ---------- 1. Documentos + 2. Chunking ----------

def gerar_chunks():
    """Quebra cada nota pelos títulos (##, ###, ####). O Q&A fica de fora: é o gabarito."""
    for arq in sorted(PASTA_ITIL.rglob("*.md")):
        if arq.name == GABARITO:
            continue
        texto = arq.read_text(encoding="utf-8")
        for i, parte in enumerate(re.split(r"\n(?=#{2,4} )", texto)):
            parte = parte.strip()
            if len(parte) < 50:
                continue
            titulo = parte.splitlines()[0].lstrip("# ").strip()
            yield f"{arq.parent.name}/{arq.stem}#{i}", parte, {
                "arquivo": arq.stem, "pasta": arq.parent.name, "titulo": titulo}

# ---------- 3. Embeddings + 4. Vector Database ----------

def colecao():
    emb = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODELO_EMB)
    db = chromadb.PersistentClient(path=str(AQUI / "itil_db"))
    return db.get_or_create_collection("itil4", embedding_function=emb)

def indexar():
    col = colecao()
    ids, docs, metas = zip(*gerar_chunks())
    col.upsert(ids=list(ids), documents=list(docs), metadatas=list(metas))
    print(f"{len(ids)} trechos indexados de {PASTA_ITIL}")

# ---------- 5. Retrieval ----------

def recuperar(col, pergunta, k):
    r = col.query(query_texts=[pergunta], n_results=k)
    return list(zip(r["documents"][0], r["metadatas"][0]))

def montar_contexto(trechos):
    return "\n\n".join(f"[{m['arquivo']}]\n{d}" for d, m in trechos)

# ---------- 6. Prompt + 7. LLM ----------

SISTEMA = ("Você é um tutor para a prova ITIL 4 Foundation. Use SOMENTE o contexto fornecido. "
           "Cite entre colchetes o nome da nota de origem. Se o contexto não tiver a resposta, "
           "diga que não encontrou no material. Responda em português.")

_cliente = None

def llm(prompt, max_tokens=1000):
    global _cliente
    _cliente = _cliente or anthropic.Anthropic()
    msg = _cliente.messages.create(model=MODELO_LLM, max_tokens=max_tokens, system=SISTEMA,
                                   messages=[{"role": "user", "content": prompt}])
    return msg.content[0].text

def perguntar(col, pergunta, k=5):
    trechos = recuperar(col, pergunta, k)
    print(llm(f"Contexto:\n{montar_contexto(trechos)}\n\nPergunta: {pergunta}"))
    print("\nTrechos recuperados:")
    for _, m in trechos:
        print(f"  - {m['arquivo']} > {m['titulo']}")

def simulado(col, tema, n=3, k=6):
    trechos = recuperar(col, tema, k)
    prompt = (f"Contexto:\n{montar_contexto(trechos)}\n\n"
              f"Com base no contexto, crie {n} questões de múltipla escolha sobre \"{tema}\", "
              "no estilo da prova ITIL 4 Foundation, cada uma com 4 alternativas (A a D). "
              "Liste todas as questões primeiro. Depois, numa linha só com a palavra GABARITO, "
              "indique a alternativa correta de cada uma, com explicação curta e a nota de origem.")
    texto = llm(prompt, max_tokens=2000)
    perguntas, _, gabarito = texto.partition("GABARITO")
    print(perguntas.strip())
    input("\nPressione Enter para ver o gabarito...")
    print("GABARITO" + gabarito)

# ---------- Avaliação com o gabarito ----------

def carregar_gabarito():
    """Lê o Q&A: cada bloco tem 'Questions for Section X' e depois 'Answers', numerados."""
    texto = (PASTA_ITIL / GABARITO).read_text(encoding="utf-8")
    itens = []
    for bloco in re.split(r"\n(?=### Questions for Section)", texto):
        cab = re.search(r"Questions for Section ([\d.]+)", bloco)
        if not cab or "### Answers" not in bloco:
            continue
        perg_txt, resp_txt = bloco.split("### Answers", 1)
        pergs = dict(re.findall(r"^(\d+)\. (.+)$", perg_txt, re.M))
        resps = dict(re.findall(r"^(\d+)\. (.+)$", resp_txt, re.M))
        for num, p in pergs.items():
            if num in resps:
                itens.append({"secao": cab.group(1).rstrip("."), "pergunta": p,
                              "esperado": resps[num]})
    return itens

def avaliar(col, n=20, k=5, semente=42):
    itens = carregar_gabarito()
    random.seed(semente)
    amostra = random.sample(itens, min(n, len(itens)))
    acertos = 0
    for i, it in enumerate(amostra, 1):
        trechos = recuperar(col, it["pergunta"], k)
        achou = any(m["arquivo"].startswith(it["secao"] + " ") for _, m in trechos)
        acertos += achou
        resposta = llm(f"Contexto:\n{montar_contexto(trechos)}\n\nPergunta: {it['pergunta']}",
                       max_tokens=400)
        print(f"\n=== {i}. [Seção {it['secao']}] {it['pergunta']}")
        print(f"Retrieval achou a nota da seção? {'SIM' if achou else 'NÃO'}")
        print(f"Esperado: {it['esperado']}")
        print(f"Tutor:    {resposta}")
    print(f"\nRetrieval: {acertos}/{len(amostra)} perguntas recuperaram a nota da seção correta.")
    print("Compare 'Esperado' x 'Tutor' para avaliar a geração.")

# ---------- CLI ----------

def chat(col, k):
    print("Tutor ITIL 4. Digite a pergunta, '/simulado <tema>' ou 'sair'.")
    while True:
        try:
            linha = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if linha.lower() in {"sair", "exit", "quit"}:
            break
        if linha.startswith("/simulado"):
            simulado(col, linha[len("/simulado"):].strip() or "ITIL 4")
        elif linha:
            perguntar(col, linha, k)

def main():
    ap = argparse.ArgumentParser(description="Tutor de ITIL 4 (RAG)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("indexar")
    p = sub.add_parser("perguntar"); p.add_argument("pergunta"); p.add_argument("--k", type=int, default=5)
    s = sub.add_parser("simulado"); s.add_argument("tema"); s.add_argument("--n", type=int, default=3)
    a = sub.add_parser("avaliar"); a.add_argument("--n", type=int, default=20); a.add_argument("--k", type=int, default=5)
    c = sub.add_parser("chat"); c.add_argument("--k", type=int, default=5)
    args = ap.parse_args()

    if args.cmd == "indexar":
        return indexar()
    col = colecao()
    if col.count() == 0:
        print("Banco vazio, indexando primeiro...")
        indexar()
    if args.cmd == "perguntar":
        perguntar(col, args.pergunta, args.k)
    elif args.cmd == "simulado":
        simulado(col, args.tema, args.n)
    elif args.cmd == "avaliar":
        avaliar(col, args.n, args.k)
    elif args.cmd == "chat":
        chat(col, args.k)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
