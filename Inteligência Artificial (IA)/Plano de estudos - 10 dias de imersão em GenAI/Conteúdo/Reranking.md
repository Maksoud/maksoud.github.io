[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Reranking

## O que é

**Reranking** é o processo de **reavaliar e reorganizar os resultados recuperados por uma etapa inicial de Retrieval**, colocando no topo aqueles que são mais relevantes para a consulta.

Uma busca inicial, como Similarity Search ou Hybrid Search, precisa ser eficiente porque pode lidar com grandes volumes de dados. Por isso, ela normalmente produz uma lista de candidatos.

O Reranking recebe esses candidatos e faz uma avaliação mais precisa:

```
Pergunta
   ↓
Retrieval
   ↓
Top-k candidatos
   ↓
Reranking
   ↓
Nova ordenação
   ↓
Melhores resultados
   ↓
LLM
```

A principal ideia é:

```
Retrieval:
"Quais resultados parecem relevantes?"

Reranking:
"Entre esses resultados, quais realmente respondem melhor à pergunta?"
```

## Como funciona

Imagine que uma busca inicial encontre 20 chunks relacionados a uma pergunta.

Eles podem ter sido encontrados porque possuem palavras semelhantes ou porque seus embeddings estão próximos da consulta.

Mas proximidade não significa necessariamente que o conteúdo seja o melhor para responder à pergunta.

O Reranking analisa esses candidatos novamente e atribui uma nova pontuação:

```
Retrieval inicial

Chunk A → 0,82
Chunk B → 0,79
Chunk C → 0,77
Chunk D → 0,75
Chunk E → 0,73
...
```

Depois do Reranking:

```
Chunk C → 0,94
Chunk A → 0,91
Chunk D → 0,87
Chunk B → 0,62
Chunk E → 0,41
```

A ordem mudou porque o segundo estágio avaliou a relação entre a consulta e o conteúdo de maneira mais detalhada.

Isso cria uma arquitetura em duas etapas:

```
                    Base de conhecimento
                            ↓
                    Busca inicial
                            ↓
                    Muitos candidatos
                            ↓
                       Reranking
                            ↓
                    Poucos candidatos
                            ↓
                           LLM
```

Essa abordagem é conhecida como **retrieve then rerank**.

A primeira etapa prioriza **velocidade e cobertura**.

A segunda prioriza **precisão na ordenação**.

Um modelo utilizado para Reranking pode receber a pergunta e cada candidato conjuntamente:

```
Consulta:
"Qual é o prazo para solicitar férias?"

Documento:
"As férias devem ser solicitadas com
30 dias de antecedência."

        ↓

Reranker

        ↓

Score de relevância
```

Assim, o Reranker consegue avaliar diretamente a relação entre a consulta e o conteúdo candidato.

Isso é diferente de simplesmente calcular a distância entre dois embeddings.

## Um exemplo

Imagine que o usuário pergunte:

```
"Qual é o prazo para solicitar férias?"
```

O Retrieval inicial retorna cinco chunks:

```
1. Política geral de férias
2. Prazo para solicitação de férias
3. Aprovação de férias pelo gestor
4. Férias coletivas
5. Cancelamento de férias
```

Todos parecem relacionados.

O resultado inicial pode ser:

```
1. Política geral de férias
2. Férias coletivas
3. Prazo para solicitação
4. Aprovação
5. Cancelamento
```

O problema é que o documento sobre **prazo para solicitação** deveria provavelmente estar no primeiro lugar.

O Reranking analisa novamente os candidatos:

```
Consulta:
"Qual é o prazo para solicitar férias?"

        ↓

Reranking

        ↓

1. Prazo para solicitação de férias
2. Política geral de férias
3. Aprovação de férias
4. Férias coletivas
5. Cancelamento de férias
```

Se o sistema precisar enviar apenas três chunks ao LLM, agora pode selecionar:

```
Top-3 após Reranking

1. Prazo para solicitação
2. Política geral
3. Aprovação de férias
```

O fluxo completo fica:

```
Pergunta
   ↓
Query Rewriting
   ↓
Metadata Filtering
   ↓
Similarity / Hybrid Search
   ↓
Top-k inicial
   ↓
Reranking
   ↓
Top-k final
   ↓
Contexto
   ↓
LLM
```

Perceba que o `k` inicial pode ser maior que o `k` final:

```
Retrieval:
k = 20

        ↓

20 candidatos

        ↓

Reranking

        ↓

Top-k final:
k = 5

        ↓

5 melhores chunks
```

Isso permite recuperar candidatos suficientes para reduzir o risco de perder uma informação relevante e, posteriormente, selecionar apenas os mais importantes.

## Por que é importante

Reranking é importante porque **a primeira etapa de Retrieval precisa ser rápida, enquanto a seleção final precisa ser precisa**.

Uma busca vetorial pode identificar conteúdos semanticamente próximos, mas não necessariamente consegue determinar com precisão qual deles responde melhor à pergunta.

O Reranking adiciona uma segunda avaliação mais específica.

Podemos comparar as duas etapas:

|Etapa|Principal objetivo|
|---|---|
|Retrieval inicial|Encontrar candidatos rapidamente|
|Reranking|Ordenar candidatos pela relevância mais precisa|
|Top-k final|Selecionar os resultados que seguirão adiante|

Isso cria um equilíbrio entre **recall e precisão**:

```
Retrieval inicial
      ↓
Maior cobertura
      ↓
Mais candidatos
      ↓
Reranking
      ↓
Maior precisão
      ↓
Poucos resultados
      ↓
LLM
```

Esse padrão é particularmente útil quando a base possui muitos documentos semanticamente semelhantes.

Também é importante diferenciar Reranking de Similarity Search:

```
Similarity Search:
compara a consulta com representações
armazenadas para encontrar candidatos.

Reranking:
reavalia os candidatos recuperados
para determinar sua relevância relativa.
```

O Reranking também não precisa necessariamente utilizar o mesmo mecanismo da busca inicial. Um sistema pode, por exemplo, utilizar embeddings para recuperar candidatos e depois utilizar um modelo especializado de Reranking para comparar diretamente a consulta com cada documento.

A ideia central é: **Reranking é uma segunda etapa de avaliação que reorganiza os candidatos recuperados, priorizando aqueles que apresentam maior relevância para a consulta antes que o contexto seja enviado ao LLM.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/reranking/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
