[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Token
### 1. O que é?

**Token** é uma unidade de texto que o LLM consegue processar.

Um token **não é necessariamente uma palavra**. Dependendo do texto, pode ser uma palavra inteira, parte de uma palavra, pontuação ou até um espaço associado a caracteres.

Por exemplo, a frase:

> `Eu gosto de programação.`

poderia ser dividida aproximadamente em:

```
"Eu" | " gosto" | " de" | " programação" | "."
```

A divisão exata depende do **tokenizador** utilizado pelo modelo.

### 2. Como funciona?

Antes de o LLM processar seu texto, ele passa por um processo chamado **tokenização**:

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

Por exemplo:

```
"Olá, mundo!"
       ↓
["Olá", ",", " mundo", "!"]
       ↓
[15432, 11, 8921, 0]   ← IDs ilustrativos
```

O modelo não trabalha diretamente com as palavras como nós as enxergamos. Ele trabalha com **representações numéricas desses tokens**.

### 3. Um exemplo interessante

Uma palavra pouco comum pode ser dividida em vários tokens.

Por exemplo, imagine:

```
"internacionalização"
```

O tokenizador pode dividi-la em algo parecido com:

```
"inter" | "nacional" | "ização"
```

Enquanto uma palavra muito comum pode ser um único token.

Por isso, **número de palavras ≠ número de tokens**.

### 4. Por que é importante?

Porque praticamente tudo em LLMs está relacionado a tokens.

Quando você ouvir:
- **context window de 128k tokens**
- **custo de X dólares por milhão de tokens**
- **input tokens / output tokens**
- **token limit**
- **tokenização**

todos estão falando dessa unidade.

E existe uma consequência prática importante:

> **Quanto mais tokens você coloca no contexto, mais informação o modelo precisa processar e, em geral, maior pode ser o custo e o tempo de inferência.**

Uma forma simples de guardar:

> **Token é a unidade básica de texto que um LLM processa.**

E a relação com o que vimos até agora fica:

```
Texto
  ↓
Tokenização
  ↓
Tokens
  ↓
Transformer
  ↓
LLM
  ↓
Próximos tokens
  ↓
Texto gerado
```

Essa sequência é uma das bases para entender LLMs.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
