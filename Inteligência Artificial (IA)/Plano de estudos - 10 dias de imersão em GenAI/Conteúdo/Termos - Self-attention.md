[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Self-attention

### 1. O que é?

**Self-Attention** é um mecanismo pelo qual cada token de uma sequência pode **analisar a relação com os outros tokens da própria sequência**.

O termo _self_ vem justamente daí. A atenção acontece dentro da própria sequência.

O conceito foi central na arquitetura Transformer apresentada no artigo _Attention Is All You Need_, de 2017. [Google Pesquisa](https://research.google/pubs/attention-is-all-you-need/?utm_source=chatgpt.com)

### 2. Como funciona?

Imagine:

> "O cachorro perseguiu o gato porque ele estava assustado."

Para interpretar **"ele"**, o modelo precisa avaliar quais outros tokens da frase têm relação com ele.

O Self-Attention permite fazer isso:

```
"ele"
  ↓
analisa os demais tokens
  ↓
cachorro  → relação forte
gato      → relação menor
porque    → relação menor
estava    → relação menor
```

Os valores de atenção são calculados matematicamente. O resultado é uma nova representação do token que incorpora informações relevantes do restante da sequência.

Uma característica importante é que isso permite capturar relações entre tokens que estão **distantes entre si**. [Attention Is All You Need](https://attentionisallyouneed.uk/?utm_source=chatgpt.com)

### 3. Um exemplo simples

Considere:

> "O banco aprovou o empréstimo porque precisava avaliar o risco."

Quando o modelo processa **"banco"**, ele pode estabelecer relações com palavras como:

```
banco
 ↓
empréstimo
 ↓
avaliar
 ↓
risco
```

Essas relações ajudam a construir uma representação contextual de "banco" associada ao contexto financeiro.

Se a frase fosse:

> "Sentei no banco da praça."

as relações seriam diferentes:

```
banco
 ↓
sentei
 ↓
praça
```

Portanto, o significado representado pelo modelo depende do contexto.

### 4. Por que é importante?

O Self-Attention é uma das principais características que tornam o Transformer tão eficiente para trabalhar com linguagem. A arquitetura consegue relacionar diferentes posições de uma sequência diretamente, em vez de depender de um processamento necessariamente sequencial como nas arquiteturas recorrentes anteriores. [Google Pesquisa](https://research.google/pubs/attention-is-all-you-need/?utm_source=chatgpt.com)

Uma forma boa de guardar:

> **Attention é o mecanismo de atenção. Self-Attention é quando essa atenção relaciona os elementos dentro da própria sequência.**

E um detalhe que será útil quando chegarmos aos próximos conceitos: **Self-Attention utiliza as chamadas Query, Key e Value para calcular essas relações**. 

---
### Complemento: Query, Key e Value

Para realizar essa operação, o Transformer transforma cada token em três representações:

**Query (Q)**  
Representa o que o token está procurando ou tentando entender.

**Key (K)**  
Representa quais características aquele token oferece para ser encontrado.

**Value (V)**  
Representa a informação que será utilizada caso aquele token seja considerado relevante.

Uma analogia simples seria uma busca:

```
Query
"Que informação é relevante para mim?"

        ↓

Keys
"Eu tenho esta informação."
"Eu tenho aquela informação."
"Eu tenho outra informação."

        ↓

Attention
"Qual delas é mais relevante?"

        ↓

Values
"Então vou utilizar esta informação."
```

O cálculo de attention determina o quanto cada **Key** combina com uma **Query** e usa esses resultados para combinar os **Values**.

Você não precisa decorar as fórmulas agora. Para o seu material, basta guardar:

> **Self-Attention permite que cada token considere os outros tokens da sequência, enquanto Query, Key e Value são as representações usadas para calcular e aplicar essas relações.**


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-self-attention/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
