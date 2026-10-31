[← Voltar para o Plano de estudos: 10 dias de imersão em GenAI](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai-2/)

# Dia 4: RAG: finalmente

Aqui começa a parte que provavelmente terá maior retorno para a vaga.

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

### 1. Ingestion

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

### 2. Chunking

Estude:

- fixed-size chunking
- semantic chunking
- recursive chunking
- overlap
- metadata

### 3. Embeddings

```
chunk
 ↓
embedding model
 ↓
vector
```

### 4. Indexing

Onde armazenamos os vetores?

Pesquise:

- FAISS
- Chroma
- Pinecone
- Weaviate
- Qdrant
- pgvector

Não precisa aprender todos.

**Escolha um.**

Para seu primeiro projeto, eu escolheria **Chroma ou FAISS**, porque você quer entender o conceito antes de entrar em infraestrutura.

### 5. Retrieval

Pesquise:

- top-k
- similarity search
- semantic search
- hybrid search
- metadata filtering
- query rewriting

### 6. Reranking

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

### 7. Generation

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
