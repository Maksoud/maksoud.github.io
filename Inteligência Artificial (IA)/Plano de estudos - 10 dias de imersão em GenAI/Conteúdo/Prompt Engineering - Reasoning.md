[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Reasoning

## O que é

**Reasoning**, ou **raciocínio**, é a capacidade de um modelo de IA de **combinar informações, estabelecer relações, avaliar possibilidades e chegar a conclusões que não estão explicitamente presentes na entrada**.

Em [LLMs](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/), isso vai além de simplesmente recuperar uma informação conhecida. O modelo precisa processar diferentes elementos do problema e utilizá-los para produzir uma conclusão.

Por exemplo, considere:

```
João é mais velho que Maria.
Maria é mais velha que Pedro.

Quem é o mais novo?
```

A resposta "Pedro" não aparece diretamente como uma afirmação no texto. O modelo precisa relacionar as duas informações para chegar à conclusão.

## Como funciona

Imagine que você precise resolver um quebra-cabeça.

Você recebe várias peças:

```
A é maior que B.
B é maior que C.
D é menor que C.
```

Para descobrir quem é o menor, você precisa **combinar as relações existentes**:

```
A > B > C > D
```

Logo, D é o menor.

O raciocínio em um modelo de IA funciona de maneira semelhante em nível conceitual. O modelo precisa transformar as informações disponíveis em uma sequência de inferências que permita chegar a uma conclusão.

Em problemas mais complexos, isso pode envolver:
1. Identificar as informações relevantes.
2. Estabelecer relações entre elas.
3. Dividir o problema em etapas.
4. Avaliar diferentes possibilidades.
5. Eliminar alternativas inconsistentes.
6. Chegar a uma conclusão.

É importante diferenciar **Reasoning** de simplesmente "saber informações". Um modelo pode saber que determinada fórmula existe, por exemplo, mas ainda precisar raciocinar para decidir **qual fórmula utilizar e como aplicá-la ao problema apresentado**.

## Um exemplo

Imagine que um sistema precise decidir se uma empresa deve aumentar ou reduzir seu investimento em publicidade.

Ele recebe:

```
Investimento atual: R$ 10.000
Receita gerada: R$ 50.000
Custo adicional de publicidade: R$ 5.000
Receita adicional estimada: R$ 30.000
```

Uma análise simples poderia estabelecer:

```
Receita adicional: R$ 30.000
Custo adicional: R$ 5.000
Resultado adicional: R$ 25.000
```

A partir dessas informações, o modelo pode concluir que, **considerando apenas esses números**, o investimento adicional parece economicamente favorável.

Observe que a conclusão não estava explicitamente fornecida. Ela foi obtida pela combinação das informações.

## Por que é importante

Reasoning é importante porque muitas aplicações de IA exigem mais do que geração ou recuperação de texto. Elas exigem que o modelo **transforme informações em conclusões, decisões ou planos**.

Ele é particularmente relevante em:
1. Matemática e resolução de problemas.
2. Programação.
3. Análise de dados.
4. Planejamento.
5. Tomada de decisão.
6. Diagnóstico de problemas.
7. Agentes de IA.
8. Tarefas com múltiplas etapas.

O conceito também ajuda a entender a evolução dos **[Reasoning Models](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-reasoning-models/)**. LLMs tradicionais foram inicialmente otimizados principalmente para prever e gerar texto. Modelos voltados para reasoning são desenvolvidos para lidar melhor com problemas que exigem **inferência, planejamento e resolução de tarefas complexas**.

Isso também explica por que **[Chain-of-Thought](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-chain-of-thought/)** e **Reasoning** estão relacionados, mas não são a mesma coisa.

**Chain-of-Thought é uma técnica ou abordagem para decompor um problema em etapas de raciocínio. Reasoning é a capacidade mais ampla de realizar inferências e chegar a conclusões.**

**Em uma frase:** Reasoning é a capacidade de **processar informações e estabelecer inferências para chegar a uma conclusão que não está explicitamente presente nos dados fornecidos**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-reasoning/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
