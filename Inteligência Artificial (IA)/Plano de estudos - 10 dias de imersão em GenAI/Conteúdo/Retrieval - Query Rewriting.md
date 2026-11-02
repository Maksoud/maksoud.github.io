# Query Rewriting

## O que é

**Query Rewriting** é a técnica de **reescrever ou transformar a consulta do usuário antes de realizar o Retrieval**, buscando produzir uma consulta mais adequada para encontrar informações relevantes.

A pergunta original nem sempre é a melhor representação para uma busca. Ela pode ser curta, ambígua, conter referências ao contexto anterior ou utilizar uma linguagem diferente daquela presente nos documentos.

Por exemplo:

```
Pergunta original:
"E nesse caso, como funciona?"

        ↓

Query Rewriting

        ↓

Consulta reformulada:
"Como funciona o processo de solicitação
de férias para funcionários em 2026?"
```

O objetivo não é responder à pergunta nessa etapa. É **transformar a consulta em algo que facilite a recuperação das informações corretas**.

## Como funciona

Imagine uma conversa:

```
Usuário:
"Qual é a política de férias da empresa?"

Assistente:
"Os funcionários devem solicitar férias
com pelo menos 30 dias de antecedência."

Usuário:
"E para estagiários?"
```

A última pergunta, isoladamente, é bastante vaga.

Se for enviada diretamente ao mecanismo de Retrieval:

```
"E para estagiários?"
```

pode ser difícil encontrar os documentos corretos.

O Query Rewriting pode utilizar o contexto da conversa para produzir:

```
"Qual é a política de férias para estagiários?"
```

A busca passa a ter uma consulta muito mais informativa:

```
Pergunta original
      ↓
Contexto da conversa
      ↓
Query Rewriting
      ↓
Consulta reformulada
      ↓
Retrieval
      ↓
Documentos relevantes
```

O modelo também pode corrigir ou explicitar aspectos da consulta.

Por exemplo:

```
Original:
"Como faço pra pedir?"

Reescrita:
"Como solicitar férias pelo sistema
de recursos humanos?"
```

Ou:

```
Original:
"Quanto tempo?"

Reescrita:
"Qual é o prazo mínimo de antecedência
para solicitar férias?"
```

A consulta reformulada não precisa necessariamente ser uma frase mais longa. O objetivo é **melhorar sua capacidade de recuperar a informação correta**.

Uma aplicação também pode gerar mais de uma consulta.

Por exemplo:

```
Pergunta:
"Quais são as regras para trabalhar de casa?"

        ↓

Query Rewriting

        ├── "Política de trabalho remoto"
        ├── "Regras de home office"
        └── "Requisitos para trabalho remoto"
                ↓
             Retrieval
```

Os resultados das diferentes consultas podem posteriormente ser combinados.

Isso é especialmente útil quando diferentes formas de expressar a mesma intenção podem aparecer nos documentos.

## Um exemplo

Imagine uma base contendo documentos sobre benefícios corporativos.

O usuário pergunta:

```
"Posso usar o plano fora da cidade?"
```

A pergunta pode ser ambígua porque "plano" pode significar diferentes coisas.

O histórico da conversa indica que o assunto é o plano de saúde.

O Query Rewriting pode transformar a consulta em:

```
"Funcionários podem utilizar o plano de saúde
fora da cidade de residência?"
```

O Retrieval então utiliza essa consulta para procurar os chunks relevantes:

```
Pergunta original
        ↓
Contexto da conversa
        ↓
Query Rewriting
        ↓
"Funcionários podem utilizar o plano de saúde
fora da cidade de residência?"
        ↓
Dense / Sparse / Hybrid Retrieval
        ↓
Chunks relevantes
        ↓
LLM
```

Outro caso comum acontece quando a pergunta contém uma referência temporal ou contextual:

```
Usuário:
"Qual era o limite em 2025?"
```

O Query Rewriting pode transformar isso em:

```
"Qual era o limite do benefício de alimentação
para funcionários em 2025?"
```

A busca passa a ter os elementos necessários para encontrar o conteúdo correto.

É importante perceber que **Query Rewriting não é a mesma coisa que responder à pergunta**. O resultado da reescrita é uma nova consulta, que será utilizada pelo mecanismo de Retrieval.

## Por que é importante

Query Rewriting é importante porque a qualidade do Retrieval depende também da **qualidade da consulta utilizada para pesquisar**.

Uma consulta mal formulada pode produzir resultados ruins mesmo quando a base de conhecimento contém exatamente a informação necessária.

Podemos representar isso como:

```
Pergunta do usuário
        ↓
Query Rewriting
        ↓
Consulta otimizada
        ↓
Retrieval
        ↓
Resultados
        ↓
Reranking
        ↓
Contexto
        ↓
LLM
```

A técnica é especialmente útil para:
- perguntas muito curtas;
- perguntas dependentes do histórico da conversa;
- referências como "isso", "aquilo", "nesse caso";
- consultas ambíguas;
- diferentes formas de expressar a mesma intenção;
- correção ou expansão de termos;
- consultas complexas que podem ser divididas em várias buscas.

Também é importante observar que **reescrever uma consulta pode introduzir erros**. Se o sistema interpretar incorretamente a intenção do usuário, poderá produzir uma consulta aparentemente melhor, mas que procura a informação errada.

Por isso, Query Rewriting deve preservar a intenção original.

Uma forma de visualizar essa preocupação é:

```
Pergunta original
       ↓
Preservar intenção
       ↓
Consulta reformulada
       ↓
Retrieval
```

Isso diferencia Query Rewriting de simplesmente "deixar a pergunta mais bonita". A finalidade é **melhorar a recuperação**, não melhorar a redação.

Também podemos relacioná-lo aos conceitos anteriores:

|Conceito|Função|
|---|---|
|Metadata Filtering|Restringe quais dados podem participar da busca|
|Query Rewriting|Melhora a consulta utilizada na busca|
|Dense Retrieval|Busca por proximidade semântica|
|Sparse Retrieval|Busca por termos e correspondências lexicais|
|Hybrid Search|Combina diferentes mecanismos de busca|
|Reranking|Reordena os resultados recuperados|

A ideia central é: **Query Rewriting transforma a pergunta original em uma consulta mais adequada ao mecanismo de Retrieval, preservando sua intenção e aumentando a possibilidade de encontrar as informações relevantes.**