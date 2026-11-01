[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Role Prompting

## O que é

**Role Prompting** é uma técnica de engenharia de prompts na qual atribuímos ao modelo um **papel, identidade ou perspectiva específica** para orientar a maneira como ele deve interpretar uma tarefa e construir sua resposta.

Em vez de simplesmente dizer:

```
Analise este código.
```

podemos dizer:

```
Atue como um engenheiro de software especializado em segurança.

Analise este código e identifique possíveis vulnerabilidades.
```

A ideia é fornecer ao modelo um **contexto de atuação** que ajude a direcionar sua resposta para determinado domínio, objetivo ou perspectiva.

## Como funciona

Imagine que você faça a mesma pergunta para três profissionais diferentes:

```
Analise este contrato.
```

Um advogado provavelmente observará cláusulas, riscos jurídicos e obrigações.

Um contador poderá se concentrar em valores, impostos e implicações financeiras.

Um gerente de projetos poderá observar prazos, responsabilidades e riscos de execução.

A pergunta é a mesma, mas o **papel atribuído ao profissional muda a perspectiva utilizada na análise**.

Com um [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/), o Role Prompting tenta produzir algo semelhante. Ao definir um papel, fornecemos ao modelo um contexto que pode influenciar quais conhecimentos, padrões de resposta e perspectivas são mais relevantes para a tarefa.

Por exemplo:

```
Atue como um professor de matemática especializado em ensinar conceitos complexos para iniciantes.

Explique o conceito de derivada para alguém que nunca estudou cálculo.
```

O papel de "professor para iniciantes" direciona a resposta para uma explicação pedagógica, em vez de simplesmente apresentar uma definição técnica.

## Um exemplo

Considere a seguinte solicitação:

```
Analise este currículo e sugira melhorias.
```

Podemos utilizar diferentes papéis:

```
Atue como um recrutador de tecnologia com experiência em contratação de profissionais de IA.

Analise este currículo e sugira melhorias para aumentar sua relevância para vagas de engenharia de IA.
```

Ou:

```
Atue como um especialista em comunicação profissional.

Analise este currículo e sugira melhorias na clareza, objetividade e apresentação das informações.
```

As duas instruções podem produzir respostas diferentes porque direcionam o modelo para **perspectivas diferentes sobre o mesmo material**.

## Por que é importante

Role Prompting é importante porque permite **direcionar a perspectiva e o estilo de raciocínio esperado do modelo** sem precisar modificar o modelo em si.

Ele pode ser útil quando:
1. A tarefa envolve um domínio específico.
2. Queremos uma determinada perspectiva profissional.
3. Precisamos adaptar a linguagem ao público.
4. Queremos que o modelo priorize determinados critérios durante uma análise.
5. Precisamos simular diferentes perspectivas sobre o mesmo problema.

Porém, existe uma ressalva importante: **atribuir um papel não transforma o modelo em um especialista real**. Dizer "você é um médico", "você é um advogado" ou "você é um engenheiro experiente" não adiciona conhecimento que o modelo não possua.

O papel funciona principalmente como uma **forma de contextualização e direcionamento**. A qualidade da resposta continuará dependendo do conhecimento do modelo, das informações fornecidas e da qualidade das instruções.

Isso também mostra uma evolução importante em relação ao [zero-shot](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-zero-shot-prompting/) e ao [few-shot prompting](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-few-shot-prompting/). No zero-shot, fornecemos a tarefa. No few-shot, adicionamos exemplos. No Role Prompting, adicionamos uma **perspectiva de atuação** para orientar a execução.

**Em uma frase:** Role Prompting é **atribuir ao modelo um papel ou perspectiva específica para direcionar como ele deve abordar uma tarefa**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-role-prompting/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
