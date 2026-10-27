# Limitações e Potencial dos LLMs – O que um Engenheiro de Prompt Precisa Saber


## 📌 Introdução

Os **LLMs (Large Language Models)**, como o GPT-4, Claude 3 e Gemini, são hoje uma revolução na forma como interagimos com tecnologia. No entanto, para aplicar essas ferramentas de forma estratégica nas empresas, é fundamental entender tanto o **potencial** quanto as **limitações** desses modelos.

Como engenheiro de prompt, seu papel será **maximizar o potencial** e **mitigar os riscos** de uso.

## Potencial dos LLMs

### ✅ 1. **Versatilidade Multitarefa**

Os LLMs podem realizar uma enorme variedade de tarefas com o mesmo modelo base:

| Tipo de tarefa     | Exemplo                                   |
| ------------------ | ----------------------------------------- |
| Geração de texto   | Redação de e-mails, descrições de produto |
| Suporte ao cliente | Respostas a FAQs                          |
| Análise de dados   | Resumos de planilhas                      |
| Tradução           | De inglês para português, por exemplo     |
| Programação        | Geração de código                         |

### ✅ 2. **Alta Capacidade de Adaptação via Prompt**

Com uma boa engenharia de prompt, o mesmo modelo pode:

* Mudar de tom (formal, técnico, humorado)
* Simular papéis (ex: advogado, atendente, professor)
* Resolver problemas complexos com técnicas como **Chain-of-Thought** ou **RAG (Retrieval-Augmented Generation)**

### ✅ 3. **Automação e Redução de Custos**

Empresas estão economizando tempo e dinheiro usando LLMs para:

* Automatizar atendimento
* Gerar relatórios
* Criar conteúdo em larga escala

### ✅ 4. **Aceleração de Desenvolvimento**

LLMs estão sendo usados por times de tecnologia para:

* Refatorar código
* Criar documentação
* Gerar testes unitários
* Ajudar no brainstorming de soluções técnicas

### ✅ 5. **Facilidade de Integração**

Modelos como GPT-4, Claude e Gemini possuem **APIs bem documentadas**, fáceis de integrar com sistemas empresariais, CRMs, ferramentas de BI, etc.

## ⚠️ Limitações dos LLMs

### ❌ 1. **Alucinação (Hallucination)**

O modelo pode gerar respostas **falsas, imprecisas ou inventadas**, mesmo que a forma pareça confiante e bem escrita.

**Exemplo de risco:**
Dar uma recomendação médica incorreta ou fornecer um dado técnico errado.

**Como mitigar:**

* Uso de embeddings + RAG
* Prompt claro pedindo fontes ou validação
* Revisão humana em processos críticos

### ❌ 2. **Memória de Curto Prazo (Context Window)**

O modelo só consegue "lembrar" de um número limitado de tokens por interação.

| Modelo      | Limite médio             |
| ----------- | ------------------------ |
| GPT-4 Turbo | Até 128k tokens          |
| Claude 3    | Até 200k tokens          |
| Mistral     | Varia de 8k a 32k tokens |

**Impacto:**
Diálogos ou contextos muito longos podem ser esquecidos ou truncados.

**Solução:**

* Dividir tarefas
* Usar ferramentas como LangChain para gerenciar histórico

### ❌ 3. **Falta de Conhecimento Atualizado**

Se o modelo não for conectado à internet (como via API com browsing ou via RAG), ele **só saberá informações até a data do seu último treinamento**.

**Exemplo:**
O ChatGPT só conhece eventos até 2023 (salvo uso com browsing).

**Solução:**

* Uso de integrações com bases atualizadas
* Implementação de RAG

### ❌ 4. **Sensibilidade a Prompt**

Mudanças pequenas no prompt podem causar **grandes variações na resposta**.

**Exemplo:**
Prompt 1: "Liste 3 benefícios" → Resposta direta
Prompt 2: "Me fale um pouco sobre os benefícios" → Resposta extensa e genérica

**Solução:**

* Teste A/B de prompts
* Versionamento de prompts
* Uso de prompt templates

### ❌ 5. **Custo Operacional**

Modelos maiores como GPT-4 e Claude 3 podem gerar **custo por token elevado**, principalmente em aplicações com grande volume de requisições.

**Exemplo de custo (simulado):**

* GPT-4 Turbo: \$0.01 por 1.000 tokens de entrada

**Solução:**

* Otimização de prompts para reduzir tokens
* Uso de modelos menores (Mistral, Llama) quando possível

### ❌ 6. **Riscos Éticos e de Privacidade**

* Vazamento de dados sensíveis via prompts
* Geração de conteúdo tendencioso ou ofensivo
* Uso indevido em engenharia social

**Solução:**

* Políticas de governança de IA
* Filtragem de conteúdo
* Anonimização de dados antes de enviar ao modelo

## Conclusão

#### **Potencial:**
LLMs são ferramentas poderosas, capazes de transformar processos empresariais com geração de conteúdo, análise de dados e atendimento automatizado.

#### **Limitações:**
Alucinação, custo, contexto limitado e sensibilidade ao prompt são desafios reais que o engenheiro de prompt precisa saber contornar.

#### **Papel do Engenheiro de Prompt:**
Saber explorar o potencial **maximizando resultados** e **minimizando riscos** através de boas práticas de design, teste, validação e governança de prompts.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/engenharia-de-prompt/1-fundamentos-da-engenharia-de-prompt/limitacoes-e-potencial-dos-llms/)

<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>