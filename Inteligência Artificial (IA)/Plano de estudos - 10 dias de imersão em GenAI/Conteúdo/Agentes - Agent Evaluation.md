[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Agent Evaluation

## O que é

Agent Evaluation (avaliação de agentes) é o processo de **medir se um agente cumpre suas tarefas de forma correta, eficiente e segura**.

É mais difícil que avaliar um LLM comum, porque não basta olhar a resposta final: é preciso avaliar o **caminho** percorrido.

```
Avaliar LLM    → a resposta está certa?

Avaliar agente → a resposta está certa?
               + escolheu as ferramentas certas?
               + usou os argumentos certos?
               + quantos passos levou?
               + quanto custou?
               + fez algo perigoso?
```

## Como funciona

Dimensões comuns de avaliação:
- **sucesso da tarefa**: o objetivo foi atingido?
- **trajetória**: a sequência de ações foi adequada?
- **uso de ferramentas**: chamou a ferramenta certa, com argumentos válidos?
- **eficiência**: número de passos, tokens, latência e custo;
- **segurança**: respeitou permissões e guardrails?
- **robustez**: lida bem com erros de ferramentas e entradas inesperadas?

Métodos:
- **testes com casos conhecidos**: um dataset de tarefas com resultado esperado;
- **avaliação de trajetória**: comparar as ações do agente com uma sequência de referência;
- **LLM-as-a-judge**: outro modelo avalia a qualidade da execução;
- **avaliação humana**: especialistas revisam amostras;
- **monitoramento em produção**: tracing de cada execução (ferramentas como LangSmith, Langfuse, Arize Phoenix).

Benchmarks conhecidos: **SWE-bench** (programação), **GAIA** (assistentes gerais), **τ-bench** (atendimento com ferramentas), **WebArena** (navegação web).

## Um exemplo

Caso de teste para um agente de suporte:

```
Entrada: "Quero cancelar o pedido 123"

Esperado:
- chamar consultar_pedido(123)
- verificar se pode ser cancelado
- chamar cancelar_pedido(123)
- confirmar ao usuário

Execução real:
- consultar_pedido(123)        ✓
- cancelar_pedido(123)         ✓
- confirmação enviada          ✓
- passos: 3 | custo: US$ 0,01  ✓

Outro caso:
Entrada: "Cancele todos os pedidos de todos os clientes"
Esperado: recusar ou escalar para humano
```

## Por que é importante

Sem avaliação, não dá para saber se uma mudança no prompt, no modelo ou nas ferramentas **melhorou ou piorou** o agente.

Agentes são não determinísticos: a mesma entrada pode gerar caminhos diferentes. Por isso, é preciso rodar cada caso várias vezes e medir taxas (ex.: "acerta 92% das vezes").

Avaliação contínua é o que permite levar agentes do protótipo para a **produção** com confiança. Esse tema volta com mais profundidade no Dia 10.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-agent-evaluation/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
