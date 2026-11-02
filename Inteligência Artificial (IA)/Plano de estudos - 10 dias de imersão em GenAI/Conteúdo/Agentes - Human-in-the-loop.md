[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Human-in-the-loop

## O que é

Human-in-the-loop (HITL, humano no circuito) é a prática de **inserir uma pessoa em pontos específicos do fluxo do agente** para aprovar, corrigir ou complementar suas decisões.

O agente faz o trabalho pesado, mas **decisões críticas passam por um humano**.

```
Agente planeja → Humano aprova → Agente executa
```

## Como funciona

Formas comuns de intervenção:
- **aprovação**: o agente pausa antes de uma ação sensível ("Posso enviar este e-mail?");
- **edição**: o humano ajusta o que o agente propôs (texto, argumentos de uma ferramenta);
- **esclarecimento**: o agente pergunta quando falta informação;
- **escalonamento**: o agente transfere o caso para um humano quando não tem confiança suficiente;
- **revisão posterior**: o humano avalia amostras do que o agente fez.

Tecnicamente, depende de **State** persistido: o agente salva o estado, pausa, aguarda a resposta humana e retoma.

```
Agente
   ↓
Ação sensível?
 ├── Não → executa
 └── Sim → salva estado e pausa
               ↓
          Humano decide
           ├── Aprova → executa
           ├── Edita → executa versão editada
           └── Rejeita → agente replaneja
```

O LangGraph, por exemplo, tem recursos de "interrupt" para isso.

## Um exemplo

Agente financeiro:

```
Pedido: "Pague as faturas vencidas deste mês"
   ↓
Agente encontra 4 faturas
   ↓
3 faturas abaixo de R$ 1.000 → paga automaticamente
1 fatura de R$ 25.000 → pausa
   ↓
"Encontrei uma fatura de R$ 25.000 do fornecedor X. Confirma o pagamento?"
   ↓
Gestor aprova
   ↓
Agente paga e registra
```

## Por que é importante

Agentes erram. Em ações irreversíveis (pagar, apagar, enviar, publicar), um erro pode ser caro.

O HITL permite:
- usar agentes em processos críticos com segurança;
- atender exigências de compliance e auditoria;
- gerar dados de feedback para melhorar o agente;
- aumentar a autonomia aos poucos, conforme a confiança cresce.

A arte está em **calibrar**: pedir aprovação demais torna o agente inútil; pedir de menos o torna perigoso.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-human-in-the-loop/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
