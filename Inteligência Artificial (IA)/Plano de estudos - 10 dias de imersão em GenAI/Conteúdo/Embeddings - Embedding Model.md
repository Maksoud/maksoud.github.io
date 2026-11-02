[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Embedding Model

## O que é

**Embedding Model** é um modelo de IA especializado em transformar informações, como textos, em **vetores numéricos que representam suas características semânticas**.

É o componente responsável por gerar os embeddings que estudamos anteriormente.

No contexto de RAG, o Embedding Model normalmente recebe cada chunk durante a ingestão e transforma seu conteúdo em um vetor:

```
Chunk
   ↓
Embedding Model
   ↓
Vector Embedding
   ↓
Vector Database
```

Quando o usuário faz uma pergunta, o mesmo princípio é aplicado:

```
Pergunta
   ↓
Embedding Model
   ↓
Vector da pergunta
   ↓
Vector Search
   ↓
Chunks relevantes
```

Assim, o Embedding Model funciona como uma espécie de **ponte entre linguagem e representação matemática**, permitindo que o sistema compare conteúdos pelo significado.

## Como funciona

Imagine que precisamos colocar milhares de textos em um mapa.

O Embedding Model analisa cada texto e determina uma posição nesse espaço matemático com base em suas características semânticas.

Por exemplo:

```
"Como solicitar férias?"
        ↓
   Embedding Model
        ↓
[0.21, -0.73, 0.45, ...]
```

Outro texto:

```
"Qual é o procedimento para marcar férias?"
        ↓
   Embedding Model
        ↓
[0.19, -0.70, 0.48, ...]
```

Como os conteúdos possuem significado semelhante, seus vetores tendem a ficar próximos no espaço vetorial.

Já um texto sobre culinária provavelmente será representado em uma região diferente:

```
"Como preparar uma pizza?"
        ↓
   Embedding Model
        ↓
[0.81, 0.12, -0.64, ...]
```

O modelo não está simplesmente transformando palavras em números. Durante seu treinamento, ele aprende representações que capturam relações entre conteúdos.

Isso permite que conceitos diferentes, mas semanticamente relacionados, tenham representações próximas.

Um ponto importante é que **o Embedding Model não é o LLM responsável por gerar a resposta final**. Ele possui uma função diferente.

```
Embedding Model
→ representa informações como vetores

LLM
→ interpreta informações e gera respostas
```

## Um exemplo

Imagine que uma empresa tenha estes três chunks:

```
Chunk A:
"Funcionários devem solicitar férias com 30 dias
de antecedência."

Chunk B:
"O pedido de férias precisa ser enviado ao gestor
com antecedência mínima de um mês."

Chunk C:
"Funcionários podem solicitar reembolso de despesas
pelo sistema financeiro."
```

Durante a ingestão, o Embedding Model transforma cada chunk em um vetor:

```
Chunk A → Embedding Model → Vetor A
Chunk B → Embedding Model → Vetor B
Chunk C → Embedding Model → Vetor C
```

Os vetores A e B provavelmente ficarão próximos porque os textos tratam de um assunto semelhante.

Agora o usuário pergunta:

> "Com quanto tempo de antecedência devo pedir férias?"

A pergunta também passa pelo Embedding Model:

```
Pergunta
   ↓
Embedding Model
   ↓
Vetor da pergunta
```

O sistema compara esse vetor com os vetores armazenados.

```
Vetor da pergunta
       ↓
   comparação
       ↓
┌─────────────────────┐
│ Chunk A   → próximo │
│ Chunk B   → próximo │
│ Chunk C   → distante│
└─────────────────────┘
```

Os chunks A e B podem então ser recuperados e enviados ao LLM como contexto para gerar a resposta.

O Embedding Model, portanto, não responde diretamente à pergunta. Ele ajuda o sistema a **encontrar a informação que deverá ser utilizada para respondê-la**.

## Por que é importante

O Embedding Model é uma peça fundamental de sistemas que dependem de **busca semântica**, incluindo RAG.

A qualidade desse modelo influencia a capacidade do sistema de identificar quais conteúdos são semanticamente relacionados à pergunta.

Um Embedding Model inadequado pode produzir representações que não distinguem bem determinados conceitos. Isso pode fazer com que o retrieval encontre documentos pouco relevantes, mesmo que o restante do pipeline esteja corretamente configurado.

Por isso, a escolha do modelo envolve características como:
- capacidade de representar o idioma utilizado;
- qualidade das representações semânticas;
- dimensão dos vetores;
- velocidade de processamento;
- custo;
- tamanho máximo de entrada;
- adequação ao domínio da aplicação.

Também é importante que o modelo utilizado para gerar os embeddings dos documentos seja compatível com o utilizado para gerar os embeddings das consultas. Caso contrário, os vetores podem não estar em um espaço comparável.

A relação com os conceitos anteriores pode ser resumida assim:

```
Chunking
   ↓
divide o documento em unidades

Embedding Model
   ↓
transforma cada unidade em vetor

Vector Embedding
   ↓
representação numérica do conteúdo

Vector Database
   ↓
armazena os vetores

Vector Search
   ↓
compara o vetor da pergunta com os vetores armazenados

Retrieval
   ↓
seleciona os chunks relevantes

LLM
   ↓
utiliza o contexto para gerar a resposta
```

O ponto central é: **o Embedding Model transforma conteúdos em representações vetoriais que permitem ao sistema comparar e recuperar informações com base em significado, sendo uma das peças fundamentais do mecanismo de busca semântica em RAG.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-embedding-model/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
