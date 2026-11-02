[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Cross Encoder

## O que é

Cross Encoder é uma arquitetura de modelo usada para calcular a relevância entre uma consulta e um documento, analisando os dois textos conjuntamente.

No contexto de RAG, ele é frequentemente utilizado como **Reranker**. Depois que o Retrieval recupera um conjunto de candidatos, o Cross Encoder analisa cada par formado pela consulta e por um documento e atribui uma pontuação de relevância.

A principal diferença em relação ao modelo usado para gerar embeddings é a forma como os textos são processados.

Em um modelo de embeddings, a consulta e o documento são normalmente transformados em vetores separadamente:

```
Consulta ──────→ Embedding da consulta
                         ↓
                    Similaridade
                         ↑
Documento ─────→ Embedding do documento
```

No Cross Encoder, os dois são enviados juntos ao modelo:

```
Consulta + Documento
        ↓
   Cross Encoder
        ↓
Score de relevância
```

Isso permite que o modelo analise diretamente a relação entre os dois textos, considerando palavras, contexto e interações entre eles.

## Como funciona

Imagine que o Retrieval inicial tenha encontrado 20 documentos para uma pergunta. Esses documentos são candidatos, mas ainda não estão necessariamente na melhor ordem.

O Cross Encoder recebe a consulta junto com cada candidato:

```
Consulta
   +
Documento 1
   ↓
Cross Encoder
   ↓
Score: 0.92

Consulta
   +
Documento 2
   ↓
Cross Encoder
   ↓
Score: 0.37

Consulta
   +
Documento 3
   ↓
Cross Encoder
   ↓
Score: 0.81
```

Depois, os documentos são reorganizados de acordo com seus scores:

```
Documentos recuperados
        ↓
Cross Encoder
        ↓
Cálculo de relevância
        ↓
Ranking atualizado
        ↓
Top-k final
```

O ponto importante é que o Cross Encoder não precisa simplesmente verificar se consulta e documento são semanticamente próximos. Ele pode analisar a relação entre os dois textos de maneira mais detalhada.

Por exemplo, considere a pergunta:

```
"Qual é o prazo para cancelar um contrato após a assinatura?"
```

E dois documentos:

```
Documento A:
"Contratos podem ser cancelados em até 7 dias após a assinatura."

Documento B:
"Contratos empresariais possuem prazo de renovação anual."
```

Ambos podem conter termos relacionados a contratos e prazos. Porém, o Cross Encoder consegue analisar a relação entre a pergunta e cada documento e tende a atribuir uma pontuação maior ao Documento A.

Isso torna o Cross Encoder especialmente útil depois do Retrieval inicial.

```
Consulta
   ↓
Retrieval
   ↓
Top-k candidatos
   ↓
Cross Encoder
   ↓
Reranking
   ↓
Top-k final
   ↓
Contexto
   ↓
LLM
```

Existe, porém, um custo computacional maior. Como cada consulta precisa ser analisada junto com cada documento candidato, executar o modelo sobre milhares ou milhões de documentos seria muito caro.

Por isso, a arquitetura normalmente utiliza um primeiro estágio mais rápido para reduzir o conjunto de candidatos. O Cross Encoder atua somente sobre esse conjunto menor.

```
Milhões de documentos
        ↓
Retrieval rápido
        ↓
50 candidatos
        ↓
Cross Encoder
        ↓
10 documentos mais relevantes
        ↓
LLM
```

## Um exemplo

Imagine um assistente corporativo que responde perguntas sobre políticas internas.

O usuário pergunta:

```
"Funcionários podem trabalhar remotamente durante viagens internacionais?"
```

O Retrieval inicial encontra 5 documentos:

```
D1: Política de trabalho remoto
D2: Política de viagens internacionais
D3: Política de segurança da informação
D4: Benefícios para funcionários
D5: Política de trabalho híbrido
```

A primeira etapa pode recuperar todos esses documentos porque eles possuem alguma relação com os termos da consulta.

O Cross Encoder então analisa cada par:

```
Pergunta + D1 → Score 0.89
Pergunta + D2 → Score 0.94
Pergunta + D3 → Score 0.51
Pergunta + D4 → Score 0.22
Pergunta + D5 → Score 0.73
```

O ranking passa a ser:

```
D2 → 0.94
D1 → 0.89
D5 → 0.73
D3 → 0.51
D4 → 0.22
```

O sistema pode então selecionar os documentos mais relevantes:

```
Retrieval
   ↓
D1, D2, D3, D4, D5
   ↓
Cross Encoder
   ↓
D2, D1, D5
   ↓
Contexto
   ↓
LLM
   ↓
Resposta
```

O Cross Encoder, portanto, não substitui necessariamente o Retrieval. Ele melhora a ordenação dos resultados que já foram recuperados.

## Por que é importante

Cross Encoder é importante porque existe uma diferença entre **encontrar documentos potencialmente relevantes** e **determinar quais deles são realmente os mais relevantes para aquela consulta**.

O Retrieval inicial precisa ser rápido e capaz de trabalhar com uma coleção grande. O Cross Encoder pode ser mais lento porque realiza uma análise mais detalhada da relação entre consulta e documento.

Isso cria uma arquitetura de dois estágios:

```
                 Consulta
                    ↓
             Retrieval inicial
                    ↓
             Muitos candidatos
                    ↓
              Cross Encoder
                    ↓
                Reranking
                    ↓
             Poucos resultados
                    ↓
                 Contexto
                    ↓
                   LLM
```

Essa separação é importante para sistemas RAG porque permite combinar **velocidade na recuperação** com **maior precisão na ordenação**.

Também ajuda a entender a relação entre os conceitos estudados:

```
Similarity Search
        ↓
Top-k inicial
        ↓
Reranker
        ↓
Cross Encoder
        ↓
Reranking
        ↓
Top-k final
        ↓
Contexto
        ↓
LLM
```

Aqui, **Reranking** é o processo de reorganizar os resultados, **Reranker** é o componente responsável por realizar esse processo, e **Cross Encoder** é uma das arquiteturas que pode ser utilizada para construir esse componente.

Essa distinção é importante porque nem todo Reranker precisa ser um Cross Encoder. O Cross Encoder é uma abordagem particularmente relevante quando o objetivo é obter uma avaliação mais detalhada da relevância entre uma consulta e cada documento candidato.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/reranking-cross-encoder/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
