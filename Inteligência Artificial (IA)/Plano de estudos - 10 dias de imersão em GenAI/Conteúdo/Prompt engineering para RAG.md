[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Prompt Engineering para RAG

## O que é

**Prompt Engineering para [RAG](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-rag/)** é a aplicação de técnicas de engenharia de prompts em sistemas de **Retrieval-Augmented Generation**, com o objetivo de fazer o modelo utilizar melhor as informações recuperadas antes de gerar uma resposta.

Em um sistema RAG, o modelo não recebe apenas a pergunta do usuário. Ele também recebe informações recuperadas de uma ou mais fontes externas.

Um prompt para RAG precisa, portanto, orientar o modelo sobre **como interpretar, utilizar e limitar-se às informações recuperadas**.

Um fluxo simplificado é:

```
Pergunta
   ↓
Busca / Retrieval
   ↓
Documentos relevantes
   ↓
Construção do contexto
   ↓
Prompt
   ↓
LLM
   ↓
Resposta fundamentada
```

O desafio não é simplesmente colocar documentos no prompt. É fazer com que o modelo **use corretamente esses documentos para responder à pergunta**.

## Como funciona, de forma intuitiva

Imagine que você está fazendo uma prova e pode consultar um livro.

Não basta entregar o livro inteiro ao aluno. É preciso indicar:

```
Qual é a pergunta?
Quais páginas são relevantes?
Quais informações devem ser consideradas?
O que fazer se a resposta não estiver no material?
Como apresentar a resposta?
```

Em RAG, o prompt desempenha uma função semelhante.

Ele pode estabelecer regras como:

```
Responda utilizando exclusivamente as informações
presentes no contexto fornecido.

Se a informação necessária não estiver no contexto,
informe que não foi possível encontrar a resposta.

Não invente informações para completar lacunas.

Quando possível, indique a fonte utilizada.
```

O contexto recuperado pode então ser apresentado ao modelo:

```
CONTEXTO:

[Documento 1]
A política de reembolso permite solicitações
em até 30 dias após a compra.

[Documento 2]
Solicitações devem ser realizadas pelo portal
do cliente.

PERGUNTA:

Como solicitar um reembolso?
```

O modelo utiliza o contexto para construir a resposta.

O ponto fundamental é que **o prompt não substitui a etapa de recuperação**. Se o sistema recuperar documentos inadequados, incompletos ou irrelevantes, mesmo um excelente prompt pode produzir uma resposta ruim.

Por isso, RAG possui pelo menos dois problemas diferentes:

```
Retrieval
"Encontrei a informação certa?"

Generation
"Usei corretamente a informação encontrada?"
```

Prompt Engineering atua principalmente na segunda questão, embora possa influenciar indiretamente a primeira quando o próprio prompt participa da formulação da consulta.

## Um exemplo

Imagine uma empresa que possui centenas de documentos internos e deseja criar um assistente para responder perguntas sobre suas políticas.

O usuário pergunta:

```
Quantos dias de férias um funcionário pode tirar?
```

O sistema recupera alguns trechos:

```
Documento: Política de Férias

Funcionários têm direito a 30 dias de férias por
período aquisitivo, conforme as regras estabelecidas
pela empresa.
```

O prompt pode orientar o modelo:

```
Você é um assistente interno da empresa.

Responda à pergunta utilizando apenas as informações
presentes no contexto.

Se o contexto não contiver informações suficientes,
informe isso claramente.

Não faça suposições para preencher informações ausentes.

Contexto:
{{documentos_recuperados}}

Pergunta:
{{pergunta}}
```

A resposta esperada seria baseada diretamente no documento:

```
De acordo com a Política de Férias, o funcionário
tem direito a 30 dias de férias por período aquisitivo.
```

Agora imagine que o usuário pergunte:

```
Posso dividir esses 30 dias em três períodos?
```

Se o documento recuperado não informar essa possibilidade, um prompt bem projetado deve impedir que o modelo simplesmente invente uma resposta.

Ele poderia responder:

```
O contexto fornecido informa que o funcionário tem direito
a 30 dias de férias, mas não contém informações suficientes
sobre a possibilidade de dividir esse período em três partes.
```

Esse comportamento é uma das principais preocupações do Prompt Engineering para RAG: **ensinar o modelo a reconhecer os limites das evidências disponíveis**.

## Por que é importante

Prompt Engineering para RAG é importante porque adicionar recuperação de documentos **não garante automaticamente respostas confiáveis**.

O modelo ainda precisa interpretar o contexto corretamente, lidar com informações conflitantes e saber quando não possui evidências suficientes.

Um bom prompt de RAG normalmente precisa considerar:
1. **Uso do contexto:** deixar claro que as informações recuperadas devem ser utilizadas como base da resposta.
2. **Limites da evidência:** orientar o modelo a não preencher lacunas com informações inventadas.
3. **Relevância:** instruir o modelo a priorizar os trechos relacionados à pergunta.
4. **Conflitos:** definir como lidar com documentos que apresentam informações diferentes.
5. **Fontes:** quando necessário, solicitar referências aos documentos utilizados.
6. **Formato:** estabelecer como a resposta deve ser apresentada.
7. **Incerteza:** permitir que o modelo reconheça quando o contexto não é suficiente.

Também é importante entender que **Prompt Engineering para RAG não resolve problemas de recuperação**.

Se o usuário perguntar sobre uma política específica e o sistema recuperar documentos completamente diferentes, o problema está principalmente no **retrieval**, não no prompt.

Podemos pensar no sistema como uma sequência:

```
Pergunta
   ↓
Retrieval
   ↓
Documentos recuperados
   ↓
Context Management
   ↓
Prompt para RAG
   ↓
LLM
   ↓
Resposta
```

Cada etapa pode introduzir erros.

Por isso, um sistema RAG robusto precisa avaliar tanto **a qualidade da recuperação** quanto **a qualidade da geração**.

### Grounding × Prompt Engineering para RAG

Os dois conceitos estão diretamente relacionados, mas não são iguais.

**[Grounding](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-grounding/)** é o princípio de fundamentar a resposta em informações externas relevantes.

**RAG** é uma arquitetura que recupera informações e as fornece ao modelo.

**Prompt Engineering para RAG** define como o modelo deve utilizar essas informações recuperadas.

Podemos resumir:

```
Grounding
   ↓
Princípio

RAG
   ↓
Arquitetura

Prompt Engineering para RAG
   ↓
Orientação do modelo
```

Essa distinção é importante porque mostra que melhorar um sistema RAG não significa apenas escrever um prompt melhor.

É preciso considerar o **retrieval, a qualidade dos documentos, a construção do contexto, as instruções fornecidas ao modelo e a validação da resposta**.

Em sistemas mais avançados, isso se conecta diretamente a **[Context Management](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-context-management/), [Tool Instructions](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-tool-instructions/), [Guardrails](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-guardrails/) e agentes**, formando uma arquitetura na qual o [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) não apenas responde perguntas, mas utiliza informações externas de maneira controlada e fundamentada.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-para-rag/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
