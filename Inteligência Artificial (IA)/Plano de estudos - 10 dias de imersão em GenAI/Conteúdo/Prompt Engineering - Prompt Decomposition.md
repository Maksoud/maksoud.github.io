[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Prompt Decomposition

## O que é

**Prompt Decomposition**, ou **decomposição de prompts**, é uma técnica de engenharia de prompts que consiste em **dividir uma tarefa complexa em partes menores e mais específicas**, em vez de solicitar que o modelo resolva tudo de uma única vez.

A ideia é transformar uma solicitação grande em uma sequência de subtarefas mais fáceis de compreender, executar e verificar.

Por exemplo, em vez de:

```
Analise este produto, identifique seu público, avalie seus concorrentes e crie uma estratégia de marketing.
```

podemos decompor:

```
1. Identifique as principais características do produto.
2. Determine o público-alvo.
3. Identifique os principais concorrentes.
4. Compare o produto com os concorrentes.
5. Desenvolva uma estratégia de marketing com base na análise.
```

A tarefa final continua sendo a mesma, mas sua estrutura fica mais clara.

## Como funciona

Imagine que você precise organizar uma mudança de casa.

Dizer:

```
Organize minha mudança.
```

é uma tarefa grande e pouco específica.

Uma abordagem de decomposição seria:

```
1. Liste os objetos que precisam ser transportados.
2. Separe os objetos por cômodo.
3. Identifique o que precisa ser embalado primeiro.
4. Organize o transporte.
5. Crie um cronograma.
```

Cada etapa reduz a complexidade do problema original.

Com [LLMs](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/), o princípio é semelhante. Uma tarefa complexa é transformada em **subtarefas menores, cada uma com um objetivo específico**.

Isso também facilita a identificação de erros. Se o resultado final estiver incorreto, podemos investigar qual etapa produziu o problema.

## Um exemplo

Imagine que queremos produzir uma análise de uma empresa.

Um prompt único poderia ser:

```
Analise esta empresa e produza um relatório completo sobre sua situação, seus concorrentes, seus riscos e suas oportunidades.
```

Podemos decompor a tarefa em etapas:

```
Etapa 1:
Identifique os principais produtos e serviços da empresa.

Etapa 2:
Identifique seu público-alvo.

Etapa 3:
Analise os principais concorrentes.

Etapa 4:
Identifique os principais riscos para o negócio.

Etapa 5:
Identifique oportunidades de crescimento.

Etapa 6:
Com base nas análises anteriores, produza uma síntese estratégica.
```

Em uma implementação mais sofisticada, cada etapa pode inclusive ser executada por uma chamada diferente ao modelo, utilizando o resultado de uma etapa como entrada para a seguinte.

Isso transforma algo parecido com:

```
Problema → Resposta
```

em:

```
Problema
   ↓
Subtarefa 1
   ↓
Subtarefa 2
   ↓
Subtarefa 3
   ↓
Síntese
   ↓
Resposta final
```

## Por que é importante

Prompt Decomposition é importante porque permite lidar melhor com **tarefas complexas que envolvem múltiplas operações ou diferentes tipos de raciocínio**.

Ele é especialmente útil quando:
1. A tarefa possui muitas etapas.
2. Existem objetivos diferentes dentro da mesma solicitação.
3. Cada etapa depende do resultado da anterior.
4. Precisamos verificar os resultados intermediários.
5. Queremos reduzir ambiguidades.
6. A tarefa será implementada como um fluxo automatizado ou agente de IA.

Uma consequência importante é que a decomposição pode tornar o sistema **mais controlável e observável**. Em vez de receber apenas uma resposta final, podemos acompanhar o resultado de cada etapa.

Por outro lado, decompor excessivamente uma tarefa também pode aumentar o número de chamadas ao modelo, o consumo de [tokens](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/) e a complexidade da aplicação. Portanto, a ideia não é simplesmente dividir tudo em pequenas partes, mas **encontrar uma divisão que torne o problema mais fácil de resolver sem criar complexidade desnecessária**.

Prompt Decomposition também se relaciona diretamente com outros conceitos que já estudamos. **[Chain-of-Thought](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-chain-of-thought/)** está relacionado à decomposição do raciocínio em etapas, enquanto Prompt Decomposition pode ser aplicado de forma mais ampla, inclusive dividindo uma tarefa em várias chamadas independentes ao modelo.

**Em uma frase:** Prompt Decomposition é **dividir uma tarefa complexa em subtarefas menores e organizadas para tornar sua execução mais clara, controlável e confiável**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-prompt-decomposition/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
