[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Pgvector

## O que é

**pgvector** é uma extensão do **PostgreSQL** que permite armazenar, indexar e pesquisar vetores diretamente dentro de um banco de dados relacional.

No contexto de RAG, isso significa que os embeddings dos chunks podem ser armazenados junto com os dados tradicionais da aplicação, permitindo realizar **busca por similaridade vetorial usando o próprio PostgreSQL**.

O fluxo pode ser representado assim:

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
Embeddings
   ↓
PostgreSQL + pgvector
   ↓
Vector Search
   ↓
Chunks relevantes
```

A principal característica do pgvector é combinar **dados relacionais tradicionais** com **dados vetoriais** no mesmo banco.

## Como funciona

Imagine que uma aplicação já utiliza PostgreSQL para armazenar seus clientes, documentos e permissões.

Sem pgvector, os embeddings poderiam precisar ser armazenados em uma solução separada:

```
PostgreSQL
→ clientes
→ documentos
→ permissões

Vector Database
→ embeddings
→ busca vetorial
```

Com pgvector, os vetores podem ficar dentro do próprio PostgreSQL:

```
PostgreSQL + pgvector

┌─────────────────────────────┐
│ Documento                   │
│ Chunk                       │
│ Metadata                    │
│ Embedding                   │
│ Cliente                     │
│ Permissões                  │
└─────────────────────────────┘
```

Isso permite combinar uma busca semântica com filtros relacionais.

Por exemplo:

```
Pergunta:
"Qual é a política de férias?"

+

Filtro:
departamento = "RH"
empresa_id = 123
ano >= 2026
```

O sistema pode utilizar a similaridade dos embeddings para encontrar os chunks mais relevantes e, ao mesmo tempo, aplicar condições sobre os dados armazenados no PostgreSQL.

Assim, o pgvector aproxima duas formas de busca:

```
Busca tradicional
→ filtros, campos, relacionamentos

Busca vetorial
→ similaridade entre embeddings
```

## Um exemplo

Imagine uma tabela de chunks de documentos:

```
documents_chunks

id | content | embedding | department | year
------------------------------------------------
1  | ...     | [0.21,...] | RH         | 2026
2  | ...     | [0.72,...] | Finance    | 2026
3  | ...     | [0.19,...] | RH         | 2025
```

Durante a ingestão, cada chunk recebe um embedding:

```
Chunk
   ↓
Embedding Model
   ↓
Vector
   ↓
PostgreSQL + pgvector
```

Quando o usuário faz uma pergunta, ela também é transformada em um vetor:

```
"Qual é o prazo para solicitar férias?"
                ↓
         Embedding Model
                ↓
         Vetor da consulta
```

O pgvector pode então realizar uma busca por similaridade e encontrar os chunks mais próximos.

O sistema ainda pode aplicar filtros:

```
Busca:

similaridade vetorial
        +
department = "RH"
        +
year = 2026
```

O resultado é uma lista de chunks relevantes que pode ser enviada ao LLM como contexto.

## Por que é importante

O pgvector é importante porque permite implementar **busca vetorial dentro de uma infraestrutura PostgreSQL**, evitando necessariamente a introdução de um banco vetorial separado.

Isso pode simplificar arquiteturas nas quais a aplicação já utiliza PostgreSQL e precisa combinar embeddings com informações relacionais.

Suas características também ajudam a entender uma diferença importante entre as tecnologias estudadas:

```
Chroma
→ solução orientada a armazenamento e recuperação vetorial

FAISS
→ biblioteca especializada em indexação e busca vetorial

pgvector
→ extensão do PostgreSQL que adiciona suporte a vetores
   e busca por similaridade ao banco relacional
```

O pgvector também suporta diferentes tipos de índices para tornar a busca mais eficiente, incluindo estratégias baseadas em **HNSW** e **IVFFlat**. Essas estruturas serão importantes quando estudarmos **Approximate Nearest Neighbor (ANN)**.

Isso conecta o conceito de Indexing aos anteriores:

```
Embedding Model
→ transforma chunks em vetores

pgvector
→ armazena esses vetores no PostgreSQL

Indexing
→ cria estruturas para tornar a busca mais eficiente

Vector Search
→ procura vetores semelhantes

Metadata / SQL
→ permite aplicar filtros estruturados

Retrieval
→ seleciona os chunks relevantes

LLM
→ utiliza esses chunks como contexto
```

O ponto central é: **pgvector permite que o PostgreSQL armazene e pesquise embeddings, combinando busca vetorial com os recursos tradicionais de um banco de dados relacional.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-pgvector/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
