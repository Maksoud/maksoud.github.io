[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Hyperparameters Temperature

### 1. O que é?

**Temperature** é um parâmetro usado durante a geração de texto para controlar o **grau de aleatoriedade na escolha dos próximos tokens**.

De forma intuitiva:

> **Temperature baixa tende a tornar a resposta mais previsível. Temperature alta tende a aumentar a variedade das respostas.**

Ela não altera o conhecimento que o modelo possui nem seus parâmetros aprendidos.

### 2. Como funciona?

O LLM calcula probabilidades para os possíveis próximos tokens.

Por exemplo:

```
"O Brasil fica na América..."

Sul       → 70%
Latina    → 20%
do Norte  →  5%
Central   →  3%
...
```

A temperature altera a distribuição dessas probabilidades antes de o modelo escolher o próximo token.

Com uma **temperature baixa**, as opções mais prováveis ficam muito favorecidas:

```
Sul       → ███████████████
Latina    → ██
do Norte  → ▏
```

Com uma **temperature mais alta**, a distribuição fica mais equilibrada:

```
Sul       → ████████
Latina    → █████
do Norte  → ██
Central   → ██
```

Isso aumenta a possibilidade de o modelo escolher alternativas menos prováveis.

### 3. Um exemplo simples

Imagine pedir:

> "Crie um slogan para uma empresa de tecnologia."

Com temperature baixa, você tende a obter respostas mais previsíveis e consistentes.

Com temperature alta, pode obter ideias mais variadas, inesperadas ou criativas.

Por isso, de forma geral:

```
Temperature baixa
       ↓
Mais previsibilidade
Mais consistência
Menos variedade

Temperature alta
       ↓
Mais variedade
Mais criatividade
Menos previsibilidade
```

Isso não significa que **temperature alta = melhor criatividade** em qualquer situação. Existe um ponto em que aumentar a aleatoriedade pode simplesmente produzir respostas menos coerentes.

### 4. Por que é importante?

Temperature é importante porque permite adaptar a geração ao tipo de tarefa.

Para tarefas em que você quer **consistência e previsibilidade**, uma configuração mais baixa pode ser adequada.

Para tarefas em que você quer **explorar diferentes possibilidades**, uma configuração mais alta pode ser útil.

Um ponto importante para guardar:

> **Temperature atua na distribuição de probabilidade dos próximos tokens durante a inferência. Ela não modifica os parâmetros aprendidos pelo modelo.**

E isso conecta diretamente com os conceitos anteriores:

```
Prompt
  ↓
Inference
  ↓
LLM calcula probabilidades
  ↓
Temperature ajusta a distribuição
  ↓
Escolha do próximo token
  ↓
Próximo token
  ↓
...
```

**Observação:** os valores exatos e o comportamento de `temperature = 0` podem variar entre APIs e modelos. Portanto, não é bom memorizar que "0 sempre significa completamente determinístico".


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-temperature/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
