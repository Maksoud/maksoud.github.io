[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# State

## O que é

State (estado) é o **retrato atual da execução do agente**: tudo o que descreve em que ponto a tarefa está naquele momento.

Pode incluir:
- histórico de mensagens;
- resultados de ferramentas já executadas;
- plano e etapas concluídas;
- variáveis de negócio (ex.: `pedido_id`, `aprovado = false`);
- número de passos já usados.

Diferença em relação a Memory:

```
State  → situação da tarefa em andamento (o "agora")
Memory → conhecimento guardado para usar depois (o "lembrar")
```

Na prática, os termos se sobrepõem: a memória de curto prazo faz parte do estado.

## Como funciona

Em frameworks como o **LangGraph**, o estado é um objeto explícito que passa de etapa em etapa:

```python
class Estado(TypedDict):
    mensagens: list
    pedido_id: str | None
    status: str | None
    aprovado: bool
```

Cada nó do grafo lê o estado, faz seu trabalho e devolve atualizações:

```
[Identificar pedido] → estado.pedido_id = "123"
         ↓
[Consultar status]   → estado.status = "atrasado"
         ↓
[Pedir aprovação]    → estado.aprovado = True
         ↓
[Abrir reembolso]
```

O estado pode ser salvo (**checkpoint**) em um banco, permitindo pausar e retomar a execução.

## Um exemplo

Um agente de reembolso precisa de aprovação do gerente, que só responde no dia seguinte.

```
Dia 1:
Estado = {pedido: 123, valor: 900, aguardando_aprovacao: true}
→ salvo no banco, execução pausada

Dia 2:
Gerente aprova
→ estado recarregado
→ agente continua exatamente de onde parou
```

Sem estado persistido, seria preciso refazer tudo.

## Por que é importante

Gerenciar estado é o que separa um protótipo de um **agente de produção**.

Ele permite:
- retomar tarefas longas após falhas;
- Human-in-the-loop (pausar para aprovação);
- depurar ("em que estado o agente estava quando errou?");
- reproduzir execuções;
- controlar o fluxo com regras de negócio explícitas, em vez de depender só do LLM.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-state/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
