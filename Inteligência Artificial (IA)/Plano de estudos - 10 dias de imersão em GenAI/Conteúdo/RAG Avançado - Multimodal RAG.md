[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Multimodal RAG

## O que é

Multimodal RAG é uma abordagem de RAG capaz de **recuperar e utilizar informações de diferentes modalidades de dados**, como texto, imagens, tabelas, gráficos, áudio e vídeo.

Em um RAG tradicional, o conhecimento recuperado é predominantemente textual:

```
Documento
↓
Texto
↓
Chunks
↓
Embeddings
↓
Retrieval
↓
Contexto textual
↓
LLM
```

No Multimodal RAG, a informação pode estar distribuída entre diferentes tipos de conteúdo:

```
                 ┌──→ Texto
                 ├──→ Imagem
Documentos ──────┼──→ Tabela
                 ├──→ Gráfico
                 ├──→ Áudio
                 └──→ Vídeo
                       ↓
                    Retrieval
                       ↓
                  Contexto multimodal
                       ↓
                      LLM
```

Isso é importante porque muitos documentos reais não são compostos apenas por texto. Um relatório financeiro, por exemplo, pode conter explicações textuais, tabelas e gráficos. Uma documentação técnica pode conter texto, diagramas e screenshots. Um contrato digitalizado pode depender de OCR para transformar uma imagem em texto.

O Multimodal RAG procura preservar e recuperar essas diferentes formas de informação de maneira que o modelo possa utilizá-las para responder à pergunta.

## Como funciona

O processo começa com a ingestão dos diferentes tipos de conteúdo. Cada modalidade pode exigir uma estratégia específica de processamento.

Um documento PDF, por exemplo, pode conter:

```
PDF
├── Texto
├── Tabelas
├── Imagens
├── Gráficos
└── Diagramas
```

O sistema precisa identificar e processar esses elementos antes de realizar o Retrieval.

Uma arquitetura simplificada pode ser:

```
                         ┌──→ Texto → Embedding
                         │
Documentos ──────────────┼──→ Imagem → Embedding visual
                         │
                         ├──→ Tabela → Estrutura / Texto
                         │
                         └──→ Gráfico → Imagem / Descrição
                                      ↓
                                  Indexação
                                      ↓
                                    Query
                                      ↓
                              Multimodal Retrieval
                                      ↓
                              Contexto multimodal
                                      ↓
                                     LLM
```

Existem diferentes formas de implementar esse processo.

Uma delas é transformar modalidades não textuais em representações textuais. Por exemplo, uma imagem pode passar por OCR ou por um modelo multimodal que gere uma descrição:

```
Imagem
↓
Modelo multimodal
↓
"Gráfico mostrando crescimento de vendas entre janeiro e junho"
↓
Embedding
↓
Indexação
```

Nesse caso, o Retrieval continua sendo predominantemente textual, mas a informação visual foi convertida para texto antes de ser indexada.

Outra abordagem é manter representações específicas para cada modalidade. Uma imagem pode possuir um embedding visual, enquanto um trecho de texto possui um embedding textual. Modelos multimodais podem permitir que essas representações sejam comparadas em um espaço compartilhado.

Por exemplo:

```
Pergunta textual
       ↓
Embedding multimodal
       ↓
Busca
   ↙       ↓       ↘
Texto    Imagem   Gráfico
   ↘       ↓       ↙
      Resultados
          ↓
   Contexto multimodal
          ↓
         LLM
```

Isso permite uma situação interessante: uma pergunta feita em texto pode recuperar uma imagem ou um gráfico porque o conteúdo visual possui relação semântica com a pergunta.

As tabelas apresentam outro desafio. Uma tabela pode conter informações que não devem ser tratadas simplesmente como um bloco de texto.

Considere:

```
Produto     Receita     Crescimento
Produto A   R$ 500 mil  +12%
Produto B   R$ 320 mil  -8%
Produto C   R$ 180 mil  +21%
```

Uma pergunta como:

> "Qual produto teve maior crescimento?"

pode ser respondida a partir da estrutura da tabela. Dependendo da implementação, o sistema pode armazenar a tabela de forma estruturada, convertê-la para texto ou utilizar um modelo capaz de interpretar diretamente sua representação visual.

Um dos pontos mais importantes é que **Multimodal RAG não significa apenas aceitar imagens como entrada**. O aspecto central é que informações multimodais podem participar do processo de conhecimento, Retrieval e geração da resposta.

## Um exemplo

Imagine um sistema de assistência técnica utilizado por uma empresa de engenharia.

A base de conhecimento contém:

```
Manuais em PDF
├── Texto
├── Diagramas
├── Tabelas técnicas
└── Fotografias

Relatórios de manutenção
├── Texto
├── Fotografias dos equipamentos
└── Gráficos

Vídeos
└── Gravações de procedimentos
```

O usuário pergunta:

> "Qual componente está causando esse tipo de falha e como devo substituí-lo?"

O sistema pode recuperar diferentes evidências:

```
Pergunta
↓
Retrieval
├── Manual textual do equipamento
├── Diagrama do componente
├── Fotografia de uma falha semelhante
└── Procedimento de substituição
        ↓
Contexto multimodal
        ↓
Modelo multimodal
        ↓
Resposta
```

O modelo pode utilizar o texto do manual para entender o procedimento, o diagrama para identificar a posição do componente e a fotografia para comparar visualmente o tipo de falha.

Nesse caso, nenhuma modalidade isoladamente necessariamente contém toda a resposta. **A resposta surge da combinação das evidências.**

Outro exemplo seria um assistente financeiro.

O usuário poderia perguntar:

> "Por que a margem caiu no último trimestre?"

O sistema poderia recuperar:

```
Relatório financeiro
        ├── Texto explicativo
        ├── Tabela de resultados
        └── Gráfico de margem
                 ↓
          Contexto multimodal
                 ↓
                LLM
```

O texto poderia explicar o aumento dos custos, enquanto o gráfico mostraria visualmente a queda da margem e a tabela permitiria verificar os valores.

## Por que é importante

Multimodal RAG é importante porque grande parte do conhecimento empresarial e técnico **não está armazenada exclusivamente em texto**.

Relatórios, apresentações, PDFs, documentos digitalizados, diagramas, screenshots, fotografias, gráficos e tabelas podem conter informações essenciais que seriam perdidas por um RAG que considerasse apenas texto.

A diferença pode ser resumida assim:

```
RAG textual

Pergunta
↓
Texto
↓
Retrieval
↓
Contexto textual
↓
LLM


Multimodal RAG

Pergunta
↓
Texto + imagens + tabelas + gráficos + outras modalidades
↓
Retrieval multimodal
↓
Contexto multimodal
↓
LLM
```

Isso também cria novos desafios. Diferentes modalidades precisam ser processadas, indexadas e recuperadas de maneira adequada. Além disso, o sistema precisa preservar a relação entre elementos que pertencem ao mesmo documento.

Por exemplo, um gráfico pode depender da legenda que aparece ao lado dele, e uma tabela pode depender do título e das unidades apresentadas acima dela. Recuperar apenas a imagem ou apenas a tabela pode remover justamente o contexto necessário para interpretá-la corretamente.

Por isso, um bom Multimodal RAG precisa considerar não apenas **qual conteúdo recuperar**, mas também **como preservar as relações entre os diferentes elementos recuperados**.

Nesse sentido, ele representa uma evolução natural do RAG para ambientes onde o conhecimento é distribuído entre múltiplas modalidades, permitindo que o LLM raciocine sobre evidências textuais e visuais dentro do mesmo processo de geração.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/rag-avancado-multimodal-rag/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
