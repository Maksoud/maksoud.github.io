# Similarity Search

## O que é

**Similarity Search** é a técnica utilizada para encontrar informações que são **mais semelhantes a uma determinada consulta**, de acordo com algum critério de similaridade ou distância.

Em sistemas RAG baseados em embeddings, a consulta é transformada em um vetor e comparada com os vetores armazenados na base.

```
Pergunta
   ↓
Embedding Model
   ↓
Query Vector
   ↓
Similarity Search
   ↓
Vetores mais semelhantes
   ↓
Chunks correspondentes
```

A ideia fundamental é simples: **encontrar os pontos mais próximos da consulta dentro do espaço vetorial**.

Por exemplo, uma pergunta sobre "solicitação de férias" pode encontrar um chunk que utiliza a expressão "pedido de férias", mesmo que as palavras não sejam exatamente iguais.

Isso acontece porque os embeddings representam relações semânticas, e não apenas palavras isoladas.

## Como funciona

Imagine que cada chunk de uma base de conhecimento seja representado como um ponto em um espaço multidimensional.

```
             Espaço vetorial

       ● A
                    ● B

                         ★ Consulta

       ● C
             ● D
```

A consulta também possui uma posição nesse espaço.

O Similarity Search procura quais pontos estão mais próximos dela, de acordo com a métrica utilizada.

De forma simplificada:

```
Query Vector
     ↓
Comparar com vetores armazenados
     ↓
Calcular similaridade/distância
     ↓
Ordenar resultados
     ↓
Selecionar os mais próximos
```

Uma das métricas mais conhecidas é a **Cosine Similarity**, que compara o ângulo entre dois vetores:

$$  
\text{similaridade}(A,B)=\frac{A\cdot B}{|A||B|}  
$$

Outras métricas também podem ser utilizadas, como **Euclidean Distance** e **Dot Product**.

O mecanismo de busca utilizado depende da tecnologia e da configuração do sistema.

Por exemplo, um banco vetorial pode armazenar milhões de embeddings e utilizar estruturas de indexação para evitar comparar a consulta individualmente com todos os vetores.

Isso conecta Similarity Search ao conceito de **Nearest Neighbor**:

```
Similarity Search
       ↓
Encontrar os vetores mais semelhantes
       ↓
Nearest Neighbors
       ↓
Top-K resultados
```

O `K` representa quantos resultados serão recuperados.

Se `K = 5`, por exemplo, o sistema pode retornar os cinco chunks considerados mais relevantes.

## Um exemplo

Imagine uma base com quatro chunks:

```
Chunk A:
"Como solicitar férias pelo sistema corporativo."

Chunk B:
"Procedimento para marcar o período de descanso."

Chunk C:
"Regras para utilização do plano de saúde."

Chunk D:
"Política de reembolso de despesas."
```

O usuário pergunta:

```
"Como faço para pedir minhas férias?"
```

A pergunta é transformada em um embedding:

```
Pergunta
   ↓
Embedding Model
   ↓
[0.18, -0.42, 0.71, ...]
```

Os chunks também possuem embeddings.

O Similarity Search compara o vetor da pergunta com os vetores armazenados:

```
Query
  ↓
┌─────────────────────────────┐
│ Chunk A → similaridade alta │
│ Chunk B → similaridade alta │
│ Chunk C → baixa             │
│ Chunk D → baixa             │
└─────────────────────────────┘
```

O sistema pode retornar:

```
1. Chunk A
2. Chunk B
```

Esses chunks então podem ser enviados ao LLM como contexto:

```
Pergunta
   ↓
Similarity Search
   ↓
Chunks relevantes
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

Note que o Chunk B pode ser considerado relevante mesmo sem utilizar a palavra "férias". A expressão "período de descanso" possui relação semântica com a consulta.

Esse é justamente um dos principais benefícios da busca baseada em embeddings.

## Por que é importante

Similarity Search é fundamental para o **Dense Retrieval** e, consequentemente, para muitas arquiteturas de RAG.

Ele permite que o sistema procure informações pelo **significado representado nos embeddings**, e não apenas pela correspondência literal de palavras.

Podemos posicioná-lo na arquitetura que estamos construindo:

```
Documentos
   ↓
Chunking
   ↓
Embedding
   ↓
Indexing
   ↓
Base vetorial
        ↑
        │
Pergunta
   ↓
Query Rewriting
   ↓
Query Embedding
   ↓
Similarity Search
   ↓
Top-K resultados
   ↓
Reranking
   ↓
Contexto
   ↓
LLM
```

Isso também ajuda a diferenciar conceitos que já estudamos:

|Conceito|Função|
|---|---|
|Semantic Similarity|Mede o grau de relação semântica|
|Cosine Similarity|Uma métrica para comparar vetores|
|Similarity Search|Usa similaridade para encontrar conteúdos relevantes|
|Vector Search|Busca realizada sobre representações vetoriais|
|Nearest Neighbor|Identifica os vetores mais próximos|
|Vector Database|Armazena e disponibiliza os vetores para busca|
|Dense Retrieval|Estratégia de Retrieval baseada em representações densas|

Uma observação importante: **similaridade não significa necessariamente correção**.

Um documento pode ser muito semelhante semanticamente à pergunta e ainda assim estar desatualizado, contradizer outra fonte ou não responder exatamente ao que foi perguntado.

Por isso, em um RAG mais sofisticado, Similarity Search costuma ser apenas uma das etapas:

```
Similarity Search
       ↓
Candidatos
       ↓
Reranking
       ↓
Filtros / validações
       ↓
Contexto final
       ↓
LLM
```

A ideia central é: **Similarity Search encontra, dentro de uma coleção de representações, os conteúdos mais próximos de uma consulta segundo uma métrica de similaridade ou distância. Em RAG, ele é uma das principais formas de transformar uma pergunta em um conjunto de informações candidatas para o LLM.**