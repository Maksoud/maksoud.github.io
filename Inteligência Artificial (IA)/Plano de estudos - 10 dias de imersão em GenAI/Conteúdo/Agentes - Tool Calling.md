[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Tool Calling

## O que é

Tool Calling é a capacidade de um LLM **solicitar a execução de uma ferramenta externa** em vez de (ou antes de) responder diretamente em texto.

Ponto essencial: **o modelo não executa a ferramenta**. Ele apenas gera uma solicitação estruturada dizendo qual ferramenta quer usar e com quais argumentos. Quem executa é a aplicação.

```
LLM: "Quero chamar a ferramenta X com estes argumentos"
   ↓
Aplicação executa X
   ↓
Aplicação devolve o resultado ao LLM
   ↓
LLM continua o raciocínio
```

## Como funciona

1. A aplicação envia ao modelo a pergunta e a **lista de ferramentas disponíveis** (nome, descrição e parâmetros, geralmente em JSON Schema).
2. O modelo decide se precisa de alguma ferramenta.
3. Se precisar, responde com uma chamada estruturada.
4. A aplicação executa e envia o resultado de volta.
5. O modelo usa o resultado para responder ou chamar outra ferramenta.

Exemplo de definição de ferramenta:

```json
{
  "name": "consultar_clima",
  "description": "Retorna a previsão do tempo para uma cidade",
  "parameters": {
    "type": "object",
    "properties": {
      "cidade": { "type": "string" }
    },
    "required": ["cidade"]
  }
}
```

Resposta do modelo:

```json
{
  "tool": "consultar_clima",
  "arguments": { "cidade": "São Paulo" }
}
```

## Um exemplo

```
Usuário: "Vai chover em São Paulo amanhã?"
   ↓
LLM → tool_call: consultar_clima(cidade="São Paulo")
   ↓
Aplicação chama a API de clima
   ↓
Resultado: {"amanha": "chuva, 80%"}
   ↓
LLM: "Sim, há 80% de chance de chuva amanhã em São Paulo."
```

## Por que é importante

Tool Calling é a **base técnica de qualquer agente**. Sem ele, o LLM fica limitado ao conhecimento do treinamento e ao texto do prompt.

Com ele, o modelo pode:
- buscar dados atualizados;
- consultar bancos e APIs;
- executar código;
- realizar ações em sistemas.

A qualidade do Tool Calling depende muito de **boas descrições de ferramentas**: nomes claros, descrições objetivas e parâmetros bem definidos. Uma ferramenta mal descrita é chamada na hora errada ou com argumentos errados.

Padrões como o **MCP (Model Context Protocol)** surgiram para padronizar a forma de expor ferramentas aos modelos.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-tool-calling/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
