[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Context Relevance

## O que é

Context Relevance, ou relevância do contexto, é a medida de quanto o conteúdo fornecido à LLM é realmente relevante para responder à pergunta do usuário.

Em um sistema RAG, o Retrieval pode recuperar documentos relacionados à consulta, mas isso não significa que todo o conteúdo desses documentos seja útil. Context Relevance avalia justamente essa relação entre a pergunta e o contexto recuperado.

Uma distinção importante é:

```
Retrieval
↓
Quais documentos podem ser relevantes?

Context Relevance
↓
O contexto recuperado é realmente relevante para esta pergunta?
```

Por exemplo, para a pergunta:

```
"Qual é o prazo para solicitar reembolso?"
```

um documento sobre reembolso pode ser relevante. Porém, se o contexto recuperado contiver cinco páginas sobre regras de viagens internacionais e apenas uma frase sobre o prazo de reembolso, grande parte desse contexto possui baixa relevância para a pergunta.

Context Relevance, portanto, não significa simplesmente que o documento pertence ao mesmo assunto. O contexto deve conter informações úteis para a consulta específica.

## Como funciona

A relevância do contexto pode ser analisada depois que o Retrieval recupera os candidatos e antes que a LLM gere a resposta.

```
Pergunta
   ↓
Retrieval
   ↓
Documentos recuperados
   ↓
Avaliação da relevância
   ↓
Contexto relevante
   ↓
LLM
   ↓
Resposta
```

Imagine que o Retrieval encontre três trechos:

```
Consulta:
"Qual é o prazo para solicitar reembolso?"

Trecho A:
"Solicitações devem ser feitas em até 30 dias após a viagem."

Trecho B:
"Viagens internacionais precisam ser aprovadas pelo gestor."

Trecho C:
"O limite diário para hospedagem é de R$ 500."
```

Todos os três pertencem ao domínio de viagens e despesas, mas possuem diferentes níveis de relevância:

```
Trecho A → Alta relevância
Trecho B → Baixa relevância
Trecho C → Baixa relevância
```

O sistema pode então manter apenas o conteúdo mais relevante:

```
Retrieval
   ↓
A, B, C
   ↓
Context Relevance
   ↓
A
   ↓
LLM
```

Essa avaliação pode ser feita por diferentes mecanismos. Um Reranker, por exemplo, pode atribuir uma pontuação de relevância para cada documento ou trecho. Um modelo específico também pode avaliar se determinado trecho contém informações úteis para responder à consulta.

Isso se conecta diretamente ao Relevance Score estudado anteriormente:

```
Consulta + Documento
        ↓
Reranker
        ↓
Relevance Score
        ↓
Avaliação da relevância
```

Porém, é importante distinguir os conceitos. **Relevance Score é uma pontuação**, enquanto **Context Relevance é uma propriedade ou critério de qualidade do contexto recuperado**.

Além disso, Context Relevance pode ser avaliada não apenas no nível de documentos completos, mas também no nível de trechos, sentenças ou informações específicas.

## Um exemplo

Imagine um assistente de IA que consulta documentos internos de uma empresa.

O usuário pergunta:

```
"Quantos dias o funcionário tem para apresentar os comprovantes de uma despesa?"
```

O Retrieval recupera:

```
D1:
"Os comprovantes devem ser apresentados em até 10 dias
após o retorno da viagem."

D2:
"Viagens internacionais exigem autorização prévia."

D3:
"O limite para despesas com alimentação é de R$ 120 por dia."

D4:
"Despesas superiores a R$ 1.000 precisam de aprovação."
```

O contexto recuperado possui informações relacionadas ao domínio de despesas, mas apenas D1 responde diretamente à pergunta.

Uma etapa de avaliação pode identificar:

```
D1 → Alta relevância
D2 → Baixa relevância
D3 → Baixa relevância
D4 → Baixa relevância
```

O sistema pode então fornecer à LLM somente D1:

```
Pergunta
   ↓
Retrieval
   ↓
D1, D2, D3, D4
   ↓
Reranking / avaliação de relevância
   ↓
D1
   ↓
Contexto
   ↓
LLM
   ↓
"Os comprovantes devem ser apresentados em até
10 dias após o retorno da viagem."
```

Agora considere um caso mais sutil. D1 pode ser relevante, mas conter muito conteúdo adicional:

```
D1:
Política completa de despesas

[100 linhas sobre diferentes regras]

"Os comprovantes devem ser apresentados
em até 10 dias após o retorno da viagem."

[80 linhas sobre auditoria e aprovação]
```

Nesse caso, o documento é relevante, mas grande parte do seu conteúdo não é.

É aqui que Context Relevance se relaciona diretamente com Context Compression:

```
Documento relevante
        ↓
Context Compression
        ↓
Trecho relevante
        ↓
LLM
```

Assim, podemos ter:

```
Document Relevance
↓
O documento é relevante?

Context Relevance
↓
O conteúdo fornecido como contexto é relevante?

Context Compression
↓
Como reduzir o contexto mantendo o conteúdo relevante?
```

## Por que é importante

Context Relevance é importante porque a qualidade de um sistema RAG depende não apenas da capacidade de encontrar documentos, mas também da qualidade do contexto entregue à LLM.

Um Retrieval que retorna muitos documentos parcialmente relacionados pode produzir um contexto grande e ruidoso:

```
Retrieval
   ↓
Muitos documentos
   ↓
Informações relevantes + irrelevantes
   ↓
Contexto ruidoso
   ↓
LLM
```

Isso pode aumentar custos, consumir a Context Window e dificultar que a LLM identifique as informações realmente importantes.

Por isso, o objetivo é aproximar o pipeline de:

```
Consulta
   ↓
Retrieval
   ↓
Top-k
   ↓
Reranking
   ↓
Context Relevance
   ↓
Context Compression
   ↓
Contexto final
   ↓
LLM
```

Esse conceito também ajuda a entender melhor o problema de Lost in the Middle. Quanto mais informação irrelevante existe dentro de um contexto, maior pode ser a dificuldade de a LLM identificar aquilo que realmente importa.

Em um RAG de qualidade, portanto, não basta perguntar:

```
"Encontrei documentos relacionados?"
```

É necessário perguntar:

```
"O contexto que estou entregando à LLM
contém exatamente as informações necessárias
para responder à pergunta?"
```

Essa mudança de perspectiva é fundamental para avaliar e melhorar pipelines RAG. Retrieval trata da descoberta de candidatos, enquanto Context Relevance trata da qualidade da informação que efetivamente chega à etapa de geração.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-context-relevance/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
