[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Function Calling

## O que é

Function Calling é o nome que a OpenAI deu, em 2023, ao recurso que permite ao LLM **gerar uma chamada estruturada para uma função** definida pelo desenvolvedor.

Na prática, **Function Calling e Tool Calling são o mesmo conceito**. "Function Calling" foi o termo original; "Tool Calling" se tornou o termo mais geral, porque uma ferramenta pode ser uma função, uma API, uma busca na web, um interpretador de código etc.

```
Function Calling  ≈  Tool Calling
(termo original)     (termo atual e mais amplo)
```

## Como funciona

O desenvolvedor descreve a função com nome, descrição e parâmetros:

```python
def buscar_pedido(numero: str) -> dict:
    """Busca os dados de um pedido pelo número."""
    ...
```

Essa função é apresentada ao modelo como um schema. Quando o usuário pergunta algo relacionado, o modelo devolve:

```json
{
  "name": "buscar_pedido",
  "arguments": "{\"numero\": \"12345\"}"
}
```

O código da aplicação lê essa saída, chama `buscar_pedido("12345")` de verdade e devolve o resultado ao modelo.

```
Usuário → LLM → JSON com função e argumentos
                         ↓
               Código executa a função
                         ↓
               Resultado volta ao LLM
                         ↓
                     Resposta
```

## Um exemplo

```
Usuário: "Qual o status do pedido 12345?"
   ↓
LLM: buscar_pedido(numero="12345")
   ↓
Resultado: {"status": "enviado", "previsao": "05/11"}
   ↓
LLM: "Seu pedido foi enviado e deve chegar em 05/11."
```

O mesmo recurso também é usado sem agente nenhum, apenas para **extrair dados estruturados** de um texto (por exemplo, transformar um e-mail em um objeto com nome, data e assunto).

## Por que é importante

Function Calling resolveu um problema antigo: fazer o modelo devolver **saídas confiáveis e estruturadas** que um programa consegue processar, em vez de texto livre difícil de interpretar.

Ele também conecta diretamente com **Structured Output** e **JSON Schema**, vistos no Dia 2.

Em entrevistas, vale saber explicar que:
- o modelo **não executa** a função;
- a aplicação é responsável por validar argumentos e tratar erros;
- é preciso cuidado com permissões, porque o modelo pode pedir a função errada ou com argumentos inesperados.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-function-calling/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
