[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Semantic Search

## O que é

**Semantic Search**, ou busca semântica, é uma forma de pesquisa que procura informações com base no **significado e na intenção da consulta**, e não apenas na correspondência exata entre palavras.

Em uma busca tradicional por palavras-chave, o sistema tende a procurar termos que aparecem diretamente no conteúdo.

Na busca semântica, a consulta é transformada em uma representação que permite identificar conteúdos relacionados mesmo quando utilizam palavras diferentes.

Por exemplo:

```
Consulta:
"Como faço para marcar minhas férias?"
```

Uma busca semântica pode encontrar:

```
"Os colaboradores devem registrar o período de descanso
pelo portal corporativo."
```

As frases não utilizam as mesmas palavras, mas possuem significado relacionado.

Esse é o principal objetivo da Semantic Search: **encontrar informação relevante pelo significado, e não apenas pelo vocabulário utilizado.**

---

## Como funciona

Podemos imaginar que todos os conteúdos de uma base são colocados em um **mapa semântico**.

Conteúdos relacionados ficam próximos nesse espaço:

```
                 Férias
             ●   ●   ●
          ●
                            ● Salários
                       ●
      ● Benefícios

                         ● Segurança
```

Quando o usuário faz uma pergunta, ela também é transformada em um embedding e posicionada nesse espaço.

Por exemplo:

```
"Como marcar minhas férias?"
            ↓
        Embedding
            ↓
       ● Pergunta
```

A busca procura os conteúdos semanticamente mais próximos da pergunta.

O processo pode ser simplificado assim:

```
Consulta do usuário
        ↓
Embedding Model
        ↓
Vetor da consulta
        ↓
Vector Search
        ↓
Nearest Neighbors
        ↓
Conteúdos relevantes
```

Aqui aparecem vários conceitos que já estudamos.

O **Embedding** transforma a consulta em um vetor.

A **Vector Search** procura vetores semelhantes.

O **Nearest Neighbor** representa a ideia de encontrar os vetores mais próximos.

Uma métrica como **Cosine Similarity** pode ser utilizada para calcular essa proximidade.

Em sistemas maiores, o Vector Database pode armazenar os embeddings e realizar essa busca de forma eficiente.

Portanto, Semantic Search é o conceito mais amplo. Vector Search é uma das principais formas de implementá-lo.

---

## Um exemplo

Imagine uma base de conhecimento de uma empresa com os seguintes documentos:

```
Documento A:
"Os funcionários podem solicitar férias pelo portal corporativo."

Documento B:
"O pagamento do salário é realizado até o quinto dia útil."

Documento C:
"O colaborador deve obter aprovação do gestor antes de
definir o período de descanso."
```

O usuário pesquisa:

```
"Qual é o procedimento para tirar férias?"
```

Uma busca simples por palavras-chave poderia ter dificuldade, porque o documento pode não conter exatamente as palavras "procedimento" ou "tirar férias".

A Semantic Search transforma a consulta em um embedding:

```
Pergunta
   ↓
Embedding
   ↓
Vetor da consulta
```

Depois, compara esse vetor com os vetores dos documentos:

```
Documento A → alta similaridade
Documento B → baixa similaridade
Documento C → alta similaridade
```

Os documentos A e C são então recuperados como informações relevantes.

Em uma aplicação RAG, eles podem ser enviados para a LLM:

```
Pergunta
   ↓
Semantic Search
   ↓
Informações relevantes
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

A LLM pode então combinar as informações dos dois documentos para responder à pergunta.

---

## Por que é importante

Semantic Search é importante porque permite que sistemas de IA lidem melhor com a **variação natural da linguagem**.

Duas pessoas podem fazer a mesma pergunta de maneiras completamente diferentes:

```
"Como solicitar férias?"

"Quero marcar meu período de descanso."

"Qual é o procedimento para tirar férias?"

"Como faço para agendar minhas férias?"
```

Uma busca baseada apenas em palavras-chave pode tratar essas consultas de maneira bastante diferente.

Uma busca semântica procura identificar que todas elas estão relacionadas ao mesmo conceito.

Isso é especialmente importante em:
- RAG
- Bases de conhecimento
- Busca em documentos
- Assistentes virtuais
- Sistemas de perguntas e respostas
- Sistemas de recomendação
- Pesquisa em grandes volumes de conteúdo

Também é importante diferenciar alguns conceitos:

**Keyword Search** procura principalmente correspondências entre palavras.

**Semantic Search** procura correspondências de significado.

**Embedding** é a representação vetorial usada para capturar características semânticas do conteúdo.

**Vector Search** é o mecanismo utilizado para procurar vetores semelhantes.

**Vector Database** é uma infraestrutura que pode armazenar esses vetores e realizar buscas eficientes.

A relação pode ser visualizada assim:

```
Texto / Pergunta
       ↓
Embedding Model
       ↓
Vector Embedding
       ↓
Vector Search
       ↓
Nearest Neighbors
       ↓
Conteúdo semanticamente relevante
       ↓
RAG / Aplicação de IA
```

Um ponto importante é que **Semantic Search não significa necessariamente que a informação encontrada está correta**. Ela indica que o conteúdo parece semanticamente relacionado à consulta.

Por exemplo, dois documentos podem falar sobre férias, mas um deles pode conter uma política antiga e o outro uma política atual. A busca semântica pode considerar ambos relevantes.

Por isso, em sistemas RAG, a qualidade da resposta depende não apenas da busca, mas também de fatores como **qualidade dos documentos, filtros, ranking, contexto fornecido à LLM e validação das informações**.

A ideia central é: **Semantic Search permite encontrar informações relevantes pelo significado da consulta, mesmo quando as palavras utilizadas na pergunta e nos documentos são diferentes.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-semantic-search/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
