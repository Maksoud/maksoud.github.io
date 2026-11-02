# Ingestion

## O que é

**Ingestion**, ou ingestão de dados, é o processo de **receber, coletar e preparar dados para que eles possam ser utilizados por um sistema de IA**.

No contexto de **RAG**, a ingestion é o ponto de entrada das informações que posteriormente poderão ser recuperadas para responder às perguntas dos usuários.

Por exemplo, uma empresa pode possuir informações em:

```
PDFs
Documentos
Páginas web
Bancos de dados
Planilhas
Sistemas internos
APIs
```

Esses dados precisam passar por um processo de ingestão antes de serem utilizados pelo RAG.

De forma simplificada:

```
Fontes de dados
      ↓
   Ingestion
      ↓
Dados preparados
      ↓
Próximas etapas do RAG
```

A ingestion, portanto, não é simplesmente "fazer upload de um arquivo". Ela representa todo o processo necessário para **trazer os dados de suas fontes de origem para dentro do pipeline de processamento do sistema**.

---

## Como funciona

Imagine que queremos construir um RAG para responder perguntas sobre os documentos internos de uma empresa.

Os documentos estão espalhados por diferentes lugares:

```
PDFs ───────────────┐
Word ───────────────┤
Planilhas ──────────┤
Wiki interna ───────┤
Banco de dados ─────┤
APIs ───────────────┘
          ↓
      Ingestion
```

O processo de ingestion coleta esses dados e os coloca em um fluxo controlado.

Depois da coleta, podem existir várias etapas de preparação:

```
Fonte de dados
      ↓
Coleta
      ↓
Extração do conteúdo
      ↓
Limpeza
      ↓
Normalização
      ↓
Preparação para processamento
```

A partir daí, o conteúdo pode seguir para etapas que já estudamos:

```
Dados
  ↓
Ingestion
  ↓
Documentos preparados
  ↓
Chunking
  ↓
Embeddings
  ↓
Vector Database
```

É importante perceber que **Ingestion vem antes de Embeddings**.

O sistema primeiro precisa conseguir obter e preparar o conteúdo. Só depois poderá dividir os documentos em partes, gerar embeddings e armazenar os vetores.

Também é comum que a ingestion aconteça de forma contínua.

Por exemplo, uma empresa pode atualizar diariamente seus documentos:

```
Novo documento
      ↓
Ingestion
      ↓
Processamento
      ↓
Embedding
      ↓
Atualização do índice
```

Assim, o sistema RAG consegue incorporar novas informações sem precisar reconstruir manualmente toda a base.

---

## Um exemplo

Imagine um RAG criado para responder perguntas sobre as políticas de uma empresa.

Os documentos estão armazenados em uma pasta:

```
/politicas
    ferias.pdf
    beneficios.pdf
    home-office.pdf
    reembolso.pdf
```

O pipeline de ingestion pode começar assim:

```
Pasta de documentos
        ↓
Ingestion
        ↓
Leitura dos arquivos
        ↓
Extração do texto
        ↓
Documentos preparados
```

O conteúdo de `ferias.pdf`, por exemplo, pode ser extraído:

```
"Os colaboradores devem solicitar férias
com antecedência mínima de 30 dias..."
```

Esse conteúdo ainda não precisa estar em um Vector Database. Primeiro ele precisa ser preparado para as próximas etapas.

Depois:

```
Texto extraído
      ↓
Chunking
      ↓
Chunks
      ↓
Embedding Model
      ↓
Vector Embeddings
      ↓
Vector Database
```

Quando o usuário posteriormente perguntar:

```
"Com quanto tempo de antecedência preciso solicitar férias?"
```

o sistema poderá utilizar o conteúdo que entrou originalmente pelo processo de ingestion.

Isso mostra uma característica importante:

**A qualidade do RAG começa antes da busca.**

Se a ingestion falhar, o problema pode aparecer muito mais tarde.

Por exemplo, se um PDF não tiver seu texto extraído corretamente, o embedding será gerado a partir de conteúdo incompleto ou incorreto. Consequentemente, a busca poderá não recuperar a informação necessária.

---

## Por que é importante

A ingestion é importante porque estabelece a **entrada de conhecimento do RAG**.

Um sistema pode ter um excelente modelo de embeddings, uma ótima Vector Database e uma LLM poderosa, mas se os dados não entrarem corretamente no pipeline, todo o restante será prejudicado.

Alguns problemas que podem ocorrer durante a ingestion incluem:
- Arquivos não encontrados.
- Texto extraído de forma incorreta.
- Caracteres corrompidos.
- Informações duplicadas.
- Documentos desatualizados.
- Estrutura importante perdida durante a extração.
- Metadados ausentes ou incorretos.
- Conteúdo que deveria ser excluído sendo incorporado à base.

Por isso, ingestion está diretamente relacionada à **qualidade e atualidade da base de conhecimento** utilizada pelo RAG.

Também é importante diferenciar **Ingestion** de **Retrieval**.

**Ingestion** acontece quando os dados entram no sistema:

```
Fonte → Ingestion → Processamento → Indexação
```

**Retrieval** acontece quando um usuário faz uma pergunta e o sistema procura informações relevantes:

```
Pergunta → Retrieval → Conteúdo relevante
```

Podemos visualizar o RAG completo em duas grandes fases:

```
             RAG
              │
      ┌───────┴───────┐
      ↓               ↓
 Ingestion          Retrieval
      ↓               ↓
Preparar dados    Buscar dados
      ↓               ↓
Chunks            Similaridade
      ↓               ↓
Embeddings        Top-k
      ↓               ↓
Vector Database   Contexto
                      ↓
                     LLM
                      ↓
                   Resposta
```

Essa separação é fundamental para entender a arquitetura.

A **Ingestion** prepara o conhecimento antes da pergunta existir.

O **Retrieval** utiliza esse conhecimento quando a pergunta chega.

A ideia central é: **Ingestion é o processo de trazer dados de suas fontes para dentro do pipeline do RAG, extraindo, preparando e organizando essas informações para que possam posteriormente ser indexadas e recuperadas.**