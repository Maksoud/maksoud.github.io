[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Context Compression

## O que é

Context Compression, ou compressão de contexto, é uma técnica de RAG que reduz o conteúdo recuperado antes de enviá-lo para a LLM, mantendo principalmente as informações relevantes para responder à consulta.

Em um pipeline tradicional, o Retrieval pode encontrar documentos relevantes, mas esses documentos podem conter muito conteúdo desnecessário. Context Compression tenta remover esse excesso.

```
Retrieval
   ↓
Documentos relevantes
   ↓
Context Compression
   ↓
Contexto relevante e menor
   ↓
LLM
```

A ideia não é simplesmente diminuir o tamanho do texto. O objetivo é **reduzir o volume de informação sem perder aquilo que é necessário para responder à pergunta**.

Por isso, Context Compression é diferente de simplesmente utilizar um Chunk Size menor. Chunk Size define como os documentos são divididos durante a preparação dos dados. Context Compression acontece posteriormente, durante o fluxo de Retrieval.

## Como funciona

Depois que o Retrieval recupera os documentos, um componente de compressão analisa o conteúdo em relação à consulta e identifica quais partes são realmente úteis.

Um fluxo simplificado é:

```
Pergunta
   ↓
Retrieval
   ↓
Top-k documentos
   ↓
Análise de relevância
   ↓
Remoção ou redução de conteúdo irrelevante
   ↓
Contexto comprimido
   ↓
LLM
```

Imagine que o Retrieval encontre um documento com 2.000 tokens, mas apenas um parágrafo contenha a informação necessária.

Sem compressão:

```
Documento
├── Introdução
├── Histórico
├── Definições
├── Regras
├── Exceções
├── Exemplos
├── Informação relevante
└── Conclusão

        ↓

LLM recebe todo o documento
```

Com Context Compression:

```
Documento
        ↓
Identificação do conteúdo relevante
        ↓
Trecho relevante
        ↓
LLM
```

A compressão pode ser realizada de diferentes maneiras. Uma abordagem pode selecionar apenas determinados trechos ou sentenças. Outra pode utilizar um modelo para extrair somente as informações relevantes. Também pode haver uma combinação de seleção, filtragem e redução do conteúdo.

Um ponto importante é que a compressão deve ser feita **em relação à consulta**. O mesmo documento pode ser comprimido de maneiras diferentes dependendo da pergunta.

Por exemplo:

```
Documento:
Política de viagens corporativas

Pergunta A:
"Qual é o limite de hospedagem?"

        ↓

Contexto comprimido:
Informações sobre limite de hospedagem


Pergunta B:
"Quais documentos são necessários para solicitar reembolso?"

        ↓

Contexto comprimido:
Informações sobre documentação para reembolso
```

O documento original é o mesmo, mas o conteúdo considerado relevante muda conforme a consulta.

## Um exemplo

Imagine um sistema RAG corporativo utilizado para consultar políticas internas.

O usuário pergunta:

```
"Qual é o prazo para solicitar o reembolso de uma viagem?"
```

O Retrieval encontra três documentos:

```
D1: Política de viagens
D2: Política de reembolso
D3: Manual de despesas corporativas
```

Cada documento possui muitas informações:

```
D1
├── Passagens
├── Hospedagem
├── Transporte
├── Reembolso
├── Viagens internacionais
└── Segurança

D2
├── Elegibilidade
├── Documentação
├── Prazos
├── Valores
├── Exceções
└── Aprovação

D3
├── Cartão corporativo
├── Compras
├── Despesas
├── Reembolso
└── Auditoria
```

Enviar tudo para a LLM pode desperdiçar espaço no contexto.

Um processo de Context Compression poderia produzir:

```
D1 → trecho sobre reembolso
D2 → trecho sobre prazo de solicitação
D3 → trecho sobre regras de reembolso
```

O contexto final seria:

```
Contexto comprimido
        ↓
Informações sobre reembolso
        ↓
Prazo para solicitação
        ↓
Exceções relacionadas
        ↓
LLM
        ↓
Resposta
```

O fluxo completo poderia ser:

```
Pergunta
   ↓
Retrieval
   ↓
Top-k documentos
   ↓
Reranking
   ↓
Context Compression
   ↓
Contexto final
   ↓
LLM
```

Observe que Context Compression pode ser utilizado depois do Reranking. Primeiro o sistema identifica os candidatos mais relevantes e depois reduz o conteúdo desses candidatos para fornecer à LLM apenas aquilo que importa.

## Por que é importante

Context Compression é importante porque recuperar informação relevante não significa que todo o conteúdo recuperado seja necessário.

Em sistemas RAG, enviar contexto excessivo pode aumentar:
- custo de inferência;
- quantidade de tokens processados;
- latência;
- possibilidade de informações irrelevantes influenciarem a resposta;
- dificuldade da LLM em identificar a informação mais importante.

Podemos visualizar o problema assim:

```
Sem compressão:

Retrieval
   ↓
10 documentos
   ↓
Muito conteúdo
   ↓
LLM


Com compressão:

Retrieval
   ↓
10 documentos
   ↓
Reranking
   ↓
Conteúdo relevante
   ↓
Context Compression
   ↓
Contexto menor
   ↓
LLM
```

Isso cria uma distinção importante entre **selecionar documentos** e **selecionar informações dentro dos documentos**.

O Reranking pode determinar:

```
"Quais documentos são mais relevantes?"
```

Enquanto Context Compression pode determinar:

```
"Quais partes desses documentos são relevantes para esta pergunta?"
```

Essa diferença é especialmente útil quando os documentos são grandes ou quando o Retrieval retorna chunks que ainda contêm bastante informação desnecessária.

Context Compression também se relaciona diretamente com o conceito de Context Window. Mesmo que uma LLM tenha capacidade para receber uma grande quantidade de tokens, isso não significa que seja desejável enviar tudo o que foi recuperado.

O objetivo de um bom pipeline RAG não é simplesmente colocar o máximo possível de informação no contexto. É fornecer **a informação mais relevante, suficiente e bem contextualizada para que a LLM produza uma resposta correta**.

```
Retrieval
   ↓
Encontrar informação relevante
   ↓
Reranking
   ↓
Priorizar os melhores resultados
   ↓
Context Compression
   ↓
Reduzir o excesso
   ↓
Contexto
   ↓
LLM
```

Assim, Context Compression funciona como uma etapa de refinamento entre o Retrieval e a geração da resposta, ajudando a transformar um conjunto de documentos potencialmente relevantes em um contexto mais enxuto e focado.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-context-compression/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
