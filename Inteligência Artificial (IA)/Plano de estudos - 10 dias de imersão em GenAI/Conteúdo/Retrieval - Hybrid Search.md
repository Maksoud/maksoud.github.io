[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Hybrid Search

## O que é

**Hybrid Search** é uma estratégia de Retrieval que combina diferentes mecanismos de busca para encontrar informações relevantes.

No contexto de RAG, o uso mais comum é combinar:

```
Sparse Retrieval
       +
Dense Retrieval
       ↓
Hybrid Search
       ↓
Resultados combinados
```

A ideia é aproveitar as vantagens de cada abordagem.

O **Sparse Retrieval** é muito bom para encontrar termos específicos, nomes, códigos, identificadores e palavras importantes. O **Dense Retrieval** é melhor para encontrar conteúdos semanticamente relacionados, mesmo quando as palavras utilizadas são diferentes.

Por isso, em vez de escolher entre uma abordagem e outra, o Hybrid Search pode utilizar as duas.

## Como funciona

Imagine que uma empresa possui milhares de documentos e o usuário pergunta:

```
"Qual é o procedimento para solicitar férias no sistema RH-2026?"
```

Existem dois aspectos importantes nessa pergunta.

Primeiro, o significado geral:

```
"procedimento para solicitar férias"
```

O Dense Retrieval consegue identificar documentos relacionados a esse conceito mesmo que utilizem palavras diferentes, como:

```
"marcação de férias"
"pedido de férias"
"solicitação do período de descanso"
```

Segundo, existe um identificador específico:

```
"RH-2026"
```

Nesse caso, o Sparse Retrieval pode ser mais eficiente porque procura diretamente pelos termos presentes no conteúdo.

O Hybrid Search combina os resultados:

```
                 Pergunta
                    ↓
          ┌─────────┴─────────┐
          ↓                   ↓
  Dense Retrieval      Sparse Retrieval
          ↓                   ↓
 Resultados semânticos  Resultados por termos
          └─────────┬─────────┘
                    ↓
          Combinação dos resultados
                    ↓
             Ranking final
                    ↓
             Contexto para LLM
```

A combinação pode ser feita de diferentes maneiras.

Uma possibilidade é calcular uma pontuação para cada resultado e combinar as pontuações:

```
Score final =
    α × Score Dense
    +
    β × Score Sparse
```

Os pesos `α` e `β` determinam quanto cada mecanismo influencia o resultado.

Por exemplo:

```
α = 0,7
β = 0,3
```

Nesse cenário, a busca semântica teria maior influência.

Outra possibilidade é utilizar técnicas de combinação de rankings, como **Reciprocal Rank Fusion (RRF)**, que combina a posição dos resultados em diferentes rankings em vez de depender diretamente das pontuações produzidas por cada mecanismo.

O ponto importante é que **não existe uma única forma obrigatória de implementar Hybrid Search**.

## Um exemplo

Considere estes documentos:

```
Documento A:
"Procedimento para marcação do período anual de descanso..."

Documento B:
"Manual do sistema RH-2026: solicitação de férias..."

Documento C:
"Política de benefícios e plano de saúde..."

Documento D:
"Como registrar o pedido de férias no portal corporativo..."
```

O usuário pergunta:

```
"Como solicitar férias no RH-2026?"
```

O Dense Retrieval pode produzir:

```
1. Documento D
2. Documento A
3. Documento B
```

Porque identifica a relação semântica entre "solicitar férias" e conteúdos sobre "pedido", "marcação" ou "registro".

Enquanto isso, o Sparse Retrieval pode produzir:

```
1. Documento B
2. Documento D
3. Documento C
```

Porque encontra diretamente termos como `RH-2026`, `férias` e `solicitação`.

O Hybrid Search combina essas informações:

```
Dense Results
      +
Sparse Results
      ↓
Combinação / Fusion
      ↓
Ranking final
      ↓
Top-K documentos
      ↓
LLM
```

O Documento B pode subir no ranking porque apresenta simultaneamente **alta relevância semântica** e **correspondência direta com o identificador pesquisado**.

## Por que é importante

Hybrid Search é importante porque **Dense Retrieval e Sparse Retrieval possuem pontos fortes diferentes**.

|Abordagem|Ponto forte|
|---|---|
|Sparse Retrieval|Termos exatos, nomes, códigos e identificadores|
|Dense Retrieval|Significado, contexto e paráfrases|
|Hybrid Search|Combinação das duas capacidades|

Isso é especialmente útil em bases de conhecimento reais, nas quais uma pergunta pode conter simultaneamente conceitos abstratos e termos muito específicos.

Por exemplo:

```
"Qual é a política de reembolso para o produto ERP-X500?"
```

O Dense Retrieval ajuda a encontrar documentos relacionados a **reembolso**, mesmo que utilizem expressões diferentes.

O Sparse Retrieval ajuda a localizar especificamente **ERP-X500**.

Essa combinação pode melhorar a capacidade do sistema de recuperar os documentos certos antes que eles sejam enviados ao LLM.

É importante perceber também onde o Hybrid Search se encaixa na arquitetura que estamos construindo:

```
Documentos
   ↓
Ingestion
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
   ├── Dense Retrieval
   ├── Sparse Retrieval
   └── Hybrid Search
          ↓
       Ranking
          ↓
      Contexto
          ↓
         LLM
```

Assim, **Hybrid Search não substitui o Retrieval**. Ele é uma estratégia utilizada **dentro do Retrieval** para combinar diferentes sinais de relevância.

A ideia central é: **Hybrid Search combina busca por significado com busca por termos para aumentar a probabilidade de recuperar as informações realmente relevantes para a consulta.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-hybrid-search/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
