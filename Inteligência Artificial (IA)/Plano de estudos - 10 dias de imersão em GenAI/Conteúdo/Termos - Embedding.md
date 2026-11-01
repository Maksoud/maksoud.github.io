[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Embedding

### 1. O que é?

**Embedding** é uma **representação numérica de um conteúdo**, como uma palavra, frase, documento ou imagem, em forma de um **vetor de números**.

A ideia principal é transformar algo que o computador não entende diretamente, como:

> `"gato"`

em algo como:

```
[0.21, -0.73, 0.45, 0.08, ...]
```

Esse vetor representa características semânticas daquele conteúdo.

### 2. Como funciona?

Imagine que temos:

```
"gato"
"cachorro"
"carro"
```

Um modelo de embeddings transforma cada um em um vetor:

```
gato       → [ ... ]
cachorro   → [ ... ]
carro      → [ ... ]
```

Como **gato** e **cachorro** têm significados relacionados, seus vetores tendem a ficar **próximos** em um espaço matemático.

Já **carro** tende a ficar mais distante.

Visualmente, podemos imaginar:

```
          cachorro
             ●
          ↗
       ● gato


                           ● carro
```

Essa proximidade permite trabalhar matematicamente com **similaridade semântica**.

### 3. Um exemplo prático

Imagine uma busca:

> "Como faço para recuperar minha senha?"

E você tem três documentos:

```
A → "Como alterar sua senha de acesso"
B → "Política de férias dos funcionários"
C → "Como configurar seu computador"
```

Com embeddings, podemos transformar a pergunta e os documentos em vetores e comparar a proximidade entre eles.

A pergunta provavelmente ficará mais próxima de:

```
A → "Como alterar sua senha de acesso"
```

mesmo que as palavras **não sejam exatamente iguais**.

É justamente essa característica que torna embeddings muito importantes para **busca semântica**.

### 4. Por que é importante?

Embeddings são fundamentais em aplicações como:
- **RAG**
- busca semântica
- sistemas de recomendação
- classificação
- agrupamento de documentos
- comparação de textos

No caso de RAG, por exemplo:

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
Busca por vetores semelhantes
    ↓
Documentos relevantes
    ↓
LLM
```

### Uma distinção importante

**Token e embedding não são a mesma coisa.**

```
Texto
 ↓
Tokenização
 ↓
Tokens
 ↓
Embeddings
 ↓
Representações vetoriais
```

Um **token** é uma unidade do texto.

Um **embedding** é uma representação numérica que captura características/significado daquele conteúdo.

E aqui existe um detalhe que vale guardar para depois: **embeddings não são necessariamente produzidos apenas para tokens individuais**. Existem modelos de embedding que transformam frases, parágrafos ou documentos inteiros em vetores.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-embedding/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
