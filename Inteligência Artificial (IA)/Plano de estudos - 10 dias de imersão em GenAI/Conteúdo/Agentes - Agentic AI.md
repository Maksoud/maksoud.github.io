[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Agentic AI

## O que é

Agentic AI (IA agêntica) é o **paradigma** de construir sistemas de IA que agem com algum grau de autonomia: recebem um objetivo, planejam, usam ferramentas, avaliam resultados e ajustam o rumo.

Enquanto "AI Agent" se refere a **um agente específico**, "Agentic AI" descreve a **abordagem como um todo**, que pode envolver um ou vários agentes, workflows, memória e orquestração.

Uma forma de pensar é como um espectro de autonomia:

```
Menos autonomia                                   Mais autonomia
     │                                                  │
Prompt simples → Prompt Chaining → Workflow com LLM → Agente → Multi-agentes
```

Quanto mais à direita, mais "agêntico" é o sistema: o LLM decide mais e o código fixo decide menos.

## Como funciona

Sistemas agênticos costumam combinar alguns padrões:
- **Tool use**: o modelo chama ferramentas externas.
- **Planning**: o modelo divide o objetivo em etapas.
- **Reflection**: o modelo revisa o próprio trabalho e corrige erros.
- **Multi-agent collaboration**: vários agentes especializados trabalham juntos.

```
Objetivo
   ↓
Planejar
   ↓
Executar (tools)
   ↓
Refletir sobre o resultado
   ↓
Ajustar plano ou concluir
```

## Um exemplo

Uma solução tradicional de IA para atendimento:

```
Cliente pergunta → LLM responde com base em FAQ
```

Uma solução agêntica:

```
Cliente: "Meu pedido não chegou"
   ↓
Agente consulta o pedido no ERP
   ↓
Agente consulta o rastreio na transportadora
   ↓
Agente identifica atraso
   ↓
Agente abre reclamação e oferece reenvio
   ↓
Se o valor for alto → pede aprovação humana
```

O sistema não apenas informa: ele **resolve**.

## Por que é importante

Agentic AI é a direção para onde o mercado está indo: muitas vagas de GenAI pedem experiência com "agentes" e "sistemas agênticos".

O ponto importante é saber **calibrar a autonomia**. Mais autonomia traz flexibilidade, mas também imprevisibilidade, custo e risco. Um bom profissional sabe escolher o nível certo do espectro para cada problema, adicionando guardrails, limites e Human-in-the-loop quando necessário.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-agentic-ai/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
