[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Dense Retrieval

## O que é

**Dense Retrieval**, ou recuperação densa, é uma técnica de recuperação de informações que representa consultas e documentos como **vetores densos**, normalmente gerados por modelos de embeddings.

A ideia é encontrar documentos relevantes comparando a representação vetorial da consulta com as representações vetoriais dos documentos.

Por exemplo:

```
Pergunta
"Como solicitar férias?"
        ↓
Embedding
        ↓
Vetor da consulta
        ↓
Comparação com vetores dos documentos
        ↓
Documentos mais semelhantes
```

O termo **dense**, ou denso, vem da forma como esses vetores são representados. Em geral, um vetor denso possui muitas dimensões e a maioria delas contém algum valor.

Isso contrasta com métodos de recuperação **sparse**, como a busca tradicional baseada em palavras-chave, nos quais a representação pode ter milhares ou milhões de posições, mas apenas algumas são relevantes para cada documento.

---

## Como funciona

Imagine que cada documento seja transformado em um ponto dentro de um espaço com muitas dimensões.

```
Documento A → vetor
Documento B → vetor
Documento C → vetor
Documento D → vetor
```

A consulta do usuário também é transformada em um vetor:

```
Consulta → vetor
```

O Dense Retrieval procura os documentos cujos vetores estão mais próximos do vetor da consulta.

```
Consulta
   ↓
Embedding
   ↓
Vetor denso
   ↓
Busca por similaridade
   ↓
Documentos mais próximos
```

A proximidade pode ser calculada usando métricas como **Cosine Similarity** ou produto interno.

Por exemplo:

```
Consulta
"Como marcar minhas férias?"

        ↓

Embedding

        ↓

[0.82, 0.14, 0.67, 0.31, ...]

        ↓

Comparação com documentos

        ↓

Documento A → 0.92
Documento B → 0.41
Documento C → 0.87
```

Nesse exemplo, os documentos A e C seriam candidatos relevantes para a consulta.

A grande diferença em relação à busca por palavras-chave é que o sistema não precisa encontrar necessariamente as mesmas palavras. O embedding procura capturar características relacionadas ao **significado** do conteúdo.

Isso permite que uma consulta como:

```
"Como faço para marcar minhas férias?"
```

encontre um documento que contenha:

```
"O colaborador deve registrar o período de descanso
no portal corporativo."
```

Mesmo com vocabulário diferente, os conteúdos podem produzir vetores próximos.

Em bases grandes, essa busca normalmente utiliza técnicas de **Approximate Nearest Neighbor**, permitindo encontrar rapidamente vetores próximos sem comparar a consulta individualmente com todos os vetores existentes.

---

## Um exemplo

Imagine uma base de conhecimento com milhares de documentos de uma empresa.

Entre eles existem:

```
Documento A:
"Os funcionários devem registrar o período de férias
no sistema corporativo."

Documento B:
"O salário é depositado até o quinto dia útil."

Documento C:
"O período de descanso precisa ser aprovado pelo gestor."
```

O usuário pergunta:

```
"Quero saber como agendar minhas férias."
```

No Dense Retrieval, tanto a pergunta quanto os documentos são transformados em embeddings:

```
Pergunta
   ↓
Embedding
   ↓
Vetor da pergunta

Documentos
   ↓
Embedding
   ↓
Vetores dos documentos
```

O sistema então calcula a similaridade entre a consulta e os documentos:

```
Documento A → alta similaridade
Documento B → baixa similaridade
Documento C → alta similaridade
```

Os documentos A e C podem ser recuperados e enviados para a próxima etapa de um sistema RAG:

```
Pergunta
   ↓
Dense Retrieval
   ↓
Documentos relevantes
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

Nesse cenário, o Dense Retrieval é responsável pela **etapa de recuperação**, não pela geração da resposta.

---

## Por que é importante

Dense Retrieval é importante porque permite que sistemas de recuperação encontrem informações relacionadas pelo **significado**, mesmo quando existe pouca correspondência literal entre a consulta e o documento.

Ele é especialmente relevante em:
- Semantic Search
- RAG
- Sistemas de perguntas e respostas
- Bases de conhecimento
- Busca em documentos
- Sistemas de recomendação
- Agentes que precisam recuperar informações externas

Também ajuda a entender a diferença entre **Sparse Retrieval** e **Dense Retrieval**.

No Sparse Retrieval, a representação tende a estar ligada à presença de termos específicos:

```
"férias" → palavra encontrada
"salário" → palavra encontrada
"benefícios" → palavra encontrada
```

No Dense Retrieval, o conteúdo é representado por um vetor de alta dimensão:

```
Texto
  ↓
Embedding
  ↓
[0.21, 0.73, 0.14, 0.91, ...]
```

O sistema procura proximidade entre essas representações.

Isso não significa que Dense Retrieval seja sempre superior ao Sparse Retrieval. Cada abordagem possui vantagens.

O Sparse Retrieval pode ser muito útil quando termos exatos são importantes, como nomes, códigos, identificadores ou termos técnicos. O Dense Retrieval tende a ser mais útil quando queremos recuperar conteúdo semanticamente relacionado.

Por isso, sistemas modernos frequentemente combinam os dois em uma abordagem chamada **Hybrid Search**.

A relação entre os conceitos estudados pode ser resumida assim:

```
Texto
   ↓
Embedding Model
   ↓
Dense Vector
   ↓
Dense Retrieval
   ↓
Similarity Search
   ↓
Nearest Neighbors
   ↓
Documentos relevantes
   ↓
RAG
   ↓
LLM
```

Uma distinção importante:

**Semantic Search** descreve o objetivo de encontrar informações pelo significado.

**Vector Search** descreve a busca realizada sobre representações vetoriais.

**Dense Retrieval** descreve uma abordagem de recuperação em que consultas e documentos são representados por vetores densos e comparados para encontrar conteúdo relevante.

A ideia central é: **Dense Retrieval transforma consultas e documentos em representações vetoriais densas e utiliza a proximidade entre esses vetores para recuperar informações semanticamente relevantes.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-dense-retrieval/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
