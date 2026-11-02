[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# GraphRAG

## O que é

GraphRAG é uma abordagem de RAG que utiliza um **grafo de conhecimento** para representar as relações entre informações antes de recuperá-las.

Em um RAG tradicional, os documentos são normalmente divididos em chunks, transformados em embeddings e armazenados em um índice vetorial. Quando o usuário faz uma pergunta, o sistema procura os chunks semanticamente mais relevantes.

No GraphRAG, além de armazenar o conteúdo dos documentos, o sistema procura identificar **entidades e relações entre elas**.

Por exemplo, considere documentos que mencionam:

```
Empresa A
    ↓ possui
Produto X
    ↓ desenvolvido por
Equipe Y
    ↓ liderada por
Pessoa Z
```

Essas relações podem ser representadas como um grafo:

```
[Empresa A]
     │
   possui
     ↓
[Produto X]
     │
desenvolvido por
     ↓
[Equipe Y]
     │
  liderada por
     ↓
[Pessoa Z]
```

O objetivo é permitir que o Retrieval considere não apenas a proximidade semântica entre uma pergunta e um trecho de texto, mas também **as conexões existentes entre as informações**.

GraphRAG, portanto, não substitui necessariamente o RAG tradicional. Ele é uma forma de enriquecer a recuperação utilizando a estrutura relacional dos dados.

## Como funciona

O processo geralmente começa com a ingestão dos documentos, assim como em outros sistemas RAG. A diferença aparece quando o sistema tenta extrair uma estrutura de conhecimento a partir deles.

Um fluxo simplificado seria:

```
Documentos
↓
Parsing
↓
Chunking
↓
LLM / NLP extrai entidades e relações
↓
Construção do grafo
↓
Indexação
↓
Consulta do usuário
↓
Graph Retrieval
↓
Contexto estruturado
↓
LLM
↓
Resposta
```

Imagine que os documentos contenham informações como:

```
"A empresa Acme adquiriu a Beta em 2024.
A Beta possuía a plataforma Gamma.
Após a aquisição, a equipe da Beta foi incorporada à divisão de Tecnologia da Acme."
```

Um sistema pode transformar essas informações em uma estrutura semelhante a:

```
[Acme]
  │
adquiriu
  ↓
[Beta]
  │
possuía
  ↓
[Gamma]

[Beta]
  │
equipe incorporada à
  ↓
[Divisão de Tecnologia]
```

Essa estrutura permite realizar consultas baseadas em relações.

Por exemplo:

> "Quais produtos passaram a fazer parte da Acme após aquisições?"

O sistema pode percorrer as relações:

```
[Acme]
  ↓ adquiriu
[Empresa adquirida]
  ↓ possuía
[Produto]
```

Isso é diferente de simplesmente procurar chunks que contenham palavras relacionadas a "Acme", "aquisição" e "produto".

Um aspecto importante é que GraphRAG pode trabalhar junto com **busca vetorial**. Nesse caso, o sistema pode combinar diferentes estratégias:

```
                    ┌──→ Vector Search
Pergunta → Retrieval ┼──→ Keyword Search
                    └──→ Graph Retrieval
                              ↓
                         Reranking
                              ↓
                         Contexto
                              ↓
                             LLM
```

Assim, o grafo não precisa substituir embeddings ou busca semântica. Ele pode complementar essas técnicas.

A grande vantagem aparece principalmente quando a resposta depende de **múltiplas relações entre entidades**.

Considere uma pergunta como:

> "Quais departamentos são afetados pelos projetos que dependem da plataforma X?"

Uma busca vetorial pode encontrar documentos sobre a plataforma X, projetos e departamentos. Porém, o grafo pode representar explicitamente:

```
[Plataforma X]
      ↓
   utilizada por
      ↓
[Projeto A]
      ↓
impacta
      ↓
[Departamento Financeiro]
```

e:

```
[Plataforma X]
      ↓
   utilizada por
      ↓
[Projeto B]
      ↓
impacta
      ↓
[Departamento Comercial]
```

O sistema consegue então seguir essas conexões para construir uma resposta mais estruturada.

GraphRAG também pode ser especialmente útil para perguntas **globais sobre um conjunto de documentos**.

Em vez de perguntar apenas:

> "Qual documento fala sobre X?"

podemos perguntar:

> "Quais são os principais temas discutidos nesses documentos e como eles se relacionam?"

Nesse tipo de cenário, a estrutura do grafo pode ajudar o sistema a identificar comunidades, entidades recorrentes e relações entre diferentes partes do corpus.

## Um exemplo

Imagine uma empresa com milhares de documentos contendo informações sobre clientes, contratos, produtos, projetos e equipes.

Um usuário pergunta:

> "Quais clientes possuem contratos relacionados a produtos desenvolvidos pela equipe de IA?"

Um RAG baseado apenas em embeddings poderia procurar documentos semanticamente próximos dessa pergunta.

Um GraphRAG poderia representar as relações:

```
[Cliente]
   │
possui
   ↓
[Contrato]
   │
relacionado a
   ↓
[Produto]
   │
desenvolvido por
   ↓
[Equipe de IA]
```

A consulta pode então seguir o caminho:

```
Cliente
  ↓
Contrato
  ↓
Produto
  ↓
Equipe de IA
```

O resultado não depende apenas de encontrar um chunk contendo todas essas informações. As informações podem estar distribuídas em vários documentos, desde que as relações entre elas tenham sido identificadas durante a construção do grafo.

Esse é um ponto fundamental do GraphRAG: **a informação relevante pode estar distribuída, mas suas relações podem conectá-la**.

## Por que é importante

GraphRAG é importante porque muitos problemas reais não dependem apenas de encontrar informações semelhantes à pergunta. Eles dependem de **entender relações**.

Isso é particularmente relevante para perguntas que envolvem:

```
Entidades
   ↓
Relações
   ↓
Dependências
   ↓
Caminhos entre entidades
   ↓
Conclusões
```

Por exemplo, perguntas como "quem trabalha com quem", "qual sistema depende de qual", "quais projetos são afetados por determinada mudança" ou "quais empresas estão relacionadas por aquisições" possuem uma estrutura naturalmente relacional.

A principal diferença em relação ao RAG baseado apenas em busca vetorial pode ser resumida assim:

```
Vector RAG

Pergunta
↓
Similaridade semântica
↓
Chunks relevantes
↓
Contexto
↓
LLM


GraphRAG

Pergunta
↓
Entidades e relações relevantes
↓
Grafo
↓
Caminhos / vizinhanças / subgrafos
↓
Contexto estruturado
↓
LLM
```

Isso não significa que GraphRAG seja sempre superior. A construção do grafo pode ser complexa, especialmente quando é necessário extrair relações corretamente de grandes volumes de documentos. Além disso, a qualidade das respostas depende diretamente da qualidade das entidades e relações identificadas.

Por isso, GraphRAG é melhor entendido como uma **estratégia de Retrieval orientada a relações**, especialmente útil quando a pergunta exige conectar informações que estão distribuídas por diferentes documentos ou entidades.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/rag-avancado-graphrag/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
