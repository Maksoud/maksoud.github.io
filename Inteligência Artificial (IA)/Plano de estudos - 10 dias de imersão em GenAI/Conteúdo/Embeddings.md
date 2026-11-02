[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Embeddings

## O que é

**Embeddings** são representações numéricas de informações, como textos, imagens ou outros tipos de dados, que permitem que um modelo de IA trabalhe com relações de **significado e similaridade** entre esses dados.

Um texto, por exemplo, é transformado em uma sequência de números chamada **vetor**.

A ideia é representar conteúdos semanticamente semelhantes de maneira que seus vetores também estejam próximos em um determinado espaço matemático.

Por exemplo:

```
"carro"
"automóvel"
"veículo"
```

Essas palavras possuem significados relacionados. Um modelo de embeddings tende a produzir representações que capturam essa relação.

Já palavras como:

```
"carro"
"banana"
```

tendem a apresentar uma relação semântica diferente.

O embedding, portanto, não é simplesmente uma tradução de uma palavra para números. Ele é uma **representação matemática de características e relações aprendidas a partir dos dados**.

## Como funciona

Imagine um mapa.

Em vez de representar cidades pela aparência física, você poderia posicioná-las de acordo com características como distância, clima, população e localização.

Nesse mapa, cidades com características semelhantes tenderiam a ficar próximas.

Embeddings funcionam de maneira parecida, mas em um espaço matemático que pode possuir centenas ou milhares de dimensões.

Considere:

```
"Como solicitar férias?"
"Qual é o procedimento para tirar férias?"
"Como faço para marcar minhas férias?"
```

As frases utilizam palavras diferentes, mas possuem significados semelhantes.

Um modelo de embeddings pode transformar cada uma em um vetor:

```
Frase 1 → [0.21, -0.34, 0.72, ...]
Frase 2 → [0.19, -0.31, 0.69, ...]
Frase 3 → [0.23, -0.36, 0.74, ...]
```

Os números individualmente não possuem uma interpretação simples para nós. O que importa é a **relação entre os vetores**.

Podemos então calcular uma medida de similaridade entre eles. Uma das mais utilizadas é a **similaridade de cosseno**.

De forma simplificada:

```
Vetores próximos
      ↓
Maior similaridade

Vetores distantes
      ↓
Menor similaridade
```

Isso permite que um sistema encontre conteúdos semanticamente relacionados, mesmo quando eles não utilizam exatamente as mesmas palavras.

## Um exemplo

Imagine que uma empresa tenha milhares de documentos internos.

Um funcionário pergunta:

```
Como faço para tirar férias?
```

O sistema poderia procurar apenas documentos que contenham exatamente as palavras "tirar férias".

Isso pode falhar se o documento utilizar uma expressão diferente, como:

```
Procedimento para solicitação do período de descanso anual
```

Com embeddings, os dois textos podem ser transformados em vetores.

O sistema então compara o vetor da pergunta com os vetores dos documentos:

```
Pergunta
"Como faço para tirar férias?"
        ↓
     Embedding
        ↓
    Vetor da pergunta
        ↓
   Comparação
        ↓
Documentos semanticamente semelhantes
```

O documento sobre "período de descanso anual" pode ser recuperado mesmo sem utilizar as mesmas palavras da pergunta.

Esse mecanismo é fundamental para sistemas de **RAG**.

Um fluxo simplificado seria:

```
Documento
   ↓
Embedding
   ↓
Vetor armazenado

Pergunta do usuário
   ↓
Embedding
   ↓
Vetor da pergunta
   ↓
Busca por similaridade
   ↓
Trechos relevantes
   ↓
LLM
   ↓
Resposta
```

Esse tipo de busca é frequentemente chamado de **busca semântica**.

## Por que é importante

Embeddings são importantes porque permitem transformar relações semânticas em uma forma que os computadores conseguem comparar matematicamente.

Eles são utilizados em diversas aplicações, como:
- **RAG:** encontrar documentos relevantes para uma pergunta;
- **busca semântica:** encontrar conteúdos pelo significado, não apenas por palavras exatas;
- **recomendação:** identificar itens semanticamente semelhantes;
- **classificação:** representar conteúdos para posteriormente classificá-los;
- **agrupamento:** encontrar grupos de conteúdos relacionados;
- **detecção de similaridade:** comparar textos ou outros dados.

A relação com RAG é especialmente importante para o que estamos estudando.

Até agora, vimos que RAG precisa **recuperar informações relevantes** antes de gerar uma resposta. Os embeddings fornecem uma das principais formas de realizar essa recuperação.

Podemos enxergar a evolução assim:

```
Documento
   ↓
Embedding
   ↓
Representação vetorial
   ↓
Busca por similaridade
   ↓
Informação relevante
   ↓
Contexto
   ↓
LLM
```

Isso também ajuda a entender por que embeddings não são apenas uma técnica de armazenamento.

Eles funcionam como uma espécie de **ponte entre linguagem e espaço matemático**. O texto continua sendo linguagem para nós, mas passa a ser representado de uma maneira que permite ao sistema calcular proximidade, similaridade e relações entre diferentes conteúdos.

Um ponto importante é que **um embedding não é uma base de conhecimento completa**. Ele representa características do conteúdo em um espaço vetorial, mas não substitui o documento original nem garante que uma resposta esteja correta.

Em sistemas RAG, normalmente armazenamos o embedding junto com uma referência ao conteúdo original. Quando um trecho é considerado relevante, o sistema recupera o texto correspondente e o fornece ao LLM.

Por isso, podemos resumir:

> **Embedding é uma representação vetorial de um dado, construída para preservar informações relevantes sobre seu significado e suas relações com outros dados.**

A partir daqui, o próximo conceito natural é **Vector Database**, porque depois de transformar documentos em vetores surge a necessidade de armazená-los e realizar buscas eficientes por similaridade.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
