[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Context Management

## O que é

**Context Management**, ou **gerenciamento de contexto**, é o conjunto de técnicas utilizadas para controlar quais informações um modelo recebe, em que momento elas são apresentadas e por quanto tempo permanecem disponíveis durante uma interação.

Um [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) não trabalha com uma memória ilimitada. A cada chamada, existe uma quantidade limitada de informações que pode ser considerada pelo modelo, determinada principalmente pela **[context window](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-context-window/)**.

Por isso, em aplicações mais complexas, não basta fornecer informações ao modelo. É necessário decidir **quais informações realmente precisam estar no contexto**.

Context Management envolve, por exemplo:
- selecionar informações relevantes;
- organizar o contexto;
- remover informações desnecessárias;
- resumir conversas longas;
- recuperar informações externas quando necessário;
- preservar instruções importantes ao longo de uma interação.

## Como funciona

Imagine que você está conversando com alguém durante várias horas sobre um projeto.

No início, você explica o objetivo, as regras e várias decisões. Depois de algum tempo, a conversa fica enorme.

Se você entregar absolutamente tudo para a pessoa a cada nova decisão, haverá muito conteúdo irrelevante. Além disso, informações importantes podem ficar escondidas entre centenas de mensagens.

O gerenciamento de contexto procura resolver esse problema.

Em vez de enviar toda a informação disponível, o sistema pode montar um contexto mais adequado para cada momento:

```
Informações disponíveis
        ↓
Seleção do que é relevante
        ↓
Organização / resumo
        ↓
Contexto atual
        ↓
LLM
        ↓
Resposta
```

Por exemplo, em uma conversa sobre desenvolvimento de software, o sistema pode preservar:

```
Objetivo do projeto
Requisitos importantes
Decisões já tomadas
Código relevante
Erros recentes
Pergunta atual
```

Enquanto informações antigas e irrelevantes podem ser removidas ou resumidas.

Assim, **contexto não significa simplesmente tudo o que o modelo sabe ou tudo o que foi dito anteriormente**. É o conjunto de informações selecionadas para influenciar uma determinada resposta.

## Um exemplo

Imagine um agente de atendimento que conversa com um cliente durante várias interações.

No início, o cliente informa:

```
Cliente: Estou usando o plano Enterprise.
Meu problema é que a integração com a API está retornando erro 401.
```

Durante a conversa, várias outras mensagens são trocadas.

Quando o cliente pergunta novamente sobre o erro, o sistema pode construir um contexto contendo:

```
Cliente: plano Enterprise
Produto: API
Problema: erro 401
Tentativas anteriores: renovação do token
Pergunta atual: como corrigir o erro?
```

Em vez de enviar toda a conversa desde o início, o sistema pode utilizar apenas as informações relevantes.

Em uma aplicação mais sofisticada, esse contexto pode ser construído dinamicamente:

```
Histórico recente
        +
Memória relevante
        +
Documentação recuperada
        +
Instruções do sistema
        +
Pergunta atual
        ↓
Contexto final
        ↓
LLM
```

Esse processo pode acontecer a cada nova interação.

## Por que é importante

Context Management é fundamental porque a qualidade de uma resposta depende não apenas da capacidade do modelo, mas também **das informações que chegam até ele**.

Um contexto mal gerenciado pode causar problemas como:
- excesso de informações;
- perda de instruções importantes;
- informações conflitantes;
- aumento desnecessário do consumo de [tokens](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/);
- respostas influenciadas por conteúdo irrelevante;
- dificuldade para manter coerência em conversas longas.

Um contexto bem gerenciado, por outro lado, permite que o modelo receba **a informação certa, no momento certo e no formato adequado**.

Isso conecta vários conceitos estudados anteriormente.

**Context Window** define o espaço disponível para o contexto.

**[RAG](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-rag/)** fornece informações externas relevantes para esse contexto.

**[Prompt Chaining](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-prompt-chaining/)** permite distribuir uma tarefa entre várias etapas, cada uma com seu próprio contexto.

**[Prompt Decomposition](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-prompt-decomposition/)** ajuda a decidir como dividir uma tarefa complexa.

**Context Management** atua em um nível mais amplo, coordenando quais informações devem acompanhar cada etapa.

Por isso, em sistemas modernos de IA, a engenharia de prompts deixa gradualmente de ser apenas a arte de escrever boas instruções. Ela passa a envolver também a construção e o gerenciamento do **contexto que será apresentado ao modelo**.

Essa evolução é especialmente importante em aplicações com conversas longas, RAG, agentes, ferramentas e múltiplas etapas de processamento.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-context-management/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
