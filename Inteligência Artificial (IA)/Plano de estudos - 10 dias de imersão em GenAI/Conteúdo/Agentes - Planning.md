[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Planning

## O que é

Planning (planejamento) é a capacidade do agente de **decompor um objetivo complexo em etapas menores** e decidir a ordem em que serão executadas.

Ele se relaciona com **Chain-of-thought** e **Prompt Decomposition** (Dia 2), mas aplicado à execução de ações reais.

```
Objetivo: "Preparar relatório mensal de vendas"
   ↓
Plano:
1. Buscar vendas do mês no banco
2. Comparar com o mês anterior
3. Gerar gráfico
4. Escrever resumo
5. Enviar por e-mail ao gestor
```

## Como funciona

Há duas abordagens principais:

**1. Planejamento passo a passo (ReAct)**

O agente decide apenas o próximo passo, observa o resultado e decide de novo. É flexível, mas pode "se perder" em tarefas longas.

```
Pensa → Age → Observa → Pensa → Age → ...
```

**2. Plan-and-Execute**

O agente cria o plano completo primeiro e depois executa as etapas, revisando o plano se algo der errado.

```
Planejar tudo
   ↓
Executar etapa 1 → etapa 2 → etapa 3
   ↓
Algo falhou? → Replanejar
```

Outras técnicas relacionadas:
- **Reflection**: o agente avalia o resultado e corrige o plano;
- **Tree of Thoughts**: explora vários caminhos possíveis antes de escolher;
- **To-do list**: o agente mantém uma lista de tarefas atualizada no próprio contexto.

## Um exemplo

Pedido: "Descubra por que o faturamento caiu em outubro."

```
Plano inicial:
1. Buscar faturamento de setembro e outubro
2. Quebrar por região
3. Quebrar por produto
4. Identificar maior variação

Execução:
Etapa 2 → Região Sul caiu 40%
   ↓
Replanejamento:
5. Investigar vendas da região Sul por vendedor
   ↓
Descoberta: maior cliente da região cancelou o contrato
```

O plano mudou conforme as descobertas.

## Por que é importante

Sem planejamento, agentes tendem a:
- repetir ações;
- esquecer partes do objetivo;
- tomar caminhos aleatórios em tarefas longas.

Com planejamento, o agente fica mais **previsível, eficiente e fácil de depurar**, já que o plano pode ser inspecionado (e até aprovado por um humano) antes da execução.

Modelos com **reasoning** (que "pensam" antes de responder) melhoraram muito essa capacidade.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-planning/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
