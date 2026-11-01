[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Parameters

### 1. O que é?

Em um [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/), **parameters são os valores numéricos que o modelo aprende durante o treinamento.** Eles determinam como o modelo transforma os dados de entrada em previsões. [Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/journey/llm-fundamentals?utm_source=chatgpt.com)

Uma forma intuitiva de pensar:

> **Os parâmetros são os "ajustes internos" que o modelo aprendeu para reconhecer padrões.**

Quando você vê algo como:

```
Modelo 7B
Modelo 70B
Modelo 405B
```

o número indica aproximadamente a quantidade de **bilhões de parâmetros** do modelo.

### 2. Como funciona?

Durante o treinamento, o modelo recebe muitos exemplos e tenta prever os próximos [tokens](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/).

Quando erra, um processo de otimização ajusta seus parâmetros para reduzir o erro.

De forma simplificada:

```
Texto de treinamento
        ↓
       LLM
        ↓
  previsão do token
        ↓
    erro calculado
        ↓
 parâmetros ajustados
        ↓
       LLM
        ↓
   nova previsão
```

Esse processo acontece repetidamente em uma quantidade enorme de exemplos.

Ao final, os parâmetros armazenam **padrões estatísticos aprendidos durante o treinamento**. Eles não são uma coleção de documentos ou fatos armazenados individualmente. [Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/journey/llm-fundamentals?utm_source=chatgpt.com)

### 3. Um exemplo simples

Imagine uma rede neural muito pequena com apenas três parâmetros:

```
Parâmetro A = 0,7
Parâmetro B = 1,2
Parâmetro C = -0,4
```

Esses números influenciam os cálculos realizados pelo modelo.

Um LLM real possui **bilhões desses valores**, distribuídos pelas diferentes partes da arquitetura [Transformer](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-transformer/). [BfDI](https://www.bfdi.bund.de/SharedDocs/Downloads/EN/Berlin-Group/20241206-WP-LLMs.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)

É por isso que você verá expressões como:

> "Esse é um modelo de 70 bilhões de parâmetros."

Isso significa que existem aproximadamente **70 bilhões de valores aprendidos dentro da rede**.

### 4. Por que é importante?

O número de parâmetros é uma indicação da **capacidade e do tamanho do modelo**, mas não significa automaticamente que um modelo maior seja melhor.

Um modelo com mais parâmetros pode representar padrões mais complexos, mas **qualidade dos dados, arquitetura, treinamento e pós treinamento também são fundamentais**. [Google for Developers](https://developers.google.com/machine-learning/crash-course/llm/transformers?utm_source=chatgpt.com)

Existe ainda uma distinção importante para sua lista:

**Parameters ≠ Hyperparameters**

Parâmetros são aprendidos pelo modelo durante o treinamento.

Hyperparameters são configurações definidas para controlar aspectos do treinamento ou da geração. **[Temperature](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-temperature/)** e **[top-p](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-top-p/)**, por exemplo, são hyperparameters utilizados na [inferência](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-inference/). [IBM](https://www.ibm.com/think/topics/llm-parameters?trk=article-ssr-frontend-pulse_little-text-block&utm_source=chatgpt.com)

### Para guardar

> **Parameters são os valores numéricos aprendidos durante o treinamento que determinam o comportamento interno do LLM.**

E isso conecta com os conceitos anteriores:

```
Transformer
    ↓
possui muitas camadas
    ↓
cada camada possui parâmetros
    ↓
parâmetros são ajustados durante o treinamento
    ↓
modelo aprende padrões
    ↓
durante a inferência, usa esses parâmetros
    ↓
gera os próximos tokens
```

A ideia mais importante aqui é **não confundir "70 bilhões de parâmetros" com "70 bilhões de informações ou fatos"**. Parâmetros são números que, em conjunto, permitem ao modelo representar padrões complexos.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-parameters/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
