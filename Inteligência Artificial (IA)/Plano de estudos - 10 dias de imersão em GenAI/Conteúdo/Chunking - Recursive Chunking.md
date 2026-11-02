# Recursive Chunking

## O que é

**Recursive Chunking** é uma estratégia de divisão de documentos que tenta criar chunks respeitando a estrutura do conteúdo, utilizando uma sequência de separadores, do mais amplo para o mais específico.

Em vez de simplesmente cortar o texto quando ele atinge determinado número de tokens, o método tenta primeiro dividir em unidades maiores, como seções ou parágrafos. Se essas unidades ainda forem grandes demais, elas são divididas novamente em unidades menores.

Por isso o nome **recursive**, ou recursivo: o processo de divisão pode ser repetido sobre partes que ainda não atingiram o tamanho desejado.

Uma representação simplificada seria:

```
Documento
   ↓
Seções
   ↓
Parágrafos
   ↓
Frases
   ↓
Palavras
```

A ideia é encontrar o maior nível de estrutura que permita produzir chunks dentro do tamanho definido.

## Como funciona

Imagine um documento com vários capítulos.

Primeiro, o sistema tenta dividir o documento pelos capítulos. Se um capítulo for pequeno o suficiente, ele pode permanecer inteiro.

Se um capítulo for grande demais, o sistema tenta dividi-lo em seções.

Se uma seção ainda for grande demais, tenta dividi-la em parágrafos.

Se um parágrafo ainda exceder o limite, pode finalmente ser dividido em frases ou até em unidades menores.

```
Documento
    │
    ├── Capítulo 1
    │      ├── Seção 1
    │      └── Seção 2
    │
    └── Capítulo 2
           ├── Seção 3
           │      ├── Parágrafo
           │      └── Parágrafo
           │
           └── Seção 4
```

O processo poderia seguir uma hierarquia de separadores como:

```
1. Seções
2. Parágrafos
3. Frases
4. Palavras
5. Caracteres
```

O sistema começa pelo primeiro separador. Se os pedaços resultantes estiverem dentro do limite desejado, eles são utilizados.

Quando um pedaço ainda for grande demais, o processo continua com o próximo separador.

Isso permite que o chunking seja mais sensível à estrutura natural do texto do que o Fixed-size Chunking.

## Um exemplo

Considere um documento com esta estrutura:

```
POLÍTICA DE FÉRIAS

Solicitação de férias

Os funcionários devem solicitar férias com pelo menos
30 dias de antecedência.

Aprovação

A solicitação deve ser realizada pelo sistema interno
e aprovada pelo gestor responsável.

Períodos superiores a 15 dias devem ser previamente
alinhados com o departamento de Recursos Humanos.
```

Imagine que o limite definido seja pequeno demais para manter todo o documento em um único chunk.

O Recursive Chunking pode primeiro tentar separar pelas seções:

```
Chunk 1:
"Solicitação de férias

Os funcionários devem solicitar férias com pelo menos
30 dias de antecedência."

Chunk 2:
"Aprovação

A solicitação deve ser realizada pelo sistema interno
e aprovada pelo gestor responsável.

Períodos superiores a 15 dias devem ser previamente
alinhados com o departamento de Recursos Humanos."
```

Se o segundo chunk ainda for grande demais, ele pode ser dividido novamente:

```
Chunk 2:
"Aprovação

A solicitação deve ser realizada pelo sistema interno
e aprovada pelo gestor responsável."

Chunk 3:
"Períodos superiores a 15 dias devem ser previamente
alinhados com o departamento de Recursos Humanos."
```

Observe que o método tentou preservar a estrutura semântica antes de recorrer a divisões menores.

## Por que é importante

Recursive Chunking é importante porque oferece um equilíbrio entre **controle do tamanho dos chunks** e **preservação da estrutura do documento**.

Em comparação com o Fixed-size Chunking:

```
Fixed-size Chunking
→ divide principalmente pelo tamanho

Recursive Chunking
→ tenta respeitar a estrutura antes de dividir pelo tamanho
```

Isso pode produzir chunks mais coerentes para tarefas de recuperação semântica.

É particularmente útil para documentos que possuem uma estrutura relativamente clara, como:
- manuais;
- políticas internas;
- artigos;
- documentação técnica;
- contratos;
- páginas de conhecimento;
- livros e relatórios.

Ainda assim, Recursive Chunking não entende necessariamente o significado do texto como um ser humano. Ele normalmente trabalha com uma hierarquia de separadores e regras de tamanho. Por isso, não deve ser confundido com **Semantic Chunking**, que utiliza informações semânticas para determinar onde dividir o conteúdo.

A relação entre as estratégias pode ser resumida assim:

```
Chunking
   │
   ├── Fixed-size Chunking
   │      └── divide por tamanho
   │
   ├── Recursive Chunking
   │      └── tenta preservar estrutura hierárquica
   │
   └── Semantic Chunking
          └── tenta preservar unidades de significado
```

No contexto de RAG, essa escolha influencia diretamente quais unidades serão transformadas em embeddings e posteriormente recuperadas.

O ponto central é: **Recursive Chunking divide o conteúdo progressivamente, começando por estruturas maiores e recorrendo a divisões menores apenas quando necessário, buscando manter chunks coerentes sem perder o controle sobre seu tamanho.**