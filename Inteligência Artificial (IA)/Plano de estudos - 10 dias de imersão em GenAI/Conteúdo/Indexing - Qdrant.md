# Indexing Qdrant
## O que é

**Qdrant** é um banco de dados vetorial desenvolvido para armazenar, indexar e pesquisar vetores, sendo utilizado em aplicações como busca semântica, sistemas de recomendação e RAG.

No contexto de RAG, o Qdrant recebe os embeddings gerados a partir dos chunks, armazena esses vetores junto com seus metadados e permite encontrar os vetores mais semelhantes quando uma nova consulta é realizada.

O fluxo é:

```
Documentos
   ↓
Parsing
   ↓
Cleaning
   ↓
Chunking
   ↓
Embedding Model
   ↓
Embeddings + Metadata
   ↓
Qdrant
   ↓
Vector Search
   ↓
Chunks relevantes
   ↓
LLM
```

Assim como Pinecone, Chroma e outras soluções estudadas, o Qdrant pode atuar como uma camada de armazenamento e recuperação vetorial dentro da arquitetura RAG.

## Como funciona

Imagine que cada chunk de um documento seja transformado em um ponto dentro de um enorme espaço matemático.

O Embedding Model cria esses pontos:

```
Chunk A → [0.21, -0.73, 0.45, ...]
Chunk B → [0.68,  0.14, -0.31, ...]
Chunk C → [0.19, -0.70, 0.48, ...]
```

O Qdrant organiza esses vetores em uma estrutura que permite realizar buscas por proximidade.

Quando chega uma pergunta, ela também é transformada em um vetor:

```
Pergunta
   ↓
Embedding Model
   ↓
Vetor da consulta
   ↓
Qdrant
   ↓
Vetores mais próximos
```

O sistema procura os pontos mais próximos do vetor da pergunta e retorna os registros correspondentes.

O Qdrant também associa os vetores a **payloads**, que são informações adicionais armazenadas junto aos vetores. Na prática, esses dados funcionam como os metadados dos chunks.

Por exemplo:

```
Vector:
[0.21, -0.73, 0.45, ...]

Payload:
{
  "documento": "politica_ferias.pdf",
  "pagina": 12,
  "seção": "Férias",
  "ano": 2026
}
```

Isso permite combinar busca vetorial com filtros estruturados.

## Um exemplo

Imagine uma empresa com milhares de documentos internos.

Durante a ingestão, um documento é dividido em chunks:

```
Documento
   ↓
Chunking
   ↓
Chunk 1
Chunk 2
Chunk 3
...
```

Cada chunk passa pelo Embedding Model:

```
Chunk 1 → Vetor 1
Chunk 2 → Vetor 2
Chunk 3 → Vetor 3
```

Esses vetores podem ser armazenados no Qdrant junto com os dados necessários para identificar e recuperar o conteúdo original.

Imagine que o usuário pergunte:

> "Qual é o prazo para solicitar férias?"

A pergunta é transformada em um vetor:

```
Pergunta
   ↓
Embedding Model
   ↓
Query Vector
```

O Qdrant pesquisa os vetores mais próximos:

```
Query Vector
      ↓
   Qdrant
      ↓
┌──────────────────────┐
│ Chunk 42  → próximo  │
│ Chunk 91  → próximo  │
│ Chunk 17  → próximo  │
└──────────────────────┘
```

O sistema pode então recuperar o conteúdo desses chunks e utilizá-los como contexto para o LLM.

Também podemos restringir a busca usando os metadados:

```
Busca semântica:
"Qual é o prazo para solicitar férias?"

Filtro:
seção = "Férias"
ano = 2026
```

Isso reduz o universo de informações consideradas pelo retrieval.

## Por que é importante

O Qdrant é importante porque oferece uma infraestrutura especializada para **busca vetorial com filtros e metadados**, permitindo construir sistemas de recuperação semântica em diferentes escalas.

Um de seus conceitos importantes é a organização dos dados em **collections**. Uma collection pode ser entendida, de forma simplificada, como um conjunto de pontos vetoriais que compartilham determinadas características de configuração.

Cada ponto pode conter:

```
Point
├── ID
├── Vector
└── Payload
```

Isso ajuda a separar o vetor em si das informações associadas a ele.

A relação com as tecnologias estudadas anteriormente fica assim:

```
FAISS
→ biblioteca focada em busca e indexação vetorial

Chroma
→ solução orientada a aplicações com armazenamento e busca vetorial

pgvector
→ extensão do PostgreSQL para dados e busca vetorial

Pinecone
→ plataforma especializada em banco de dados vetorial

Qdrant
→ banco de dados vetorial com busca por similaridade
  e filtragem baseada em payloads
```

O Qdrant também utiliza estruturas especializadas para acelerar a busca por vizinhos próximos, incluindo **HNSW**, conceito que se conecta diretamente ao próximo nível de Indexing e à ideia de **Approximate Nearest Neighbor**.

Assim, a arquitetura pode ser resumida:

```
Chunking
   ↓
Embedding Model
   ↓
Vector Embedding
   ↓
Qdrant
   ↓
Indexing
   ↓
Vector Search
   ↓
Metadata Filtering
   ↓
Retrieval
   ↓
Contexto
   ↓
LLM
```

O ponto central é: **Qdrant é um banco de dados vetorial que armazena embeddings e informações associadas, utilizando índices de busca vetorial para encontrar rapidamente os chunks semanticamente mais relevantes para uma consulta.**