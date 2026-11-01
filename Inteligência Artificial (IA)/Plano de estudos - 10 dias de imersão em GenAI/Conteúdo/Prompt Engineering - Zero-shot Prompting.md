[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Zero-shot Prompting

## O que é

**Zero-shot prompting** é uma técnica de engenharia de prompts na qual pedimos ao modelo para executar uma tarefa **sem fornecer exemplos de como ela deve ser realizada**.

O modelo recebe apenas a instrução e o contexto necessário para executar a tarefa. O termo _zero-shot_ significa, literalmente, "sem exemplos".

Isso é possível porque modelos de linguagem modernos já foram treinados com grandes volumes de texto e aprenderam padrões gerais de linguagem, tarefas e relações entre conceitos.

## Como funciona

Imagine que você peça a uma pessoa que já domina um determinado assunto:

> "Classifique esta frase como positiva ou negativa."

Você não precisa necessariamente mostrar exemplos anteriores. A própria instrução é suficiente para que ela entenda o que deve fazer.

Com um [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) acontece algo semelhante. O prompt descreve a tarefa e o modelo tenta inferir:

1. O que precisa ser feito.
2. Qual é o formato esperado da resposta.
3. Quais conhecimentos são relevantes.
4. Qual resposta é mais provável de atender à instrução.

Por exemplo:

```
Classifique o sentimento desta frase como positivo, negativo ou neutro:

"Adorei o atendimento e voltarei novamente."
```

Não fornecemos nenhum exemplo de classificação anterior. O modelo precisa compreender a tarefa diretamente a partir da instrução.

$$
m=\frac{y_2-y_1}{x_2-x_1}
$$

> **Observação:** o conceito de zero-shot não depende de uma fórmula ou de exemplos prévios. A visualização acima não representa adequadamente o conceito e, portanto, deve ser desconsiderada como parte do conteúdo. O ponto central é a relação entre **instrução → tarefa → resposta**, sem exemplos intermediários.

## Um exemplo

Imagine que queremos extrair informações de uma mensagem:

```
Extraia o nome da empresa, o valor e a data mencionados no texto.

"Contratei a empresa Acme por R$ 2.500 em 15 de outubro de 2026."
```

Um modelo usando zero-shot prompting pode responder:

```
Empresa: Acme
Valor: R$ 2.500
Data: 15 de outubro de 2026
```

Perceba que não precisamos fornecer exemplos como:

```
Texto: "Comprei na Empresa X por R$ 1.000 em 10/10."
Empresa: Empresa X
Valor: R$ 1.000
Data: 10/10
```

Esse exemplo seria uma outra técnica, chamada **[few-shot prompting](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-few-shot-prompting/)**, que veremos posteriormente.

## Por que é importante

O zero-shot prompting é importante porque representa a forma mais simples de interagir com um modelo de linguagem: **descrever o que queremos e deixar o modelo executar a tarefa**.

Ele é especialmente útil quando:
1. A tarefa é relativamente simples ou conhecida pelo modelo.
2. Não queremos gastar espaço do contexto fornecendo exemplos.
3. Precisamos criar prompts rapidamente.
4. A tarefa precisa ser aplicada a muitos tipos diferentes de entrada.
5. Queremos testar primeiro a capacidade do modelo antes de sofisticar o prompt.

Por outro lado, zero-shot não significa que o modelo sempre produzirá a melhor resposta. Quando a tarefa é ambígua, complexa ou exige um formato muito específico, podemos melhorar o resultado adicionando exemplos, contexto, critérios ou etapas de raciocínio.

**Em uma frase:** zero-shot prompting é **pedir ao modelo para realizar uma tarefa apenas com uma instrução, sem fornecer exemplos de entrada e saída**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-zero-shot-prompting/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
