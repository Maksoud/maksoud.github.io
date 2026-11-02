[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Orchestration

## O que é

Orchestration (orquestração) é a **coordenação do fluxo de um sistema com LLMs**: quem faz o quê, em que ordem, com quais dados e o que acontece em caso de erro.

O "orquestrador" pode ser:
- **código fixo** (o desenvolvedor define o fluxo);
- **o próprio LLM** (ele decide o próximo passo);
- **uma combinação** dos dois (o mais comum em produção).

## Como funciona

Padrões de orquestração frequentes (descritos, por exemplo, pela Anthropic em "Building effective agents"):

**Prompt Chaining**: etapas em sequência.

```
Etapa 1 → Etapa 2 → Etapa 3
```

**Routing**: classificar a entrada e enviar para o fluxo certo.

```
Entrada → Classificador ─┬→ Fluxo financeiro
                         ├→ Fluxo técnico
                         └→ Fluxo comercial
```

**Parallelization**: várias tarefas ao mesmo tempo e depois juntar.

```
       ┌→ Tarefa A ┐
Entrada├→ Tarefa B ├→ Combinar
       └→ Tarefa C ┘
```

**Orchestrator-Workers**: um LLM central divide o trabalho e delega a outros.

```
Orquestrador → Worker 1
             → Worker 2
             → Worker 3
      ↓
  Sintetiza
```

**Evaluator-Optimizer**: um gera, outro avalia, repete até ficar bom.

```
Gerar → Avaliar → Melhorar → Avaliar → ...
```

Frameworks como **LangGraph** representam a orquestração como um grafo de nós (etapas) e arestas (transições), inclusive com condições e ciclos.

## Um exemplo

Sistema de atendimento:

```
Mensagem do cliente
   ↓
Router (LLM classifica)
   ├── Dúvida → Agente RAG (base de conhecimento)
   ├── Problema técnico → Agente de suporte (tools de diagnóstico)
   └── Cancelamento → Fluxo fixo + aprovação humana
   ↓
Revisor (checa tom e políticas)
   ↓
Resposta
```

Parte do fluxo é decidida pelo LLM (classificação), parte é fixa (cancelamento sempre passa por humano).

## Por que é importante

Boa orquestração é o que torna sistemas de IA **confiáveis**. Deixar tudo nas mãos do LLM é flexível, mas imprevisível; fixar tudo em código é previsível, mas rígido.

O trabalho do engenheiro é encontrar o equilíbrio: **determinístico onde dá, agêntico onde precisa**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-orchestration/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
