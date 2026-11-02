# Top-k

## O que é

**Top-k** é uma estratégia de Retrieval que determina que o sistema deve selecionar os **k resultados mais relevantes** encontrados durante uma busca.

O `k` representa a quantidade de resultados que serão retornados.

Por exemplo:

```
Similarity Search
      ↓
100 resultados possíveis
      ↓
Ranking por relevância
      ↓
Top-k
      ↓
5 melhores resultados
```

Se `k = 5`, o sistema recupera os cinco resultados mais relevantes.

Se `k = 10`, recupera os dez primeiros.

Portanto, Top-k não é uma métrica de similaridade nem um algoritmo específico de busca. É uma **regra de seleção dos resultados**.

## Como funciona

Imagine que uma busca encontre 1.000 chunks candidatos.

Cada um recebe uma pontuação de relevância:

```
Chunk A → 0,92
Chunk B → 0,87
Chunk C → 0,84
Chunk D → 0,79
Chunk E → 0,74
...
Chunk Z → 0,21
```

Se configurarmos:

```
k = 3
```

o sistema selecionará:

```
1. Chunk A → 0,92
2. Chunk B → 0,87
3. Chunk C → 0,84
```

Os demais resultados não entram no contexto enviado ao LLM.

Podemos visualizar:

```
Consulta
   ↓
Busca
   ↓
Candidatos
   ↓
Ranking
   ↓
┌──────────────────────┐
│ Top-1                │
│ Top-2                │
│ Top-3                │ ← k = 3
└──────────────────────┘
   ↓
Contexto
   ↓
LLM
```

A escolha de `k` cria um equilíbrio.

Se `k` for **muito pequeno**, informações relevantes podem ficar de fora.

Se `k` for **muito grande**, o sistema pode recuperar informações desnecessárias, aumentando o tamanho do contexto e potencialmente dificultando a tarefa do LLM.

Por isso, `k` é um parâmetro importante para ajustar o comportamento do Retrieval.

## Um exemplo

Imagine uma base de conhecimento com documentos sobre férias.

O usuário pergunta:

```
"Quais são as regras para solicitar férias?"
```

O Similarity Search encontra:

```
Resultado 1 → Solicitação de férias
Resultado 2 → Prazo para aprovação
Resultado 3 → Fracionamento das férias
Resultado 4 → Cancelamento
Resultado 5 → Férias coletivas
Resultado 6 → Benefícios
Resultado 7 → Licença médica
Resultado 8 → Banco de horas
```

Se configurarmos:

```
k = 3
```

apenas os três primeiros resultados serão inicialmente recuperados:

```
1. Solicitação de férias
2. Prazo para aprovação
3. Fracionamento das férias
```

Esses resultados podem então passar por outras etapas antes de chegar ao LLM.

Por exemplo:

```
Pergunta
   ↓
Query Rewriting
   ↓
Similarity Search
   ↓
Top-k = 10
   ↓
10 candidatos
   ↓
Reranking
   ↓
Top-k final = 3
   ↓
Contexto
   ↓
LLM
```

Isso mostra que podemos ter **mais de um Top-k em diferentes etapas**.

Um sistema pode inicialmente recuperar muitos candidatos para não perder informações relevantes e depois reduzir a quantidade através de Reranking.

Por exemplo:

```
Retrieval inicial
k = 20
       ↓
20 candidatos
       ↓
Reranking
       ↓
Top-k final
k = 5
       ↓
5 chunks
       ↓
LLM
```

Essa abordagem cria uma distinção importante entre **recuperação de candidatos** e **seleção do contexto final**.

## Por que é importante

Top-k é importante porque controla **quanto conhecimento recuperado será levado para as próximas etapas do RAG**.

Ele influencia diretamente o equilíbrio entre **recall**, custo e quantidade de contexto.

Um `k` baixo tende a reduzir a quantidade de informação recuperada, mas pode aumentar o risco de excluir um resultado importante.

Um `k` alto aumenta a cobertura potencial, mas pode trazer mais conteúdo irrelevante.

Podemos pensar assim:

```
k pequeno
   ↓
Menos resultados
   ↓
Menos contexto
   ↓
Menor custo
   ↓
Maior risco de perder informação


k grande
   ↓
Mais resultados
   ↓
Mais contexto
   ↓
Maior custo
   ↓
Menor risco de perder informação
```

O valor ideal depende da aplicação.

Uma pergunta simples sobre um fato específico pode funcionar bem com poucos resultados. Uma pergunta complexa que exige informações distribuídas em diferentes documentos pode precisar de um `k` maior.

Também é importante entender que **Top-k não garante que todos os resultados selecionados sejam realmente úteis**. Ele apenas determina quantos resultados serão selecionados de acordo com o ranking produzido pelo mecanismo de busca.

Por isso, Top-k frequentemente trabalha em conjunto com outros mecanismos:

```
Query
   ↓
Query Rewriting
   ↓
Metadata Filtering
   ↓
Similarity Search
   ↓
Top-k
   ↓
Reranking
   ↓
Contexto final
   ↓
LLM
```

A ideia central é: **Top-k define quantos dos resultados mais relevantes serão selecionados durante o Retrieval. O valor de** `**k**` **controla o equilíbrio entre cobertura da informação, quantidade de contexto e custo computacional.**