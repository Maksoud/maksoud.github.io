### [Sumário](<https://maksoud.github.io/Sumário>)

# Integração com Sistemas Legados, APIs e RPA usando LLMs


## 📌 Introdução

Uma das áreas de maior crescimento para engenheiros de prompt é o uso de **LLMs integrados com sistemas corporativos**, como **sistemas legados**, **APIs** e **plataformas de RPA (Robotic Process Automation)**.

A combinação de LLMs com integrações permite que empresas automatizem processos complexos, conectem sistemas antigos a novas interfaces de IA e acelerem a transformação digital sem a necessidade de grandes reescritas de código legado.


## 🧱 Principais Cenários de Integração

### ✅ 1. **Interação com Sistemas Legados**

**O que são sistemas legados?**  
Softwares antigos ou obsoletos, muitas vezes sem APIs modernas, mas ainda críticos para o negócio (ex: ERP antigos, sistemas bancários, bancos de dados em mainframe).

**Como os LLMs ajudam:**

- Transformando respostas textuais de sistemas legados em respostas amigáveis para o usuário
- Criando camadas de tradução entre linguagem técnica e linguagem natural
- Gerando resumos, insights ou alertas com base em dados extraídos desses sistemas

**Exemplo de Prompt:**

> **Prompt:**  
> _"Você é um assistente corporativo. Transforme a seguinte saída de sistema legado em um resumo claro e amigável para o time de operações:"_


### ✅ 2. **Orquestração via APIs**

**O que é:**  
Usar LLMs para **gerar, processar ou interpretar dados recebidos de APIs corporativas**, como CRM, ERP, plataformas de vendas, etc.

**Como os LLMs ajudam:**

- Formatando respostas de API para linguagem humana
- Gerando inputs dinâmicos para chamadas de API
- Atuando como camada de NLP entre usuários e backends via API

**Exemplo de Prompt:**

> **Prompt:**  
> _"Com base na resposta JSON da API de vendas a seguir, gere um resumo de desempenho semanal, destacando o produto mais vendido e a região com maior faturamento."_


### ✅ 3. **Integração com Plataformas de RPA**

**O que é RPA:**  
Automação de tarefas repetitivas feitas por robôs de software (ex: UiPath, Automation Anywhere, Power Automate).

**Como os LLMs ajudam:**

- Interpretando e respondendo e-mails antes de iniciar fluxos de RPA
- Classificando documentos antes de ações de automação
- Gerando respostas automáticas após execução de tarefas
- Ajudando a construir fluxos de RPA com geração automática de scripts ou passos

**Exemplo de Prompt:**

> **Prompt:**  
> _"Classifique o e-mail abaixo como: Pedido, Reclamação ou Consulta. Se for um Pedido, gere um resumo para o RPA iniciar o processo de faturamento."_


## ✅ Fluxo Prático de Integração com LLM + API + RPA (Exemplo Real)

1. **Usuário envia uma solicitação em linguagem natural:**  
    _"Quero saber o status da minha última fatura."_
2. **LLM interpreta o pedido e transforma em consulta API:**  
    Chamada à API de ERP com ID do cliente
3. **API devolve resposta técnica:**  
    `{"fatura": "Pendente", "vencimento": "10/06/2025"}`
4. **LLM gera resposta humanizada:**  
    _"Sua última fatura está pendente e vence em 10 de junho de 2025."_
5. **Se necessário, um RPA pode iniciar um processo de cobrança ou envio de segunda via.**


## ✅ Benefícios Empresariais

|Benefício|Impacto|
|---|---|
|Modernização sem reescrever sistemas antigos|Evita custos de migração|
|Melhor experiência para o usuário|Respostas em linguagem natural|
|Aumento de produtividade|Redução de tarefas manuais|
|Redução de erros humanos|Processos mais padronizados e rastreáveis|


## ✅ Riscos e Cuidados

|Risco|Mitigação|
|---|---|
|Exposição de dados sensíveis em prompts|Uso de máscaras ou anonimização|
|Dependência de múltiplas integrações|Monitoramento de falhas de API/RPA|
|Latência (respostas lentas em fluxos muito longos)|Divisão de fluxos e otimização de chamadas|


## ✅ Boas Práticas de Prompt Engineering para Integrações:

✔ Deixar claro o **formato de entrada esperado** (ex: JSON, XML, CSV)  
✔ Definir o **formato de saída esperado**, especialmente para leitura por robôs RPA  
✔ Garantir instruções de **fallback e tratamento de erro** dentro do fluxo  
✔ Testar **respostas com diferentes cenários de API (sucesso, erro, vazio)**  
✔ Documentar o prompt para manutenção futura


## ✅ Conclusão

Integrar LLMs com **sistemas legados**, **APIs** e **RPA** abre um mundo de possibilidades para empresas de tecnologia que querem modernizar processos com rapidez e baixo custo.

Como engenheiro de prompt, sua responsabilidade será garantir que o **modelo entenda as entradas técnicas**, **converta as saídas de forma amigável** e **funcione de forma confiável dentro do fluxo de automação.**



<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>