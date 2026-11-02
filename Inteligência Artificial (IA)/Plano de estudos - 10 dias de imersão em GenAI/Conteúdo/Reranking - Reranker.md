# Reranker

## O que é

Um **Reranker** é um modelo ou componente responsável por **avaliar novamente os resultados recuperados por uma busca inicial e atribuir uma nova pontuação de relevância a cada candidato**.

Enquanto o **Reranking** é o processo, o **Reranker** é quem executa esse processo.

A arquitetura pode ser representada assim:

```
Pergunta
   ↓
Retrieval
   ↓
Top-k candidatos
   ↓
Reranker
   ↓
Novas pontuações
   ↓
Ranking reorganizado
   ↓
Top-k final
   ↓
LLM
```

O Reranker normalmente recebe a **consulta e um documento ou chunk candidato juntos**, avaliando o quanto aquele conteúdo realmente responde à consulta.

Isso é diferente de uma busca vetorial tradicional, que normalmente compara a representação vetorial da consulta com os vetores armazenados.

## Como funciona

Imagine que o Retrieval encontrou cinco candidatos para a pergunta:

```
Pergunta:
"Qual é o prazo para solicitar férias?"

Candidatos:

A → Política geral de férias
B → Férias coletivas
C → Prazo para solicitação de férias
D → Aprovação das férias
E → Cancelamento de férias
```

A busca inicial pode considerar vários deles relevantes.

O Reranker recebe cada combinação:

```
Pergunta + Documento A
Pergunta + Documento B
Pergunta + Documento C
Pergunta + Documento D
Pergunta + Documento E
```

e calcula uma pontuação de relevância para cada uma.

Por exemplo:

```
Documento A → 0,72
Documento B → 0,48
Documento C → 0,97
Documento D → 0,61
Documento E → 0,29
```

O ranking passa a ser:

```
1. Documento C → 0,97
2. Documento A → 0,72
3. Documento D → 0,61
4. Documento B → 0,48
5. Documento E → 0,29
```

O sistema pode então selecionar somente os primeiros resultados para construir o contexto do LLM.

Uma característica importante é que o Reranker pode fazer uma avaliação mais detalhada da relação entre a pergunta e o conteúdo.

Por isso, ele pode perceber que:

```
"Política geral de férias"
```

é relacionado ao assunto, mas:

```
"Prazo para solicitação de férias"
```

responde diretamente à pergunta.

Essa diferença entre **relação temática** e **relevância para a consulta específica** é uma das razões para utilizar um Reranker.

## Um exemplo

Imagine uma aplicação RAG para uma empresa.

O usuário pergunta:

```
"Funcionários podem trabalhar remotamente durante viagens?"
```

O Retrieval inicial encontra:

```
1. Política de trabalho remoto
2. Política de viagens
3. Benefícios para trabalho remoto
4. Trabalho remoto durante viagens
5. Segurança para acesso remoto
```

Todos parecem relacionados ao tema.

O Reranker recebe a pergunta e cada candidato:

```
Pergunta + Documento 1 → 0,81
Pergunta + Documento 2 → 0,76
Pergunta + Documento 3 → 0,43
Pergunta + Documento 4 → 0,95
Pergunta + Documento 5 → 0,51
```

Depois da reordenação:

```
1. Trabalho remoto durante viagens
2. Política de trabalho remoto
3. Política de viagens
4. Segurança para acesso remoto
5. Benefícios para trabalho remoto
```

Se o sistema utilizar apenas os três primeiros:

```
Top-3 final
   ↓
Documento 4
Documento 1
Documento 2
   ↓
Contexto
   ↓
LLM
```

O Reranker, portanto, não precisa encontrar documentos em toda a base. Ele normalmente trabalha sobre um **conjunto menor de candidatos que já foi recuperado**.

Isso é importante para manter o custo e o tempo de processamento sob controle.

## Por que é importante

O Reranker é importante porque permite separar duas responsabilidades:

```
Primeira etapa:
"Encontre candidatos rapidamente."

Segunda etapa:
"Analise esses candidatos com mais precisão."
```

Isso é especialmente útil em bases grandes.

Uma arquitetura típica pode ser:

```
                 Base de conhecimento
                         ↓
                 Retrieval inicial
                         ↓
                    Top-k = 20
                         ↓
                      Reranker
                         ↓
                    Top-k = 5
                         ↓
                      Contexto
                         ↓
                        LLM
```

O primeiro mecanismo pode utilizar **Dense Retrieval**, **Sparse Retrieval** ou **Hybrid Search**.

O Reranker então recebe os candidatos e produz uma avaliação mais precisa.

Essa arquitetura também ajuda a entender a relação entre os termos:

|Conceito|O que representa|
|---|---|
|Retrieval|Processo de encontrar informações relevantes|
|Similarity Search|Mecanismo de busca por similaridade|
|Top-k|Quantidade de candidatos selecionados|
|Reranking|Processo de reavaliar e reorganizar candidatos|
|Reranker|Modelo ou componente que executa essa reavaliação|

Um Reranker pode ser baseado em diferentes arquiteturas. Uma abordagem comum é utilizar um modelo que analisa conjuntamente a consulta e o documento, em vez de representar cada um isoladamente como um embedding.

Isso cria uma diferença importante:

```
Embedding para Retrieval:

Pergunta → vetor
Documento → vetor

Comparação entre vetores
        ↓
Similaridade
```

Enquanto um Reranker pode trabalhar assim:

```
Pergunta + Documento
        ↓
Reranker
        ↓
Score de relevância
```

Essa segunda abordagem pode ser mais precisa para determinar se um documento realmente responde à consulta, embora normalmente seja mais custosa computacionalmente.

Por isso, é comum utilizar os dois em sequência:

```
Embedding
   ↓
Retrieval rápido e amplo
   ↓
Candidatos
   ↓
Reranker
   ↓
Avaliação mais precisa
   ↓
Contexto final
   ↓
LLM
```

A ideia central é: **Reranker é o componente que reavalia os resultados recuperados, atribuindo uma pontuação de relevância mais específica à relação entre a consulta e cada candidato, para produzir um conjunto final de informações mais adequado ao LLM.**