[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Tool Instructions

## O que é

**Tool Instructions**, ou **instruções de ferramentas**, são orientações que definem **quando, por que e como um modelo deve utilizar uma ferramenta externa**.

Uma ferramenta pode dar ao [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) capacidades que ele não possui sozinho, como consultar uma API, pesquisar informações, executar código, acessar um banco de dados ou realizar uma ação em um sistema.

O modelo precisa então entender não apenas **qual ferramenta existe**, mas também **em quais situações deve utilizá-la e quais regras precisa seguir ao utilizá-la**.

De forma simplificada:

```
Usuário
   ↓
LLM interpreta a tarefa
   ↓
Decide se precisa de uma ferramenta
   ↓
Tool Instructions
   ↓
Executa a ferramenta
   ↓
Recebe o resultado
   ↓
LLM interpreta o resultado
   ↓
Resposta ou próxima ação
```

## Como funciona

Imagine um assistente que possui três ferramentas:

```
Pesquisar na internet
Consultar banco de dados
Enviar e-mail
```

Não basta dizer ao modelo que essas ferramentas existem.

Ele precisa saber, por exemplo:

```
Pesquisar na internet:
Use quando precisar de informações atuais.

Banco de dados:
Use para consultar informações internas.

Enviar e-mail:
Use somente quando o usuário tiver solicitado
explicitamente o envio.
```

Essas regras ajudam o modelo a decidir **qual ferramenta utilizar, quando utilizá-la e quais limites respeitar**.

As Tool Instructions também podem definir como os argumentos devem ser fornecidos:

```
Ferramenta: consultar_cliente

Parâmetros:
- id_cliente: identificador do cliente
- incluir_pedidos: verdadeiro ou falso

Regra:
Nunca consulte um cliente sem possuir
um identificador válido.
```

O modelo precisa transformar a intenção do usuário em uma chamada compatível com essas regras.

## Um exemplo

Imagine um agente de atendimento conectado a uma ferramenta chamada `consultar_pedido`.

O usuário pergunta:

```
Onde está meu pedido?
```

O modelo pode precisar utilizar a ferramenta para obter a informação atual.

As instruções da ferramenta poderiam estabelecer:

```
Use consultar_pedido quando o usuário perguntar
sobre o status ou localização de um pedido.

É obrigatório informar o número do pedido.

Se o número não estiver disponível, solicite-o
ao usuário antes de chamar a ferramenta.
```

Se o usuário disser:

```
Meu pedido é 45872.
```

O fluxo pode ser:

```
Pedido do usuário
        ↓
LLM
        ↓
Identifica necessidade de consultar ferramenta
        ↓
Tool Instructions
        ↓
consultar_pedido(45872)
        ↓
Resultado da ferramenta
        ↓
LLM interpreta o resultado
        ↓
Resposta ao usuário
```

Suponha que a ferramenta retorne:

```
Status: Em transporte
Previsão: 4 de novembro
```

O modelo pode então transformar esse resultado em uma resposta natural:

```
Seu pedido está em transporte e a previsão de entrega
é 4 de novembro.
```

Nesse processo, o modelo não está simplesmente "respondendo". Ele está **decidindo quando utilizar uma capacidade externa e incorporando o resultado dessa capacidade à resposta**.

## Por que é importante

Tool Instructions são importantes porque, quando um LLM passa a utilizar ferramentas, **a qualidade do prompt deixa de ser suficiente para controlar todo o comportamento do sistema**.

As instruções precisam orientar o modelo sobre:
- quando utilizar uma ferramenta;
- quando não utilizar;
- qual ferramenta escolher;
- quais parâmetros fornecer;
- quais dados são obrigatórios;
- quais ações exigem confirmação;
- como interpretar os resultados;
- o que fazer quando a ferramenta falhar.

Isso é especialmente importante em **agentes de IA**, nos quais o modelo pode decidir quais ações executar para atingir um objetivo.

Existe também uma relação direta com os conceitos estudados anteriormente.

**[Instruction Hierarchy](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-instruction-hierarchy/)** ajuda a determinar quais instruções devem prevalecer.

**[Context Management](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-context-management/)** controla quais informações são apresentadas ao modelo.

**Tool Instructions** orientam o uso das capacidades externas disponíveis.

**[Guardrails](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-guardrails/)** podem limitar ou validar o uso dessas ferramentas.

Podemos visualizar a relação:

```
Usuário
   ↓
Context Management
   ↓
LLM
   ↓
Instruction Hierarchy
   ↓
Decisão
   ↓
Tool Instructions
   ↓
Ferramenta
   ↓
Resultado
   ↓
Guardrails / validação
   ↓
LLM
   ↓
Resposta
```

Um ponto importante é que **Tool Instructions não devem ser confundidas com a documentação técnica da ferramenta**.

A documentação explica como a ferramenta funciona.

As Tool Instructions explicam **como o modelo deve utilizá-la dentro daquele sistema**.

Por exemplo:

```
Documentação:
"Esta API recebe um ID e retorna os dados do cliente."

Tool Instruction:
"Utilize esta API somente quando o usuário
estiver autorizado a consultar esse cliente."
```

A primeira descreve a capacidade técnica. A segunda estabelece uma regra de uso.

Esse conceito prepara o caminho para **Tool Calling** e **Function Calling**, nos quais o modelo passa a produzir chamadas estruturadas para ferramentas externas.

A partir desse ponto, o LLM deixa de ser apenas um gerador de texto e passa a atuar como um **componente de decisão dentro de um sistema maior**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-tool-instructions/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
