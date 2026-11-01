[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Transformer
### 1. O que é?

**Transformer** é uma **arquitetura de rede neural** criada para trabalhar especialmente bem com dados sequenciais, como texto.

Ela foi apresentada no artigo de 2017 **“Attention Is All You Need”** e se tornou a arquitetura fundamental por trás de grande parte dos LLMs modernos.

Uma distinção importante:

> **LLM é o modelo/aplicação de linguagem em grande escala. Transformer é a arquitetura que pode ser usada para construir esse modelo.**

### 2. Como funciona?

O grande diferencial do Transformer é o mecanismo chamado **Attention (atenção)**.

Imagine a frase:

> "O cachorro correu atrás do gato porque **ele** estava assustado."

Para interpretar "ele", precisamos considerar outras palavras da frase. O mecanismo de atenção permite que o modelo avalie **quais partes da entrada são mais relevantes umas para as outras**.

De forma simplificada:

```
"O cachorro correu atrás do gato porque ele estava assustado."
                         ↓
                    Attention
                         ↓
        Quais palavras estão relacionadas?
                         ↓
              representação contextual
```

Isso é muito poderoso porque o modelo consegue analisar **relações entre diferentes partes do texto**, inclusive quando estão distantes umas das outras.

### 3. Um exemplo simples

Compare:

> "João colocou o livro sobre a mesa porque **ela** estava limpa."

e:

> "João colocou o livro sobre a mesa porque **ele** estava cansado."

O Transformer consegue usar o contexto para determinar que:

- **ela** provavelmente se refere à mesa;
- **ele** provavelmente se refere a João.

Não é simplesmente uma busca pela palavra mais próxima. A **atenção permite considerar o contexto**.

### 4. Por que é importante?

Porque o Transformer é uma das principais peças que permitiram o avanço dos LLMs modernos.

Uma visão simplificada da relação é:

```
Transformer
     ↓
Arquitetura
     ↓
Modelo treinado em enormes quantidades de texto
     ↓
LLM
     ↓
Aplicações
(ChatGPT, assistentes, agentes, RAG etc.)
```

E aqui vale guardar uma ideia fundamental:

> **Attention é o mecanismo central do Transformer que permite ao modelo relacionar diferentes partes da informação de entrada e construir uma representação contextual.**

Não precisamos entrar ainda em **Self-Attention, Query, Key e Value**, esses são os próximos níveis de detalhe do Transformer.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-transformer/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
