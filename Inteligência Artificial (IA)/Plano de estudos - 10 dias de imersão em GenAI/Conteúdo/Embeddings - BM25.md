[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# BM25

## O que é

**BM25**, abreviação de **Best Matching 25**, é um algoritmo utilizado para **calcular a relevância de documentos em relação a uma consulta**, sendo uma das técnicas mais conhecidas de **Sparse Retrieval**.

Ele analisa principalmente os termos presentes na consulta e nos documentos e atribui uma pontuação de relevância para cada documento.

De forma simplificada, o BM25 considera fatores como:
- Quantas vezes um termo da consulta aparece no documento.
- Quão raro ou comum esse termo é em toda a coleção.
- O tamanho do documento.

O objetivo é responder:

> "Quais documentos são mais relevantes para os termos que o usuário pesquisou?"

Diferentemente do Dense Retrieval, o BM25 **não depende de embeddings para encontrar similaridade semântica**.

---

## Como funciona

Imagine uma coleção com milhares de documentos e a seguinte consulta:

```
"política de férias"
```

O BM25 procura documentos que contenham termos importantes da consulta, como:

```
política
férias
```

Mas simplesmente contar quantas vezes uma palavra aparece não é suficiente.

Imagine dois documentos:

```
Documento A:
"Política de férias dos funcionários.
A política de férias determina..."
```

e:

```
Documento B:
"Política de benefícios, política salarial,
política de segurança e política de férias..."
```

A palavra "política" aparece várias vezes no Documento B, mas isso não significa necessariamente que ele seja mais relevante para a consulta.

O BM25 procura equilibrar esses fatores.

Uma forma simplificada de visualizar seu funcionamento é:

```
Consulta
   ↓
Identificação dos termos
   ↓
Verificação dos termos nos documentos
   ↓
Frequência dos termos
   ↓
Importância dos termos na coleção
   ↓
Ajuste pelo tamanho dos documentos
   ↓
Pontuação BM25
   ↓
Ranking dos documentos
```

Um dos conceitos importantes é o **IDF, Inverse Document Frequency**. Termos que aparecem em praticamente todos os documentos possuem menor capacidade de diferenciar um documento dos demais.

Por exemplo, em uma coleção de documentos sobre uma empresa, palavras como "empresa" ou "funcionário" podem aparecer frequentemente.

Já um termo mais específico, como "reembolso", pode ser muito mais útil para identificar os documentos relevantes para determinada consulta.

O BM25 também considera a **frequência do termo no próprio documento**, mas aplica uma espécie de saturação. Isso significa que repetir uma palavra muitas vezes não faz a relevância crescer indefinidamente.

Além disso, ele considera o **tamanho do documento**, evitando favorecer automaticamente documentos muito longos apenas porque eles possuem mais oportunidades de conter os termos pesquisados.

A fórmula completa pode ser representada como:

$$  
\text{score}(D,Q)=\sum_{t\in Q} IDF(t)\cdot  
\frac{f(t,D)\cdot(k_1+1)}  
{f(t,D)+k_1\cdot\left(1-b+b\cdot\frac{|D|}{avgdl}\right)}  
$$

Onde:
- $D$ é o documento.
- $Q$ é a consulta.
- $t$ é um termo da consulta.
- $f(t,D)$ é a frequência do termo no documento.
- $|D|$ é o tamanho do documento.
- $avgdl$ é o tamanho médio dos documentos.
- $k_1$ controla a influência da frequência do termo.
- $b$ controla o efeito do tamanho do documento.
- $IDF(t)$ representa a importância do termo considerando toda a coleção.

Não é necessário memorizar a fórmula neste momento. O mais importante é entender que o BM25 combina **frequência, importância dos termos e tamanho do documento** para produzir uma pontuação de relevância.

---

## Um exemplo

Imagine uma base de documentos de uma empresa:

```
Documento A:
"Os funcionários podem solicitar férias
pelo portal corporativo."

Documento B:
"O pagamento do salário é realizado
até o quinto dia útil."

Documento C:
"A política de férias determina que o
funcionário deve solicitar o período
com antecedência."
```

O usuário pesquisa:

```
"solicitar férias"
```

O BM25 analisa a presença desses termos nos documentos.

Um resultado simplificado poderia ser:

```
Documento A → BM25 = 4.8
Documento C → BM25 = 3.9
Documento B → BM25 = 0.2
```

O sistema então ordena os documentos:

```
1. Documento A
2. Documento C
3. Documento B
```

Os primeiros resultados podem então ser utilizados pelo sistema RAG:

```
Consulta
   ↓
BM25
   ↓
Documentos mais relevantes
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

Agora imagine uma consulta diferente:

```
"Como marcar meu período de descanso?"
```

O documento utiliza a expressão "solicitar férias", não "marcar período de descanso".

Nesse caso, o BM25 pode ter dificuldade porque a correspondência entre os termos é menor.

Um Dense Retrieval pode identificar que "marcar meu período de descanso" e "solicitar férias" possuem significado semelhante, mesmo sem uma correspondência literal forte.

É justamente por isso que podemos combinar as duas abordagens.

---

## Por que é importante

BM25 é importante porque continua sendo uma das principais técnicas de **recuperação lexical** e é especialmente eficiente quando os termos exatos da consulta são relevantes.

Ele é particularmente útil para encontrar:
- Códigos
- Nomes próprios
- Identificadores
- Termos técnicos
- Números de documentos
- Expressões específicas
- Palavras exatamente utilizadas pelo usuário

Considere uma consulta como:

```
"erro HTTP 403"
```

Nesse caso, encontrar exatamente `HTTP`, `403` e `erro` pode ser muito importante. Uma busca puramente semântica poderia recuperar documentos sobre problemas de autenticação ou permissões, mas talvez não priorize o documento que contém exatamente o código `403`.

Por isso, BM25 e Dense Retrieval possuem características complementares:

|Abordagem|Principal característica|
|---|---|
|**BM25**|Correspondência de termos|
|**Dense Retrieval**|Similaridade semântica|
|**Hybrid Search**|Combinação das duas|

Podemos visualizar:

```
                 Consulta
                    ↓
          ┌─────────┴─────────┐
          ↓                   ↓
       BM25              Dense Retrieval
          ↓                   ↓
   Termos relevantes    Significado semelhante
          ↓                   ↓
          └─────────┬─────────┘
                    ↓
              Hybrid Search
                    ↓
          Documentos relevantes
                    ↓
                   RAG
                    ↓
                   LLM
```

Essa combinação é especialmente interessante em RAG porque permite aproveitar duas formas diferentes de relevância.

O BM25 pode encontrar um documento porque ele contém **exatamente o termo importante**.

O Dense Retrieval pode encontrar outro porque ele possui **significado semelhante**, mesmo usando palavras diferentes.

A ideia central é: **BM25 é um algoritmo de Sparse Retrieval que calcula a relevância de documentos com base principalmente na correspondência e importância dos termos da consulta, considerando também a frequência dos termos e o tamanho dos documentos.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-bm25/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
