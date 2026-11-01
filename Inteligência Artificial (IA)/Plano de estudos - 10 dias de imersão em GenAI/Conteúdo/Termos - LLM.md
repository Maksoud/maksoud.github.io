[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# LLM
### 1. O que é?

**LLM** significa **Large Language Model**, ou **Modelo de Linguagem de Grande Escala**.

É um tipo de modelo de IA treinado com enormes quantidades de texto para **entender e gerar linguagem humana**.

Exemplos conhecidos incluem modelos da família GPT, Claude, Gemini e Llama.

### 2. Como funciona?

De forma simplificada:

```
Texto de entrada
      ↓
   LLM
      ↓
Probabilidades dos próximos tokens
      ↓
   Próximo token
      ↓
   Próximo token
      ↓
     ...
      ↓
Texto gerado
```

O ponto fundamental é que um LLM aprende padrões da linguagem durante o treinamento.

Por exemplo, se você perguntar:

> "Qual é a capital da França?"

o modelo não está simplesmente procurando essa frase em um banco de dados. Ele utiliza os padrões e conhecimentos aprendidos durante o treinamento para produzir algo como:

> "A capital da França é Paris."

Tecnicamente, ele faz isso trabalhando com **tokens** e calculando probabilidades sobre o que deve vir a seguir.

### 3. Um exemplo simples

Imagine que você escreva:

> "O céu é"

O modelo pode calcular probabilidades aproximadamente assim:

```
azul       → 85%
nublado    →  7%
vermelho   →  3%
...
```

Ele então seleciona um token e continua o processo.

É dessa repetição que surge uma resposta aparentemente complexa.

### 4. Por que é importante?

Porque **LLM é a base de grande parte da IA generativa atual voltada para linguagem**.

Quando você ouvir termos como **RAG, agentes, prompt engineering, tool calling, fine-tuning**, normalmente existe um LLM no centro desse sistema.

Mas um detalhe importante: **LLM não é sinônimo de ChatGPT**.

O ChatGPT é uma **aplicação/sistema** que utiliza modelos de linguagem, além de outras capacidades e componentes.

**Resumo para guardar:**

> **LLM = um modelo de IA treinado em grandes volumes de dados para processar e gerar linguagem, produzindo texto token por token com base nos padrões aprendidos.**


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
