[← Voltar para o Plano de estudos: 10 dias de imersão em GenAI](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/)

# Dia 7: Agentes

Agora vem a segunda grande área da vaga.

E aqui existe muita confusão no mercado.

Você precisa abandonar a definição:

> “Agente é um chatbot inteligente.”

Pense:

> **Agente = LLM + ferramentas + estado/contexto + loop de decisão + capacidade de executar ações.**

Exemplo:

```
Usuário
   ↓
LLM
   ↓
"Preciso consultar o banco"
   ↓
Tool: database()
   ↓
Resultado
   ↓
LLM
   ↓
"Preciso consultar API"
   ↓
Tool: API()
   ↓
Resultado
   ↓
Resposta
```

---

## Estude estes termos

- AI agent
- agentic AI
- tool calling
- function calling
- tools
- actions
- observations
- planning
- agent loop
- memory
- state
- orchestration
- multi-agent systems
- human-in-the-loop
- autonomous agents
- agent evaluation

A formação atual da Hugging Face é excelente para isso porque estrutura o aprendizado justamente em **LLMs → mensagens → tools → ciclo Thought/Action/Observation → agentes**, avançando depois para frameworks como smolagents, LlamaIndex e LangGraph. [Hugging Face](https://huggingface.co/learn/agents-course/unit1/introduction?utm_source=chatgpt.com)

---

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
