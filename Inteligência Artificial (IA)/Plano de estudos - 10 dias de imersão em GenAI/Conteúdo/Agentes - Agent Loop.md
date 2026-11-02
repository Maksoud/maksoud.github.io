[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Agent Loop

## O que é

Agent Loop é o **ciclo repetitivo que faz um agente funcionar**: o modelo pensa, age, observa o resultado e repete até concluir a tarefa.

É o que transforma uma chamada única ao LLM em um **processo iterativo**.

```
        ┌──────────────┐
        │   Thought    │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │    Action    │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Observation  │
        └──────┬───────┘
               ↓
       Tarefa concluída?
         ↙         ↘
       Não         Sim
        ↓            ↓
  volta ao início  Resposta final
```

## Como funciona

Em código, o loop é surpreendentemente simples:

```python
mensagens = [{"role": "user", "content": pergunta}]

for passo in range(MAX_PASSOS):
    resposta = llm(mensagens, tools=ferramentas)

    if not resposta.tool_calls:
        return resposta.texto          # terminou

    for chamada in resposta.tool_calls:
        resultado = executar(chamada)  # Action
        mensagens.append(resultado)    # Observation

return "Limite de passos atingido"
```

Os elementos essenciais:
- **condição de parada**: o modelo responde sem pedir ferramentas;
- **limite de iterações**: evita loops infinitos e custos descontrolados;
- **histórico**: cada passo é adicionado às mensagens, formando o estado.

## Um exemplo

Pergunta: "Qual a população da capital do país que ganhou a Copa de 2002?"

```
Volta 1
Thought: preciso saber quem ganhou a Copa de 2002
Action: buscar_web("campeão Copa 2002")
Observation: Brasil

Volta 2
Thought: a capital do Brasil é Brasília; preciso da população
Action: buscar_web("população Brasília")
Observation: cerca de 2,8 milhões

Volta 3
Thought: tenho a resposta
Resposta: "Brasília, com cerca de 2,8 milhões de habitantes."
```

## Por que é importante

Entender o loop desmistifica os agentes: por trás dos frameworks (LangGraph, smolagents, CrewAI, OpenAI Agents SDK), quase sempre existe esse mesmo ciclo.

Problemas comuns que surgem no loop:
- **loops infinitos**: o agente repete a mesma ação;
- **contexto crescente**: cada volta adiciona tokens, aumentando custo e latência;
- **erros em cascata**: um passo errado contamina os seguintes.

Soluções: limite de passos, compressão de contexto, detecção de repetição e checkpoints com Human-in-the-loop.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-agent-loop/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
