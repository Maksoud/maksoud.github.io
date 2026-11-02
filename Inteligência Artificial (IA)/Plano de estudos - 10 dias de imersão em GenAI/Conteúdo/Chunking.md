# Chunking
## O que é

**Chunking** é o processo de dividir um documento ou conteúdo maior em partes menores, chamadas de _chunks_, para que essas partes possam ser processadas, indexadas e recuperadas de forma eficiente por um sistema de RAG.

Um documento pode ter dezenas ou centenas de páginas, mas dificilmente será útil enviar todo esse conteúdo para o modelo a cada pergunta. O chunking cria unidades menores que podem ser associadas a embeddings e posteriormente recuperadas conforme a pergunta do usuário.

No fluxo de ingestão, o chunking normalmente acontece depois do parsing e da limpeza:

```
Fonte
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

O objetivo não é simplesmente cortar o texto em pedaços iguais. Um bom chunk deve preservar, tanto quanto possível, uma unidade de significado.

## Como funciona

Imagine um manual de 100 páginas sobre uma empresa.

Se todo o manual fosse transformado em um único vetor, seria difícil recuperar apenas a informação necessária para responder a uma pergunta específica. Por outro lado, se cada palavra fosse transformada em um chunk separado, perderíamos contexto.

O chunking busca um equilíbrio:

```
Documento completo
        ↓
┌──────────────────────┐
│ Chunk 1              │
│ Introdução           │
│ Objetivo da política │
└──────────────────────┘

┌──────────────────────┐
│ Chunk 2              │
│ Regras de férias     │
│ Prazo para solicitação│
└──────────────────────┘

┌──────────────────────┐
│ Chunk 3              │
│ Aprovação das férias │
│ Responsabilidades    │
└──────────────────────┘
```

Existem diferentes estratégias para definir onde um chunk começa e termina. Ele pode ser dividido por tamanho, número de tokens, parágrafos, seções, títulos ou pela estrutura semântica do documento.

Um aspecto importante é o **contexto**. Um chunk muito pequeno pode perder informações necessárias para compreender uma afirmação. Um chunk muito grande pode conter informações demais e dificultar a recuperação precisa.

Por isso, o tamanho dos chunks é uma decisão importante no projeto de um sistema RAG.

## Um exemplo

Considere um documento com a seguinte política:

```
POLÍTICA DE FÉRIAS

Os funcionários devem solicitar férias com pelo menos
30 dias de antecedência.

A solicitação deve ser realizada pelo sistema interno
e aprovada pelo gestor responsável.

Períodos superiores a 15 dias devem ser previamente
alinhados com o departamento de Recursos Humanos.
```

Uma estratégia de chunking poderia produzir:

```
Chunk 1:
"Os funcionários devem solicitar férias com pelo
menos 30 dias de antecedência."

Chunk 2:
"A solicitação deve ser realizada pelo sistema interno
e aprovada pelo gestor responsável."

Chunk 3:
"Períodos superiores a 15 dias devem ser previamente
alinhados com o departamento de Recursos Humanos."
```

Quando o usuário perguntar:

> "Com quanto tempo preciso solicitar minhas férias?"

O sistema pode transformar a pergunta em um embedding e realizar a busca entre os chunks. O **Chunk 1** provavelmente terá alta similaridade com a pergunta e será recuperado para compor o contexto enviado ao LLM.

Em sistemas reais, porém, os chunks podem ser maiores e podem utilizar **overlap**, mantendo uma pequena quantidade de conteúdo compartilhada entre chunks consecutivos para reduzir a perda de contexto.

## Por que é importante

O chunking influencia diretamente a qualidade do **retrieval** em um sistema RAG.

Um chunk mal definido pode causar problemas como:
- informação importante ficar separada do contexto necessário para entendê-la;
- recuperação de trechos muito genéricos;
- perda de relações entre frases ou elementos de uma tabela;
- excesso de conteúdo irrelevante no contexto do LLM;
- aumento desnecessário do consumo de tokens.

Um chunk bem definido aumenta a chance de o sistema recuperar exatamente a informação necessária para responder à pergunta.

Isso também mostra por que **chunking não é apenas uma etapa técnica de divisão de texto**. Ele é uma decisão sobre como o conhecimento será organizado para posteriormente ser encontrado.

A relação com os conceitos anteriores pode ser resumida assim:

```
Parsing
  ↓
entende e estrutura o documento

Cleaning
  ↓
remove ruídos e normaliza o conteúdo

Chunking
  ↓
divide o conteúdo em unidades recuperáveis

Embedding
  ↓
transforma essas unidades em vetores

Vector Database
  ↓
armazena e permite pesquisar esses vetores

Retrieval
  ↓
encontra os chunks relevantes para a pergunta
```

O ponto central é: **o chunking define, em grande parte, quais unidades de conhecimento estarão disponíveis para o mecanismo de recuperação.**