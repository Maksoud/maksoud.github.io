[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Grounding

## O que é

**Grounding**, ou **fundamentação**, é a técnica de conectar a resposta de um modelo de IA a informações concretas, verificáveis e relevantes para a tarefa.

Um [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) consegue gerar respostas com base nos padrões aprendidos durante seu treinamento, mas isso não significa que tenha acesso aos dados mais recentes ou que todas as informações que produz estejam necessariamente corretas.

O grounding busca reduzir essa dependência ao fornecer ao modelo uma **base de referência específica** para responder.

Essa referência pode ser:

```
Documentos
Banco de dados
APIs
Páginas da web
Dados corporativos
Resultados de busca
Informações fornecidas pelo usuário
```

A ideia central é:

**não pedir ao modelo apenas para lembrar ou inferir uma informação, mas fornecer evidências nas quais ele possa fundamentar a resposta.**

## Como funciona

Imagine que você pergunte a alguém:

> "Qual é o valor atual do dólar?"

Se essa pessoa tentar responder apenas com aquilo que lembra, a informação pode estar desatualizada.

Agora imagine que ela consulte uma fonte atual antes de responder.

O processo passa a ser:

```
Pergunta
   ↓
Fonte de informação
   ↓
Dados relevantes
   ↓
LLM
   ↓
Resposta fundamentada
```

O modelo continua sendo responsável por interpretar e organizar a informação, mas a resposta passa a estar **ancorada em uma fonte específica**.

Isso é especialmente útil quando a pergunta depende de informações que o modelo não deveria simplesmente inventar ou inferir.

## Um exemplo

Imagine um chatbot interno de uma empresa.

O funcionário pergunta:

```
Qual é a política atual de férias da empresa?
```

Em vez de depender apenas do conhecimento geral do modelo, o sistema pode recuperar o documento oficial de Recursos Humanos:

```
Política de férias 2026

Funcionários podem solicitar férias com antecedência
mínima de 30 dias...
```

Esse conteúdo é então incluído no contexto do modelo.

O fluxo seria:

```
Pergunta do funcionário
        ↓
Busca na documentação interna
        ↓
Documento relevante
        ↓
Contexto
        ↓
LLM
        ↓
Resposta baseada no documento
```

O modelo pode então responder utilizando aquela informação como referência.

Esse processo também permite que o sistema indique a origem da informação, quando a aplicação foi projetada para isso:

```
Segundo a Política de Férias 2026, a solicitação
deve ser realizada com pelo menos 30 dias de antecedência.
```

## Por que é importante

Grounding é importante porque ajuda a reduzir um dos problemas mais conhecidos dos LLMs: **responder com informações incorretas ou não verificadas com aparência de certeza**.

Ele é particularmente útil quando a resposta depende de:
- informações atualizadas;
- dados privados ou específicos de uma organização;
- documentos oficiais;
- informações factuais que precisam ser verificáveis;
- dados que não estavam disponíveis no treinamento do modelo.

Grounding também está diretamente relacionado ao **[RAG](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-rag/)** estudado anteriormente.

Podemos pensar assim:

```
Grounding
    ↓
Princípio: fundamentar a resposta em informações externas

RAG
    ↓
Uma arquitetura que pode implementar esse princípio
```

RAG normalmente recupera informações relevantes e as coloca no contexto do modelo. Essas informações fornecem uma base para a geração da resposta.

Mas **grounding é um conceito mais amplo que RAG**. Uma aplicação pode fundamentar uma resposta utilizando uma API, banco de dados, ferramenta, documento fornecido pelo usuário ou outra fonte confiável, sem necessariamente utilizar uma arquitetura RAG tradicional.

Também existe uma relação importante com **[Context Management](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-context-management/)**:

```
Fonte de informação
        ↓
Recuperação
        ↓
Seleção do conteúdo relevante
        ↓
Context Management
        ↓
Contexto fundamentado
        ↓
LLM
```

Isso mostra que grounding não significa simplesmente colocar mais informações no prompt. O objetivo é colocar **informações relevantes e confiáveis que possam sustentar a resposta**.

Por fim, grounding **não garante automaticamente que a resposta esteja correta**. Se a fonte estiver errada, desatualizada ou for interpretada incorretamente, o modelo ainda poderá produzir uma resposta inadequada.

Por isso, em sistemas mais robustos, grounding pode ser combinado com **validação, citações, ferramentas, [guardrails](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-guardrails/) e verificação das fontes**.

Em resumo:

> **Grounding conecta a geração do modelo a informações externas e verificáveis, reduzindo a dependência de conhecimento implícito e ajudando a produzir respostas mais confiáveis e contextualizadas.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-grounding/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
