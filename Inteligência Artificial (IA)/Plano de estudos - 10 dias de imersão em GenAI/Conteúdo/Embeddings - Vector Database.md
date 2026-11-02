[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Vector Database

## O que é

Um **Vector Database**, ou banco de dados vetorial, é um sistema especializado em **armazenar, organizar e consultar vetores**, especialmente os vetores gerados por modelos de embeddings.

Em aplicações de IA, ele permite encontrar informações que são **semanticamente semelhantes** a uma consulta, mesmo quando as palavras utilizadas são diferentes.

Um banco de dados tradicional pode responder:

> “Quais registros possuem a palavra `férias`?”

Um Vector Database pode responder:

> “Quais documentos possuem informações relacionadas ao processo de solicitar férias?”

Para isso, ele utiliza os vetores produzidos pelos embeddings e algoritmos de busca por similaridade, como a **Cosine Similarity**.

---

## Como funciona

Imagine que temos vários documentos de uma empresa.

Primeiro, os documentos são divididos em partes menores. Cada parte passa por um **Embedding Model**, que transforma o conteúdo em um vetor.

O fluxo pode ser representado assim:

```
Documento
   ↓
Chunking
   ↓
Embedding Model
   ↓
Vector Embedding
   ↓
Vector Database
```

O banco armazena o vetor junto com informações que permitem identificar sua origem, como o texto original, o documento, a página ou outros metadados.

Quando o usuário faz uma pergunta, acontece um processo semelhante:

```
Pergunta do usuário
   ↓
Embedding Model
   ↓
Vetor da pergunta
   ↓
Busca por similaridade
   ↓
Vetores mais semelhantes
   ↓
Trechos correspondentes
   ↓
LLM
   ↓
Resposta
```

O ponto importante é que o banco não precisa procurar apenas pelas mesmas palavras. Ele procura **vetores próximos no espaço vetorial**.

Por isso, uma pergunta como:

```
"Como posso marcar minhas férias?"
```

pode encontrar um documento que diga:

```
"Os colaboradores devem registrar o período de descanso
no sistema de gestão de pessoas."
```

Mesmo sem compartilhar exatamente as mesmas palavras, os dois conteúdos podem possuir uma representação vetorial semanticamente próxima.

Um Vector Database normalmente também permite armazenar **metadados** associados aos vetores. Isso possibilita combinar busca semântica com filtros.

Por exemplo:

```
Buscar conteúdos semanticamente semelhantes
+
filtrar documentos do departamento = RH
+
filtrar ano = 2026
```

Isso torna a recuperação de informações mais precisa.

---

## Um exemplo

Imagine uma empresa com uma base de documentos contendo:

```
Documento A:
"Funcionários podem solicitar férias pelo sistema interno."

Documento B:
"O pagamento do salário ocorre até o quinto dia útil."

Documento C:
"O período de férias deve ser combinado previamente com o gestor."
```

Esses documentos são transformados em embeddings e armazenados no Vector Database.

O usuário pergunta:

```
"Como faço para pedir minhas férias?"
```

A pergunta também é transformada em um embedding.

O Vector Database compara o vetor da pergunta com os vetores armazenados usando uma métrica de similaridade.

O resultado poderia ser:

```
Documento A → alta similaridade
Documento C → alta similaridade
Documento B → baixa similaridade
```

O sistema recupera os trechos mais relevantes e os fornece à LLM como contexto.

Assim, em uma arquitetura RAG:

```
Pergunta
   ↓
Embedding
   ↓
Vector Database
   ↓
Busca por similaridade
   ↓
Documentos relevantes
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

O Vector Database, portanto, funciona como uma espécie de **índice semântico** da base de conhecimento.

---

## Por que é importante

O Vector Database é uma peça fundamental de muitas arquiteturas modernas de **RAG**, porque permite recuperar rapidamente informações relevantes a partir de grandes volumes de conteúdo.

Ele é especialmente útil quando precisamos encontrar informações por **significado**, e não apenas por correspondência literal de palavras.

Suas principais aplicações incluem:
- Busca semântica
- RAG
- Sistemas de recomendação
- Busca por documentos semelhantes
- Detecção de conteúdo relacionado
- Classificação e agrupamento
- Sistemas de perguntas e respostas
- Memória de agentes de IA

É importante também entender que o Vector Database **não é a mesma coisa que um banco de dados tradicional**.

Um banco relacional é excelente para consultas estruturadas, como:

```
SELECT * FROM clientes
WHERE idade > 30;
```

Já um Vector Database é especializado em perguntas como:

```
"Encontre os documentos mais relacionados
a esta pergunta."
```

Na prática, sistemas de IA podem utilizar os dois. Um banco tradicional pode armazenar os dados estruturados, enquanto um Vector Database pode armazenar os embeddings utilizados para busca semântica.

A relação entre os conceitos estudados até aqui pode ser resumida assim:

```
Embedding
    ↓
Vector Embedding
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Cosine Similarity
    ↓
Conteúdo relevante
    ↓
RAG
    ↓
LLM
```

A ideia central é simples: **o embedding transforma o conteúdo em uma representação vetorial, enquanto o Vector Database torna possível armazenar e encontrar essas representações de forma eficiente.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-vector-database/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
