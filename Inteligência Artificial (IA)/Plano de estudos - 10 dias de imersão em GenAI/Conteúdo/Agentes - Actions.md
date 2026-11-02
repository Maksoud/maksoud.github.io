[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Actions

## O que é

Action (ação) é o **passo concreto que o agente decide executar** em um momento do ciclo. Normalmente é uma chamada de ferramenta com argumentos específicos, mas também pode ser "responder ao usuário" ou "encerrar a tarefa".

A diferença entre Tool e Action:

```
Tool   → a capacidade disponível        (buscar_pedido)
Action → o uso dela em um momento       (buscar_pedido(numero="123"))
```

## Como funciona

No ciclo **Thought → Action → Observation**, a Action é a ponte entre o raciocínio e o mundo externo:

```
Thought:     "Preciso do status do pedido"
Action:      buscar_pedido(numero="123")
Observation: {"status": "atrasado"}
```

As ações podem ser expressas de formas diferentes:
- **JSON**: o modelo gera um objeto com ferramenta e argumentos (o formato mais comum nas APIs).
- **Código**: o modelo escreve um trecho de código que chama as ferramentas (abordagem dos "code agents", como no smolagents da Hugging Face).
- **Texto estruturado**: formato do ReAct original, como `Action: search[...]`.

Code agents permitem combinar várias ações em um passo só:

```python
pedido = buscar_pedido("123")
if pedido["status"] == "atrasado":
    abrir_reclamacao(pedido["id"])
```

## Um exemplo

Tarefa: "Agende uma reunião com a Ana na próxima terça às 10h."

```
Action 1: consultar_agenda(pessoa="Ana", data="terça")
Action 2: criar_evento(titulo="Reunião", data="terça 10h", convidados=["Ana"])
Action 3: responder("Reunião marcada para terça às 10h.")
```

Cada ação é uma decisão do modelo, tomada com base no que foi observado antes.

## Por que é importante

Ações são onde o agente **produz efeito no mundo**, e por isso são onde estão os maiores riscos.

Pontos de atenção:
- **ações reversíveis vs irreversíveis**: consultar é seguro, apagar ou pagar não;
- **validação**: a aplicação deve conferir os argumentos antes de executar;
- **limites**: número máximo de ações por tarefa, para evitar loops;
- **auditoria**: registrar cada ação executada (logs e tracing).

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-actions/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
