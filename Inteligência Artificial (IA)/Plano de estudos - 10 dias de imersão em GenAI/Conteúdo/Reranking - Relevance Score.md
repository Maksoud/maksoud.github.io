[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Relevance Score

## O que é

Relevance Score, ou pontuação de relevância, é um valor utilizado para representar o quanto um documento ou trecho é relevante para uma determinada consulta.

No contexto de Reranking, essa pontuação é produzida por um Reranker, como um Cross Encoder, depois que os documentos candidatos já foram recuperados.

É importante não confundir Relevance Score com Similarity Score. Embora ambos sejam utilizados para ordenar resultados, eles podem representar coisas diferentes. O Similarity Score normalmente mede a proximidade entre representações, como embeddings. O Relevance Score de um Reranker busca avaliar diretamente a relação entre a consulta e o conteúdo recuperado.

Por exemplo:

```
Consulta
   ↓
"Qual é o prazo para cancelar o contrato?"
   ↓
Reranker
   ↓
Documento A → 0.94
Documento B → 0.71
Documento C → 0.28
```

Nesse exemplo, o Documento A foi considerado mais relevante para a consulta do que os demais.

## Como funciona

Depois do Retrieval inicial, o sistema possui um conjunto de documentos candidatos. O Reranker analisa cada candidato em relação à consulta e produz uma pontuação.

```
Consulta
   +
Documento 1
   ↓
Reranker
   ↓
Relevance Score

Consulta
   +
Documento 2
   ↓
Reranker
   ↓
Relevance Score

Consulta
   +
Documento 3
   ↓
Reranker
   ↓
Relevance Score
```

Os resultados são então ordenados pela pontuação:

```
Documento A → 0.94
Documento C → 0.88
Documento B → 0.63
Documento D → 0.21
```

O sistema pode selecionar apenas os documentos mais relevantes para formar o contexto enviado à LLM:

```
Retrieval
   ↓
Top-k inicial
   ↓
Reranker
   ↓
Relevance Scores
   ↓
Ordenação
   ↓
Top-k final
   ↓
Contexto
   ↓
LLM
```

Um detalhe importante é que **o significado numérico do score depende do modelo e da implementação**.

Um score de `0.9` não significa necessariamente que o documento possui 90% de relevância. Em alguns sistemas, valores maiores indicam maior relevância. Em outros, a saída pode ser um logit, uma distância transformada ou outro valor cuja escala não seja diretamente interpretável.

Por isso, o mais importante normalmente é a **ordenação relativa entre os candidatos**, e não interpretar o número isoladamente.

Por exemplo:

```
Documento A → 8.7
Documento B → 6.2
Documento C → 3.4
```

Podemos concluir que A foi considerado mais relevante que B, e B mais relevante que C. Não devemos concluir automaticamente que A é "87% relevante".

Em alguns sistemas também é possível estabelecer um threshold, ou limiar mínimo:

```
Relevance Score ≥ 0.70
        ↓
Aceitar resultado

Relevance Score < 0.70
        ↓
Descartar resultado
```

Isso pode ser útil quando o sistema precisa evitar enviar ao contexto documentos que tenham pouca relação com a pergunta.

## Um exemplo

Imagine um RAG corporativo que possui documentos sobre políticas de reembolso.

O usuário pergunta:

```
"Qual é o prazo para solicitar reembolso de uma viagem?"
```

O Retrieval inicial recupera cinco documentos:

```
D1: Política de reembolso de viagens
D2: Política de viagens internacionais
D3: Política de contratação de fornecedores
D4: Benefícios corporativos
D5: Política de cartão corporativo
```

O Reranker avalia a relação entre a pergunta e cada documento:

```
D1 → 0.96
D2 → 0.81
D5 → 0.64
D4 → 0.32
D3 → 0.08
```

O ranking final fica:

```
1. D1 → 0.96
2. D2 → 0.81
3. D5 → 0.64
4. D4 → 0.32
5. D3 → 0.08
```

Se o sistema precisar enviar apenas os dois melhores documentos para a LLM:

```
Pergunta
   ↓
Retrieval
   ↓
D1, D2, D3, D4, D5
   ↓
Reranker
   ↓
Relevance Score
   ↓
D1, D2
   ↓
Contexto
   ↓
LLM
```

O Relevance Score, portanto, funciona como um mecanismo para transformar a avaliação do Reranker em uma ordenação dos candidatos.

## Por que é importante

Relevance Score é importante porque o Retrieval inicial pode recuperar documentos que parecem relacionados, mas que não são igualmente úteis para responder à pergunta.

O score permite ao Reranker diferenciar esses candidatos e priorizar aqueles que apresentam uma relação mais forte com a consulta.

Isso é especialmente importante em RAG porque o contexto enviado à LLM é limitado. Se documentos pouco relevantes ocuparem esse espaço, informações importantes podem ficar de fora.

A relação entre os conceitos pode ser visualizada assim:

```
Retrieval
   ↓
Top-k inicial
   ↓
Reranker
   ↓
Relevance Score
   ↓
Ranking
   ↓
Top-k final
   ↓
Contexto
   ↓
LLM
```

O Relevance Score também ajuda a estabelecer uma distinção importante entre as etapas. O **Retrieval** encontra candidatos, o **Reranking** reorganiza esses candidatos e o **Relevance Score** representa a avaliação de relevância utilizada nessa reorganização.

Por fim, o score não deve ser tratado automaticamente como uma medida universal de qualidade. Seu valor depende do modelo, da função utilizada e do contexto de aplicação. Em sistemas reais, é comum avaliar empiricamente quais scores ou posições no ranking produzem os melhores resultados para o conjunto de consultas utilizado.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/reranking-relevance-score/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
