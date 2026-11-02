[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Indexing FAISS

## O que é

**FAISS**, sigla para _Facebook AI Similarity Search_, é uma biblioteca desenvolvida pela Meta para realizar **busca eficiente por similaridade entre vetores**.

No contexto de RAG, o FAISS pode ser utilizado na etapa de **Indexing** para organizar embeddings e permitir encontrar rapidamente os vetores mais próximos de uma consulta.

Diferentemente do Chroma, que oferece uma solução mais completa para armazenamento e gerenciamento de dados vetoriais, o FAISS é principalmente uma **biblioteca de busca e indexação vetorial**.

O fluxo simplificado é:

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
FAISS Index
   ↓
Vector Search
   ↓
Chunks relevantes
```

## Como funciona

Imagine que temos milhões de pontos espalhados em um espaço multidimensional.

Cada ponto representa um embedding:

```
Embedding 1 → ●
Embedding 2 →       ●
Embedding 3 →   ●
Embedding 4 →                 ●
Embedding 5 →      ●
...
```

Quando chega uma nova pergunta, seu embedding também se transforma em um ponto:

```
Consulta → ★
```

O objetivo é encontrar rapidamente os pontos mais próximos da estrela.

O FAISS cria estruturas de índice que tornam essa busca muito mais eficiente do que simplesmente comparar a consulta com todos os vetores individualmente.

```
Pergunta
   ↓
Embedding
   ↓
Vetor da consulta
   ↓
FAISS Index
   ↓
Vetores mais próximos
   ↓
IDs dos chunks
   ↓
Conteúdo dos chunks
```

Existem diferentes tipos de índices no FAISS, com diferentes compromissos entre **velocidade, memória e precisão da busca**.

Por exemplo, uma busca exaustiva pode comparar a consulta com todos os vetores, enquanto índices aproximados podem pesquisar apenas regiões mais promissoras do espaço vetorial.

Isso é especialmente relevante quando a quantidade de embeddings cresce muito.

## Um exemplo

Imagine uma base com 1 milhão de chunks.

Depois do processamento:

```
Chunk 1 → Embedding → Vetor 1
Chunk 2 → Embedding → Vetor 2
Chunk 3 → Embedding → Vetor 3
...
Chunk 1.000.000 → Embedding → Vetor 1.000.000
```

O FAISS pode construir um índice sobre esses vetores.

Cada vetor pode estar associado ao identificador do chunk correspondente:

```
FAISS Index

Vetor 1 → ID 001
Vetor 2 → ID 002
Vetor 3 → ID 003
...
Vetor N → ID N
```

Quando o usuário pergunta:

> "Qual é o prazo para solicitar férias?"

a pergunta passa pelo Embedding Model:

```
Pergunta
   ↓
Embedding Model
   ↓
Vetor da pergunta
```

Esse vetor é enviado ao FAISS para encontrar os vetores mais próximos:

```
Vetor da pergunta
       ↓
     FAISS
       ↓
IDs mais próximos
       ↓
001, 027, 184...
```

O sistema utiliza esses IDs para recuperar os respectivos chunks e entregá-los ao LLM como contexto.

Portanto, o FAISS não precisa necessariamente armazenar todo o conteúdo textual. Ele pode cuidar principalmente dos vetores e dos identificadores, enquanto o conteúdo original é mantido em outra estrutura.

## Por que é importante

FAISS é importante porque demonstra uma diferença fundamental entre **armazenar embeddings** e **pesquisar embeddings de maneira eficiente**.

Ele foi projetado especificamente para problemas de busca por similaridade em grandes conjuntos de vetores e oferece diferentes estruturas de indexação.

A relação com os conceitos anteriores pode ser resumida assim:

```
Embedding Model
→ transforma conteúdo em vetores

Vector Embedding
→ representação numérica do conteúdo

FAISS
→ cria índices e realiza busca por similaridade

Vector Search
→ procura os vetores mais próximos

Retrieval
→ utiliza os resultados para recuperar os chunks

LLM
→ utiliza os chunks recuperados para gerar a resposta
```

Também é importante diferenciar **FAISS** de **Chroma**:

```
FAISS
→ biblioteca focada em indexação e busca vetorial

Chroma
→ banco de dados vetorial com recursos de armazenamento,
  gerenciamento e consulta de embeddings
```

Essa diferença não significa que um seja necessariamente melhor que o outro. Eles atendem a necessidades diferentes e podem até aparecer em arquiteturas distintas.

Outro conceito importante é que o FAISS oferece diferentes estratégias de indexação. Algumas priorizam simplicidade e precisão, enquanto outras utilizam aproximações para conseguir maior velocidade e menor consumo de recursos em grandes volumes.

Isso introduz uma ideia importante para os próximos conceitos: **Approximate Nearest Neighbor (ANN)**, em que o sistema procura os vizinhos mais próximos de maneira aproximada para obter uma busca muito mais eficiente em grandes bases.

O ponto central é: **FAISS é uma biblioteca especializada em indexação e busca por similaridade vetorial, permitindo que sistemas como RAG encontrem rapidamente os embeddings mais próximos de uma consulta.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-faiss/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
