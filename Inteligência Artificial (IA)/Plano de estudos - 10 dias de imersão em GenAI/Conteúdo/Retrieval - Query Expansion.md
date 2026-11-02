[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Query Expansion

## O que é

Query Expansion, ou expansão de consulta, é uma técnica de Retrieval que amplia uma consulta original com termos, expressões ou variações relacionadas para aumentar as chances de encontrar informações relevantes.

A ideia central é simples: uma consulta pode ser curta demais ou utilizar palavras diferentes das utilizadas nos documentos. A expansão tenta criar uma representação mais abrangente da intenção da consulta antes de executar o Retrieval.

Por exemplo, uma consulta como:

```
"cancelamento de contrato"
```

pode ser expandida para incluir termos relacionados:

```
"cancelamento de contrato rescisão encerramento término contrato"
```

Isso pode aumentar a cobertura da busca, principalmente em Keyword Search.

Query Expansion não é a mesma coisa que Query Rewriting. No Query Rewriting, a consulta pode ser reformulada para produzir uma nova consulta mais adequada. Na Query Expansion, o foco está especificamente em **adicionar termos ou variações à consulta original**.

## Como funciona

O processo pode ser representado assim:

```
Consulta original
        ↓
Identificação de termos importantes
        ↓
Geração de termos relacionados
        ↓
Consulta expandida
        ↓
Retrieval
        ↓
Top-k resultados
```

Existem diferentes maneiras de realizar essa expansão.

Uma abordagem simples utiliza recursos linguísticos ou um dicionário de sinônimos:

```
Consulta:
"cancelamento de contrato"

Expansão:
cancelamento
rescisão
encerramento
término
contrato
```

Outra abordagem utiliza uma LLM para gerar termos relacionados à intenção da consulta:

```
Pergunta do usuário
        ↓
LLM
        ↓
Termos e conceitos relacionados
        ↓
Consulta expandida
        ↓
Retrieval
```

Também é possível utilizar informações obtidas do próprio índice ou da coleção de documentos. Por exemplo, depois de identificar termos frequentemente associados a uma determinada palavra, o sistema pode utilizá-los para ampliar consultas futuras.

Em uma Keyword Search, isso pode aumentar o número de documentos candidatos encontrados.

Porém, existe um equilíbrio importante. Adicionar muitos termos pode tornar a consulta ampla demais e trazer documentos irrelevantes. Por isso, uma boa expansão deve aumentar a **recall** sem prejudicar excessivamente a **precision**.

De forma simplificada:

```
Consulta muito específica
        ↓
Poucos resultados
        ↓
Possível perda de documentos relevantes

Query Expansion
        ↓
Consulta mais abrangente
        ↓
Mais candidatos relevantes
        ↓
Reranking
        ↓
Resultados mais precisos
```

## Um exemplo

Imagine um sistema RAG corporativo que contém documentos sobre contratos e o usuário pergunta:

```
"Quais são as regras para cancelar um contrato?"
```

Os documentos podem utilizar expressões diferentes, como:

```
rescisão contratual
encerramento do contrato
término antecipado
cancelamento
distrato
```

Uma consulta baseada apenas nas palavras originais poderia não encontrar todos esses documentos.

Com Query Expansion, o sistema pode produzir:

```
Consulta original:
"regras para cancelar um contrato"

Termos relacionados:
cancelamento
rescisão
encerramento
término
distrato
contrato
```

O Retrieval utiliza essa informação para buscar candidatos:

```
Pergunta
   ↓
Query Expansion
   ↓
"cancelamento"
"rescisão"
"encerramento"
"distrato"
   ↓
Keyword Search
   ↓
Documentos candidatos
   ↓
Top-k
   ↓
Reranking
   ↓
Contexto
   ↓
LLM
```

Nesse cenário, a expansão aumenta a possibilidade de recuperar um documento que seja relevante para a pergunta, mesmo que ele não utilize exatamente as mesmas palavras usadas pelo usuário.

## Por que é importante

Query Expansion é importante porque existe uma diferença frequente entre a linguagem utilizada pelo usuário e a linguagem utilizada nos documentos.

Em sistemas corporativos, isso pode acontecer por causa de:
- sinônimos;
- abreviações;
- terminologia técnica;
- nomes alternativos;
- diferenças entre linguagem informal e linguagem formal;
- diferentes formas de descrever o mesmo conceito.

A técnica é especialmente útil quando o Retrieval depende de correspondência lexical, como Keyword Search. Ela pode aumentar o **recall**, permitindo que mais documentos potencialmente relevantes sejam recuperados.

Dentro do fluxo que estamos estudando, podemos posicioná-la antes do Retrieval:

```
Pergunta
   ↓
Query Expansion
   ↓
Keyword Search / Semantic Search
   ↓
Top-k
   ↓
Reranking
   ↓
Contexto
   ↓
LLM
```

Ela também pode trabalhar junto com Query Rewriting. O Query Rewriting pode modificar a estrutura ou a formulação da consulta, enquanto a Query Expansion adiciona termos e variações relacionados.

O principal cuidado é evitar expansão excessiva. Se forem adicionados muitos termos pouco relacionados, o sistema pode recuperar uma quantidade maior de documentos, mas com menor relevância. Por isso, Query Expansion é uma técnica para melhorar a cobertura do Retrieval, não uma garantia de que os resultados serão melhores.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-query-expansion/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
