[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Attention

### 1. O que é?

**Attention (atenção)** é um mecanismo que permite ao modelo **determinar quais partes de uma entrada são mais relevantes para interpretar cada parte do texto**.

É um dos conceitos mais importantes da arquitetura **Transformer**.

A ideia intuitiva é:

> Em vez de tratar todas as palavras igualmente, o modelo aprende **onde prestar atenção**.

---

### 2. Como funciona?

Considere:

> **"O cachorro perseguiu o gato porque ele estava assustado."**

Para entender a palavra **"ele"**, o modelo precisa considerar o restante da frase.

O mecanismo de attention permite que o modelo atribua diferentes "pesos" às palavras:

```
O cachorro perseguiu o gato porque ele estava assustado
             ↑              ↑
          relevante      relevante
```

O modelo pode aprender que **"ele"** tem uma relação mais forte com **"cachorro"** do que com outras palavras.

Matematicamente, o mecanismo calcula algo parecido com:

```
"ele"
  ↓
Quanto devo prestar atenção em cada token?
  ↓
cachorro → 0.65
gato     → 0.12
porque   → 0.05
estava   → 0.08
...
```

Os números acima são apenas ilustrativos.

---

### 3. Um exemplo simples

Veja duas frases:

> **"O banco aprovou o empréstimo."**

> **"Sentei no banco da praça."**

A palavra **"banco"** tem significados diferentes.

O contexto ao redor ajuda o modelo a determinar qual significado faz sentido.

No Transformer, a attention permite que cada token considere **outros tokens do contexto** para construir uma representação mais adequada.

Por isso, podemos pensar:

```
TOKEN
  ↓
"banco"
  ↓
Attention
  ↓
olha para o contexto
  ↓
"empréstimo" → contexto financeiro
```

versus:

```
TOKEN
  ↓
"banco"
  ↓
Attention
  ↓
olha para o contexto
  ↓
"praça" → contexto de assento
```

---

### 4. Por que é importante?

Porque a attention é uma das principais razões pelas quais os **Transformers conseguem lidar tão bem com contexto e relações entre tokens**.

Ela é fundamental para entender como funcionam os LLMs modernos.

A relação entre os conceitos que você já viu começa a ficar assim:

```
Texto
  ↓
Tokenization
  ↓
Tokens
  ↓
Transformer
  ↓
Attention
  ↓
Representações contextuais
  ↓
Predição de próximos tokens
```

### Uma observação importante

Você provavelmente vai encontrar daqui para frente os termos **Self-Attention**, **Query (Q)**, **Key (K)** e **Value (V)**.

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


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-attention/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
