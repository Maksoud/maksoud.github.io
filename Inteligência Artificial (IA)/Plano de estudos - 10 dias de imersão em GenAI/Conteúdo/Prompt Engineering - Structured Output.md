[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Structured Output

## O que é

**Structured Output** é uma técnica na qual definimos previamente **a estrutura que a resposta do modelo deve seguir**, em vez de simplesmente pedir que ele produza uma resposta em texto livre.

Essa estrutura pode determinar campos, tipos de dados, ordem das informações ou um formato específico, como JSON, XML, uma tabela ou uma lista padronizada.

Por exemplo, em vez de pedir:

```
Extraia as informações deste cliente.
```

podemos especificar:

```
Retorne as informações no seguinte formato:

{
  "nome": "...",
  "email": "...",
  "empresa": "..."
}
```

O objetivo é tornar a saída **previsível, consistente e fácil de ser processada por outros sistemas**.

## Como funciona

Imagine que você peça a cinco pessoas para extrair informações de uma nota fiscal.

Sem nenhuma orientação, uma pessoa pode responder:

```
Empresa: Acme
Valor: R$ 2.500
Data: 15/10/2026
```

Outra pode escrever:

```
A compra foi realizada pela Acme no dia 15 de outubro, no valor de R$ 2.500.
```

As duas respostas estão corretas, mas são diferentes.

Agora imagine que você determine que todos devem preencher um formulário com três campos:

```
Empresa:
Valor:
Data:
```

As respostas passam a ter uma estrutura previsível.

Com Structured Output, fazemos algo semelhante com o modelo. Em vez de deixar completamente aberto **como** a informação será apresentada, especificamos a estrutura esperada.

Isso é especialmente importante quando a resposta do modelo será utilizada por um programa.

## Um exemplo

Suponha que queremos analisar uma avaliação de produto:

```
O produto chegou rapidamente, mas a embalagem estava danificada.
```

Um Structured Output poderia exigir:

```
{
  "sentimento": "negativo",
  "pontos_positivos": [
    "entrega rápida"
  ],
  "pontos_negativos": [
    "embalagem danificada"
  ]
}
```

O benefício é que um programa pode consumir esses dados diretamente.

Por exemplo, uma aplicação poderia receber o campo `"sentimento"` e utilizá-lo para alimentar um dashboard, enquanto `"pontos_positivos"` e `"pontos_negativos"` poderiam ser armazenados separadamente.

Aqui existe uma distinção importante: **pedir JSON no prompt não é necessariamente o mesmo que utilizar Structured Output de forma robusta**.

Um prompt como:

```
Responda em JSON.
```

é uma instrução de formato. O modelo pode seguir essa instrução, mas dependendo da implementação, ainda pode produzir uma saída inválida ou diferente da estrutura esperada.

Em sistemas que oferecem **Structured Outputs com schema**, a aplicação pode especificar formalmente quais campos são esperados e quais tipos de dados devem ser retornados. Isso oferece um nível de controle muito maior.

## Por que é importante

Structured Output é importante porque transforma a saída de um modelo de linguagem em algo **mais previsível e integrável com software**.

Ele é especialmente útil em:
1. Extração de informações de documentos.
2. Classificação automática de textos.
3. Integração entre [LLMs](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) e APIs.
4. Sistemas de agentes.
5. Automação de processos.
6. Geração de dados para bancos de dados.
7. Aplicações que precisam validar automaticamente a resposta do modelo.

Isso representa uma mudança importante na utilização de LLMs. Em uma conversa, uma resposta em linguagem natural normalmente é suficiente. Em uma aplicação, porém, o software frequentemente precisa saber **exatamente onde cada informação está**.

Por exemplo, para uma resposta estruturada, podemos ter:

```
{
  "cliente": "Maria",
  "idade": 35,
  "interessada": true
}
```

O sistema consegue interpretar cada valor de maneira independente. Já uma frase como "Maria tem 35 anos e demonstrou interesse" exige que outro componente interprete novamente o texto.

**Em uma frase:** Structured Output é **a utilização de uma estrutura previamente definida para tornar as respostas do modelo previsíveis, consistentes e facilmente utilizáveis por outros sistemas**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-structured-output/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
