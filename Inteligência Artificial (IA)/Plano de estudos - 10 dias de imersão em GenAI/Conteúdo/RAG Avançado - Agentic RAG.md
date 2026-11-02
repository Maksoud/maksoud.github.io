[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Agentic RAG

## O que é

Agentic RAG é uma abordagem de RAG em que o processo de recuperação de informações deixa de ser totalmente pré-definido e passa a ser **orquestrado por um agente de IA**.

Em um RAG tradicional, o fluxo costuma ser relativamente linear:

```
Pergunta
↓
Retrieval
↓
Top-k documentos
↓
Reranking
↓
Contexto
↓
LLM
↓
Resposta
```

No Agentic RAG, o próprio LLM pode decidir **como buscar a informação, quais fontes consultar, quando fazer novas buscas e quando já possui evidências suficientes para responder**:

```
Pergunta
↓
Agente analisa a tarefa
↓
Planeja a busca
↓
Escolhe uma fonte ou ferramenta
↓
Retrieval
↓
Avalia os resultados
↓
Nova busca, se necessário
↓
Combina as evidências
↓
Decide que possui contexto suficiente
↓
LLM gera a resposta
```

O termo "agentic" está relacionado justamente à capacidade de **tomar decisões durante o processo**, em vez de apenas executar uma sequência fixa de etapas.

Isso torna o Agentic RAG especialmente útil para perguntas complexas, que não podem ser respondidas adequadamente com uma única consulta ao mecanismo de Retrieval.

## Como funciona

A principal diferença está na existência de um **loop de decisão**.

Em vez de simplesmente recuperar os documentos mais semelhantes à consulta original, o agente pode avaliar o que encontrou e decidir qual deve ser o próximo passo.

Por exemplo, imagine a pergunta:

> "Compare o desempenho financeiro das três unidades da empresa no último trimestre e explique os principais motivos das diferenças."

Um RAG tradicional poderia fazer uma única busca por termos relacionados a desempenho financeiro e retornar alguns documentos.

Um Agentic RAG pode decompor a tarefa:

```
Pergunta
↓
Agente identifica três unidades
↓
Busca dados da Unidade A
↓
Avalia resultados
↓
Busca dados da Unidade B
↓
Avalia resultados
↓
Busca dados da Unidade C
↓
Procura informações sobre receitas, custos e margem
↓
Compara os resultados
↓
Busca explicações para diferenças relevantes
↓
Verifica se existem evidências suficientes
↓
Gera resposta
```

O agente pode inclusive utilizar diferentes fontes ou ferramentas:

```
                    ┌──→ Base de documentos
Pergunta → Agente ──┼──→ Vector Database
                    ├──→ Busca por palavras-chave
                    ├──→ Banco de dados SQL
                    └──→ API externa
```

Isso significa que Agentic RAG não é necessariamente apenas "um RAG com mais buscas". O ponto central é que **o modelo participa da orquestração do processo de busca**.

Uma característica importante é a possibilidade de **query decomposition**. O agente pode transformar uma pergunta complexa em várias perguntas menores.

Por exemplo:

```
Pergunta:
"Por que as vendas caíram no segundo trimestre?"

        ↓

Subperguntas:

1. Qual foi a variação das vendas?
2. Quais produtos apresentaram maior queda?
3. Quais regiões apresentaram maior queda?
4. Houve alteração de preços?
5. Houve problemas de estoque?
6. Existem fatores externos documentados?
```

Cada subpergunta pode gerar uma busca diferente. Depois, o agente reúne as evidências para construir uma resposta.

Outra característica importante é a capacidade de **iterar**.

Se a primeira busca retornar informações insuficientes, o agente pode reformular a consulta:

```
Consulta original
↓
Retrieval
↓
Resultados insuficientes
↓
Query Rewriting / Query Expansion
↓
Nova busca
↓
Novos resultados
↓
Avaliação
↓
Contexto suficiente?
├── Não → nova busca
└── Sim → resposta
```

Esse comportamento é bastante diferente de um pipeline RAG rígido, no qual as etapas são normalmente determinadas antecipadamente.

É importante também não confundir Agentic RAG com simplesmente utilizar um agente que acessa documentos. **O componente essencial é a capacidade de decisão sobre o processo de recuperação e utilização das informações.**

## Um exemplo

Imagine um assistente corporativo conectado a documentos internos, banco de dados financeiro e sistema de vendas.

O usuário pergunta:

> "Por que a receita da região Sul caiu em setembro e isso foi causado por redução de vendas ou por mudança no preço médio?"

O agente pode executar algo semelhante a:

```
Pergunta
↓
Agente identifica necessidade de:
  • receita
  • volume de vendas
  • preço médio
  • região Sul
  • setembro
↓
Consulta banco de dados
↓
Obtém queda de receita
↓
Busca documentos sobre vendas da região
↓
Obtém redução no volume
↓
Busca informações sobre preços
↓
Identifica alteração no preço médio
↓
Compara os fatores
↓
Busca relatório gerencial para validar a causa
↓
Evidências suficientes
↓
LLM gera resposta fundamentada
```

Nesse cenário, o agente não está apenas recuperando documentos semanticamente semelhantes à pergunta original.

Ele está **investigando a pergunta**.

Essa é uma das ideias mais importantes do Agentic RAG: a recuperação pode se tornar um processo iterativo de investigação.

## Por que é importante

Agentic RAG é importante porque permite aplicar RAG a problemas que possuem **múltiplas etapas, múltiplas fontes e necessidade de investigação**.

Um RAG tradicional funciona muito bem quando existe uma relação relativamente direta entre pergunta e informação necessária:

```
Pergunta → Recuperação → Contexto → Resposta
```

Já perguntas mais complexas podem exigir:

```
Pergunta
↓
Planejamento
↓
Decomposição
↓
Múltiplas buscas
↓
Avaliação das evidências
↓
Novas buscas
↓
Síntese
↓
Resposta
```

Isso pode melhorar a capacidade de lidar com perguntas complexas, mas existe um custo. Quanto mais autonomia o agente possui, maior tende a ser a complexidade do sistema, o número de chamadas ao modelo e às ferramentas, a latência e o custo.

Também aumenta a possibilidade de decisões ruins durante o processo. Um agente pode escolher uma fonte inadequada, realizar buscas desnecessárias ou seguir uma linha de investigação equivocada.

Por isso, Agentic RAG não significa simplesmente "quanto mais agente, melhor". Em sistemas reais, é importante controlar **quais ferramentas o agente pode utilizar, quais fontes são confiáveis, quantas iterações são permitidas e como as evidências são avaliadas**.

A principal evolução em relação ao RAG tradicional pode ser resumida assim:

```
RAG tradicional
Pergunta → Recuperar → Gerar

Agentic RAG
Pergunta → Planejar → Recuperar → Avaliar → Decidir
                    ↑                    ↓
                    └──── Nova busca ───┘
```

Assim, enquanto o RAG tradicional trata Retrieval principalmente como uma etapa do pipeline, o Agentic RAG transforma a recuperação em um **processo adaptativo de investigação**, no qual o agente decide dinamicamente o que precisa descobrir antes de produzir a resposta.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/rag-avancado-agentic-rag/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
