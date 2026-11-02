[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Chunk Size

## O que é

Chunk Size é o tamanho definido para cada chunk durante o processo de Chunking de um documento.

Em sistemas RAG, um documento geralmente é dividido em partes menores antes de ser transformado em embedding e armazenado para Retrieval. O Chunk Size determina aproximadamente quanto conteúdo cada uma dessas partes deve conter.

Dependendo da implementação, o tamanho pode ser definido em:
- tokens;
- caracteres;
- palavras;
- sentenças ou outros critérios estruturais.

Em sistemas baseados em LLMs, tokens são uma unidade particularmente comum, porque representam a forma como os modelos processam texto.

Por exemplo, um documento pode ser dividido assim:

```
Documento original
        ↓
┌──────────────────┐
│ Chunk 1          │
│ 500 tokens       │
└──────────────────┘
        ↓
┌──────────────────┐
│ Chunk 2          │
│ 500 tokens       │
└──────────────────┘
        ↓
┌──────────────────┐
│ Chunk 3          │
│ 500 tokens       │
└──────────────────┘
```

Chunk Size não deve ser confundido com Chunk Overlap. O primeiro define o tamanho aproximado de cada chunk. O segundo determina quanto conteúdo pode ser compartilhado entre chunks consecutivos.

## Como funciona

Durante o Chunking, o sistema recebe um documento e aplica uma estratégia para dividi-lo em unidades menores.

De forma simplificada:

```
Documento
    ↓
Estratégia de Chunking
    ↓
Definição do Chunk Size
    ↓
Chunks
    ↓
Embeddings
    ↓
Indexing
```

Imagine um documento com 2.000 tokens e um Chunk Size de 500 tokens:

```
Documento: 2.000 tokens

[ 1 ───────── 500 ]
[ 501 ─────── 1000 ]
[ 1001 ────── 1500 ]
[ 1501 ────── 2000 ]
```

Nesse caso, o sistema produziria aproximadamente quatro chunks.

Porém, um Chunk Size de 500 não significa necessariamente que todos os chunks terão exatamente 500 tokens. Estratégias como Recursive Chunking ou Semantic Chunking podem respeitar limites estruturais do documento.

Por exemplo, se uma seção termina antes do limite:

```
Seção 1
    ↓
Seção 2
    ↓
Seção 3
```

o algoritmo pode preferir preservar essas estruturas em vez de simplesmente cortar o texto em posições fixas.

A escolha do Chunk Size cria um equilíbrio importante.

Chunks muito pequenos podem perder contexto:

```
"Esse prazo é de 30 dias."
```

Sem o conteúdo anterior, não fica claro a que "esse prazo" se refere.

Chunks muito grandes preservam mais contexto, mas podem trazer informações irrelevantes junto com a informação procurada:

```
Chunk grande
├── Introdução
├── Histórico
├── Regras
├── Exceções
├── Exemplos
└── Conclusão
```

Isso pode dificultar o Retrieval e aumentar a quantidade de tokens enviada à LLM.

Por isso, Chunk Size não possui um valor universalmente correto. Ele deve ser ajustado de acordo com o tipo de documento, a estratégia de Chunking, o modelo de embedding, o mecanismo de Retrieval e o objetivo do sistema RAG.

## Um exemplo

Imagine uma empresa que possui um manual interno de 100 páginas sobre políticas de recursos humanos.

O sistema precisa responder perguntas como:

```
"Quantos dias de férias um funcionário pode converter em abono?"
```

Se o Chunk Size for muito pequeno, a informação pode ser separada de seu contexto:

```
Chunk 1:
"Funcionários podem solicitar a conversão..."

Chunk 2:
"de até 10 dias do período de férias..."
```

Dependendo da estratégia utilizada, o segundo chunk pode não conter informações suficientes para ser recuperado adequadamente.

Com um Chunk Size maior, a informação pode permanecer contextualizada:

```
Chunk:
"Funcionários podem solicitar a conversão de até
10 dias do período de férias em abono pecuniário,
desde que a solicitação seja realizada dentro do prazo
estabelecido pela política."
```

O fluxo completo seria:

```
Manual de RH
    ↓
Chunking
    ↓
Chunks com tamanho adequado
    ↓
Embedding
    ↓
Indexing
    ↓
Retrieval
    ↓
Reranking
    ↓
Contexto
    ↓
LLM
    ↓
Resposta
```

Agora imagine que o sistema utilize chunks muito grandes. Uma pergunta específica sobre férias poderia recuperar um chunk contendo várias páginas de políticas diferentes. O documento seria relevante, mas grande parte do conteúdo poderia ser desnecessária para a resposta.

Por isso, o objetivo não é simplesmente criar chunks grandes ou pequenos. O objetivo é criar unidades que contenham **informação suficientemente completa para serem recuperadas individualmente**, sem carregar contexto excessivo.

## Por que é importante

Chunk Size influencia diretamente a qualidade de várias etapas do RAG.

Um tamanho inadequado pode prejudicar o sistema de diferentes formas:

```
Chunk Size muito pequeno
        ↓
Menos contexto
        ↓
Possível perda de significado
        ↓
Retrieval menos eficaz

Chunk Size muito grande
        ↓
Mais conteúdo por resultado
        ↓
Mais informação irrelevante
        ↓
Contexto maior
        ↓
Maior custo e possível perda de precisão
```

Isso faz com que Chunk Size seja uma das decisões mais importantes durante a preparação dos documentos para RAG.

Ele também precisa ser analisado junto com Chunk Overlap e a estratégia utilizada para dividir o documento:

```
Chunking
   ├── Chunk Size
   ├── Chunk Overlap
   ├── Fixed-size Chunking
   ├── Recursive Chunking
   └── Semantic Chunking
        ↓
Chunks
        ↓
Embedding
        ↓
Indexing
        ↓
Retrieval
```

Uma forma prática de pensar no problema é: **cada chunk deve ser grande o suficiente para preservar o contexto necessário, mas pequeno o suficiente para representar uma unidade de informação útil para o Retrieval**.

Por isso, em projetos reais, o Chunk Size costuma ser tratado como um parâmetro que precisa ser testado e ajustado empiricamente. Não basta escolher um tamanho considerado "padrão". O melhor valor depende dos documentos e das perguntas que o sistema precisa responder.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-chunk-size/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
