[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Generation (Geração de texto)

## O que é?

**Geração** é o processo pelo qual um LLM produz a resposta. Ela acontece durante a [inferência](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-inference/) e segue uma regra simples:

> **O modelo gera um [token](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/) por vez, sempre olhando para tudo o que veio antes.**

Esse modo de funcionar se chama **geração autorregressiva**: cada token escolhido é acrescentado ao texto e passa a fazer parte da entrada para escolher o próximo.

## Como funciona?

O ciclo se repete até a resposta terminar:

```
Prompt + texto já gerado
        ↓
Modelo calcula a probabilidade de cada token possível
        ↓
Temperature e top-p ajustam essas probabilidades
        ↓
Uma estratégia escolhe o próximo token
        ↓
Token é acrescentado ao texto
        ↓
Repete
```

Exemplo com o prompt "O céu está":

```
Passo 1: "O céu está" → "azul"
Passo 2: "O céu está azul" → "e"
Passo 3: "O céu está azul e" → "limpo"
Passo 4: "O céu está azul e limpo" → "."
```

O modelo não planeja a frase inteira de uma vez. Ele decide token a token.

## Estratégias de escolha do próximo token (decoding)

Depois de calcular as probabilidades, é preciso decidir qual token usar. As principais estratégias são:
- **Greedy decoding**: escolhe sempre o token mais provável. É previsível e repetitivo, e equivale a uma [temperature](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-temperature/) igual a zero.
- **Sampling (amostragem)**: sorteia o token de acordo com as probabilidades. Um token com 40% de chance sai mais vezes, mas não sempre. Gera variedade.
- **Top-k**: sorteia apenas entre os `k` tokens mais prováveis (por exemplo, os 50 primeiros).
- **[Top-p](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-top-p/)**: sorteia entre os tokens mais prováveis até somar a probabilidade `p`.
- **Beam search**: acompanha várias sequências candidatas ao mesmo tempo e fica com a de maior probabilidade total. Muito usada em tradução automática, pouco usada em chatbots.

## Quando a geração para?

A resposta termina quando acontece uma destas situações:
- O modelo gera um **token de fim** (end of sequence), indicando que a resposta acabou.
- Atinge o limite de **max tokens** definido na chamada da API.
- Aparece uma **stop sequence**, um texto configurado para interromper a geração.

Se a resposta for cortada no meio, normalmente o motivo é o limite de max tokens.

## Por que é importante?

Entender a geração explica vários comportamentos dos LLMs:
- **Respostas diferentes para o mesmo prompt**: com sampling, cada execução pode sortear tokens diferentes.
- **[Alucinações](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-hallucination/)**: o modelo escolhe o token plausível, não necessariamente o verdadeiro. Um erro no começo pode se propagar pelo resto do texto.
- **Custo e tempo**: cada token de saída exige um novo passo do modelo, por isso respostas longas demoram e custam mais.
- **Streaming**: como os tokens saem um a um, as interfaces conseguem mostrar a resposta sendo escrita.

Uma forma simples de memorizar:

> **O modelo calcula probabilidades, temperature e top-p ajustam as opções, a estratégia de decoding escolhe o token, e o ciclo se repete até um critério de parada.**

```
Probabilidades → Temperature → Top-p → Escolha → Próximo token → ... → Fim
```

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-generation/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
