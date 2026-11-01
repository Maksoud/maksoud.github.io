[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# RAG

### 1. O que é

**RAG** significa **Retrieval-Augmented Generation**, ou **Geração Aumentada por Recuperação**.

É uma arquitetura que combina duas coisas:
1. **Retrieval:** buscar informações relevantes em uma fonte externa.
2. **Generation:** fornecer essas informações ao LLM para que ele gere a resposta.

A ideia central é:

> **Em vez de depender apenas do que o modelo aprendeu durante o treinamento, buscamos informações relevantes no momento da pergunta e entregamos esse contexto ao modelo.**

### 2. Como funciona, de forma intuitiva

Imagine que você tenha uma empresa com milhares de documentos internos:
- manuais;
- contratos;
- políticas;
- procedimentos;
- documentação técnica;
- FAQs.

Você pergunta ao chatbot:

> "Qual é a política da empresa para reembolso de viagens?"

O LLM provavelmente não conhece essa política específica.

Com RAG, o sistema faz aproximadamente isto:
```
Pergunta do usuário  
↓  
Busca nos documentos  
↓  
Encontra os trechos relevantes  
↓  
Entrega esses trechos ao LLM como contexto  
↓  
LLM gera a resposta
```

Assim, o modelo não precisa ter aprendido a política durante seu treinamento.

### 3. Um exemplo

Imagine uma empresa com um documento:

> "Despesas de hospedagem podem ser reembolsadas até o limite de R$ 500 por noite."

O usuário pergunta:

> "Quanto posso gastar com hospedagem em uma viagem?"

O sistema RAG localiza esse trecho e o coloca no contexto do modelo.

O LLM então pode responder:

> "O limite para reembolso de hospedagem é de R$ 500 por noite."

O modelo **não precisou memorizar essa informação durante o treinamento**. Ele recebeu a informação relevante no momento da consulta.

### 4. Por que é importante

RAG é extremamente importante em aplicações corporativas porque permite trabalhar com **informações específicas, privadas e que mudam frequentemente**.

Por exemplo:
- documentação interna;
- base de conhecimento;
- catálogo de produtos;
- legislação;
- manuais técnicos;
- dados de clientes;
- políticas atualizadas.

Também ajuda a reduzir **hallucinations**, porque o modelo recebe informações relevantes para fundamentar sua resposta. Porém, **RAG não elimina alucinações**. Se a busca recuperar informação errada ou insuficiente, o modelo ainda pode produzir uma resposta incorreta.

### A arquitetura básica

Uma aplicação RAG geralmente possui duas etapas principais:

**Antes da pergunta:**

Documentos → divisão em partes → embeddings → armazenamento/indexação

**Quando o usuário pergunta:**

Pergunta → busca dos trechos relevantes → contexto → LLM → resposta

Um detalhe importante para sua preparação: **RAG não é um modelo de IA**. É uma **arquitetura/padrão de construção de aplicações** que utiliza um LLM junto com mecanismos de recuperação de informação.

E isso diferencia RAG de **fine-tuning**:

**Fine-tuning:** modifica o comportamento/conhecimento aprendido pelo modelo através de treinamento adicional.

**RAG:** mantém o modelo e fornece informações externas a ele durante a consulta.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-rag/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
