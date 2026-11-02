[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Pinecone

## O que é

**Pinecone** é uma plataforma de banco de dados vetorial voltada para armazenar, indexar e pesquisar embeddings em aplicações de IA.

No contexto de RAG, o Pinecone pode receber os embeddings gerados a partir dos chunks, armazená-los junto com seus metadados e disponibilizá-los para buscas por similaridade durante o retrieval.

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
Pinecone
   ↓
Vector Search
   ↓
Chunks relevantes
   ↓
LLM
```

Assim como Chroma e pgvector, Pinecone pode desempenhar um papel importante na etapa de **Indexing**, mas possui uma característica importante: ele é uma solução especializada em infraestrutura de busca vetorial.

## Como funciona

Imagine uma grande biblioteca digital com milhões de trechos de documentos.

Cada chunk é transformado em um vetor:

```
Chunk A → [0.21, -0.73, 0.45, ...]
Chunk B → [0.67,  0.12, -0.31, ...]
Chunk C → [0.19, -0.70, 0.48, ...]
```

O Pinecone organiza esses vetores em um índice.

Quando chega uma pergunta, ela também passa pelo Embedding Model:

```
Pergunta
   ↓
Embedding Model
   ↓
Vetor da consulta
   ↓
Pinecone Index
   ↓
Vetores mais próximos
```

O sistema então recupera os identificadores e os dados associados aos vetores mais relevantes.

Uma maneira simples de visualizar isso é:

```
                Pinecone
        ┌─────────────────────┐
        │ Vector A → Chunk A  │
        │ Vector B → Chunk B  │
        │ Vector C → Chunk C  │
        │ Vector D → Chunk D  │
        │        ...          │
        └─────────────────────┘
                  ↑
                  │
           Vetor da pergunta
                  │
                  ↓
            Busca vetorial
```

Além do vetor, cada registro pode possuir **metadata**, permitindo que a aplicação combine similaridade semântica com filtros.

Por exemplo:

```
categoria = "RH"
ano = 2026
empresa = "Empresa A"
```

Isso permite restringir a busca antes de selecionar os resultados mais relevantes.

## Um exemplo

Imagine uma empresa que possui 500 mil documentos internos.

Depois do processo de ingestão:

```
500.000 documentos
       ↓
Parsing + Cleaning
       ↓
Chunking
       ↓
2.000.000 chunks
       ↓
Embedding Model
       ↓
2.000.000 embeddings
```

Esses embeddings podem ser indexados no Pinecone.

Um registro poderia representar:

```
ID:
chunk_45872

Vector:
[0.21, -0.73, 0.45, ...]

Metadata:
{
  "documento": "politica_ferias.pdf",
  "pagina": 12,
  "departamento": "RH",
  "ano": 2026
}
```

Quando o usuário pergunta:

> "Qual é o prazo para solicitar férias?"

a pergunta é transformada em um embedding e enviada ao índice.

```
Pergunta
   ↓
Embedding Model
   ↓
Query Vector
   ↓
Pinecone
   ↓
Top K resultados
   ↓
Chunks relevantes
```

Suponha que o sistema solicite os 3 resultados mais relevantes. O Pinecone pode retornar algo conceitualmente semelhante a:

```
1. chunk_45872 → similaridade alta
2. chunk_45901 → similaridade alta
3. chunk_12034 → similaridade moderada
```

A aplicação então utiliza esses resultados para recuperar ou montar o contexto que será enviado ao LLM.

## Por que é importante

Pinecone é importante porque mostra uma abordagem em que a infraestrutura de armazenamento e busca vetorial é oferecida como um serviço especializado, evitando que a equipe precise implementar e operar toda essa infraestrutura internamente.

Ele é especialmente relevante em arquiteturas de RAG porque oferece recursos voltados para grandes coleções de embeddings, busca por similaridade e filtragem por metadata.

A comparação com as tecnologias anteriores ajuda a organizar os conceitos:

```
Chroma
→ solução orientada a aplicações de busca vetorial

FAISS
→ biblioteca para indexação e busca por similaridade

pgvector
→ extensão do PostgreSQL para armazenar e pesquisar vetores

Pinecone
→ plataforma especializada em banco de dados vetorial
```

Essas soluções não são simplesmente versões diferentes da mesma coisa. Elas ocupam posições diferentes na arquitetura.

Também é importante distinguir **Pinecone** de **Indexing**:

```
Pinecone
→ tecnologia utilizada para armazenar e pesquisar vetores

Indexing
→ processo de preparar estruturas que tornam a busca eficiente
```

Dentro de uma arquitetura RAG, podemos visualizar a sequência completa:

```
Documento
   ↓
Parsing
   ↓
Cleaning
   ↓
Chunking
   ↓
Embedding Model
   ↓
Vector Embedding
   ↓
Pinecone
   ↓
Indexing
   ↓
Vector Search
   ↓
Retrieval
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

O ponto central é: **Pinecone é uma plataforma especializada em armazenamento e busca vetorial que pode manter os embeddings e seus metadados indexados, permitindo que sistemas RAG recuperem rapidamente os chunks mais relevantes para uma consulta.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-pinecone/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
