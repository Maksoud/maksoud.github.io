[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Sparse Retrieval

## O que é

**Sparse Retrieval**, ou recuperação esparsa, é uma técnica de recuperação de informações baseada principalmente na **presença e importância de termos específicos** em uma consulta e nos documentos.

Em vez de representar um texto como um vetor denso de embeddings, o conteúdo é representado de forma **esparsa**, geralmente com um grande número de posições possíveis e apenas uma pequena quantidade delas contendo valores relevantes.

Um exemplo simplificado:

```
Vocabulário:
["férias", "salário", "benefícios", "contrato", "gestor"]

Documento:
"férias gestor"

Representação:
[1, 0, 0, 0, 1]
```

A maioria das posições contém `0`, por isso a representação é chamada de **sparse**, ou esparsa.

Um dos métodos mais conhecidos para esse tipo de recuperação é o **BM25**, uma evolução de técnicas tradicionais baseadas em frequência de termos.

A ideia central é:

> Encontrar documentos que contenham termos relevantes para a consulta e atribuir maior importância aos termos mais significativos.

---

## Como funciona

Imagine uma biblioteca com milhares de documentos.

O usuário pesquisa:

```
"política de férias"
```

O sistema procura documentos que contenham termos relacionados à consulta, especialmente:

```
"política"
"férias"
```

Um documento que contenha essas palavras várias vezes e de forma relevante tende a receber uma pontuação maior.

Podemos representar o processo assim:

```
Consulta
   ↓
Identificação dos termos
   ↓
Busca por correspondência
   ↓
Cálculo da relevância dos termos
   ↓
Documentos ordenados por relevância
```

Uma das técnicas clássicas por trás desse processo é o **TF-IDF**, que considera fatores como a frequência de um termo dentro de um documento e o quanto esse termo é comum ou raro na coleção.

O BM25 aprimora essa ideia levando em consideração, entre outros fatores, a frequência dos termos e o tamanho dos documentos.

Imagine agora três documentos:

```
Documento A:
"Política de férias dos funcionários"

Documento B:
"Política de benefícios dos funcionários"

Documento C:
"Gestão financeira da empresa"
```

Para a consulta:

```
"política de férias"
```

um Sparse Retrieval provavelmente atribuirá maior relevância ao Documento A porque ele contém os termos mais diretamente relacionados à consulta.

A característica importante é que a correspondência depende bastante dos **termos utilizados**.

Se o usuário pesquisar:

```
"período de descanso"
```

e o documento utilizar somente:

```
"férias"
```

uma busca esparsa tradicional pode ter mais dificuldade para perceber que os dois conceitos estão relacionados.

É justamente nesse ponto que o Dense Retrieval pode complementar o Sparse Retrieval.

---

## Um exemplo

Imagine uma empresa com os seguintes documentos:

```
Documento A:
"Os funcionários devem solicitar férias pelo portal corporativo."

Documento B:
"O salário é depositado até o quinto dia útil."

Documento C:
"O colaborador precisa obter aprovação do gestor
para definir o período de férias."
```

O usuário pesquisa:

```
"solicitar férias"
```

O Sparse Retrieval identifica os termos:

```
"solicitar"
"férias"
```

Os documentos A e C possuem termos diretamente relacionados à consulta e podem receber pontuações elevadas.

Agora imagine que o usuário faça uma pergunta diferente:

```
"Como marcar meu período de descanso?"
```

O documento A fala sobre "solicitar férias", enquanto a consulta utiliza "marcar" e "período de descanso".

Um método puramente baseado em correspondência de termos pode não identificar tão bem essa relação semântica.

O Dense Retrieval, por outro lado, pode transformar a consulta e os documentos em embeddings e identificar proximidade semântica.

Podemos comparar as duas abordagens:

```
Consulta:
"Como marcar meu período de descanso?"

        ↓

Sparse Retrieval
→ procura termos correspondentes

Dense Retrieval
→ procura significado semelhante
```

Por isso, em sistemas modernos de RAG, é comum combinar as duas estratégias.

---

## Por que é importante

Sparse Retrieval continua sendo importante porque **termos exatos muitas vezes carregam informações extremamente relevantes**.

Imagine uma consulta como:

```
"erro HTTP 403"
```

ou:

```
"API-92871"
```

ou:

```
"contrato ABC-2026-041"
```

Nesses casos, encontrar exatamente os termos presentes na consulta pode ser mais importante do que encontrar apenas conteúdos semanticamente semelhantes.

Sparse Retrieval possui algumas vantagens:
- É eficiente para grandes coleções de documentos.
- É bom para termos específicos e identificadores.
- É interpretável, pois podemos entender quais palavras contribuíram para a relevância.
- Pode funcionar muito bem quando a consulta utiliza o mesmo vocabulário dos documentos.
- É especialmente útil quando correspondência literal é importante.

Por outro lado, ele pode ter dificuldade com **sinônimos, paráfrases e diferenças de vocabulário**.

É por isso que Sparse Retrieval e Dense Retrieval são frequentemente combinados.

Podemos visualizar a diferença:

```
                  Recuperação
                       │
             ┌─────────┴─────────┐
             ↓                   ↓
     Sparse Retrieval      Dense Retrieval
             │                   │
      Termos e palavras      Significado
             │                   │
        BM25, TF-IDF          Embeddings
             │                   │
             └─────────┬─────────┘
                       ↓
                 Hybrid Search
```

A diferença fundamental pode ser resumida assim:

**Sparse Retrieval** pergunta, essencialmente:

> "Quais documentos possuem termos relevantes para esta consulta?"

**Dense Retrieval** pergunta:

> "Quais documentos possuem significado semelhante ao desta consulta?"

Nenhuma das duas abordagens resolve todos os casos sozinha. Uma busca por termos exatos pode perder relações semânticas, enquanto uma busca semântica pode não dar o devido peso a identificadores ou palavras específicas.

Por isso, uma arquitetura RAG pode utilizar **Hybrid Search**, combinando os resultados das duas abordagens antes de selecionar o contexto que será enviado à LLM.

A relação com os conceitos anteriores fica assim:

```
Consulta
   │
   ├──→ Sparse Retrieval
   │       ↓
   │   Termos relevantes
   │
   └──→ Dense Retrieval
           ↓
       Embeddings
           ↓
     Similaridade semântica
           │
           └──────┐
                  ↓
             Hybrid Search
                  ↓
          Documentos relevantes
                  ↓
                 RAG
                  ↓
                 LLM
```

A ideia central é: **Sparse Retrieval recupera informações principalmente pela relevância dos termos presentes na consulta e nos documentos, sendo especialmente útil quando palavras, códigos ou expressões exatas são importantes.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-sparse-retrieval/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
