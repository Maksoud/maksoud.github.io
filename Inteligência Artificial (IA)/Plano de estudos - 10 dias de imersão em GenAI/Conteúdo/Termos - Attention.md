[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Attention

### 1. O que é?

**Attention (atenção)** é um mecanismo que permite ao modelo **determinar quais partes de uma entrada são mais relevantes para interpretar cada parte do texto**.

É um dos conceitos mais importantes da arquitetura **[Transformer](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-transformer/)**.

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

No Transformer, a attention permite que cada [token](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/) considere **outros tokens do contexto** para construir uma representação mais adequada.

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

Ela é fundamental para entender como funcionam os [LLMs](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) modernos.

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

Você provavelmente vai encontrar daqui para frente os termos **[Self-Attention](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-self-attention/)**, **Query (Q)**, **Key (K)** e **Value (V)**.

---
### Complemento: Query, Key e Value

Attention funciona como uma **busca por relevância**. Para isso, a informação é organizada em três papéis:
- **Query (Q)**: a pergunta. O que este ponto da sequência precisa saber agora?
- **Key (K)**: a etiqueta. O que cada elemento disponível oferece?
- **Value (V)**: o conteúdo. A informação que de fato será entregue.

Uma analogia é a busca em uma biblioteca:
- A **Query** é o assunto que você procura ("receitas com chocolate").
- As **Keys** são os títulos e etiquetas dos livros na estante.
- Os **Values** são o conteúdo dos livros.

Você compara o seu assunto com as etiquetas, percebe quais livros combinam mais e lê principalmente esses, sem ignorar totalmente os outros.

O cálculo segue três passos:
- **Comparar**: a Query é comparada com cada Key, gerando uma pontuação de compatibilidade.
- **Normalizar**: as pontuações viram pesos que somam 100% (função softmax).
- **Combinar**: os Values são misturados de acordo com esses pesos. Quem pontuou mais contribui mais.

Na notação do artigo "Attention Is All You Need" (2017):

```
Attention(Q, K, V) = softmax(Q · Kᵀ / √d) · V
```

O "√d" só serve para manter os números em uma escala estável.

Um detalhe importante: Query, Key e Value **não precisam vir da mesma sequência**. Na tradução, por exemplo, a Query vem da frase que está sendo gerada e as Keys e Values vêm da frase original (isso se chama **Cross-Attention**). Quando os três vêm da mesma sequência, temos o **Self-Attention**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-attention/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
