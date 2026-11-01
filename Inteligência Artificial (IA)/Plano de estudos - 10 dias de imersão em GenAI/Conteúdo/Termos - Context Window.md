[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Context Window

### 1. O que é?

**Context Window**, ou **janela de contexto**, é a quantidade máxima de **[tokens](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/) que um modelo consegue considerar dentro de uma interação**. [Claude Platform](https://platform.claude.com/docs/pt-BR/build-with-claude/context-windows?utm_source=chatgpt.com)

Pense nela como a **memória de trabalho do [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) durante aquela requisição**.

Não é a quantidade de informação que o modelo aprendeu durante o treinamento. É a quantidade de informação que ele consegue **ter disponível naquele momento** para produzir uma resposta. [Claude Platform](https://platform.claude.com/docs/pt-BR/build-with-claude/context-windows?utm_source=chatgpt.com)

### 2. Como funciona?

Imagine que um modelo tenha uma janela de contexto de **100.000 tokens**.

Dentro dela podem estar:

```
┌──────────────────────────────────────────┐
│ Instruções                               │
│ Histórico da conversa                    │
│ Sua pergunta atual                       │
│ Documentos enviados                      │
│ Resultados de buscas / ferramentas       │
│ Resposta que o modelo está gerando       │
└──────────────────────────────────────────┘
              ↓
        100.000 tokens
```

Tudo isso precisa caber no limite do modelo. [Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/journey/llm-fundamentals?utm_source=chatgpt.com)

Por isso, **context window é medido em tokens, não em palavras**.

### 3. Um exemplo simples

Imagine uma conversa muito longa.

No começo:

```
Usuário → informações
LLM     → respostas
```

Depois de muitas mensagens:

```
Usuário → informações
LLM     → respostas
Usuário → mais informações
LLM     → mais respostas
...
```

O contexto vai ficando maior.

Se a quantidade de tokens ultrapassar a capacidade da janela, o sistema precisa **reduzir ou administrar o contexto**, por exemplo resumindo partes anteriores, removendo informações antigas ou recuperando apenas informações relevantes. [Claude Platform](https://platform.claude.com/docs/pt-BR/build-with-claude/context-windows?utm_source=chatgpt.com)

### 4. Por que é importante?

Porque o tamanho da janela influencia diretamente o tipo de tarefa que podemos fazer.

Uma janela maior permite trabalhar com:

**Documentos maiores**

```
PDF grande
   ↓
LLM
```

**Conversas mais longas**

```
Histórico extenso
   ↓
LLM
```

**Mais contexto em [RAG](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-rag/)**

```
Pergunta
   ↓
Documentos recuperados
   ↓
Context Window
   ↓
LLM
```

Mas existe uma ideia importante aqui:

> **Uma janela maior não significa automaticamente que o modelo vai usar melhor toda aquela informação.**

Quando existe contexto demais, pode haver dificuldade para encontrar ou utilizar corretamente informações específicas. Esse problema é estudado, entre outras formas, como **context rot**. [Claude Platform](https://platform.claude.com/docs/pt-BR/build-with-claude/context-windows?utm_source=chatgpt.com)

### Para guardar

> **Context Window é o espaço de trabalho temporário do LLM: a quantidade de tokens que ele consegue considerar em uma requisição.**

E isso conecta diretamente com o que você já estudou:

```
Texto
 ↓
Tokenization
 ↓
Tokens
 ↓
Context Window
 ↓
Transformer / Attention
 ↓
Resposta
```

Um detalhe que vale guardar para mais tarde: **context window não é memória permanente**. É uma diferença importante quando começarmos a falar de sistemas que precisam manter informações entre diferentes interações.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-context-window/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
