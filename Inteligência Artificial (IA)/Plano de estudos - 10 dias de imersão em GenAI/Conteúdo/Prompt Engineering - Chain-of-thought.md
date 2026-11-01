[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Chain-of-Thought

## O que é

**Chain-of-Thought (CoT)**, ou **cadeia de pensamento**, é uma técnica de prompting que incentiva o modelo a **dividir um problema complexo em etapas intermediárias de raciocínio antes de chegar à resposta final**.

A ideia central é que, para determinadas tarefas, o modelo pode obter resultados melhores quando não tenta chegar diretamente à conclusão, mas organiza o problema em uma sequência de passos.

Por exemplo, em vez de simplesmente perguntar:

```
Qual é o resultado de 23 × 17?
```

podemos estruturar a solicitação para que o modelo raciocine sobre a operação em etapas.

É importante fazer uma distinção: **Chain-of-Thought é um conceito sobre o processo de raciocínio do modelo, não simplesmente sobre pedir uma resposta mais longa**.

## Como funciona

Imagine uma pessoa tentando resolver um problema de matemática.

Em vez de pensar apenas:

```
Resposta: 391
```

ela pode decompor o problema:

```
23 × 17

23 × 10 = 230
23 × 7 = 161

230 + 161 = 391
```

A decomposição torna o problema mais manejável e reduz a possibilidade de um erro durante a resolução.

Com problemas complexos, a mesma ideia pode ser aplicada ao prompting. Em vez de solicitar apenas uma conclusão, podemos orientar o modelo a **decompor a tarefa em etapas**.

Por exemplo:

```
Analise o problema.
Identifique as informações relevantes.
Divida o problema em etapas.
Resolva cada etapa.
Apresente a conclusão.
```

Esse tipo de estrutura pode ajudar especialmente em problemas que exigem múltiplas operações ou decisões encadeadas.

## Um exemplo

Imagine o seguinte problema:

```
Uma empresa possui 120 clientes.
30% são clientes empresariais.
Desses clientes empresariais, 25% contrataram um segundo serviço.

Quantos clientes contrataram o segundo serviço?
```

Uma abordagem de raciocínio em etapas seria:

```
1. Calcular quantos clientes são empresariais:
120 × 0,30 = 36

2. Calcular quantos desses contrataram o segundo serviço:
36 × 0,25 = 9

3. Resultado:
9 clientes.
```

A vantagem da decomposição é que cada etapa pode ser verificada independentemente.

Em problemas mais complexos, a mesma lógica pode envolver várias etapas de análise, comparação, dedução ou cálculo.

## Por que é importante

Chain-of-Thought foi importante no desenvolvimento das técnicas modernas de prompting porque mostrou que **a forma como uma tarefa é apresentada pode influenciar significativamente a capacidade do modelo de resolver determinados problemas**.

A técnica é especialmente relevante para:
1. Problemas matemáticos.
2. Problemas de lógica.
3. Tarefas que exigem várias etapas.
4. Planejamento.
5. Análise de informações.
6. Problemas que envolvem decisões encadeadas.

Ela também ajudou a abrir caminho para uma evolução importante nos modelos atuais: os chamados **[Reasoning Models](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-reasoning-models/)**, que são desenvolvidos especificamente para lidar melhor com tarefas que exigem raciocínio complexo.

Há, porém, uma diferença importante entre **Chain-of-Thought como técnica de prompting** e **raciocínio interno de modelos modernos**. Nem todo modelo precisa receber uma instrução explícita para expor seu raciocínio passo a passo. Modelos mais recentes podem realizar processos internos de raciocínio e fornecer apenas uma resposta ou uma explicação resumida.

Além disso, em aplicações reais, muitas vezes é preferível solicitar **uma justificativa concisa ou um resumo das etapas relevantes**, em vez de exigir que o modelo revele todo o seu processo interno de raciocínio.

**Em uma frase:** Chain-of-Thought é uma abordagem que **decompõe problemas complexos em etapas intermediárias para ajudar o modelo a chegar a uma resposta mais consistente**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-chain-of-thought/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
