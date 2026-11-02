# Ingestion Cleaning

## O que é

**Ingestion Cleaning**, ou limpeza durante a ingestão, é o conjunto de processos utilizados para **remover, corrigir ou normalizar informações indesejadas ou problemáticas enquanto os dados entram no pipeline de um sistema RAG**.

Depois que um documento é coletado, seu conteúdo nem sempre está pronto para ser utilizado.

Um PDF, por exemplo, pode produzir um texto como:

```
POLÍTICA DE FÉRIAS

Página 1 de 12

Os colaboradores podem solicitar férias...

Página 2 de 12

Os colaboradores devem...
```

Informações como números de página, cabeçalhos repetidos, rodapés, caracteres estranhos e elementos de formatação podem não contribuir para o conhecimento que queremos recuperar.

O Ingestion Cleaning busca transformar esse conteúdo em uma representação mais limpa e consistente:

```
Documento original
      ↓
Extração
      ↓
Cleaning
      ↓
Conteúdo limpo
      ↓
Chunking
      ↓
Embedding
```

O objetivo não é simplesmente deixar o texto "bonito". É **preservar o conteúdo útil e remover ruídos que possam prejudicar as etapas seguintes**.

---

## Como funciona

Imagine que recebemos um documento com:

```
POLÍTICA DE FÉRIAS
Empresa XYZ
Página 1

Os funcionários podem solicitar férias
com 30 dias de antecedência.

Empresa XYZ
Página 2

O período deve ser aprovado pelo gestor.
```

Antes de gerar os embeddings, podemos identificar elementos que não representam informação relevante:

```
Cabeçalho repetido
Rodapé
Número de página
Espaços desnecessários
Caracteres inválidos
```

O conteúdo pode então ser normalizado:

```
Os funcionários podem solicitar férias
com 30 dias de antecedência.

O período deve ser aprovado pelo gestor.
```

O processo pode envolver várias operações:

```
Dados coletados
      ↓
Extração do conteúdo
      ↓
Remoção de ruídos
      ↓
Normalização
      ↓
Correção de problemas de formatação
      ↓
Validação
      ↓
Conteúdo preparado
```

É importante entender que **Cleaning não significa remover tudo que parece desnecessário**.

Uma informação aparentemente pequena pode ser importante para o significado.

Por exemplo:

```
"Prazo: 30 dias"
```

não deve ser transformado em:

```
"30"
```

Da mesma forma, uma estrutura como:

```
Benefício: Plano de saúde
Elegibilidade: Funcionários efetivos
```

pode precisar ser preservada porque a relação entre as informações é relevante.

Por isso, o objetivo do cleaning é **reduzir ruído sem destruir contexto**.

---

## Um exemplo

Imagine que um sistema RAG receba um PDF contendo uma política de reembolso.

A extração produz:

```
POLÍTICA DE REEMBOLSO
EMPRESA XYZ
Página 1

1. OBJETIVO

Esta política estabelece as regras para reembolso.

EMPRESA XYZ | CONFIDENCIAL
Página 2

2. DESPESAS ELEGÍVEIS

São elegíveis despesas relacionadas a viagens corporativas.

EMPRESA XYZ | CONFIDENCIAL
Página 3
```

Durante o cleaning, podemos remover elementos repetitivos:

```
EMPRESA XYZ
Página 1
EMPRESA XYZ | CONFIDENCIAL
Página 2
EMPRESA XYZ | CONFIDENCIAL
Página 3
```

Preservando o conteúdo:

```
1. OBJETIVO

Esta política estabelece as regras para reembolso.

2. DESPESAS ELEGÍVEIS

São elegíveis despesas relacionadas a viagens corporativas.
```

Depois disso, o texto pode seguir para o restante do pipeline:

```
Texto limpo
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
```

Agora imagine que o usuário pergunte:

```
"Quais despesas podem ser reembolsadas?"
```

Se o documento tiver sido corretamente ingerido e limpo, o sistema terá maior chance de recuperar o trecho relevante.

Por outro lado, se a extração tiver produzido algo como:

```
EMPRESA XYZ Página 2 CONFIDENCIAL
2. DESPESAS ELEGÍVEIS São elegíveis despesas...
```

o sistema ainda pode funcionar, mas o ruído pode prejudicar a qualidade do conteúdo, especialmente quando ocorre em grande escala.

---

## Por que é importante

Ingestion Cleaning é importante porque **a qualidade dos dados que entram no RAG influencia diretamente a qualidade das etapas posteriores**.

Um pipeline pode ter excelentes embeddings e uma ótima Vector Database, mas se o conteúdo original estiver cheio de ruídos, informações duplicadas ou problemas de extração, a recuperação poderá ser prejudicada.

O cleaning pode ajudar a:
- Remover cabeçalhos e rodapés repetitivos.
- Eliminar caracteres inválidos.
- Corrigir problemas de codificação.
- Normalizar espaços e quebras de linha.
- Remover conteúdo claramente irrelevante.
- Tratar documentos duplicados.
- Padronizar formatos.
- Preservar estruturas importantes do conteúdo.

Mas existe um cuidado importante: **limpeza excessiva também pode prejudicar o RAG**.

Se removermos informações relevantes, podemos alterar o significado do documento.

Por exemplo:

```
Antes:
"O reembolso deve ser solicitado em até 30 dias
após a realização da despesa."

Depois de uma limpeza inadequada:
"O reembolso deve ser solicitado após a realização
da despesa."
```

A informação sobre os **30 dias** desapareceu.

O texto parece mais limpo, mas o conhecimento ficou pior.

Por isso, Ingestion Cleaning deve buscar um equilíbrio:

```
Dados brutos
     ↓
Remover ruído
     ↓
Preservar significado
     ↓
Normalizar estrutura
     ↓
Dados confiáveis
```

Também é importante diferenciar **Cleaning** de **Chunking**.

**Cleaning** prepara e limpa o conteúdo.

**Chunking** divide o conteúdo em unidades menores para facilitar sua recuperação.

A sequência normalmente é:

```
Fonte
  ↓
Ingestion
  ↓
Extraction
  ↓
Cleaning
  ↓
Chunking
  ↓
Embedding
  ↓
Vector Database
```

Essa ordem não é obrigatória em todos os sistemas, pois pipelines reais podem ter etapas adicionais ou diferentes, mas ela representa bem a lógica geral.

A ideia central é: **Ingestion Cleaning prepara o conteúdo coletado para as etapas seguintes do RAG, removendo ruídos e problemas de formatação sem eliminar informações necessárias para preservar o significado original.**