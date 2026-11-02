[← Voltar para o Plano de estudos: 10 dias de imersão em GenAI](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai-2/)

# Dia 5: Construir seu primeiro RAG

Aqui eu faria uma pausa total na teoria.

Você vai construir.

### Projeto

Pegue **10: 30 documentos reais**.

Pode ser:
- documentação técnica;
- PDFs;
- artigos;
- documentos sobre sua área profissional;
- documentação de uma empresa;
- documentação de uma ferramenta.

Construa:

> **“Chat com meus documentos”**

Arquitetura:

```
             DOCUMENTOS
                  ↓
              Chunking
                  ↓
              Embeddings
                  ↓
           Vector Database
                  ↓
               Retrieval
                  ↓
          Contexto recuperado
                  ↓
                Prompt
                  ↓
                 LLM
                  ↓
               Resposta
```

Não tente criar uma aplicação bonita.

A finalidade é **entender cada etapa**.

---

### Projeto escolhido: Tutor de ITIL 4

Como base de documentos, vou usar as notas da pasta [ITIL 4](https://correiarodrigues.com.br/notas/itil-4/itil-4/). São 31 arquivos em Markdown (capítulos, resumos e um banco de perguntas e respostas), exatamente o tamanho sugerido para o exercício.

O objetivo é ter um assistente que ajude a estudar para a prova **ITIL 4 Foundation**, respondendo **apenas com base nesse material** e mostrando de qual nota veio cada resposta.

#### O que o tutor deve fazer

- **Responder perguntas**: "Qual a diferença entre utilidade e garantia?", citando a nota de origem.
- **Gerar simulados**: criar questões de múltipla escolha sobre um tema (ex.: princípios orientadores), no estilo da prova.
- **Corrigir respostas**: o usuário responde, o tutor diz se está certo e explica usando o trecho recuperado.
- **Admitir quando não sabe**: se o assunto não estiver nas notas, dizer isso em vez de inventar.

#### Como cada etapa se aplica ao material

| Etapa | Decisão no projeto |
|---|---|
| Documentos | `Chapters/`, `Summaries/`, `ITIL 4.md` e `Summary of ITIL 4 Foundation.md` |
| Chunking | Quebrar por títulos (`###`, `####`), porque cada seção trata de um conceito. Guardar no metadado o arquivo e o título |
| Embeddings | Um modelo multilíngue (ex.: `paraphrase-multilingual-MiniLM-L12-v2`), já que as notas estão em inglês e as perguntas podem ser em português |
| Vector Database | ChromaDB local, sem servidor |
| Retrieval | Buscar os 4 ou 5 trechos mais parecidos com a pergunta |
| Prompt | Instruir o LLM a responder só com o contexto, citar a fonte e responder em português |
| LLM | Qualquer modelo via API (Claude, GPT etc.) |

#### Separar o gabarito

O arquivo `Q&A - ITIL 4 Foundation - Exam preparation.md` tem centenas de perguntas com respostas e página do livro. Ele **não entra no índice**: vira o conjunto de teste.

Assim dá para medir o RAG de verdade:
- sortear 20 perguntas do Q&A;
- comparar a resposta do tutor com a resposta do gabarito;
- verificar se o trecho recuperado era da seção certa (ex.: pergunta da seção 4.3 deveria recuperar a nota `4.3 The ITIL guiding principles`).

Se a resposta estiver errada, a pergunta passa a ser: **o erro foi no retrieval ou na geração?** Essa é a principal lição do dia.

#### Esqueleto em Python

~~~python
# pip install chromadb sentence-transformers anthropic
import re, pathlib, chromadb
from chromadb.utils import embedding_functions
import anthropic

PASTA = pathlib.Path("ITIL 4")
GABARITO = "Q&A - ITIL 4 Foundation - Exam preparation.md"

# 1. Documentos + 2. Chunking por títulos
def chunks():
    for arq in PASTA.rglob("*.md"):
        if arq.name == GABARITO:
            continue
        texto = arq.read_text(encoding="utf-8")
        for i, parte in enumerate(re.split(r"\n(?=#{2,4} )", texto)):
            if len(parte.strip()) > 50:
                titulo = parte.strip().splitlines()[0]
                yield f"{arq.stem}-{i}", parte, {"arquivo": arq.stem, "titulo": titulo}

# 3. Embeddings + 4. Vector Database
emb = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2")
db = chromadb.PersistentClient(path="itil_db")
col = db.get_or_create_collection("itil4", embedding_function=emb)
ids, docs, metas = zip(*chunks())
col.upsert(ids=list(ids), documents=list(docs), metadatas=list(metas))

# 5. Retrieval + 6. Prompt + 7. LLM
cliente = anthropic.Anthropic()

def perguntar(pergunta, k=5):
    r = col.query(query_texts=[pergunta], n_results=k)
    contexto = "\n\n".join(
        f"[{m['arquivo']}]\n{d}" for d, m in zip(r["documents"][0], r["metadatas"][0]))
    prompt = f"""Você é um tutor para a prova ITIL 4 Foundation.
Responda em português usando SOMENTE o contexto abaixo.
Cite entre colchetes a nota de origem. Se o contexto não tiver a resposta, diga que não sabe.

Contexto:
{contexto}

Pergunta: {pergunta}"""
    msg = cliente.messages.create(
        model="claude-sonnet-5-5", max_tokens=800,
        messages=[{"role": "user", "content": prompt}])
    return msg.content[0].text, r["metadatas"][0]

resposta, fontes = perguntar("Quais são os sete princípios orientadores do ITIL?")
print(resposta)
~~~

Para o modo simulado, basta trocar a instrução do prompt: "Com base no contexto, crie 3 questões de múltipla escolha com 4 alternativas, indique a correta e explique".

A versão completa (com simulado, avaliação pelo gabarito e modo chat) está na pasta `Projeto/tutor_itil.py`, ao lado destas notas.

#### Experimentos para fazer

- Mudar o tamanho do chunk (por título vs. a cada 500 caracteres) e ver o efeito no gabarito.
- Mudar o `k` (2, 5, 10) e observar quando o contexto começa a atrapalhar.
- Perguntar em português e em inglês e comparar o que é recuperado.
- Fazer uma pergunta fora do material (ex.: sobre COBIT) e ver se o tutor admite que não sabe.

---

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-05-construir-seu-primeiro-rag/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
