[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Indexing

## O que é

**Indexing** é o processo de organizar e preparar os dados para que possam ser encontrados de forma rápida e eficiente durante uma busca.

No contexto de RAG, o indexing acontece principalmente durante a preparação da base de conhecimento. Depois que os documentos foram ingeridos, processados, divididos em chunks e transformados em embeddings, o sistema cria estruturas que permitem localizar rapidamente os conteúdos relevantes.

De forma simplificada:

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
Indexing
   ↓
Base preparada para Retrieval
```

É importante diferenciar **armazenar** de **indexar**.

Armazenar significa guardar os dados. Indexar significa criar uma estrutura que permita encontrá-los de maneira eficiente.

## Como funciona

Imagine uma biblioteca com um milhão de livros.

Se alguém perguntar:

> "Onde encontro informações sobre astronomia?"

seria muito ineficiente abrir todos os livros, um por um, até encontrar os relevantes.

Por isso, uma biblioteca possui mecanismos de organização e consulta, como catálogos e índices.

O Indexing desempenha uma função semelhante em sistemas de informação.

Em um sistema RAG, podemos imaginar:

```
Milhares de chunks
       ↓
    Indexing
       ↓
Estrutura organizada para busca
       ↓
Consulta
       ↓
Localização rápida dos chunks relevantes
```

No caso de embeddings, o índice pode ser especializado em busca por proximidade entre vetores.

Por exemplo:

```
Vetor da pergunta
       ↓
      Index
       ↓
encontra vetores próximos
       ↓
Chunks relevantes
```

Isso é especialmente importante porque uma base real pode conter milhões ou até bilhões de vetores. Comparar manualmente a pergunta com todos eles pode ser muito caro.

O índice permite utilizar estruturas e algoritmos especializados para tornar essa busca muito mais eficiente.

## Um exemplo

Imagine que uma empresa tenha 500 mil documentos.

Depois do processo de ingestão e chunking, esses documentos podem gerar milhões de chunks.

Cada chunk recebe um embedding:

```
Chunk 1 → [0.12, 0.81, -0.32, ...]
Chunk 2 → [0.14, 0.79, -0.29, ...]
Chunk 3 → [0.72, -0.15, 0.64, ...]
...
Chunk 2.000.000 → [0.09, 0.77, -0.35, ...]
```

Esses vetores são armazenados e indexados.

Quando o usuário pergunta:

> "Qual é o prazo para solicitar férias?"

a pergunta também é transformada em um vetor:

```
Pergunta
   ↓
Embedding Model
   ↓
Vetor da pergunta
   ↓
Índice
   ↓
Busca por vetores próximos
   ↓
Chunks relevantes
```

O índice ajuda o sistema a localizar rapidamente os vetores mais próximos, sem necessariamente comparar a consulta com todos os milhões de vetores de maneira exaustiva.

Os chunks recuperados então podem ser enviados ao LLM:

```
Pergunta
   ↓
Embedding
   ↓
Index / Vector Search
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

Indexing é importante porque transforma uma coleção de dados armazenados em uma estrutura que pode ser **consultada de maneira eficiente**.

Em RAG, isso afeta diretamente o desempenho do retrieval. Um sistema pode possuir excelentes documentos e embeddings, mas ainda assim precisar de uma estratégia eficiente para localizar os vetores relevantes.

Também é importante entender que **indexing não significa necessariamente apenas indexação vetorial**.

Dependendo da arquitetura, podem existir diferentes tipos de índices:

```
Índice tradicional
→ busca por termos e campos

Índice vetorial
→ busca por proximidade entre embeddings

Índice híbrido
→ combina diferentes mecanismos de busca
```

Isso se conecta diretamente aos conceitos que estudamos anteriormente.

Por exemplo, uma arquitetura pode combinar **Sparse Retrieval**, usando um índice lexical como parte de uma busca por termos, com **Dense Retrieval**, usando um índice vetorial para busca semântica.

A distinção entre alguns conceitos importantes fica assim:

```
Embedding
→ transforma conteúdo em vetor

Vector Database
→ armazena e gerencia vetores

Indexing
→ cria estruturas para tornar a busca eficiente

Vector Search
→ realiza a busca por vetores semelhantes

Retrieval
→ seleciona as informações relevantes para a consulta
```

Portanto, o Indexing fica entre a preparação dos dados e a recuperação eficiente dessas informações. Ele não é o conteúdo em si nem a busca realizada pelo usuário. É a **estrutura que torna a busca viável e eficiente em grandes volumes de dados**.

O ponto central é: **Indexing é o processo de criar estruturas organizadas que permitem localizar informações de forma eficiente, sendo fundamental para que o retrieval consiga encontrar rapidamente os chunks relevantes em uma base de conhecimento.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
