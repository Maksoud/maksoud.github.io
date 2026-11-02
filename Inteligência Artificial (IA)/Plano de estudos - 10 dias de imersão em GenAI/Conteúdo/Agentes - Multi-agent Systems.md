[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Multi-agent Systems

## O que é

Multi-agent Systems (sistemas multiagentes) são arquiteturas em que **vários agentes, cada um com seu papel, ferramentas e instruções**, colaboram para resolver uma tarefa.

A ideia é a mesma de uma equipe: em vez de um generalista fazendo tudo, especialistas dividem o trabalho.

```
Um agente só:
Agente → faz pesquisa, análise, redação e revisão

Multiagentes:
Pesquisador → Analista → Redator → Revisor
```

## Como funciona

Arquiteturas comuns:

**Supervisor (hierárquica)**: um agente coordena os demais.

```
           Supervisor
        ↙      ↓      ↘
Pesquisador  Analista  Redator
```

**Sequencial (pipeline)**: cada agente passa o resultado ao próximo.

```
Agente A → Agente B → Agente C
```

**Handoff**: um agente transfere a conversa para outro mais adequado (padrão do OpenAI Agents SDK).

```
Triagem → "isso é financeiro" → Agente Financeiro
```

**Rede/colaborativa**: agentes conversam entre si livremente (estilo AutoGen).

Frameworks populares: **LangGraph**, **CrewAI**, **AutoGen**, **OpenAI Agents SDK**. Protocolos como **A2A (Agent-to-Agent)** buscam padronizar a comunicação entre agentes de fornecedores diferentes.

## Um exemplo

Tarefa: "Produza um relatório sobre concorrentes no mercado de CRM."

```
Supervisor divide a tarefa
   ↓
Agente Pesquisador (tool: busca web)
→ coleta dados de 5 concorrentes (em paralelo)
   ↓
Agente Analista (tool: Python)
→ compara preços e funcionalidades
   ↓
Agente Redator
→ escreve o relatório
   ↓
Agente Revisor
→ verifica fontes e consistência
   ↓
Supervisor entrega o resultado
```

## Por que é importante

Vantagens:
- **especialização**: prompts e ferramentas focados funcionam melhor;
- **contextos menores**: cada agente vê só o que precisa;
- **paralelismo**: tarefas independentes rodam ao mesmo tempo;
- **manutenção**: dá para melhorar um agente sem mexer nos outros.

Desvantagens:
- custo e latência bem maiores (muitas chamadas ao LLM);
- falhas de comunicação entre agentes;
- depuração mais difícil.

A recomendação comum é: **comece com um agente só**. Passe para multiagentes quando houver ganho claro, como tarefas paralelizáveis ou domínios muito diferentes.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-multi-agent-systems/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
