[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Prompt Chaining

## O que é

**Prompt Chaining** é uma técnica em que uma tarefa complexa é dividida em uma sequência de prompts menores, nos quais a saída de uma etapa é utilizada como entrada para a próxima.

Em vez de pedir ao modelo que execute todo o trabalho de uma só vez, construímos uma cadeia de etapas, cada uma responsável por uma parte específica do processo.

A ideia central é:

**Entrada → Prompt 1 → Resultado 1 → Prompt 2 → Resultado 2 → Prompt 3 → Resultado final**

Isso torna o processo mais controlável, porque cada etapa pode ter um objetivo, um formato e critérios de qualidade próprios.

## Como funciona

Imagine que você queira produzir um artigo completo sobre uma empresa.

Um prompt único poderia pedir:

```
Analise esta empresa, pesquise seus concorrentes,
identifique oportunidades e escreva um artigo estratégico.
```

O modelo precisaria interpretar e executar várias tarefas diferentes simultaneamente.

Com **Prompt Chaining**, podemos separar o processo:

```
Prompt 1:
Analise a empresa e identifique seus principais produtos,
clientes e diferenciais.

        ↓

Resultado 1

Prompt 2:
Com base na análise anterior, identifique os principais
concorrentes e compare seus diferenciais.

        ↓

Resultado 2

Prompt 3:
Com base nas análises anteriores, identifique oportunidades
estratégicas.

        ↓

Resultado 3

Prompt 4:
Utilize todas as análises anteriores para produzir um
relatório estratégico.
```

Cada etapa recebe o resultado da anterior como contexto.

A principal vantagem é que podemos **controlar o processo entre as etapas**. Podemos validar, corrigir, transformar ou enriquecer o resultado antes de utilizá-lo na próxima etapa.

## Um exemplo

Considere um sistema que precisa analisar uma avaliação de cliente e produzir uma resposta para ele.

Em vez de fazer tudo em um único prompt, podemos criar uma cadeia:

**Etapa 1, classificação**

```
Classifique esta avaliação como positiva, neutra ou negativa.

Avaliação:
"O produto chegou rapidamente, mas apresentou problemas
durante a instalação."
```

Resultado:

```
Classificação: negativa
```

**Etapa 2, identificação do problema**

```
Identifique os principais problemas mencionados na avaliação.

Avaliação:
"O produto chegou rapidamente, mas apresentou problemas
durante a instalação."
```

Resultado:

```
Problema principal: dificuldade durante a instalação.
```

**Etapa 3, elaboração da resposta**

```
Com base na avaliação e no problema identificado,
escreva uma resposta profissional ao cliente,
demonstrando empatia e oferecendo ajuda.
```

Resultado:

```
Olá! Sentimos muito que você tenha enfrentado dificuldades
durante a instalação. Gostaríamos de ajudá-lo a resolver
o problema...
```

O sistema agora possui etapas independentes para classificação, análise e geração da resposta.

## Por que é importante

Prompt Chaining é importante porque permite transformar uma interação complexa com um [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) em um **processo estruturado**.

Ele pode trazer algumas vantagens:
1. **Maior controle:** cada etapa possui uma responsabilidade específica.
2. **Menor complexidade:** cada prompt precisa resolver apenas uma parte do problema.
3. **Validação intermediária:** resultados podem ser verificados antes de continuar.
4. **Reutilização:** uma etapa pode ser utilizada em diferentes fluxos.
5. **Depuração mais fácil:** quando algo dá errado, é possível identificar em qual etapa ocorreu o problema.
6. **Integração com sistemas:** cada etapa pode utilizar diferentes modelos, ferramentas, bancos de dados ou APIs.

Prompt Chaining também representa uma mudança importante na forma de pensar sobre engenharia de prompts.

Em vez de considerar o prompt como uma pergunta isolada, passamos a enxergá-lo como **uma etapa dentro de um fluxo de processamento**.

Isso aproxima a engenharia de prompts da construção de sistemas de IA mais complexos.

### Prompt Decomposition × Prompt Chaining

Os dois conceitos estão relacionados, mas não são exatamente a mesma coisa.

**[Prompt Decomposition](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-prompt-decomposition/)** responde principalmente à pergunta:

> Como dividir um problema complexo em partes menores?

**Prompt Chaining** responde:

> Como conectar essas partes em uma sequência de execução?

Assim, podemos primeiro decompor uma tarefa e depois utilizar Prompt Chaining para conectar as etapas:

```
Problema complexo
       ↓
Decomposição
       ↓
Etapa 1 → Etapa 2 → Etapa 3 → Etapa 4
            Prompt Chaining
       ↓
Resultado final
```

Essa distinção será importante para conceitos mais avançados, como **ReAct, Plan-and-Execute e agentes de IA**, nos quais os prompts passam a fazer parte de fluxos que podem envolver planejamento, ferramentas, memória e decisões intermediárias.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-prompt-chaining/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
