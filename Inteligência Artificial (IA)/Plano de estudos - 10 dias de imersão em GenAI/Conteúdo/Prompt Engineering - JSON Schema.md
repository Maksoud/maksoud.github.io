[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# JSON Schema

## O que é

**JSON Schema** é uma forma padronizada de **descrever e validar a estrutura esperada de um objeto JSON**.

Ele permite especificar quais campos devem existir, quais são seus tipos de dados, quais são obrigatórios e quais valores são aceitos.

Por exemplo, podemos definir que uma resposta de um modelo deve conter:

```
{
  "nome": "string",
  "idade": "number",
  "email": "string"
}
```

O JSON Schema transforma essa ideia em uma especificação formal que pode ser utilizada por aplicações para verificar se os dados recebidos estão no formato esperado.

É importante perceber a relação com o assunto anterior: **[Structured Output](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-structured-output/) define a necessidade de uma resposta estruturada, enquanto JSON Schema pode definir formalmente qual é essa estrutura**.

## Como funciona

Imagine que você tenha um formulário que precisa ser preenchido por um sistema.

Você estabelece algumas regras:

```
Nome: obrigatório, texto
Idade: obrigatória, número
Email: obrigatório, texto
```

Se alguém preencher:

```
Nome: Carlos
Idade: 42
Email: carlos@email.com
```

o formulário está de acordo com as regras.

Mas se alguém enviar:

```
Nome: Carlos
Idade: quarenta e dois
Email: carlos@email.com
```

o campo `idade` não está no formato esperado.

O JSON Schema funciona como esse **contrato da estrutura dos dados**.

Em aplicações com [LLMs](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/), podemos usar esse contrato para especificar ao modelo e ao sistema consumidor exatamente como a resposta deve ser estruturada.

## Um exemplo

Imagine que queremos que um LLM classifique uma avaliação de cliente.

Podemos definir um JSON Schema conceitualmente assim:

```
{
  "type": "object",
  "properties": {
    "sentimento": {
      "type": "string",
      "enum": ["positivo", "negativo", "neutro"]
    },
    "confianca": {
      "type": "number"
    },
    "justificativa": {
      "type": "string"
    }
  },
  "required": ["sentimento", "confianca", "justificativa"]
}
```

Esse schema estabelece várias regras:

1. A resposta deve ser um objeto.
2. Deve existir um campo `sentimento`.
3. `sentimento` deve ser um texto.
4. O sentimento só pode ser `positivo`, `negativo` ou `neutro`.
5. `confianca` deve ser um número.
6. `justificativa` deve ser um texto.
7. Os três campos são obrigatórios.

Uma resposta válida poderia ser:

```
{
  "sentimento": "positivo",
  "confianca": 0.94,
  "justificativa": "O cliente demonstrou satisfação com o produto."
}
```

Uma resposta como esta seria incompatível com o schema:

```
{
  "sentimento": "muito bom",
  "confianca": "alta"
}
```

porque `sentimento` possui um valor que não está entre os valores permitidos e `confianca` deveria ser um número.

## Por que é importante

JSON Schema é importante porque permite transformar uma expectativa sobre a resposta em um **contrato verificável**.

Isso é especialmente valioso quando LLMs fazem parte de sistemas maiores, nos quais a resposta do modelo precisa ser consumida automaticamente por outro componente.

Ele é útil em:
1. Structured Outputs.
2. APIs que recebem ou retornam JSON.
3. Extração estruturada de informações.
4. Sistemas de agentes.
5. Automação de processos.
6. Validação de dados produzidos por LLMs.
7. Integração entre modelos de IA e aplicações tradicionais.

A diferença fundamental pode ser resumida assim:

**Prompt:** "Responda em JSON."

**Structured Output:** "A resposta deve seguir uma estrutura definida."

**JSON Schema:** "Esta é a especificação formal dessa estrutura."

Isso torna o JSON Schema particularmente importante para aplicações de IA porque ajuda a reduzir a distância entre **linguagem natural e software determinístico**.

**Em uma frase:** JSON Schema é **um contrato formal que descreve e valida a estrutura, os tipos e as regras dos dados JSON que um sistema espera receber**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-json-schema/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
