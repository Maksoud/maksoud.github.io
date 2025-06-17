### [Sumário](<https://maksoud.github.io/Sumário>)

# Ferramentas e Plataformas de Integração: OpenAI API (ChatGPT, Assistants, GPTs)


## 📌 Introdução

A **OpenAI API** é uma das principais portas de entrada para empresas que desejam integrar **modelos de linguagem (LLMs)** em seus sistemas, produtos e processos.

Ela oferece diferentes formas de interação, cada uma com características próprias:

* **ChatGPT API (API tradicional)**
* **Assistants API (orquestração com ferramentas e memória)**
* **GPTs Customizados (via ChatGPT Web App)**

Como engenheiro de prompt, entender cada uma dessas formas é essencial para escolher a melhor estratégia de integração para o seu projeto.


## 1️⃣ ChatGPT API (API tradicional)

### ✅ O que é:

Uma API RESTful onde você envia **prompts** e recebe respostas, de forma simples e direta.

**Modelos mais usados via API:**

* `gpt-4o`
* `gpt-4-turbo`
* `gpt-3.5-turbo`

### ✅ Como funciona:

Você faz uma requisição POST para o endpoint `/v1/chat/completions`, enviando:

* Mensagens no formato "role" (user, assistant, system)
* Parâmetros como `temperature`, `max_tokens`, `top_p`, entre outros

### ✅ Exemplo de Payload:

```json
{
  "model": "gpt-4o",
  "messages": [
    {"role": "system", "content": "Você é um assistente de suporte técnico."},
    {"role": "user", "content": "Como posso redefinir minha senha?"}
  ],
  "temperature": 0.7
}
```

### ✅ Casos de uso:

* Chatbots
* Geração de relatórios
* Respostas a perguntas
* Automação de conteúdo
* Processos com **prompt simples ou composto**


## 2️⃣ Assistants API (API de Assistentes)

### ✅ O que é:

Uma camada mais avançada da OpenAI, lançada em 2023, que permite criar **assistentes personalizados com memória, ferramentas e arquivos de contexto**.

### ✅ Principais Recursos:

* **Memória de longo prazo (beta)**: O assistente pode lembrar interações passadas.
* **Ferramentas integradas:**

  * **Code interpreter** (Python para cálculos, análises)
  * **Retrieval** (busca de informações em arquivos enviados)
  * **Funções customizadas (function calling)**

### ✅ Como funciona:

Você cria um **"assistant"** com configurações específicas:

* Nome
* Instruções de comportamento
* Ferramentas habilitadas

Depois, faz interações com **threads** e **runs**, mantendo um histórico de contexto.

### ✅ Casos de uso:

* Assistentes de BI com análise de arquivos
* Chatbots com contexto de longo prazo
* Ferramentas internas para times (ex: suporte, RH, vendas)

### ✅ Exemplo de Aplicação:

* Analisar automaticamente uma planilha de vendas enviada pelo usuário
* Permitir que um usuário pergunte sobre interações passadas e o assistente lembre


## 3️⃣ GPTs Customizados (ChatGPT Web App)

### ✅ O que é:

Uma opção **no ambiente web do ChatGPT (chat.openai.com)** onde você cria **GPTs personalizados sem código**, apenas configurando o comportamento via interface gráfica.

### ✅ Recursos:

* Personalização de instruções (behavior instructions)
* Upload de arquivos como fonte de contexto
* Integração com APIs externas via API calls (opcional para usuários avançados)
* Compartilhamento via link público ou privado

### ✅ Casos de uso:

* Criação de assistentes internos sem precisar programar
* Suporte a clientes com regras pré-definidas
* GPTs específicos para geração de conteúdo, tradução, etc.

### ✅ Limitações:

* Não é programável via API tradicional
* Uso restrito ao ambiente da OpenAI Web App


## ✅ Comparativo das Opções OpenAI API

| Recurso               | ChatGPT API              | Assistants API                                | GPTs Customizados       |
| --------------------- | ------------------------ | --------------------------------------------- | ----------------------- |
| Acesso                | Programático via REST    | Programático via Assistants endpoint          | Web apenas              |
| Memória               | Apenas no contexto atual | Threads e runs com histórico                  | Limitada ao chat aberto |
| Ferramentas avançadas | Não                      | Code Interpreter, Retrieval, Function Calling | Parcial                 |
| Personalização        | Via prompt               | Via assistant config                          | Via interface web       |
| Melhor para           | Chatbots simples         | Assistentes complexos                         | Usuários não técnicos   |


## ✅ Conclusão

A **OpenAI API** oferece diferentes camadas de integração para empresas. Como engenheiro de prompt, a sua missão é **entender o problema de negócio e escolher a ferramenta certa para cada contexto**.

| Cenário                                         | Solução Indicada  |
| ----------------------------------------------- | ----------------- |
| Preciso de API simples                          | ChatGPT API       |
| Quero memória + ferramentas                     | Assistants API    |
| Preciso criar um assistente rápido e sem código | GPTs Customizados |


<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>