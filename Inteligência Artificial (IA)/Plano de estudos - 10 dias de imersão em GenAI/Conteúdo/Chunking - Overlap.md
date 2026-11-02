# Chunking Overlap

## O que é

**Chunking Overlap** é a técnica de repetir uma parte do conteúdo no início de um chunk e no final do chunk anterior.

O objetivo é evitar que uma informação importante seja perdida quando uma divisão acontece justamente entre duas partes relacionadas do texto.

Por exemplo, sem overlap:

```
Chunk 1:
"A empresa permite solicitar férias com até"

Chunk 2:
"30 dias de antecedência."
```

A informação ficou dividida entre os dois chunks.

Com overlap:

```
Chunk 1:
"A empresa permite solicitar férias com até 30 dias"

Chunk 2:
"com até 30 dias de antecedência. A solicitação deve..."
```

A parte compartilhada cria uma continuidade entre os chunks.

## Como funciona, de forma intuitiva

Imagine que você está cortando um texto em páginas, mas deixa algumas linhas repetidas no início da página seguinte.

```
Chunk 1
┌──────────────────────────────┐
│ Informação A                 │
│ Informação B                 │
│ Informação C                 │
│ Informação D                 │
└──────────────────────────────┘
             ↓
           overlap
             ↓
Chunk 2
┌──────────────────────────────┐
│ Informação C                 │
│ Informação D                 │
│ Informação E                 │
│ Informação F                 │
└──────────────────────────────┘
```

Nesse exemplo, as informações C e D aparecem nos dois chunks.

Esse pequeno trecho compartilhado ajuda a preservar o contexto quando uma ideia atravessa a fronteira entre dois chunks.

O tamanho do overlap é normalmente definido como uma quantidade de tokens ou caracteres.

Por exemplo:

```
Chunk size = 500 tokens
Overlap = 50 tokens
```

Nesse caso, cada novo chunk reutiliza aproximadamente os últimos 50 tokens do chunk anterior.

O overlap não significa que os chunks devem ser iguais. A maior parte de cada chunk continua sendo conteúdo novo.

## Um exemplo

Considere o seguinte texto:

```
A empresa permite que funcionários solicitem férias
com pelo menos 30 dias de antecedência. A solicitação
deve ser realizada pelo sistema interno e aprovada
pelo gestor responsável.
```

Suponha que o sistema utilize chunks pequenos.

Sem overlap, poderíamos ter:

```
Chunk 1:
"A empresa permite que funcionários solicitem férias
com pelo menos"

Chunk 2:
"30 dias de antecedência. A solicitação deve ser realizada"

Chunk 3:
"pelo sistema interno e aprovada pelo gestor responsável."
```

A informação sobre o prazo ficou separada. Além disso, o Chunk 1 termina antes de completar a ideia.

Com overlap:

```
Chunk 1:
"A empresa permite que funcionários solicitem férias
com pelo menos 30 dias de antecedência."

Chunk 2:
"com pelo menos 30 dias de antecedência. A solicitação
deve ser realizada pelo sistema interno"

Chunk 3:
"deve ser realizada pelo sistema interno e aprovada
pelo gestor responsável."
```

Agora existe uma pequena continuidade entre os chunks.

Se uma pergunta estiver relacionada ao prazo para solicitar férias, o sistema tem maior chance de recuperar um chunk que contenha a informação completa.

## Por que é importante

O overlap é importante porque **reduz a perda de contexto causada pelas fronteiras entre chunks**.

Sem overlap, uma informação pode ser dividida de maneira desfavorável:

```
Ideia completa
      ↓
[parte 1] | [parte 2]
           ↑
       fronteira
```

Com overlap:

```
Ideia completa
      ↓
[parte 1 + contexto] | [contexto + parte 2]
                       ↑
                    overlap
```

Isso pode melhorar a recuperação em documentos nos quais as informações dependem bastante do contexto anterior.

Porém, aumentar o overlap indefinidamente não melhora necessariamente o RAG. Um overlap muito grande produz muita informação repetida, aumentando:
- quantidade de chunks;
- espaço de armazenamento;
- quantidade de embeddings;
- custo de processamento;
- quantidade de conteúdo recuperado;
- consumo de tokens no contexto do LLM.

Por isso, o tamanho do chunk e o tamanho do overlap precisam ser definidos em conjunto.

Uma forma simples de visualizar essa relação é:

```
Chunk pequeno
    +
Overlap maior
    ↓
Mais contexto, mas mais repetição

Chunk grande
    +
Overlap pequeno
    ↓
Menos repetição, mas chunks potencialmente menos precisos
```

O overlap também não substitui estratégias melhores de chunking. Se o documento possui uma estrutura clara, dividir por seções, títulos ou unidades semânticas pode ser mais adequado do que simplesmente aumentar o overlap.

A relação com os conceitos anteriores fica assim:

```
Chunking
   ↓
divide o documento

Fixed-size Chunking
   ↓
define chunks por tamanho

Chunking Overlap
   ↓
mantém parte do conteúdo entre chunks consecutivos

Metadata
   ↓
adiciona informações estruturadas aos chunks

Embedding
   ↓
transforma os chunks em vetores
```

O ponto central é: **Chunking Overlap mantém uma pequena parte do contexto entre chunks consecutivos, reduzindo o risco de que informações relacionadas sejam separadas de forma prejudicial durante a divisão do documento.**