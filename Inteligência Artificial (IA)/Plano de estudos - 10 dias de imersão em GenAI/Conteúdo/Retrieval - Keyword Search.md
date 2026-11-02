[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Keyword Search

## O que é

Keyword Search, ou busca por palavras-chave, é uma técnica de Retrieval que procura documentos ou trechos de documentos com base na ocorrência de termos presentes na consulta.

Diferentemente da busca semântica, que tenta identificar o significado ou a intenção por trás da consulta usando embeddings, a Keyword Search trabalha principalmente com os termos que aparecem explicitamente no texto.

Uma forma clássica de implementar esse tipo de busca é o **BM25**, um algoritmo que atribui uma pontuação aos documentos considerando fatores como a frequência dos termos pesquisados e a relevância desses termos dentro da coleção.

Por exemplo, se um usuário pesquisar:

```
"política de reembolso para clientes corporativos"
```

uma Keyword Search procura documentos que contenham termos como `política`, `reembolso`, `clientes` e `corporativos`.

Isso significa que Keyword Search é diferente de Similarity Search baseada em embeddings. Na busca por palavras-chave, a correspondência textual tem papel central. Na busca semântica, o sistema pode encontrar um trecho relevante mesmo quando ele utiliza palavras diferentes das presentes na consulta.

## Como funciona

O processo pode ser representado de forma simplificada:

```
Consulta do usuário
        ↓
Extração e análise dos termos
        ↓
Busca por correspondência textual
        ↓
Cálculo de relevância
        ↓
Documentos classificados
        ↓
Top-k resultados
```

Antes da consulta, normalmente existe uma etapa de indexação textual. O sistema cria uma estrutura que permite localizar rapidamente quais documentos contêm determinados termos.

Um mecanismo tradicional é o **índice invertido**. Em vez de armazenar apenas quais palavras aparecem em cada documento, ele mantém uma relação entre cada termo e os documentos nos quais esse termo aparece.

Por exemplo:

```
Termo          Documentos
────────────────────────────
reembolso      D1, D4, D7
cliente        D1, D2, D4
corporativo    D1, D7
contrato       D3, D5, D7
```

Quando chega uma consulta, o mecanismo consulta esse índice e identifica os documentos que possuem os termos pesquisados.

Depois, um algoritmo de ranking, como BM25, pode calcular a relevância de cada documento:

```
Consulta
   ↓
"política de reembolso"
   ↓
Índice invertido
   ↓
Documentos que contêm os termos
   ↓
Ranking por relevância textual
   ↓
Top-k
```

A frequência de um termo também importa. Um termo muito comum em praticamente todos os documentos tende a ser menos discriminativo do que um termo raro e específico.

Por outro lado, Keyword Search possui uma limitação importante: ela pode não encontrar um documento relevante quando a consulta e o documento utilizam palavras diferentes.

Por exemplo:

```
Consulta:
"como cancelar minha assinatura?"

Documento:
"procedimento para encerramento do contrato"
```

Existe uma relação semântica entre os dois textos, mas as palavras utilizadas são diferentes. Uma busca puramente baseada em palavras-chave pode ter dificuldade para identificar essa relação.

## Um exemplo

Imagine uma empresa que possui milhares de documentos internos e um funcionário pergunta:

```
"Qual é o prazo para reembolso de despesas de viagem?"
```

Um sistema de Keyword Search pode procurar termos como:

```
reembolso
despesas
viagem
prazo
```

Suponha que encontre:

```
D1: Política de reembolso de viagens
D2: Política de despesas corporativas
D3: Benefícios para funcionários
D4: Procedimento para viagens internacionais
D5: Política de compras
```

O mecanismo calcula a relevância textual dos documentos e pode retornar:

```
Consulta
   ↓
Keyword Search
   ↓
D1
D2
D4
   ↓
Top-k
```

O RAG pode então utilizar esses documentos como contexto para a LLM:

```
Pergunta
   ↓
Keyword Search
   ↓
Documentos relevantes
   ↓
Top-k
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

Esse mecanismo funciona especialmente bem quando o usuário utiliza termos específicos presentes nos documentos, como nomes de produtos, códigos, números de contratos, identificadores, nomes de políticas ou termos técnicos.

## Por que é importante

Keyword Search é importante porque oferece uma forma precisa e eficiente de encontrar informações quando a correspondência textual é relevante.

Em sistemas RAG, ela também complementa a busca semântica. Uma consulta pode conter termos que precisam ser encontrados exatamente, como:

```
"contrato ABC-2026-047"
```

Nesse caso, uma busca baseada em palavras-chave pode ser mais adequada do que depender exclusivamente de embeddings.

Por isso, sistemas modernos de Retrieval frequentemente combinam diferentes estratégias:

```
                 Consulta
                    ↓
          ┌─────────┴─────────┐
          ↓                   ↓
   Keyword Search       Semantic Search
       BM25               Embeddings
          ↓                   ↓
          └─────────┬─────────┘
                    ↓
             Hybrid Search
                    ↓
                  Top-k
                    ↓
                Reranking
                    ↓
                 Contexto
                    ↓
                   LLM
```

Essa combinação é conhecida como **Hybrid Search**. A Keyword Search contribui com correspondência textual e lexical, enquanto a busca semântica contribui com correspondência baseada em significado.

Assim, Keyword Search não é uma alternativa necessariamente oposta à busca semântica. Em um sistema RAG robusto, as duas podem trabalhar juntas para aumentar a cobertura e a precisão do Retrieval.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-keyword-search/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
