[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Semantic Similarity

## O que é

**Semantic Similarity**, ou **similaridade semântica**, é a medida de quanto dois conteúdos possuem significados relacionados, mesmo quando utilizam palavras ou estruturas diferentes.

Em sistemas de IA, essa relação pode ser calculada comparando as representações vetoriais, ou **embeddings**, dos conteúdos.

Por exemplo:

```
"Como solicitar férias?"
"Qual é o procedimento para marcar férias?"
```

As frases são diferentes na forma, mas possuem significado muito próximo.

Já:

```
"Como solicitar férias?"
"Como preparar uma pizza?"
```

possuem palavras em comum, como "como", mas apresentam significados muito diferentes.

A similaridade semântica procura justamente capturar **o significado e a relação entre os conteúdos**, e não apenas a quantidade de palavras iguais.

## Como funciona

Imagine que cada frase seja transformada em um ponto dentro de um espaço matemático por um modelo de embeddings.

Frases semanticamente semelhantes tendem a ficar próximas:

```
"Como solicitar férias?"
        ●
          ●
"Como marcar minhas férias?"
```

Enquanto frases com significados diferentes tendem a ficar mais distantes:

```
"Como solicitar férias?" ●


                         ● "Como preparar uma pizza?"
```

O sistema pode então calcular uma medida de proximidade entre os vetores.

Uma técnica bastante utilizada é a **similaridade de cosseno**:

$$  
\text{similaridade}(A,B)=\frac{A\cdot B}{|A||B|}  
$$

De forma simplificada, quanto mais semelhantes forem as direções dos dois vetores, maior será a similaridade.

O importante é entender que o cálculo acontece sobre os **vetores**, mas o que queremos capturar é uma relação de **significado**.

## Um exemplo

Imagine que uma base de conhecimento tenha os seguintes documentos:

```
Documento A:
Como solicitar férias pelo sistema interno?

Documento B:
Procedimentos para reembolso de despesas.

Documento C:
Como alterar o período de férias solicitado?
```

O usuário pergunta:

```
Como posso marcar minhas férias?
```

A pergunta é transformada em um embedding.

Os documentos também possuem embeddings.

O sistema calcula a similaridade entre o vetor da pergunta e os vetores dos documentos:

```
Pergunta
    ↓
Embedding
    ↓
Comparação
    ↓
Documento A  → alta similaridade
Documento B  → baixa similaridade
Documento C  → alta similaridade
```

O sistema pode então recuperar os documentos A e C como candidatos relevantes.

Esse mecanismo é especialmente importante em **RAG**, porque permite encontrar informações relacionadas à pergunta mesmo quando o vocabulário utilizado pelo usuário é diferente daquele utilizado nos documentos.

Por exemplo:

```
Usuário:
"Como marcar minhas férias?"

Documento:
"Procedimento para solicitação do período de descanso."
```

Uma busca baseada apenas em correspondência exata de palavras poderia ter dificuldade para relacionar os dois textos.

A busca semântica, utilizando embeddings, pode identificar que eles tratam de um assunto semelhante.

## Por que é importante

Semantic Similarity é importante porque permite que sistemas de IA façam buscas e comparações levando em consideração **relações de significado**, e não apenas correspondências literais.

Ela é utilizada em:
- **RAG:** encontrar documentos relevantes para uma pergunta;
- **busca semântica:** recuperar conteúdos relacionados;
- **recomendação:** encontrar itens semelhantes;
- **classificação:** identificar conteúdos relacionados a determinadas categorias;
- **agrupamento:** reunir conteúdos semanticamente próximos;
- **detecção de duplicidade:** identificar textos que expressam ideias semelhantes.

A relação entre os conceitos estudados pode ser visualizada assim:

```
Texto
  ↓
Embedding Model
  ↓
Vector Embedding
  ↓
Espaço vetorial
  ↓
Semantic Similarity
  ↓
Encontrar conteúdos relacionados
```

Isso também ajuda a diferenciar **similaridade lexical** de **similaridade semântica**.

**Similaridade lexical** observa principalmente as palavras utilizadas.

```
"comprar um carro"
"comprar um carro novo"
```

As frases possuem várias palavras em comum.

**Similaridade semântica** procura identificar se os conteúdos expressam ideias relacionadas, mesmo quando utilizam vocabulários diferentes:

```
"comprar um carro"
"adquirir um automóvel"
```

Essa capacidade é uma das razões pelas quais embeddings são tão importantes para RAG.

No entanto, **similaridade semântica não significa equivalência absoluta**. Dois textos podem tratar do mesmo assunto e ainda apresentar informações diferentes ou até contraditórias.

Por exemplo:

```
"Clientes podem cancelar em até 30 dias."

"Clientes podem cancelar em até 7 dias."
```

Os textos possuem alta similaridade semântica porque tratam do mesmo assunto, mas a informação é diferente.

Por isso, em um sistema RAG, encontrar um documento semanticamente semelhante é apenas uma etapa. O sistema ainda precisa **recuperar o conteúdo correto, interpretar seu contexto e verificar se ele realmente responde à pergunta**.

Em resumo:

> **Semantic Similarity é a capacidade de medir o grau de relação de significado entre diferentes conteúdos, permitindo que sistemas de IA encontrem informações relacionadas mesmo quando elas são expressas de maneiras diferentes.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-semantic-similarity/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
