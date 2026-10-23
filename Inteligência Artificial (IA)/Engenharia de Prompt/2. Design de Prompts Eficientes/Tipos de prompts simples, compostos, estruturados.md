### Sumário

# Tipos de prompts: simples, compostos, estruturados

_Como escolher o melhor tipo de prompt para cada situação empresarial._

## 📌 Introdução

O sucesso de uma interação com um LLM depende fortemente de **como o prompt é escrito e estruturado**. Escolher o tipo de prompt certo faz a diferença entre uma resposta vaga e uma solução realmente útil para o negócio.

De forma geral, os prompts podem ser classificados em três tipos principais:

- **Prompt Simples**
- **Prompt Composto**
- **Prompt Estruturado**


## 1️⃣ Prompt Simples

### ✅ Definição:

Um prompt direto, objetivo e curto. Normalmente faz apenas **uma solicitação clara** ao modelo.

### ✅ Exemplo:

> **"Explique o que é Machine Learning."**

### ✅ Características:

- Pouco contexto
- Sem formatação ou instruções avançadas
- Fácil de testar e ajustar
- Baixo consumo de tokens

### ✅ Casos de Uso:

- Perguntas rápidas
- Definições básicas
- Traduções simples
- Exemplos rápidos de código

### ✅ Limitações:

- Pode gerar respostas genéricas
- Pouco controle sobre o tom e formato da saída


## 2️⃣ Prompt Composto

### ✅ Definição:

Prompt que inclui **várias instruções, condições ou exemplos dentro de uma mesma solicitação**. Pode conter múltiplos comandos ou etapas.

### ✅ Exemplo:

> **"Explique o que é Machine Learning de forma simples, depois dê um exemplo prático de uso em uma empresa de e-commerce, e por fim sugira duas fontes para aprofundamento."**

### ✅ Características:

- Inclui múltiplas tarefas ou camadas
- Controla melhor o tom, a estrutura e o conteúdo
- Pode incluir exemplos dentro do próprio prompt (few-shot learning)

### ✅ Casos de Uso:

- Geração de conteúdo com estrutura definida (ex: blog posts)
- Respostas mais detalhadas e com múltiplas partes
- Conversas multi-etapas (ex: triagem + sugestão + ação)

### ✅ Limitações:

- Custo maior em tokens
- Requer mais cuidado com a ordem das instruções
- Pode confundir o modelo se mal estruturado


## 3️⃣ Prompt Estruturado

### ✅ Definição:

Prompt com **formatação explícita**, geralmente incluindo **campos, delimitadores ou instruções de output no formato JSON, Markdown, listas, etc.**

### ✅ Exemplo:

> **Prompt:**

```
Responda utilizando o seguinte formato JSON:
{
  "definicao": "",
  "exemplo": "",
  "fontes_recomendadas": ["", ""]
}

Pergunta: O que é Machine Learning?
```

### ✅ Características:

- Controle total sobre o formato de saída
- Ideal para integração com APIs e automações (ex: n8n, Zapier, RPA)
- Fácil de processar por máquinas (parseável)

### ✅ Casos de Uso:

- Geração de relatórios estruturados
- Integração com sistemas (ex: salvar outputs em banco de dados)
- Respostas com campos fixos para leitura programática

### ✅ Limitações:

- Requer domínio na formatação do prompt
- Se o prompt estiver mal feito, o modelo pode "quebrar" o formato


## ✅ Comparativo Rápido

|Tipo|Complexidade|Controle de Saída|Custo em Tokens|Casos de Uso|
|---|---|---|---|---|
|Simples|Baixa|Baixo|Baixo|Respostas diretas|
|Composto|Média|Médio|Médio|Textos completos, múltiplas tarefas|
|Estruturado|Alta|Alto|Alto|Integrações, relatórios, automações|


## ✅ Dicas de Ouro para o Engenheiro de Prompt

- **Comece simples**, evolua para compostos e, só depois, para estruturados conforme a necessidade.
- Use **exemplos de output no próprio prompt** quando quiser forçar um formato.
- Se o modelo errar o formato, aplique **instruções reforçadas**, como:  
    _"Atenção: Responda apenas no formato JSON. Não inclua explicações adicionais."_


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/engenharia-de-prompt/2-design-de-prompts-eficientes/tipos-de-prompts-simples-compostos-estruturados/)

<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>