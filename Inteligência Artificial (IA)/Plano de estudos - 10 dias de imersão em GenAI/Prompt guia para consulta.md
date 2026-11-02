# Prompt para continuar meu material de estudos sobre IA Generativa

Estou criando um material de estudos sobre **IA, IA Generativa, LLMs, Prompt Engineering e RAG**, organizado em termos e conceitos individuais. O material será mantido no **Obsidian em Markdown** e deve funcionar como um material de consulta e aprendizado contínuo.

Quero continuar esse trabalho em uma nova conversa. Siga rigorosamente as instruções abaixo.

## Objetivo

Para cada novo termo que eu fornecer, produza uma explicação didática, conceitualmente correta e conectada aos termos que já foram estudados.

O objetivo não é criar definições de dicionário isoladas. Cada novo conceito deve ser explicado de forma que ele se encaixe naturalmente na arquitetura e na sequência de aprendizado.

O nível deve ser **intermediário**, com linguagem simples e intuitiva, mas sem simplificar demais a ponto de perder precisão técnica.

Evite repetir longamente conceitos que já foram explicados. Quando um conceito anterior for necessário para explicar o novo termo, faça apenas uma conexão breve e avance para o que há de novo.

## Estrutura obrigatória

Para cada termo, utilize exatamente estas quatro seções:

```markdown
# Nome do termo

## O que é

## Como funciona

## Um exemplo

## Por que é importante
```

Não crie outras seções principais além dessas quatro.

## Conteúdo de cada seção

### O que é

Apresente uma definição clara e objetiva.

Explique qual é a função do conceito e em qual contexto ele aparece.

Quando houver conceitos próximos que possam gerar confusão, diferencie-os brevemente.

### Como funciona

Explique o mecanismo de maneira visual e progressiva.

Use fluxos em blocos de código quando isso ajudar:

```text
Entrada
   ↓
Processamento
   ↓
Resultado
```

Priorize a compreensão do funcionamento em vez de apenas descrever características.

### Um exemplo

Crie um exemplo prático, preferencialmente relacionado a:

- RAG
- LLMs
- documentos
- busca
- embeddings
- sistemas corporativos
- assistentes de IA
- perguntas e respostas

Quando adequado, mostre o fluxo do exemplo em um bloco de código.

### Por que é importante

Explique por que o conceito existe, qual problema resolve e onde ele se encaixa na arquitetura maior.

Sempre que fizer sentido, conecte o conceito aos termos estudados anteriormente.

## Estilo

Escreva em **português brasileiro**.

O texto deve ser:

- didático;
- claro;
- técnico sem ser excessivamente acadêmico;
- progressivo;
- objetivo;
- conceitualmente preciso;
- fácil de consultar posteriormente.

Use analogias quando elas realmente ajudarem na compreensão.

Não transforme o conteúdo em uma lista excessiva de definições.

Prefira explicações contínuas e exemplos práticos.

## Regra importante sobre travessões

**NÃO USE travessão ou meia-risca no material.**

Não utilize:

```text
—
–
```

Substitua por vírgulas, dois-pontos, ponto e vírgula, parênteses ou frases separadas.

Essa regra vale para todo o conteúdo, inclusive títulos, tabelas, exemplos e explicações.

## Listas

Quando houver uma lista depois de dois-pontos, **não deixe uma linha em branco entre os dois-pontos e o primeiro item**.

Exemplo correto:

```markdown
Os principais benefícios são:
- maior precisão;
- menor custo;
- melhor controle.
```

Não faça:

```markdown
Os principais benefícios são:

- maior precisão;
- menor custo;
- melhor controle.
```

## Fórmulas

Quando houver fórmulas matemáticas, utilize LaTeX compatível com Obsidian em bloco:

```markdown
$$
\text{score}(A,B)=...
$$
```

Não utilize formatos incompatíveis com esse padrão.

## Blocos de código

Use blocos de código para:

- fluxos;
- exemplos estruturais;
- representações de arquitetura;
- exemplos de dados;
- comparações conceituais quando uma representação visual ajudar.

Exemplo:

```text
Pergunta
   ↓
Retrieval
   ↓
Reranking
   ↓
Contexto
   ↓
LLM
```

## Continuidade conceitual

O material já percorreu conceitos de Prompt Engineering, segurança, Grounding, Tool Instructions e RAG.

Na parte de RAG, a sequência estudada foi aproximadamente:

```text
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
   ↓
Contexto
   ↓
LLM
```

Foram estudados, entre outros:

### Ingestion
- Ingestion
- Ingestion Cleaning
- Ingestion Parsing

### Chunking
- Chunking
- Fixed-size Chunking
- Chunking Metadata
- Chunking Overlap
- Recursive Chunking
- Semantic Chunking

### Indexing
- Indexing
- Indexing Chroma
- Indexing FAISS
- Indexing pgvector
- Indexing Pinecone
- Indexing Qdrant
- Indexing Weaviate

### Retrieval
- Retrieval
- Hybrid Search
- Metadata Filtering
- Query Rewriting
- Similarity Search
- Top-k
- Reranking
- Reranker

Quando eu fornecer o próximo termo, continue a partir desse ponto sem voltar a explicar toda a sequência.

## Relações entre conceitos

Sempre que relevante, mostre a relação do novo conceito com os anteriores.

Por exemplo:

```text
Similarity Search
      ↓
Top-k
      ↓
Reranking
      ↓
Top-k final
      ↓
Contexto
      ↓
LLM
```

Não repita explicações completas de Similarity Search, Top-k ou Reranking se o novo termo apenas depender deles. Explique apenas o que for necessário para estabelecer a conexão.

## Precisão conceitual

Não trate conceitos relacionados como se fossem sinônimos quando não forem.

Por exemplo:

- Retrieval não é a mesma coisa que Vector Search.
- Vector Database não é a mesma coisa que Indexing.
- Similarity Search não é a mesma coisa que Semantic Similarity.
- Reranking é o processo, Reranker é o componente que executa o processo.
- Dense Retrieval é diferente de Sparse Retrieval.
- Hybrid Search combina mecanismos de busca.
- Top-k define quantos resultados são selecionados.
- Metadata Filtering restringe resultados por atributos estruturados.
- Query Rewriting modifica a consulta para melhorar o Retrieval.

Quando existir uma distinção importante, explique-a explicitamente.

## Evite antecipações desnecessárias

Não explique detalhadamente conceitos que ainda não foram solicitados.

Se o novo termo estiver relacionado a outro conceito que provavelmente será estudado depois, apenas estabeleça a conexão necessária.

Por exemplo, se eu pedir um conceito que utiliza ANN, explique o suficiente para contextualizar, mas não transforme a resposta em uma explicação completa de ANN se esse ainda não for o termo solicitado.

## Formato final

Sempre entregue o conteúdo como um **writing block** de documento, pronto para ser copiado para o Obsidian.

Use:

```text