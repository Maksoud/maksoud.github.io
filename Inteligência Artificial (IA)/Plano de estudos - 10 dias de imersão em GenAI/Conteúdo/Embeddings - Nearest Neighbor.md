[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Nearest Neighbor

## O que é

**Nearest Neighbor**, ou vizinho mais próximo, é o conceito de encontrar, em um conjunto de pontos ou vetores, aquele que está **mais próximo de um determinado ponto de consulta**.

No contexto de IA e embeddings, cada informação pode ser representada como um vetor. Quando fazemos uma busca, temos um vetor de consulta e queremos descobrir quais outros vetores estão mais próximos dele.

Por exemplo:

```
Vetor da pergunta
        ↓
      [Q]
     /   \
   [A]   [B]
```

Se `[A]` estiver mais próximo de `[Q]` do que `[B]`, então `[A]` é o **Nearest Neighbor** de `[Q]`.

A ideia é simples:

> Dado um vetor de consulta, encontre o vetor mais próximo dele.

Esse conceito é uma das bases matemáticas da **Vector Search**.

---

## Como funciona

Imagine novamente um mapa onde cada documento é representado por um ponto.

```
             Documento B ●


                         ● Pergunta
                      /
              ● Documento A


      ● Documento C
```

Se queremos saber qual documento é mais relevante para a pergunta, podemos procurar o ponto mais próximo dela.

Nesse caso:

```
Pergunta → Documento A
```

O Documento A é o **vizinho mais próximo**.

A proximidade, porém, precisa ser calculada por alguma medida. Dependendo do sistema, podemos utilizar, por exemplo:
- Cosine Similarity
- Distância Euclidiana
- Produto interno

Isso significa que **Nearest Neighbor não é uma métrica específica**. É o conceito de encontrar o elemento mais próximo. A métrica define como essa proximidade será calculada.

Para embeddings, podemos representar o processo de maneira simplificada:

```
Vetor da consulta
       ↓
Comparar com vetores disponíveis
       ↓
Calcular proximidade
       ↓
Encontrar o vetor mais próximo
       ↓
Retornar o conteúdo correspondente
```

Quando queremos encontrar não apenas um, mas vários vizinhos próximos, utilizamos o conceito de **k-Nearest Neighbors (k-NN)**.

Por exemplo, se `k = 5`, queremos encontrar os **5 vetores mais próximos** da consulta.

```
Consulta
   ↓
k = 5
   ↓
Vetor 1
Vetor 2
Vetor 3
Vetor 4
Vetor 5
```

Isso é especialmente importante em Vector Search, porque normalmente um sistema RAG não precisa recuperar apenas um documento. Ele pode recuperar vários trechos relevantes para construir o contexto da LLM.

---

## Um exemplo

Imagine que temos três documentos representados por vetores:

```
Documento A → [0.90, 0.80]
Documento B → [0.20, 0.10]
Documento C → [0.85, 0.75]
```

O usuário faz uma pergunta que gera:

```
Pergunta → [0.88, 0.78]
```

Visualmente, podemos imaginar:

```
A ●
     ● Pergunta
   ● C


                    ● B
```

Os documentos A e C estão próximos da pergunta, enquanto B está muito distante.

Se procurarmos apenas o **Nearest Neighbor**, teremos:

```
Pergunta → Documento A
```

Se procurarmos os **3-Nearest Neighbors**, teremos algo como:

```
1. Documento A
2. Documento C
3. Documento B
```

Na prática, sistemas de busca normalmente utilizam uma métrica de similaridade ou distância para produzir essa ordenação.

Em um sistema RAG, isso pode resultar em:

```
Pergunta
   ↓
Embedding
   ↓
Vetor da pergunta
   ↓
Nearest Neighbor Search
   ↓
Documentos mais próximos
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

Assim, o conceito de Nearest Neighbor ajuda a explicar **como a Vector Search decide quais vetores são mais relevantes para uma consulta**.

---

## Por que é importante

Nearest Neighbor é importante porque fornece uma forma matemática de transformar a ideia de **"encontre informações parecidas com esta"** em uma operação de busca.

Ele aparece em diversas aplicações:
- Busca semântica
- RAG
- Sistemas de recomendação
- Classificação
- Detecção de similaridade
- Reconhecimento de padrões
- Busca em bases de embeddings
- Sistemas de visão computacional

Também é importante diferenciar alguns conceitos que estamos estudando:

**Vector Search** é o processo de buscar vetores semelhantes.

**Nearest Neighbor** é o conceito de encontrar o vetor mais próximo.

**k-Nearest Neighbors (k-NN)** é a busca pelos `k` vetores mais próximos.

**Cosine Similarity** é uma das formas de calcular a relação entre dois vetores.

**Vector Database** é uma infraestrutura que pode armazenar os vetores e executar buscas desse tipo de maneira eficiente.

Podemos conectar tudo:

```
Texto
   ↓
Embedding
   ↓
Vector Embedding
   ↓
Vector Database
   ↓
Vector Search
   ↓
Nearest Neighbor
   ↓
Similarity / Distance
   ↓
Vetores mais relevantes
   ↓
RAG
   ↓
LLM
```

O ponto central é: **Nearest Neighbor é a ideia de encontrar o vetor mais próximo de uma consulta dentro de um espaço vetorial. Quando buscamos vários vetores próximos, temos k-Nearest Neighbors, um conceito fundamental para sistemas de busca semântica e RAG.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-nearest-neighbor/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
