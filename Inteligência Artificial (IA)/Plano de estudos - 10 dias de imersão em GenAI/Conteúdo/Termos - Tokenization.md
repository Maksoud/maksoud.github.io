[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Tokenization

### 1. O que é?

**Tokenization (tokenização)** é o processo de **dividir um texto em [tokens](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/)** para que o [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) consiga processá-lo.

Se **token** é a unidade, **tokenização** é o processo de transformar o texto nessas unidades.

### 2. Como funciona?

De forma simplificada:

```
Texto
  ↓
Tokenizador
  ↓
Tokens
  ↓
IDs numéricos
  ↓
LLM
```

Por exemplo, um texto como:

> `Eu gosto de IA.`

poderia ser tokenizado aproximadamente como:

```
["Eu", " gosto", " de", " IA", "."]
```

Cada token recebe então um **ID numérico** que o modelo consegue processar.

Importante: **a tokenização depende do modelo**. Dois LLMs podem dividir exatamente o mesmo texto de maneiras diferentes.

### 3. Um exemplo

Considere:

> `programação`

Dependendo do tokenizador, poderia virar:

```
["program", "ação"]
```

Enquanto uma palavra muito comum poderia permanecer como um único token.

Isso também explica por que uma palavra em português pode consumir uma quantidade de tokens diferente da mesma palavra em inglês.

### 4. Por que é importante?

Porque a tokenização determina, entre outras coisas:
- **quanto texto cabe no contexto do modelo**;
- **quanto uma requisição pode custar**;
- **quantos tokens serão processados na entrada e na saída**;
- **a eficiência do modelo para diferentes idiomas e tipos de texto**.

Um detalhe importante para quem trabalha com LLMs:

> **O LLM não "vê" diretamente palavras; ele recebe uma sequência de tokens representados numericamente.**

E a relação entre os três conceitos que você já perguntou fica bem clara:

```
TOKEN
  ↓
unidade de texto

TOKENIZATION
  ↓
processo de transformar texto em tokens

TRANSFORMER
  ↓
arquitetura que processa essas representações
```

Isso já é suficiente para entender o conceito de **tokenization**.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-tokenization/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
