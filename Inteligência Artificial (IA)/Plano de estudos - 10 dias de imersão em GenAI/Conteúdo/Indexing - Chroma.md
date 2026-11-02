[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Indexing Chroma

## O que é

**Chroma** é um banco de dados vetorial desenvolvido para armazenar e recuperar informações relacionadas a embeddings. No contexto de RAG, ele pode ser utilizado como parte da etapa de **Indexing**, recebendo os chunks já processados e seus respectivos embeddings para torná-los pesquisáveis.

Em uma arquitetura simples, o fluxo fica assim:

```
Documentos
   ↓
Parsing
   ↓
Cleaning
   ↓
Chunking
   ↓
Embedding Model
   ↓
Embeddings + Metadata
   ↓
Chroma
   ↓
Vector Search
   ↓
Chunks relevantes
```

É importante perceber que **Chroma não é o processo de indexing em si**. Ele é uma tecnologia que pode ser utilizada para armazenar os dados e construir estruturas necessárias para realizar buscas vetoriais.

## Como funciona

Imagine que temos milhares de chunks de documentos.

Cada chunk possui seu conteúdo, um embedding e, opcionalmente, metadados:

```
Chunk:
"Funcionários devem solicitar férias com 30 dias
de antecedência."

Embedding:
[0.21, -0.73, 0.45, ...]

Metadata:
{
  "documento": "politica_ferias.pdf",
  "pagina": 4
}
```

O Chroma organiza essas informações para que posteriormente seja possível pesquisar por similaridade.

Quando chega uma pergunta:

```
"Com quanto tempo de antecedência
devo solicitar minhas férias?"
```

ela também passa pelo Embedding Model:

```
Pergunta
   ↓
Embedding Model
   ↓
Vetor da pergunta
```

O Chroma pode então ser consultado para encontrar os embeddings mais próximos daquele vetor.

```
Vetor da pergunta
       ↓
     Chroma
       ↓
┌──────────────────────────┐
│ Chunk A  → muito próximo │
│ Chunk B  → próximo       │
│ Chunk C  → distante      │
└──────────────────────────┘
       ↓
Chunks relevantes
```

A ideia é semelhante a procurar pontos próximos em um mapa, mas o espaço onde esses pontos existem possui muitas dimensões e representa relações semânticas.

## Um exemplo

Imagine uma pequena base de conhecimento sobre políticas de uma empresa.

Durante a ingestão, temos:

```
Chunk 1:
"Funcionários devem solicitar férias com 30 dias
de antecedência."

Chunk 2:
"O plano de saúde pode ser utilizado após o período
de carência."

Chunk 3:
"Despesas de viagem devem ser enviadas para aprovação
até o quinto dia útil."
```

O Embedding Model transforma cada chunk em um vetor:

```
Chunk 1 → Embedding → Vetor 1
Chunk 2 → Embedding → Vetor 2
Chunk 3 → Embedding → Vetor 3
```

Essas informações podem ser armazenadas no Chroma juntamente com os metadados:

```
Chroma

┌─────────────────────────────────────┐
│ ID                                  │
│ Embedding                           │
│ Documento                           │
│ Conteúdo                            │
│ Metadata                            │
└─────────────────────────────────────┘
```

Depois, o usuário pergunta:

> "Qual é o prazo para solicitar férias?"

A pergunta é transformada em um embedding e utilizada na consulta.

O Chroma retorna os chunks considerados mais próximos:

```
Pergunta
   ↓
Embedding
   ↓
Chroma
   ↓
Chunk 1
   ↓
Contexto do LLM
   ↓
Resposta
```

Nesse cenário, o Chroma está funcionando como uma camada de armazenamento e recuperação vetorial dentro do pipeline RAG.

## Por que é importante

Chroma é importante para entender como os conceitos de **Embedding, Indexing, Vector Database e Retrieval** se conectam em uma implementação real.

Até aqui, podemos pensar nos conceitos desta forma:

```
Embedding Model
→ transforma texto em vetores

Embedding
→ representação vetorial produzida pelo modelo

Chroma
→ armazena e gerencia embeddings e seus dados associados

Indexing
→ prepara estruturas para tornar a busca eficiente

Vector Search
→ procura vetores semanticamente próximos

Retrieval
→ recupera os chunks relevantes
```

O Chroma também pode armazenar **metadata**, permitindo combinar a busca vetorial com filtros estruturados.

Por exemplo:

```
Busca semântica:
"Qual é a política atual de férias?"

Filtro:
ano = 2026
departamento = "RH"
```

Isso permite restringir o universo da busca antes ou durante a recuperação.

Um ponto importante é que **Chroma não é obrigatório para construir RAG**. Ele é uma das opções de tecnologia que podem desempenhar o papel de banco de dados e mecanismo de busca vetorial. Outras soluções podem cumprir funções semelhantes.

Assim, quando falamos em **Indexing com Chroma**, estamos essencialmente falando sobre pegar os chunks já preparados e seus embeddings, armazená-los de maneira organizada e disponibilizá-los para consultas eficientes posteriormente.

O ponto central é: **Chroma é uma tecnologia de armazenamento e recuperação vetorial que pode ser utilizada na etapa de Indexing de um sistema RAG, mantendo embeddings, conteúdo e metadados organizados para que os chunks relevantes possam ser encontrados durante o retrieval.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/indexing-chroma/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
