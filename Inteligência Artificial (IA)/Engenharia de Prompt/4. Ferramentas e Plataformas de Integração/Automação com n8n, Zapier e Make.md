### [Sumário](<https://maksoud.github.io/Sumário>)

# Automação com n8n, Zapier e Make: Orquestrando LLMs com Plataformas No-code/Low-code


## 📌 Introdução

Automação de processos é um dos **maiores casos de uso para LLMs em empresas**.

Ferramentas como **n8n**, **Zapier** e **Make (ex-Integromat)** permitem conectar o poder de modelos como GPT-4 com outras plataformas (CRM, ERP, Google Sheets, bancos de dados, APIs internas etc), **sem a necessidade de desenvolver sistemas complexos do zero**.

Como engenheiro de prompt, seu papel é **criar os prompts certos para cada etapa da automação**.


## 🛠️ Visão Geral das Ferramentas

|Plataforma|Características principais|Quando escolher|
|---|---|---|
|**n8n**|Open-source, altamente personalizável, suporta self-hosting|Projetos com controle de infraestrutura e custo|
|**Zapier**|Interface simples, mais de 6.000 integrações prontas|Pequenas e médias empresas, MVPs rápidos|
|**Make (Integromat)**|Automação visual com foco em fluxos mais complexos|Projetos que precisam de lógicas ramificadas e maior controle visual|


## 📈 Exemplos de Casos de Uso com LLMs

### ✅ 1. **Geração Automática de Respostas a E-mails (Zapier)**

**Fluxo:**

1. Disparo: Novo e-mail no Gmail
2. Passo: Enviar o conteúdo do e-mail para o ChatGPT via Webhook/API
3. Passo: Receber resposta e enviar de volta ao Gmail como rascunho de resposta

**Prompt usado:**

> _"Você é um assistente de atendimento. Leia o e-mail a seguir e gere uma resposta cordial, curta e objetiva."_


### ✅ 2. **Triagem Inteligente de Tickets (Make)**

**Fluxo:**

1. Entrada: Novo ticket criado no Zendesk
2. LLM: Enviar a descrição do ticket para o ChatGPT para classificar por prioridade e departamento
3. Saída: Atualizar o ticket no Zendesk com a classificação sugerida

**Prompt usado:**

> _"Classifique o seguinte ticket de suporte como: Alta, Média ou Baixa prioridade, e sugira o departamento responsável (Suporte Técnico, Financeiro, Comercial ou Outro)."_


### ✅ 3. **Geração de Resumos de Dados (n8n)**

**Fluxo:**

1. Entrada: Novo registro em planilha (Google Sheets ou banco de dados MySQL)
2. LLM: Enviar os dados para o ChatGPT para gerar um resumo diário de vendas
3. Saída: Publicar o resumo no Slack ou por e-mail

**Prompt usado:**

> _"Crie um resumo executivo das vendas do dia com os seguintes dados: [inserir tabela JSON]. Destaque os 3 produtos mais vendidos e o total de vendas."_


## ✅ Boas Práticas ao Integrar LLMs com Ferramentas de Automação

|Boas Práticas|Por que fazer|
|---|---|
|Sempre validar entradas|Para evitar respostas fora de contexto|
|Usar prompts com formatação JSON nas saídas|Facilita o parsing da resposta|
|Definir limites de tokens|Evita consumo excessivo da API|
|Tratar erros e timeouts|Principalmente em automações críticas|
|Versionar prompts|Para rastrear melhorias e evitar regressões|


## ✅ Benefícios Empresariais da Integração com LLMs

|Benefício|Impacto|
|---|---|
|Redução de tempo|Menos tarefas manuais para o time|
|Melhoria na comunicação|Respostas mais profissionais e consistentes|
|Escalabilidade|Processos que antes exigiam humanos podem ser feitos em massa|
|Flexibilidade|Pode ser usado em vários departamentos: Vendas, Suporte, Marketing, RH|


## ✅ Exemplos de Ações com LLMs Nessas Plataformas:

|Tarefa|Ferramenta mais indicada|
|---|---|
|Automação simples de e-mails|Zapier|
|Workflows com múltiplas ramificações|Make|
|Projetos com requisitos de privacidade e controle total|n8n (self-hosted)|


## ✅ Conclusão

Ao combinar **n8n**, **Zapier** ou **Make** com LLMs como ChatGPT, você amplia o poder das automações empresariais, criando **soluções inteligentes, escaláveis e com baixo tempo de implementação**.

Como engenheiro de prompt, sua responsabilidade será:

- **Projetar prompts bem estruturados para cada etapa**
- **Garantir que a IA interaja corretamente com os dados**
- **Otimizar o custo (tokens) e a performance**



<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>