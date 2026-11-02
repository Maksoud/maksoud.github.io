[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Chunking Metadata

## O que é

**Chunking Metadata** são informações adicionais associadas a cada chunk durante o processo de divisão de um documento.

O chunk contém o **conteúdo principal** que será utilizado na recuperação. Os metadados fornecem informações sobre a origem, localização, categoria ou características desse conteúdo.

Por exemplo, um chunk pode conter:

```
Conteúdo:
"Funcionários devem solicitar férias com pelo menos
30 dias de antecedência."

Metadata:
documento = "politica_de_ferias.pdf"
página = 12
seção = "Férias"
departamento = "Recursos Humanos"
data = "2026-01-15"
```

Essas informações normalmente acompanham o embedding no armazenamento utilizado pelo sistema RAG.

## Como funciona

Imagine uma biblioteca.

O texto de um chunk seria o **conteúdo de um livro**. Os metadados seriam informações como:

```
Título: Política de Férias
Autor: Recursos Humanos
Categoria: Políticas internas
Página: 12
Ano: 2026
```

O conteúdo permite encontrar informação pelo significado. Os metadados permitem saber **de onde ela veio e como classificá-la**.

Durante a ingestão, o sistema pode preservar ou adicionar metadados ao criar os chunks:

```
Documento
   ↓
Parsing
   ↓
Cleaning
   ↓
Chunking
   ↓
┌───────────────────────────────┐
│ Chunk                         │
│ "Solicitação deve ocorrer..." │
│                               │
│ Metadata                      │
│ documento = politica.pdf      │
│ página = 12                   │
│ seção = férias                │
└───────────────────────────────┘
   ↓
Embedding
   ↓
Vector Database
```

Na etapa de retrieval, esses metadados podem ser utilizados junto com a similaridade semântica.

Por exemplo, em vez de procurar em todos os documentos:

```
Buscar semanticamente:
"Qual é a política de férias?"
```

o sistema poderia restringir a busca:

```
categoria = "Recursos Humanos"
ano >= 2026
```

e somente depois realizar a busca semântica dentro desse conjunto.

## Um exemplo

Imagine que uma empresa tenha três documentos sobre férias:

```
Documento A
Nome: politica_ferias_2024.pdf
Seção: Férias
Ano: 2024

Documento B
Nome: politica_ferias_2025.pdf
Seção: Férias
Ano: 2025

Documento C
Nome: politica_ferias_2026.pdf
Seção: Férias
Ano: 2026
```

Durante a ingestão, cada chunk pode preservar essas informações:

```
Chunk:
"Funcionários devem solicitar férias com pelo menos
30 dias de antecedência."

Metadata:
{
  "documento": "politica_ferias_2026.pdf",
  "seção": "Férias",
  "ano": 2026,
  "página": 4
}
```

Agora imagine que o usuário pergunte:

> "Qual é a regra atual para solicitar férias?"

O sistema pode utilizar o significado da pergunta para encontrar chunks relevantes, mas também pode usar o metadata `ano = 2026` para evitar recuperar uma política antiga.

Os metadados também podem ser utilizados para apresentar a origem da informação ao usuário:

```
Resposta:
"Segundo a política de férias, a solicitação deve ser feita
com pelo menos 30 dias de antecedência."

Fonte:
politica_ferias_2026.pdf, página 4
```

## Por que é importante

Chunking Metadata é importante porque permite que o sistema RAG não trate os chunks apenas como pedaços isolados de texto.

Os metadados podem ajudar em:
- filtragem antes ou durante a recuperação;
- identificação da fonte;
- controle de versões;
- organização por categorias;
- identificação de páginas e seções;
- aplicação de regras de acesso;
- geração de citações e referências;
- combinação entre busca semântica e filtros estruturados.

Isso é especialmente importante quando a base contém muitos documentos semelhantes.

Existe uma diferença importante entre **conteúdo** e **metadata**:

```
Conteúdo
→ "Funcionários devem solicitar férias com 30 dias de antecedência."

Metadata
→ documento = politica_ferias_2026.pdf
→ seção = Férias
→ página = 4
→ ano = 2026
```

O conteúdo responde principalmente à pergunta **"o que a informação diz?"**.

O metadata ajuda a responder **"de onde veio, a que pertence e em quais condições devo considerá-la?"**.

Assim, no contexto de RAG, os metadados complementam o embedding. O embedding ajuda a encontrar conteúdo semanticamente relevante, enquanto os metadados permitem restringir, organizar e contextualizar essa busca.

O ponto central é: **Chunking Metadata adiciona contexto estruturado aos chunks, permitindo que o sistema saiba não apenas o conteúdo de cada trecho, mas também sua origem, classificação e outras características úteis para a recuperação.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-metadata/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
