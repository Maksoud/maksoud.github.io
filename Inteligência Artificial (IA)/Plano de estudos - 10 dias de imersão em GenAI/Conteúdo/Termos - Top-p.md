[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Hyperparameters Top-p

### 1. O que é?

**Top-p**, também chamado de **nucleus sampling**, é um parâmetro usado durante a geração para controlar **quais [tokens](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/) podem ser considerados na escolha do próximo token**.

A diferença fundamental em relação à [Temperature](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-temperature/) é:

> **Temperature altera as probabilidades. Top-p limita o conjunto de opções consideradas.**

### 2. Como funciona?

Imagine que o modelo calculou estas probabilidades:

```
Token A → 40%
Token B → 25%
Token C → 15%
Token D → 10%
Token E →  5%
Token F →  5%
```

Com:

```
top-p = 0.80
```

o sistema começa pelas opções mais prováveis e vai acumulando suas probabilidades:

```
A → 40%
A + B → 65%
A + B + C → 80%
```

Então, o conjunto considerado será:

```
A, B e C
```

Os demais tokens ficam fora daquela escolha.

Por isso o nome **nucleus sampling**. O modelo seleciona um "núcleo" de tokens cuja probabilidade acumulada atinge o valor de `p`.

### 3. Um exemplo simples

Imagine que você peça:

> "Complete: O cachorro correu..."

O modelo pode considerar:

```
rápido     → 35%
pela       → 25%
para       → 15%
atrás      → 10%
ontem      →  5%
...
```

Com um `top-p` mais restritivo, somente as alternativas mais prováveis entram na seleção.

Com um `top-p` maior, mais alternativas podem ser consideradas.

Assim:

```
Top-p baixo
    ↓
Poucas opções
    ↓
Mais restrição

Top-p alto
    ↓
Mais opções
    ↓
Mais variedade
```

### 4. Por que é importante?

Top-p permite controlar a **diversidade da geração** sem simplesmente escolher sempre o token mais provável.

Ele é especialmente útil quando queremos encontrar um equilíbrio entre:

```
Previsibilidade ←────────────→ Variedade
```

Um ponto importante: **Top-p e Temperature podem ser usados juntos**, mas eles controlam aspectos diferentes da geração.

Uma forma simples de memorizar:

> **Temperature mexe na distribuição de probabilidades. Top-p decide quanto dessa distribuição será considerado.**

E isso fecha bem a sequência dos conceitos que você estudou:

```
Inference
   ↓
LLM calcula probabilidades
   ↓
Temperature → modifica a distribuição
   ↓
Top-p → limita as opções consideradas
   ↓
Escolha do próximo token
```

Não é necessário decorar os valores agora. O mais importante é entender **a diferença conceitual entre Temperature e Top-p**.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-top-p/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
