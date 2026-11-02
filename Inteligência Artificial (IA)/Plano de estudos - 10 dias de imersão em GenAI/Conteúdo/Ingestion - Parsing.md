[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Ingestion Parsing

## O que é

**Ingestion Parsing**, ou parsing durante a ingestão, é o processo de **interpretar e transformar os dados brutos de uma fonte em uma estrutura que o sistema consiga compreender e processar**.

Quando um arquivo entra em um pipeline RAG, ele não necessariamente está disponível como texto estruturado.

Um PDF, por exemplo, pode conter:

```
Texto
Títulos
Parágrafos
Tabelas
Listas
Imagens
Cabeçalhos
Rodapés
```

O parser precisa identificar esses elementos e transformar o conteúdo em uma representação estruturada.

Por exemplo:

```
PDF
 ↓
Parsing
 ↓
Título
Parágrafos
Tabela
Metadados
```

Isso é diferente de simplesmente extrair todos os caracteres do arquivo. O parsing busca entender **como o conteúdo está organizado**.

---

## Como funciona

Imagine um documento como uma página visual:

```
POLÍTICA DE FÉRIAS

1. Solicitação

Os funcionários devem solicitar férias
com antecedência mínima de 30 dias.

Prazo | Responsável
30 dias | Funcionário
```

Para uma pessoa, é relativamente fácil perceber que:

```
"POLÍTICA DE FÉRIAS" → título

"1. Solicitação" → seção

"Os funcionários..." → parágrafo

"Prazo | Responsável" → tabela
```

Para um sistema, essas informações precisam ser identificadas e estruturadas.

O parsing faz justamente essa interpretação:

```
Documento
   ↓
Parser
   ↓
Estrutura identificada
   ├── Título
   ├── Seção
   ├── Parágrafo
   └── Tabela
```

Depois disso, o conteúdo pode passar por etapas como cleaning e chunking:

```
Documento
   ↓
Parsing
   ↓
Estruturação
   ↓
Cleaning
   ↓
Chunking
   ↓
Embedding
   ↓
Vector Database
```

O parsing pode variar bastante dependendo do formato da fonte.

Para um arquivo de texto simples, o processo pode ser relativamente fácil.

Para um PDF complexo, pode ser necessário identificar:
- Texto
- Títulos
- Parágrafos
- Tabelas
- Listas
- Colunas
- Cabeçalhos
- Rodapés
- Imagens
- Metadados

Em documentos digitalizados, pode ser necessário utilizar **OCR**, que transforma texto presente em imagens em texto que o sistema consegue processar.

---

## Um exemplo

Imagine que recebemos um PDF com uma política de reembolso:

```
POLÍTICA DE REEMBOLSO

1. Despesas elegíveis

São elegíveis despesas relacionadas
a viagens corporativas.

Categoria       Limite
Hospedagem      R$ 500
Alimentação     R$ 150
```

Um parser pode transformar essa informação em uma estrutura semelhante a:

```
Documento
├── Título
│   └── Política de Reembolso
│
├── Seção
│   └── Despesas elegíveis
│
├── Parágrafo
│   └── São elegíveis despesas relacionadas
│       a viagens corporativas.
│
└── Tabela
    ├── Hospedagem → R$ 500
    └── Alimentação → R$ 150
```

Essa estrutura é muito mais útil para o restante do pipeline.

Imagine que simplesmente extraíssemos os caracteres do PDF:

```
POLÍTICA DE REEMBOLSO
1. Despesas elegíveis
São elegíveis despesas relacionadas...
Hospedagem R$ 500 Alimentação R$ 150
```

Nesse processo, a relação entre as colunas da tabela pode ser perdida.

O parser, quando capaz de reconhecer a estrutura, pode preservar essa relação:

```
Hospedagem → limite: R$ 500
Alimentação → limite: R$ 150
```

Isso é especialmente importante para RAG porque o sistema posteriormente poderá recuperar essas informações de maneira mais confiável.

Depois do parsing:

```
Parsing
   ↓
Conteúdo estruturado
   ↓
Cleaning
   ↓
Chunking
   ↓
Embedding
   ↓
Vector Database
```

Se um usuário perguntar:

```
"Qual é o limite para hospedagem?"
```

a informação relevante poderá ser recuperada preservando a associação entre **hospedagem** e **R$ 500**.

---

## Por que é importante

O parsing é importante porque **dados mal interpretados na entrada podem comprometer todas as etapas posteriores do RAG**.

Se uma tabela for transformada incorretamente em texto, por exemplo, o embedding será gerado sobre uma representação que pode ter perdido relações importantes.

O mesmo pode acontecer com:
- Títulos separados de seus conteúdos.
- Colunas de PDF misturadas.
- Listas desorganizadas.
- Cabeçalhos incorporados ao texto.
- Notas de rodapé confundidas com o conteúdo principal.
- Metadados perdidos.
- Texto de imagens não identificado.

Por isso, parsing é especialmente importante quando trabalhamos com documentos complexos.

Também é importante diferenciar **Parsing** de **Cleaning**.

**Parsing** procura entender e estruturar o conteúdo.

**Cleaning** procura remover ruídos e normalizar o conteúdo.

Por exemplo:

```
PDF
 ↓
Parsing
 ↓
Identifica:
título, parágrafos, tabela
 ↓
Cleaning
 ↓
Remove:
rodapés, caracteres inválidos, repetições
 ↓
Chunking
```

Podemos relacionar os conceitos que estamos estudando no pipeline de ingestion:

```
Fonte de dados
      ↓
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
Vector Database
```

Essa sequência ajuda a entender uma distinção importante:

**Ingestion** é o processo mais amplo de trazer os dados para o pipeline.

**Parsing** interpreta e estrutura os dados.

**Cleaning** remove ruídos e normaliza o conteúdo.

**Chunking** divide o conteúdo em unidades adequadas para recuperação.

**Embedding** transforma essas unidades em representações vetoriais.

A ideia central é: **Ingestion Parsing é a etapa que interpreta os dados recebidos e transforma sua estrutura original em uma representação que o pipeline de RAG consiga processar, preservando relações importantes entre os elementos do conteúdo.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/ingestion-parsing/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
