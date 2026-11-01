[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Hallucination

### 1. O que é

**Hallucination**, ou **alucinação**, acontece quando um modelo de IA gera uma informação **falsa, imprecisa ou inventada**, mas apresenta essa informação de maneira que parece verdadeira.

O ponto importante é que o modelo não está necessariamente "mentindo". Ele está gerando uma resposta com base nos padrões que aprendeu e nas informações disponíveis no contexto, mesmo quando não possui evidência suficiente para responder corretamente.

### 2. Como funciona, de forma intuitiva

Um LLM funciona essencialmente prevendo quais tokens são mais prováveis de aparecer em seguida.

Isso significa que ele não possui, por padrão, um mecanismo interno que funcione como:

> "Essa informação é verdadeira? Posso comprovar isso?"

Por exemplo, imagine que você pergunte:

> "Qual foi o primeiro livro publicado por João Silva?"

Se o modelo não tiver informação confiável sobre esse João Silva, ele pode produzir algo como:

> "O primeiro livro de João Silva foi _A Jornada_, publicado em 2018."

A frase pode ser perfeitamente plausível, mas o livro ou a data podem simplesmente não existir.

Isso acontece porque **plausibilidade e factualidade são coisas diferentes**.

Uma forma simples de pensar:

**LLM:** "Qual resposta parece mais provável neste contexto?"  
**Não necessariamente:** "Qual resposta foi comprovadamente verdadeira?"

### 3. Um exemplo

Imagine um chatbot conectado a uma empresa.

O usuário pergunta:

> "Qual é o prazo de entrega do meu pedido?"

Se o chatbot não tiver acesso aos dados do pedido, ele pode responder:

> "Seu pedido será entregue em até 5 dias úteis."

Essa resposta pode parecer útil, mas é uma alucinação se o sistema não possui informação que permita determinar aquele prazo.

Em um sistema bem projetado, o chatbot deveria dizer algo como:

> "Não tenho acesso ao status do seu pedido. Posso consultar o sistema de pedidos."

Aqui entra uma ideia importante para aplicações de IA: **dar ao modelo acesso às informações necessárias antes de pedir que ele responda**.

### 4. Por que é importante

Hallucination é um dos principais problemas de aplicações baseadas em LLMs, especialmente quando a resposta precisa ser factual.

Ela pode causar problemas em:

- atendimento ao cliente
- análise jurídica
- medicina
- programação
- pesquisa
- geração de relatórios
- sistemas corporativos

Por isso, aplicações profissionais utilizam estratégias para **reduzir e detectar alucinações**, como:

- fornecer contexto confiável ao modelo
- usar **RAG** para buscar informações antes da geração
- exigir citações ou fontes
- validar a resposta posteriormente
- limitar o modelo a informações disponíveis
- usar ferramentas externas para consultar dados reais

Um ponto fundamental para sua preparação em IA generativa é este:

**RAG não elimina completamente hallucinations. Ele fornece ao modelo informações externas relevantes para diminuir a chance de inventar respostas.**


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-hallucination/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
