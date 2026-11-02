[← Voltar para o Plano de estudos: 10 dias de imersão em GenAI](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai-2/)

# Dia 4: RAG: finalmente

Aqui começa a parte que provavelmente terá maior retorno para oportunidades de mercado.

## RAG = Retrieval-Augmented Generation

A ideia básica é:

```
Usuário
   ↓
Pergunta
   ↓
Retrieval
   ↓
Documentos relevantes
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

Ou:

> **Retrieve → Augment → Generate**

Esse é o pipeline básico descrito também pela documentação do Google. [Google Codelabs](https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/7-advanced-agent-capabilities/building-agents-with-retrieval-augmented-generation?hl=en&utm_source=chatgpt.com)

---

## Mas NÃO pare aí.

Você precisa estudar o RAG em camadas:

### 1. [Ingestion](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/ingestion/)

Como os dados entram?

```
PDF
DOCX
HTML
Banco de dados
Website
   ↓
Parsing
   ↓
Cleaning
   ↓
Chunking
```

### 2. [Chunking](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking/)

Estude:
- [fixed-size chunking](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-fixed-size-chunking/)
- [semantic chunking](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-semantic-chunking/)
- [recursive chunking](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-recursive-chunking/)
- [overlap](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-overlap/)
- [metadata](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-metadata/)

### 3. [Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings/)

```
chunk
 ↓
embedding model
 ↓
vector
```

### 4. [Indexing](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing/)

Onde armazenamos os vetores?

Pesquise:
- [FAISS](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-faiss/)
- [Chroma](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-chroma/)
- [Pinecone](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-pinecone/)
- [Weaviate](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-weaviate/)
- [Qdrant](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-qdrant/)
- [pgvector](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-pgvector/)

Para seu primeiro projeto, eu escolheria **Chroma ou FAISS**, porque você quer entender o conceito antes de entrar em infraestrutura.

### 5. [Retrieval](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval/)

Pesquise:
- [top-k](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-top-k/)
- [similarity search](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-similarity-search/)
- [semantic search](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-semantic-search/)
- [hybrid search](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-hybrid-search/)
- [metadata filtering](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-metadata-filtering/)
- [query rewriting](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-query-rewriting/)

### 6. [Reranking](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/reranking/)

Esse termo é importante.

Imagine:

```
100 documentos
      ↓
retrieval
      ↓
20 candidatos
      ↓
reranker
      ↓
5 melhores
      ↓
LLM
```

Isso é muito mais próximo de um sistema RAG real.

### 7. [Generation](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-generation/)

Finalmente:

```
Contexto recuperado
+
Pergunta
+
Instructions
       ↓
      LLM
```

---

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
