[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# AI Agent

## O que é

Um AI Agent (agente de IA) é um sistema que usa um LLM como "cérebro" para **decidir quais ações executar** a fim de atingir um objetivo, utilizando ferramentas, observando os resultados e repetindo o processo até concluir a tarefa.

A diferença em relação a um chatbot comum é que o chatbot apenas **responde**. O agente **age**.

```
Chatbot
Pergunta → LLM → Resposta

Agente
Objetivo → LLM → Ação → Resultado → LLM → Ação → ... → Resposta
```

Uma definição prática:

> **Agente = LLM + ferramentas + estado/contexto + loop de decisão + capacidade de executar ações.**

A Anthropic faz uma distinção útil:
- **Workflows**: sistemas em que o LLM e as ferramentas seguem caminhos de código predefinidos.
- **Agents**: sistemas em que o próprio LLM dirige dinamicamente o processo e decide como usar as ferramentas.

## Como funciona

Os componentes básicos de um agente são:

```
┌──────────────────────────────────┐
│              Agente              │
│                                  │
│   LLM (raciocínio e decisão)     │
│        ↓            ↑            │
│   Tools (ações)   Observations   │
│        ↓            ↑            │
│   Memory / State (contexto)      │
└──────────────────────────────────┘
```

- **LLM**: interpreta o objetivo e decide o próximo passo.
- **Tools**: funções, APIs, bancos de dados ou buscas que o agente pode acionar.
- **Observations**: os resultados retornados pelas ferramentas.
- **Memory/State**: o que o agente já fez e já sabe durante a tarefa.
- **Loop**: o ciclo que se repete até o objetivo ser alcançado ou um limite ser atingido.

O ciclo clássico é o **Thought → Action → Observation**, popularizado pelo padrão ReAct (Reasoning + Acting).

## Um exemplo

O usuário pede:

> "Quantos chamados críticos abertos temos hoje e quem está responsável por eles?"

O agente pode executar:

```
Thought: preciso consultar o sistema de chamados
Action: buscar_chamados(prioridade="crítica", status="aberto")
Observation: 3 chamados encontrados (INC001, INC002, INC003)

Thought: preciso saber os responsáveis
Action: buscar_responsaveis(["INC001", "INC002", "INC003"])
Observation: Ana, Bruno, Ana

Thought: já tenho tudo
Resposta: "Há 3 chamados críticos abertos. Ana cuida de 2 e Bruno de 1."
```

Ninguém programou essa sequência exata. O agente **decidiu** os passos.

## Por que é importante

Agentes permitem que LLMs saiam do papel de "gerador de texto" e passem a **resolver tarefas reais**: consultar sistemas, atualizar registros, enviar mensagens, escrever e executar código.

Mas autonomia tem custo:
- mais chamadas ao modelo (latência e custo maiores);
- mais pontos de falha;
- riscos de executar ações erradas.

Por isso, a recomendação comum é **começar pelo mais simples**: se um prompt ou um workflow fixo resolve, não é preciso um agente. Use agentes quando o caminho até a resposta **não pode ser previsto** com antecedência.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-ai-agent/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
