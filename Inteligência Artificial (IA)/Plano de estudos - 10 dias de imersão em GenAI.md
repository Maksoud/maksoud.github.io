Eu reservaria **3–4 horas por dia**, durante 10 dias.

Não precisa necessariamente estudar 4 horas seguidas. Minha sugestão:

**1h — teoria**  
**1h — vídeo/aula/podcast**  
**1–2h — prática**

E há uma regra importante:

> **Não estude apenas assistindo conteúdo. A cada conceito novo, você precisa conseguir explicar e/ou implementar alguma coisa.**

---
# Sumário — Plano de Estudos em IA Generativa

1. **Fundamentos de LLMs**
    - LLMs, Transformers e atenção
    - Tokens e tokenização
    - Embeddings
    - Context window
    - Treinamento vs. inferência
    - Temperature, top-p e geração
    - Hallucinations
    - Instruction tuning, RLHF e modelos de raciocínio

2. **Engenharia de Prompt**
    - Zero-shot e few-shot
    - System instructions
    - Structured outputs / JSON
    - Prompt decomposition e chaining
    - Context management
    - Instruction hierarchy
    - Prompt injection e jailbreaks
    - Grounding e guardrails
    - Prompt engineering aplicado a RAG

3. **Embeddings e Busca Semântica**
    - Embeddings e representação vetorial
    - Similaridade semântica
    - Cosine similarity
    - Vector databases
    - Semantic search
    - Sparse vs. dense retrieval
    - BM25

4. **RAG — Retrieval-Augmented Generation**
    - Conceito e arquitetura
    - Ingestion de documentos
    - Parsing e cleaning
    - Chunking e chunk overlap
    - Embeddings e indexing
    - Retrieval e top-k
    - Metadata filtering
    - Reranking
    - Contexto e geração
    - RAG vs. conhecimento paramétrico

5. **Construção de um Sistema RAG**
    - Preparação de documentos
    - Criação dos chunks
    - Geração de embeddings
    - Vector database
    - Pipeline de retrieval
    - Integração com LLM
    - Testes e análise dos resultados

6. **RAG Avançado**
    - Hybrid search
    - Query rewriting
    - Query expansion
    - Semantic chunking
    - Parent-child retrieval
    - Context compression
    - Agentic RAG
    - GraphRAG
    - Multimodal RAG
    - Contextual Retrieval
    - Corrective RAG / Self-RAG

7. **Agentes de IA**
    - AI agents vs. chatbots
    - Agentic AI
    - Tool/function calling
    - Tools e actions
    - Planning
    - Agent loop
    - State e memory
    - Orchestration
    - Human-in-the-loop
    - Multi-agent systems

8. **Construção de um Agente**
    - Definição do objetivo
    - Ferramentas
    - Retrieval
    - APIs externas
    - Fluxo de decisão
    - Execução de múltiplas etapas
    - Projeto prático de agente para análise de vagas

9. **Frameworks e Arquitetura**
    - LangChain
    - LangGraph
    - LlamaIndex
    - Hugging Face
    - Workflows vs. agents
    - State, nodes e edges
    - Escolha de frameworks conforme o problema

10. **Avaliação de Sistemas LLM/RAG**
    - Evaluation datasets
    - Benchmarks
    - Relevance
    - Faithfulness
    - Groundedness
    - Precision e recall
    - LLM-as-a-judge
    - Avaliação humana
    - Retrieval quality vs. generation quality

11. **Segurança em GenAI**
    - Prompt injection
    - Indirect prompt injection
    - Jailbreaks
    - Data leakage
    - Excessive agency
    - Insecure tool use
    - Controle de acesso
    - Segurança em RAG

12. **Conceitos que precisam ser diferenciados**
    - Prompt Engineering × RAG
    - RAG × Fine-tuning
    - RAG × Tool Calling
    - Workflow × Agent
    - Retrieval × Generation
    - Embedding × Vector Database

13. **Projeto Final de Portfólio**
    - AI Career Research Agent
    - Base de conhecimento pessoal
    - RAG sobre currículo e experiências
    - Análise de vagas
    - Identificação de gaps
    - Uso de ferramentas
    - Pesquisa externa
    - Geração de plano de estudos e preparação para entrevistas

14. **Preparação para Entrevista**
    - Explicar LLMs
    - Explicar RAG
    - Explicar embeddings
    - Diagnosticar problemas de retrieval
    - Explicar reranking
    - Projetar prompts
    - Explicar agentes e tool calling
    - Escolher RAG vs. fine-tuning
    - Identificar vulnerabilidades
    - Avaliar qualidade de um sistema GenAI

15. **Fontes e Estratégia de Estudo**
    - Documentação oficial
    - Cursos especializados
    - Vídeos técnicos
    - Podcasts e conteúdo em áudio
    - Preferência por fontes em inglês para aprofundamento
    - Teoria + prática + projeto como método principal

---
# Mapa do que você precisa dominar

Antes do cronograma, quero te mostrar a árvore de conhecimento.

```
                    IA GENERATIVA
                         │
             ┌───────────┴───────────┐
             │                       │
           LLMs                  Aplicações
             │                       │
      ┌──────┼──────┐         ┌──────┼──────┐
      │      │      │         │      │      │
   Tokens  Context Embeddings  Prompt RAG  Agents
      │      │      │                  │      │
      │      │      └──────┐           │      │
      │      │             │           │      │
      └──────┴─────────────┤           │      │
                           │           │      │
                      Retrieval ───────┘      │
                           │                  │
                   Vector Database            │
                           │                  │
                      Reranking               │
                                              │
                                     Tool Calling
                                              │
                                      Workflow/Agent
                                              │
                                    Evaluation/Observability
```

Essa estrutura é importante porque **RAG e agentes não são simplesmente “novos tipos de prompt”**.

---

# Dia 1: LLMs de verdade

Entender o que é de fato um LLM: tokens, embeddings, atenção, janela de contexto, inferência e por que ele alucina.

[Ver detalhes do Dia 1](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

---

# Dia 2: Prompt Engineering 2.0

Ver prompt engineering como projeto de uma interface confiável entre usuário, modelo, contexto e sistema, incluindo prompts para RAG.

[Ver detalhes do Dia 2](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

---

# Dia 3: Embeddings

Compreender embeddings, similaridade semântica e bancos vetoriais, a base para o RAG fazer sentido.

[Ver detalhes do Dia 3](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

---

# Dia 4: RAG finalmente

Estudar o RAG em camadas: ingestão, chunking, embeddings, indexação, retrieval, reranking e geração.

[Ver detalhes do Dia 4](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

---

# Dia 5: Construir seu primeiro RAG

Pausa na teoria para construir um primeiro "chat com meus documentos", entendendo cada etapa do pipeline.

[Ver detalhes do Dia 5](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-05-construir-seu-primeiro-rag/)

---

# Dia 6: RAG avançado

Conhecer técnicas avançadas de retrieval, reranking, chunking e contexto, além de Agentic RAG, GraphRAG e outras variações.

[Ver detalhes do Dia 6](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

---

# Dia 7: Agentes

Entender agentes como LLM + ferramentas + estado + loop de decisão, com tool calling, planejamento e memória.

[Ver detalhes do Dia 7](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

---

# Dia 8: Construir um agente

Construir um pequeno agente de análise de vagas que combina RAG, busca e ferramentas.

[Ver detalhes do Dia 8](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-08-construir-um-agente/)

---

# Dia 9: Frameworks + arquitetura

Conhecer o ecossistema (LangChain, LangGraph, LlamaIndex, Hugging Face) para escolher a ferramenta certa para cada problema.

[Ver detalhes do Dia 9](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-09-frameworks-arquitetura/)

---

# Dia 10: Avaliação, segurança e produção

Avaliar sistemas LLM/RAG separando qualidade de retrieval e de geração, e estudar segurança, como prompt injection.

[Ver detalhes do Dia 10](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-10-avaliacao-seguranca-e-producao/)

---

# O projeto final

Se você tiver disposição para fazer apenas **um projeto realmente bom**, eu faria este:

## “AI Career Research Agent”

Você pode transformar isso em um pequeno projeto de portfólio.

### Entrada

Uma descrição de vaga.

### Knowledge base

Documentos contendo:

- seu currículo;
- experiências;
- projetos;
- cursos;
- certificações;
- descrição de trabalhos anteriores;
- conhecimentos técnicos.

### RAG

O sistema recupera as informações relevantes sobre você.

### Agent

O agente pode:

```
1. analisar a vaga
2. identificar competências
3. consultar sua base
4. comparar competências
5. identificar gaps
6. pesquisar conceitos desconhecidos
7. gerar plano de estudos
8. produzir perguntas para entrevista
```

### Resultado

```
MATCH: 74%

Fortes:
- X
- Y
- Z

Gaps:
- RAG
- Agent orchestration

Recomendação:
...

Perguntas prováveis:
...

Plano de preparação:
...
```

Isso permite demonstrar **LLM + Prompt Engineering + RAG + Agents + Tool Calling + Evaluation** em um único projeto.

---

# Seu dicionário obrigatório

Eu criaria um documento chamado:

**“GenAI Glossary — Interview Preparation”**

E colocaria uma linha para cada termo.

Comece com estes:

### LLM

Large Language Model.

### Token

Unidade de texto processada pelo modelo.

### Context Window

Quantidade de tokens que o modelo consegue considerar em determinado contexto.

### Embedding

Representação vetorial de conteúdo.

### Vector Database

Banco especializado em armazenar/consultar representações vetoriais.

### RAG

Retrieval-Augmented Generation.

### Retrieval

Processo de encontrar informação relevante.

### Chunk

Fragmento de documento utilizado durante retrieval.

### Reranking

Reordenação dos resultados recuperados segundo relevância.

### Grounding

Fazer o modelo fundamentar sua resposta em informações fornecidas/verificáveis.

### Hallucination

Resposta incorreta ou não fundamentada apresentada pelo modelo.

### Tool Calling

Capacidade do LLM de solicitar execução de uma ferramenta externa.

### Agent

Sistema em que um LLM pode utilizar ferramentas e executar etapas para atingir um objetivo.

### Agentic RAG

RAG em que o agente decide dinamicamente como e quando realizar retrieval.

### Fine-tuning

Adaptação dos parâmetros do modelo através de treinamento adicional.

### Prompt Engineering

Projeto sistemático das instruções/contexto fornecidos ao modelo.

### Guardrails

Mecanismos para restringir e controlar comportamento do sistema.

### Evaluation

Medição sistemática da qualidade do sistema.

---

# E tem um ponto MUITO importante para sua vaga

Eu estudaria também:

## **RAG × Fine-tuning × Prompt Engineering**

Você precisa saber explicar isso em uma entrevista.

Uma forma simplificada:

|Problema|Primeira coisa a considerar|
|---|---|
|Modelo não entende a tarefa|Prompt|
|Modelo precisa seguir formato|Prompt / Structured Output|
|Modelo não conhece seus documentos|RAG|
|Informação muda constantemente|RAG|
|Modelo precisa acessar sistemas externos|Tool Calling|
|Precisa executar múltiplas etapas|Agent|
|Precisa mudar comportamento/estilo de forma consistente|Fine-tuning|
|Precisa de dados atualizados|Retrieval / Tools|
|Sistema está respondendo com contexto errado|Retrieval|
|Sistema recupera certo mas responde errado|Prompt/model/evaluation|

Esse raciocínio é muito mais valioso profissionalmente do que decorar 50 técnicas de prompting.

---

# Como estudar vídeo, áudio e texto

Eu faria uma hierarquia.

### 🥇 Nível 1 — Documentação oficial

Priorize:

[OpenAI — Optimizing LLM Accuracy](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy?utm_source=chatgpt.com)

[Microsoft Learn — RAG Prompt Engineering](https://learn.microsoft.com/pt-br/azure/architecture/ai-ml/guide/rag/rag-prompt-engineering?utm_source=chatgpt.com)

[Hugging Face — Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction?utm_source=chatgpt.com)

Esses materiais são melhores para construir sua **base conceitual**.

### 🥈 Nível 2 — Cursos

Procure conteúdos de:

- DeepLearning.AI
- Hugging Face
- Stanford
- Google
- Microsoft
- Anthropic

### 🥉 Nível 3 — YouTube

Aqui eu usaria vídeos para **visualizar aquilo que você acabou de estudar**.

Busque literalmente:

```
LLM transformers explained
LLM tokenization explained
embeddings explained
vector database explained
RAG explained
RAG architecture
RAG chunking strategies
RAG reranking
RAG evaluation
agentic AI explained
LLM tool calling
function calling LLM
AI agent architecture
LangGraph tutorial
Agentic RAG
LLM evaluation
prompt injection RAG
```

Depois, em português:

```
RAG explicado
embeddings inteligência artificial
agentes de IA LLM
engenharia de prompt avançada
vector database
LangGraph
RAG com Python
agentes com LLM
```

**Eu daria preferência ao inglês para os conceitos técnicos.** A quantidade e qualidade do material é significativamente maior.

---

# E áudio/podcast?

Eu não usaria podcast como fonte principal.

Use áudio para **consolidação**.

Enquanto caminha ou dirige, procure episódios sobre:

```
LLM architecture
AI agents
RAG
AI engineering
LLM evaluation
AI safety
generative AI engineering
```

O objetivo não é aprender um conceito novo dirigindo.

É ouvir especialistas discutindo:

> “Por que RAG não funciona?”

> “Quando usar fine-tuning?”

> “Agents are overhyped?”

> “How do we evaluate LLM applications?”

Esse tipo de discussão vai te ajudar muito em entrevistas.

---

# O que eu NÃO estudaria agora

Isso é tão importante quanto o que estudar.

Durante essas férias, **não mergulharia profundamente em**:

- matemática de Transformers;
- treinamento de LLM do zero;
- CUDA;
- GPU optimization;
- distributed training;
- fine-tuning avançado;
- LoRA em profundidade;
- Kubernetes;
- MLOps completo;
- todos os frameworks de agentes;
- construção de um vector database do zero.

São assuntos válidos, mas **não são a melhor utilização dos seus próximos dias** considerando a descrição da vaga.

---

# Seu objetivo ao final das férias

Eu colocaria uma espécie de prova final.

Você deveria conseguir responder, sem pesquisar:

### LLM

> “Explique para um desenvolvedor como um LLM processa uma pergunta.”

### RAG

> “Como você construiria um RAG para 100 mil documentos?”

### Embeddings

> “O que é um embedding e por que ele é necessário em RAG?”

### Retrieval

> “Seu RAG está retornando documentos irrelevantes. O que você investigaria?”

### Reranking

> “Por que usar reranking?”

### Prompt

> “Como você melhoraria um prompt que está produzindo respostas inconsistentes?”

### Agents

> “Qual a diferença entre um workflow determinístico e um agente?”

### Tool Calling

> “Como um agente consulta uma API externa?”

### Fine-tuning

> “Quando você escolheria fine-tuning em vez de RAG?”

### Segurança

> “O que é prompt injection e como ela pode afetar um RAG?”

### Evaluation

> “Como você saberia se seu RAG está funcionando bem?”

Se você conseguir responder essas perguntas **com exemplos e arquitetura**, já estará em um patamar muito diferente de alguém que simplesmente colocou “IA generativa” no currículo.

---

## E eu faria uma adaptação importante para você

Como seu objetivo não é simplesmente aprender por curiosidade, mas **se preparar para uma vaga**, eu transformaria esses 10 dias em um pequeno **bootcamp pessoal**, com:

**Dia 1–3 → fundamentos**  
**Dia 4–6 → RAG**  
**Dia 7–8 → agentes**  
**Dia 9 → arquitetura/frameworks**  
**Dia 10 → avaliação + segurança + entrevista**

E, em paralelo, construiria **um único projeto de portfólio**, em vez de cinco projetos superficiais.

Isso também conversa muito bem com a evolução atual do campo: a formação de agentes da Hugging Face, por exemplo, já trata LLMs, tools, ciclos de ação/observação, frameworks e depois Agentic RAG como uma progressão natural. [Hugging Face](https://huggingface.co/learn/agents-course/unit1/introduction?utm_source=chatgpt.com)

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>