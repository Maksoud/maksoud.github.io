[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Observations

## O que é

Observation (observação) é o **resultado que volta para o agente depois de uma ação**. É o feedback do ambiente: o retorno de uma API, as linhas de uma consulta SQL, o texto de uma página, uma mensagem de erro.

```
Action      → o agente faz algo
Observation → o agente vê o que aconteceu
```

Sem observações, o agente agiria "às cegas". São elas que permitem ajustar o plano.

## Como funciona

Depois que a aplicação executa a ferramenta, o resultado é adicionado ao contexto (normalmente como uma mensagem do tipo "tool result"). Na próxima iteração, o LLM lê esse resultado e decide o próximo passo.

```
Thought:     "Vou buscar o cliente"
Action:      buscar_cliente(cpf="123")
Observation: {"erro": "CPF não encontrado"}

Thought:     "Talvez o CPF esteja formatado errado. Vou tentar com pontuação."
Action:      buscar_cliente(cpf="000.000.001-23")
Observation: {"nome": "Maria", "plano": "Premium"}
```

Repare que a observação de erro foi **útil**: ela permitiu ao agente corrigir o próprio caminho.

## Um exemplo

Um agente que escreve código:

```
Action:      executar_python("print(soma([1,2,3]))")
Observation: NameError: name 'soma' is not defined

Thought:     "Preciso usar sum()"
Action:      executar_python("print(sum([1,2,3]))")
Observation: 6
```

## Por que é importante

A qualidade das observações afeta diretamente a qualidade do agente.

Boas práticas:
- **retornos concisos**: devolver só o que é útil (um JSON de 5.000 linhas consome contexto e confunde o modelo);
- **erros informativos**: "CPF deve ter 11 dígitos" ajuda mais que "Erro 400";
- **formato consistente**: o modelo interpreta melhor estruturas previsíveis;
- **cuidado com Prompt Injection**: uma observação vinda da web ou de um documento pode conter instruções maliciosas. O agente deve tratá-la como **dado**, não como ordem.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-observations/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
