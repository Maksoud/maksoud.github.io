### [Sumário](<https://maksoud.github.io/Sumário>)

# Noções de Uso de LLMs via Código (Python/JavaScript) e Plataformas Low-code (n8n, Zapier, Make)


## 📌 Introdução

Ao trabalhar com LLMs como ChatGPT, Claude ou Gemini, você pode **integrar os modelos de duas formas principais:**

* **Programando com código (Python / JavaScript)**
* **Usando ferramentas low-code / no-code (n8n, Zapier, Make)**

Como engenheiro de prompt, entender ambas as abordagens permite que você **se adapte ao nível técnico e à infraestrutura da empresa**.


## 🧱 1. Uso via Código (Python / JavaScript)

### ✅ Por que usar?

* Maior controle sobre o fluxo de execução
* Possibilidade de customizar integrações mais complexas
* Processamento de grandes volumes de dados
* Criação de pipelines próprios

### ✅ Exemplo: Consumindo a API da OpenAI em **Python**

```python
import openai

openai.api_key = 'YOUR_API_KEY'

response = openai.ChatCompletion.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "Você é um assistente financeiro."},
    {"role": "user", "content": "Me dê um resumo das vendas do mês."}
  ],
  temperature=0.7
)

print(response.choices[0].message.content)
```


### ✅ Exemplo: Consumindo a API da OpenAI em **JavaScript (Node.js)**

```javascript
const { OpenAI } = require("openai");

const openai = new OpenAI({
  apiKey: 'YOUR_API_KEY'
});

async function runChat() {
  const completion = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: "Você é um assistente de marketing." },
      { role: "user", content: "Crie um título para um e-mail promocional sobre descontos." }
    ],
    temperature: 0.7,
  });

  console.log(completion.choices[0].message.content);
}

runChat();
```


### ✅ Casos de Uso via Código:

* Automação de alto volume (processamento de milhares de inputs)
* Integração com sistemas internos via backend
* Criação de APIs personalizadas
* Geração de relatórios customizados

### ✅ Vantagens:

✔ Alta flexibilidade
✔ Controle total sobre erros, logs e performance
✔ Integração com bancos de dados, autenticações, etc.

### ✅ Limitações:

❌ Requer conhecimento técnico de programação
❌ Mais complexo para manutenção


## 🧱 2. Uso via Plataformas Low-Code / No-Code (n8n, Zapier, Make)

### ✅ Por que usar?

* Rápida implementação
* Não precisa de programadores
* Ideal para MVPs, automações simples e validação de conceitos
* Fácil integração com centenas de serviços


### ✅ Exemplo de Fluxo no **n8n:**

**Objetivo:** Responder automaticamente a mensagens recebidas via formulário de site

**Fluxo:**

1. **Trigger:** Novo formulário no site (Webhook ou Google Forms)
2. **Node:** OpenAI API (preenchendo o prompt via campo dinâmico)
3. **Node:** Enviar resposta automática por e-mail

**Prompt usado no Node OpenAI:**

> *"Gere uma resposta educada e personalizada para o seguinte texto recebido: {{\$json\["mensagem"]}}"*


### ✅ Exemplo de Fluxo no **Zapier:**

**Fluxo:**

1. **Trigger:** Novo e-mail recebido no Gmail
2. **Action:** Enviar conteúdo para o ChatGPT API via Webhook
3. **Action:** Criar rascunho de resposta no Gmail


### ✅ Exemplo de Fluxo no **Make:**

**Fluxo:**

1. Novo registro no Google Sheets
2. ChatGPT gera uma análise dos dados
3. Publicação automática em um canal do Slack


### ✅ Casos de Uso via Low-Code:

* Respostas automáticas
* Geração de conteúdos simples
* Triagem de dados
* Automatização de tarefas administrativas

### ✅ Vantagens:

✔ Rápido de configurar
✔ Menor custo de desenvolvimento inicial
✔ Ideal para times não técnicos

### ✅ Limitações:

❌ Menor controle sobre tratamento de erro
❌ Difícil escalar para grandes volumes
❌ Limitações de personalização complexa (comparado ao uso via código)


## ✅ Comparativo: Código vs. Low-Code

| Critério          | Código (Python/JS)   | Low-Code (n8n, Zapier, Make) |
| ----------------- | -------------------- | ---------------------------- |
| Controle técnico  | Total                | Limitado                     |
| Facilidade de uso | Requer desenvolvedor | Intuitivo, drag-and-drop     |
| Escalabilidade    | Alta                 | Limitada                     |
| Custo inicial     | Alto                 | Baixo                        |
| Melhor para       | Projetos grandes     | Automação rápida e simples   |


## ✅ Conclusão

Para um engenheiro de prompt que atua em empresas de tecnologia:

* **Para MVPs e automações rápidas:** Use **n8n**, **Zapier** ou **Make**
* **Para integrações críticas, de alta performance ou personalizadas:** Use **Python** ou **JavaScript** com a **OpenAI API**

O melhor cenário? Saber usar **ambos**, escolhendo a ferramenta mais adequada para cada projeto.



<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>