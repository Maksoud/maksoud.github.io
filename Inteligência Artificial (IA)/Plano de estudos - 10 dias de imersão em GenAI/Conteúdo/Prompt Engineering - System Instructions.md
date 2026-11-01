[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# System Instructions

## O que é

**System Instructions** são instruções de alto nível que definem **como um modelo de IA deve se comportar antes de receber a solicitação específica do usuário**.

Elas podem estabelecer regras sobre comportamento, objetivo, personalidade, formato das respostas, limites, prioridades e uso de determinadas informações ou ferramentas.

Uma forma simples de entender é separar três níveis:
1. **System Instructions:** definem as regras e o comportamento geral do modelo.
2. **User Prompt:** descreve o que o usuário quer que o modelo faça.
3. **Resposta:** é produzida pelo modelo considerando as instruções disponíveis e a solicitação.

Por isso, System Instructions não são simplesmente um "prompt mais detalhado". Elas fazem parte da estrutura de controle usada para orientar o comportamento do modelo.

## Como funciona

Imagine que você contrate um profissional para realizar uma tarefa.

Antes de começar, você entrega um manual dizendo:

```
Você trabalha como analista.
Seja objetivo.
Use linguagem profissional.
Não divulgue informações confidenciais.
Siga o formato definido pela empresa.
```

Depois, você faz uma solicitação:

```
Analise este relatório e apresente os principais problemas.
```

O profissional precisa realizar a tarefa **dentro das regras estabelecidas anteriormente**.

Com um modelo de linguagem, a ideia é semelhante. As System Instructions fornecem uma camada de orientação que permanece relevante enquanto o modelo executa as solicitações.

Por exemplo, uma aplicação poderia estabelecer:

```
Você é um assistente especializado em suporte técnico.
Responda sempre em português.
Se não tiver informações suficientes, deixe isso claro.
Não invente informações.
```

O usuário poderia então perguntar:

```
Como resolvo esse erro?
```

A resposta deverá considerar tanto a pergunta quanto as instruções que definem o comportamento do assistente.

## Um exemplo

Imagine um chatbot desenvolvido para atendimento de uma empresa.

As System Instructions poderiam estabelecer:

```
Você é um atendente de suporte técnico.

Seu objetivo é ajudar clientes a solucionar problemas.

Regras:
Responda em português.
Seja objetivo.
Não invente informações sobre produtos.
Quando não souber a resposta, informe que não possui informação suficiente.
```

O usuário então pergunta:

```
Meu computador não consegue acessar a internet. O que devo fazer?
```

A resposta seria construída considerando essas regras. O modelo pode sugerir verificações básicas, mas não deveria inventar, por exemplo, uma política de suporte da empresa que não foi fornecida.

O ponto importante é que **a instrução de sistema define o comportamento esperado, enquanto o prompt do usuário define a tarefa específica**.

## Por que é importante

System Instructions são fundamentais para transformar um modelo de linguagem genérico em um **assistente especializado e controlado por regras**.

Elas são especialmente importantes em aplicações como:
1. Chatbots corporativos.
2. Assistentes de programação.
3. Sistemas de atendimento ao cliente.
4. Agentes de IA.
5. Aplicações que precisam seguir políticas específicas.
6. Sistemas que exigem respostas em um formato determinado.

Elas também ajudam a separar **o que o sistema quer que o modelo faça** daquilo que **o usuário está pedindo naquele momento**.

Isso se torna ainda mais importante em sistemas de IA mais complexos. Em um agente, por exemplo, as System Instructions podem estabelecer quais ferramentas ele pode utilizar, quais objetivos deve perseguir e quais restrições precisa respeitar.

**Em uma frase:** System Instructions são **instruções de alto nível que estabelecem o comportamento, as regras e as prioridades que orientam o modelo durante a execução das solicitações**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-system-instructions/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
