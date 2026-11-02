[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Retrieval

## O que é

**Retrieval** é o processo de **buscar e selecionar informações relevantes** em uma base de conhecimento para responder a uma determinada consulta.

Em um sistema RAG, o Retrieval acontece quando o usuário faz uma pergunta. O sistema utiliza mecanismos de busca para encontrar os documentos ou chunks que provavelmente contêm as informações necessárias e os disponibiliza para o LLM.

De forma simplificada:

```
Pergunta do usuário
        ↓
Transformação da consulta
        ↓
Busca na base de conhecimento
        ↓
Resultados relevantes
        ↓
Contexto para o LLM
        ↓
Resposta
```

É importante diferenciar Retrieval de Indexing:

```
Indexing
"Como preparar a base para que ela possa ser pesquisada?"

Retrieval
"Quais informações da base são relevantes para esta pergunta?"
```

O Indexing acontece principalmente antes da consulta, durante a preparação da base. O Retrieval acontece **durante a consulta**, quando o sistema precisa encontrar conhecimento relevante.

## Como funciona

Imagine uma biblioteca com 1 milhão de páginas.

Indexar a biblioteca significa organizar o acervo para que seja possível encontrar rapidamente determinado conteúdo.

Retrieval é o momento em que alguém pergunta:

```
"Qual é a política da empresa para férias?"
```

O sistema precisa descobrir quais partes daquele enorme acervo podem ajudar a responder à pergunta.

Em um RAG baseado em busca vetorial, o processo pode ser:

```
Pergunta
   ↓
Embedding da pergunta
   ↓
Busca por similaridade
   ↓
Candidatos relevantes
   ↓
Seleção dos melhores resultados
   ↓
Contexto
   ↓
LLM
```

A busca pode utilizar diferentes estratégias.

**Dense Retrieval** utiliza embeddings e busca por proximidade entre vetores.

**Sparse Retrieval** utiliza principalmente termos e estruturas tradicionais de busca, como BM25.

Também é possível combinar as duas abordagens:

```
                    ┌── Dense Retrieval
Pergunta ───────────┤
                    └── Sparse Retrieval
                           ↓
                    Combinação dos resultados
                           ↓
                    Contexto para o LLM
```

Outra característica importante é que Retrieval normalmente não significa simplesmente "encontrar um documento".

Um documento pode ser grande demais. Por isso, em sistemas RAG, frequentemente são recuperados **chunks específicos**.

Por exemplo:

```
Documento: politica_de_ferias.pdf

Chunk 01 → Introdução
Chunk 02 → Período de férias
Chunk 03 → Solicitação de férias
Chunk 04 → Aprovação
Chunk 05 → Exceções
```

Se a pergunta for:

```
"Com quanto tempo de antecedência devo solicitar férias?"
```

não é necessário enviar o documento inteiro ao LLM. O Retrieval pode encontrar principalmente o Chunk 03.

Isso reduz a quantidade de informação enviada ao modelo e aumenta a concentração de conteúdo relevante.

## Um exemplo

Imagine uma base contendo estes três chunks:

```
Chunk A:
"A empresa oferece plano de saúde aos funcionários
após o período de experiência."

Chunk B:
"As férias devem ser solicitadas com pelo menos
30 dias de antecedência."

Chunk C:
"O benefício de vale-alimentação é disponibilizado
no primeiro dia útil de cada mês."
```

O usuário pergunta:

```
"Quanto tempo antes preciso pedir minhas férias?"
```

O sistema transforma a pergunta em uma representação adequada para busca e procura informações relacionadas.

O Retrieval identifica o Chunk B como o resultado mais relevante:

```
Pergunta
   ↓
Busca
   ↓
┌─────────────────────────────────────┐
│ Chunk B                              │
│ "As férias devem ser solicitadas     │
│ com pelo menos 30 dias..."           │
└─────────────────────────────────────┘
   ↓
Contexto
   ↓
LLM
   ↓
"Você deve solicitar suas férias
com pelo menos 30 dias de antecedência."
```

Em uma implementação mais sofisticada, o sistema pode recuperar vários candidatos:

```
Resultado 1 → relevância alta
Resultado 2 → relevância média
Resultado 3 → relevância baixa
Resultado 4 → relevância baixa
```

Depois, outra etapa pode **reordenar os resultados**, mantendo apenas os mais úteis para o contexto final.

Isso introduz um conceito importante que aparecerá dentro de Retrieval: **Reranking**.

## Por que é importante

Retrieval é uma das etapas mais importantes de um sistema RAG porque determina **qual conhecimento será apresentado ao LLM**.

Um modelo pode receber um prompt excelente e ainda produzir uma resposta ruim se o sistema recuperar informações inadequadas.

Podemos pensar na qualidade de um RAG como uma cadeia:

```
Documentos
   ↓
Parsing
   ↓
Cleaning
   ↓
Chunking
   ↓
Embedding
   ↓
Indexing
   ↓
Retrieval
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

Se o Retrieval encontrar o conteúdo errado, o LLM terá pouca informação útil para trabalhar.

Isso também ajuda a separar dois problemas diferentes:

```
Retrieval:
"Encontrei a informação certa?"

Generation:
"Usei corretamente a informação encontrada?"
```

Essa distinção é fundamental. Um sistema pode falhar porque **não encontrou o documento correto** ou porque **encontrou o documento correto, mas o LLM o interpretou incorretamente**.

Dentro de Retrieval, portanto, começamos a estudar conceitos como:

```
Retrieval
├── Dense Retrieval
├── Sparse Retrieval
├── Hybrid Retrieval
├── Top-K Retrieval
├── Reranking
├── Query Expansion
├── Query Rewriting
└── Retrieval Evaluation
```

A ideia central é: **Retrieval é a etapa do RAG responsável por encontrar e selecionar, a partir da base de conhecimento, as informações mais relevantes para a consulta atual.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
