[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Contextual Retrieval

## O que é

Contextual Retrieval é uma técnica de RAG que busca **preservar o contexto de um chunk antes de indexá-lo**, tornando o conteúdo recuperável mais compreensível e específico.

O problema surge porque o Chunking normalmente separa um documento em partes menores. Um chunk pode conter uma informação perfeitamente compreensível dentro do documento original, mas ambígua quando analisada isoladamente.

Por exemplo, um documento pode conter:

```
Documento: Política de Reembolso da Empresa X

Seção 4. Reembolso de despesas

O colaborador deverá solicitar o reembolso em até 30 dias.
```

Depois do Chunking, podemos acabar com:

```
"O colaborador deverá solicitar o reembolso em até 30 dias."
```

O problema é que esse trecho não informa explicitamente **qual reembolso**, **de qual empresa** ou **em qual contexto**.

O Contextual Retrieval procura adicionar ao chunk informações contextuais antes de gerar seu embedding e armazená-lo para Retrieval.

O resultado poderia ser:

```
Contexto:
Política de Reembolso da Empresa X.
Seção 4, Reembolso de despesas.

Chunk:
O colaborador deverá solicitar o reembolso em até 30 dias.
```

O embedding passa então a representar não apenas a frase isolada, mas uma informação contextualizada.

É importante distinguir Contextual Retrieval de Contextual Relevance. **Contextual Retrieval é uma técnica aplicada antes e durante a indexação para melhorar a recuperação. Contextual Relevance é uma avaliação de quanto o contexto recuperado é relevante para uma consulta.**

## Como funciona

O processo tradicional pode ser representado assim:

```
Documento
↓
Chunking
↓
Chunks
↓
Embedding
↓
Indexação
↓
Retrieval
```

No Contextual Retrieval, existe uma etapa adicional entre o Chunking e o Embedding:

```
Documento
↓
Chunking
↓
Chunks
↓
Adicionar contexto ao chunk
↓
Embedding
↓
Indexação
↓
Retrieval
```

O contexto pode incluir informações como o título do documento, seção, assunto, entidade à qual o conteúdo pertence ou informações necessárias para compreender aquele trecho.

Por exemplo, considere este chunk:

```
"Ele deve ser renovado a cada 12 meses."
```

Isoladamente, existem muitas interpretações possíveis.

Com contexto:

```
Contexto:
Contrato de manutenção do sistema ERP.
Seção: Renovação contratual.

Chunk:
Ele deve ser renovado a cada 12 meses.
```

Agora o conteúdo possui muito mais informação semântica.

Em implementações mais sofisticadas, um LLM pode receber o documento original e o chunk e gerar uma pequena descrição contextual:

```
Documento original
       ↓
      LLM
       ↓
Contexto específico do chunk
       ↓
Chunk + contexto
       ↓
Embedding
       ↓
Vector Database
```

O texto contextualizado pode ser armazenado junto ao chunk original ou utilizado especificamente para gerar o embedding.

Um exemplo simplificado:

```
Contexto gerado:
"Este trecho pertence à seção de renovação do contrato de
manutenção do sistema ERP da Empresa X."

Chunk original:
"O contrato poderá ser renovado mediante aprovação do gestor."
```

Para a recuperação, o sistema pode utilizar essa representação contextualizada, enquanto o texto original continua disponível para fornecer a resposta ao LLM.

Isso é especialmente útil quando o documento possui muitos chunks que, isoladamente, são semanticamente parecidos.

O Contextual Retrieval também pode ser combinado com outras estratégias já estudadas:

```
Consulta
↓
Hybrid Search
├── Keyword Search
└── Vector Search
        ↓
Top-k
        ↓
Reranking
        ↓
Contexto
        ↓
LLM
```

Nesse cenário, o contexto adicionado durante a indexação ajuda tanto a busca semântica quanto, dependendo da implementação, a busca lexical, porque termos importantes que estavam apenas implícitos no documento podem passar a aparecer explicitamente na representação indexada.

## Um exemplo

Imagine uma base de conhecimento corporativa com centenas de documentos sobre diferentes produtos.

Um dos documentos contém:

```
Produto: Plataforma Alpha

Seção: Limitações

O limite é de 10.000 registros por operação.
```

Após o Chunking, o sistema pode armazenar apenas:

```
"O limite é de 10.000 registros por operação."
```

Agora imagine que o usuário pergunte:

> "Qual é o limite de registros da Plataforma Alpha?"

O chunk contém a informação correta, mas não necessariamente contém explicitamente "Plataforma Alpha".

Com Contextual Retrieval, o chunk poderia receber:

```
Contexto:
Este trecho pertence à seção "Limitações" da documentação
da Plataforma Alpha e descreve o limite de registros por operação.

Chunk:
O limite é de 10.000 registros por operação.
```

O embedding dessa representação possui uma associação muito mais clara com conceitos como:

```
Plataforma Alpha
limite
registros
operação
10.000
```

Isso aumenta a probabilidade de o chunk ser recuperado quando a pergunta mencionar a Plataforma Alpha.

O benefício fica ainda mais evidente quando informações relacionadas estão espalhadas pelo documento:

```
Documento
│
├── Introdução
├── Configuração
├── Limitações
│     └── "O limite é de 10.000 registros..."
├── Segurança
└── Troubleshooting
```

O chunk pode perder sua relação com "Plataforma Alpha" quando é separado. O contexto adicionado funciona como uma espécie de **ponte entre o fragmento e o documento original**.

## Por que é importante

Contextual Retrieval é importante porque resolve uma das limitações naturais do Chunking: **um chunk é menor e mais fácil de recuperar, mas pode perder informações necessárias para interpretá-lo corretamente**.

Isso cria um equilíbrio:

```
Chunk pequeno
↓
Boa precisão de Retrieval
↓
Menos contexto
```

O Contextual Retrieval procura melhorar esse cenário:

```
Chunk pequeno
+
Contexto relevante
↓
Representação mais completa
↓
Retrieval mais preciso
```

A ideia central pode ser resumida assim:

```
Chunking
↓
Fragmenta o documento
↓
Pode remover contexto
↓
Contextual Retrieval
↓
Reintroduz contexto relevante
↓
Embedding mais informativo
↓
Melhor Retrieval
```

Ele não elimina a necessidade de técnicas como Reranking, Hybrid Search ou Context Compression. Na verdade, pode atuar **antes de todas elas**, melhorando a qualidade dos dados que chegam ao processo de recuperação.

Também é importante não confundir Contextual Retrieval com simplesmente aumentar o Chunk Size. Aumentar o chunk coloca mais conteúdo original dentro de cada unidade. Contextual Retrieval procura **adicionar contexto específico ao chunk sem necessariamente aumentar significativamente a quantidade de conteúdo original recuperado**.

Essa diferença é importante em sistemas RAG porque permite manter chunks relativamente pequenos e precisos, mas com informações suficientes para que o mecanismo de Retrieval compreenda **onde aquele fragmento se encaixa no documento original**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/rag-avancado-contextual-retrieval/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
