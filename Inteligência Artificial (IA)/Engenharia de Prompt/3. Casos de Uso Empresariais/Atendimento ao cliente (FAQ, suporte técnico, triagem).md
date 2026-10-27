# Atendimento ao Cliente com LLMs (FAQ, Suporte Técnico, Triagem)


## 📌 Introdução

O **Atendimento ao Cliente** é uma das áreas mais impactadas pelo uso de **Modelos de Linguagem de Grande Escala (LLMs)** como o ChatGPT, Claude ou Gemini.

Empresas de tecnologia estão usando LLMs para:

- Reduzir o volume de tickets manuais
- Melhorar a experiência do usuário
- Agilizar a triagem e priorização de chamados
- Oferecer respostas mais rápidas e personalizadas

Como engenheiro de prompt, sua função será **criar prompts que conduzam o modelo a responder com precisão, clareza e empatia**.


## 🛠️ Principais Aplicações em Atendimento

### ✅ 1. **Respostas a FAQs (Perguntas Frequentes)**

### Objetivo:

Automatizar respostas para dúvidas recorrentes.

### Exemplos de FAQ:

- Como alterar minha senha?
- Qual o prazo de entrega?
- Como cancelar um serviço?

### Exemplo de Prompt para FAQ:

> **Prompt:**  
> _"Você é um assistente de suporte técnico. Responda a pergunta do cliente de forma objetiva, amigável e com um passo a passo, quando necessário. Pergunta: 'Como faço para resetar minha senha?'"_

### Boas práticas:

- Fornecer contexto sobre os serviços da empresa
- Definir tom (formal, casual, técnico)
- Limitar a resposta a 100-150 palavras para manter objetividade


### ✅ 2. **Suporte Técnico de Primeiro Nível**

### Objetivo:

Ajudar o cliente a solucionar problemas simples antes de abrir um chamado técnico.

### Exemplos de Problemas:

- Erros de login
- Problemas de conexão
- Dúvidas sobre configuração inicial

### Exemplo de Prompt para Suporte Técnico:

> **Prompt:**  
> _"Você é um agente de suporte técnico de uma empresa de software SaaS. Ajude o usuário a resolver problemas de login. Responda com uma lista numerada de soluções possíveis, começando pelas mais comuns. Inclua instruções claras e links úteis."_

### Boas práticas:

- Usar linguagem clara e sem jargões técnicos
- Fornecer múltiplas soluções possíveis (solução 1, 2, 3…)
- Incluir avisos de quando o usuário deve abrir um chamado (ex: _“Se nenhuma das opções resolver, por favor abra um ticket”_)


### ✅ 3. **Triagem de Chamados**

### Objetivo:

Analisar a solicitação inicial do cliente e **classificar automaticamente o tipo de problema**, **prioridade** e **departamento responsável**.

### Exemplo de Prompt para Triagem:

> **Prompt:**  
> _"Classifique o ticket a seguir com base nas categorias: Login, Pagamento, Bug, Sugestão ou Outro. Também defina a prioridade como Alta, Média ou Baixa com base na urgência implícita no texto. Ticket: 'O sistema está fora do ar e não consigo acessar minha conta há horas!'"_

### Saída esperada (formato JSON):

```json
{
  "categoria": "Login",
  "prioridade": "Alta"
}
```

### Boas práticas:

- Definir categorias fixas
- Criar prompts com exemplos de classificação (few-shot)
- Padronizar o formato de saída (ex: JSON para integração com Help Desk)


## ✅ Benefícios para a Empresa

|Benefício|Impacto|
|---|---|
|Redução de tempo de atendimento|Menos sobrecarga para a equipe de suporte|
|Padronização de respostas|Experiência mais consistente para o cliente|
|Redução de custos|Menor necessidade de atendimento humano em primeiro nível|
|Melhor triagem|Chamados críticos ganham prioridade real|


## ✅ Riscos e Cuidados

|Risco|Mitigação|
|---|---|
|Respostas incorretas ou perigosas|Revisão humana em casos críticos|
|Tom inadequado (frio ou robótico demais)|Ajuste de prompt para tom mais empático|
|Vazamento de informações sensíveis|Nunca incluir dados sigilosos nos prompts enviados ao LLM|


## ✅ Conclusão

O uso de LLMs para **FAQ, Suporte Técnico e Triagem** já está gerando **economia de tempo e custos** em empresas de tecnologia.

Como engenheiro de prompt, o seu diferencial será:

- Criar prompts que gerem **respostas objetivas e seguras**
- Garantir **consistência de tom e formato**
- Testar diferentes versões de prompts para encontrar o equilíbrio entre custo (tokens) e qualidade de atendimento


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/engenharia-de-prompt/3-casos-de-uso-empresariais/atendimento-ao-cliente-faq-suporte-tecnico-triagem/)

<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>