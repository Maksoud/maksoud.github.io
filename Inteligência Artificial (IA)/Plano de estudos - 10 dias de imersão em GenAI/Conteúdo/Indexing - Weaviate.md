# Weaviate

## O que é

**Weaviate** é um banco de dados vetorial que permite armazenar, indexar e pesquisar embeddings, sendo bastante utilizado em aplicações de **RAG**, busca semântica e sistemas de recomendação.

No contexto de **Indexing**, o Weaviate recebe os vetores gerados pelo modelo de embeddings e cria as estruturas necessárias para localizar rapidamente os vetores mais semelhantes a uma consulta.

Além do vetor, cada objeto pode armazenar os dados originais e **propriedades estruturadas**, como título, categoria, página, data ou identificador do documento.

Uma representação simplificada seria:

```
Chunk
   ↓
Embedding Model
   ↓
Vector Embedding
   ↓
Weaviate
   ├── Vector
   ├── Properties
   └── Index
```

Assim como Qdrant, Pinecone e outras soluções, o Weaviate não é o processo de indexing em si. Ele é uma tecnologia que **armazena os dados e fornece mecanismos de indexação e busca**.

## Como funciona

Imagine uma coleção com milhares de trechos de documentos.

Cada trecho é transformado em um vetor:

```
"Funcionários devem solicitar férias..."
             ↓
[0.21, -0.73, 0.45, ...]
```

O Weaviate armazena esse vetor junto com as informações relacionadas:

```
Objeto
├── Vector
└── Properties
    ├── conteúdo
    ├── documento
    ├── página
    ├── seção
    └── ano
```

Quando o usuário faz uma pergunta, ela também é transformada em um vetor:

```
Pergunta
   ↓
Embedding Model
   ↓
Query Vector
   ↓
Weaviate
   ↓
Vetores mais semelhantes
   ↓
Chunks relevantes
```

O sistema pode então utilizar esses chunks como contexto para o LLM.

Um ponto importante é que o Weaviate também permite trabalhar com **filtros estruturados**. Assim, uma busca pode combinar similaridade vetorial com informações armazenadas nas propriedades.

Por exemplo:

```
Pergunta:
"Qual é a política de férias?"

Busca semântica
        +
Filtro: ano = 2026
        ↓
Weaviate
        ↓
Documentos semanticamente relevantes
e pertencentes ao ano de 2026
```

Isso é particularmente útil em RAG, porque a similaridade semântica sozinha pode não ser suficiente para selecionar a informação correta.

## Um exemplo

Imagine uma empresa que possui 100 mil documentos internos.

Durante a ingestão:

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
Vector Embeddings
   ↓
Weaviate
```

Um chunk poderia ser armazenado aproximadamente assim:

```
ID:
chunk_84721

Vector:
[0.18, -0.42, 0.71, ...]

Properties:
{
  "content": "As férias devem ser solicitadas com 30 dias de antecedência.",
  "document": "politica_ferias.pdf",
  "section": "Férias",
  "page": 4,
  "year": 2026
}
```

Depois, o usuário pergunta:

```
"Com quanto tempo de antecedência preciso solicitar minhas férias?"
```

A pergunta é transformada em embedding e enviada ao Weaviate.

O sistema procura vetores semanticamente próximos e pode retornar o chunk correspondente à política de férias.

O resultado então segue para o LLM:

```
Pergunta
   ↓
Embedding
   ↓
Weaviate
   ↓
Chunks relevantes
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

## Por que é importante

O Weaviate é importante porque combina **armazenamento de dados, indexação vetorial e mecanismos de busca** em uma infraestrutura voltada para aplicações que precisam encontrar informações semanticamente relacionadas.

Dentro de um sistema RAG, ele pode assumir uma posição como esta:

```
Ingestion
   ↓
Parsing
   ↓
Cleaning
   ↓
Chunking
   ↓
Embedding
   ↓
Weaviate
   ↓
Vector Search
   ↓
Retrieval
   ↓
LLM
```

Ele também ajuda a entender uma distinção importante:

|Conceito|Função|
|---|---|
|Embedding Model|Transforma conteúdo em vetores|
|Vector Embedding|Representa semanticamente o conteúdo|
|Weaviate|Armazena, indexa e pesquisa vetores|
|Vector Index|Estrutura usada para acelerar a busca|
|Vector Search|Procura vetores semelhantes|
|Retrieval|Seleciona informações para fornecer ao LLM|

O Weaviate pode trabalhar com diferentes formas de busca e indexação, incluindo estruturas voltadas para **Approximate Nearest Neighbor**, conceito que será importante para entender como bancos vetoriais conseguem pesquisar grandes quantidades de embeddings sem comparar necessariamente a consulta com todos os vetores.

A ideia central é: **Weaviate é uma infraestrutura de banco de dados vetorial que organiza embeddings e seus metadados para permitir buscas semânticas eficientes, sendo uma das opções que podem ser utilizadas na etapa de indexing de um sistema RAG.**