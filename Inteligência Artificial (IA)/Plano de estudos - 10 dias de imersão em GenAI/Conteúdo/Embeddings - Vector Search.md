[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Vector Search

## O que é

**Vector Search**, ou busca vetorial, é uma técnica utilizada para encontrar informações **semanticamente semelhantes** a uma consulta.

Em vez de procurar apenas pelas mesmas palavras presentes na consulta, a busca vetorial transforma a consulta em um **embedding** e procura, em um conjunto de vetores, aqueles que estão mais próximos dela.

Por isso, uma busca como:

```
"Como solicitar férias?"
```

pode encontrar um conteúdo como:

```
"Os colaboradores devem registrar o período de descanso no sistema interno."
```

Mesmo que as palavras sejam diferentes, os dois conteúdos podem possuir significados semelhantes.

A Vector Search é, portanto, o mecanismo de busca que conecta os conceitos que estudamos anteriormente:

```
Embedding
   ↓
Vector Embedding
   ↓
Vector Search
   ↓
Vetores semelhantes
```

Quando essa busca é realizada sobre um **Vector Database**, ela se torna uma parte fundamental de arquiteturas como RAG.

---

## Como funciona

Imagine um mapa onde cada documento é representado por um ponto.

Documentos semanticamente relacionados ficam próximos uns dos outros:

```
                  Documentos sobre férias
                         ●
                      ●     ●
                   ●
                                      ●
                              Documentos sobre salários

      ●
  Documentos sobre segurança
```

Quando o usuário faz uma pergunta, ela também é transformada em um ponto nesse espaço.

Por exemplo:

```
Pergunta
"Como solicitar férias?"
        ↓
   Embedding
        ↓
       ●
```

A Vector Search procura os documentos que estão mais próximos desse ponto.

O processo pode ser representado assim:

```
Pergunta do usuário
        ↓
Embedding Model
        ↓
Vetor da pergunta
        ↓
Vector Search
        ↓
Comparação com vetores armazenados
        ↓
Documentos mais semelhantes
```

Para determinar quais vetores são mais próximos, podem ser utilizadas diferentes métricas de similaridade, como **Cosine Similarity**, distância euclidiana ou produto interno.

No caso da Cosine Similarity, por exemplo:

$$  
\text{similaridade}(A,B)=\frac{A\cdot B}{|A||B|}  
$$

Quanto maior a similaridade, mais próximos os vetores são considerados em termos da métrica utilizada.

Um detalhe importante é que Vector Search não significa simplesmente "comparar todos os vetores um por um". Em bases grandes, isso poderia ser muito lento. Por isso, os sistemas utilizam estruturas e algoritmos especializados para tornar a busca eficiente.

Esse será um ponto importante quando estudarmos conceitos como **Approximate Nearest Neighbor (ANN)** e **HNSW**.

---

## Um exemplo

Imagine que uma empresa possui milhares de documentos internos.

Entre eles existem:

```
Documento A:
"Funcionários devem solicitar férias pelo portal corporativo."

Documento B:
"O pagamento do salário é realizado até o quinto dia útil."

Documento C:
"O período de descanso deve ser previamente aprovado pelo gestor."
```

Esses documentos são transformados em embeddings e armazenados em um Vector Database.

O usuário pergunta:

```
"Quero saber como marcar minhas férias."
```

A pergunta passa pelo mesmo modelo de embeddings:

```
Pergunta
   ↓
Embedding Model
   ↓
Vetor da pergunta
```

A Vector Search compara esse vetor com os vetores dos documentos.

Um resultado possível seria:

```
Documento A → similaridade alta
Documento C → similaridade alta
Documento B → similaridade baixa
```

Os documentos A e C são então recuperados e podem ser enviados para a LLM como contexto:

```
Pergunta
   ↓
Vector Search
   ↓
Documentos relevantes
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

Esse é justamente um dos mecanismos fundamentais de um sistema RAG.

---

## Por que é importante

Vector Search é importante porque permite que sistemas de IA encontrem informações com base no **significado**, e não apenas na correspondência literal de palavras.

Isso resolve uma limitação importante da busca tradicional.

Considere:

```
Busca por palavras-chave:

"carro"
```

Ela pode priorizar documentos que contenham exatamente a palavra "carro".

Já uma busca vetorial pode encontrar conteúdos relacionados a:

```
automóvel
veículo
transporte particular
meu carro
comprar um veículo
```

mesmo quando a palavra original não aparece.

Isso torna a Vector Search especialmente útil para:
- RAG
- Busca semântica
- Sistemas de perguntas e respostas
- Busca em documentos
- Sistemas de recomendação
- Recuperação de informações em bases de conhecimento
- Agentes de IA que precisam consultar informações externas

Também é importante diferenciar alguns conceitos que podem parecer iguais:

**Semantic Similarity** é o conceito de medir o quanto dois conteúdos são semanticamente relacionados.

**Cosine Similarity** é uma das métricas matemáticas que podem ser utilizadas para comparar os vetores.

**Vector Search** é o processo de procurar os vetores mais relevantes para uma determinada consulta.

**Vector Database** é a infraestrutura especializada que pode armazenar esses vetores e realizar esse tipo de consulta.

Podemos visualizar a relação entre eles:

```
Texto
   ↓
Embedding Model
   ↓
Vector Embedding
   ↓
Vector Database
   ↓
Vector Search
   ↓
Similarity Metric
   ↓
Vetores mais relevantes
   ↓
Contexto
   ↓
LLM
```

A ideia central é: **Vector Search permite transformar uma pergunta em uma busca por significado, encontrando informações semanticamente relacionadas mesmo quando elas utilizam palavras diferentes.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-vector-search/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
