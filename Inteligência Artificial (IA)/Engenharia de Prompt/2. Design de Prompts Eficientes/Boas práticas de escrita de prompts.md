### [Sumário](<https://maksoud.github.io/Sumário>)

# Boas práticas de escrita de prompts

*Como Escrever Instruções Claras, Eficientes e Controláveis para LLMs*

## 🎯 Por que boas práticas são importantes?

Uma boa engenharia de prompt **reduz erros**, **melhora a qualidade das respostas** e **diminui o custo em tokens**. Quanto melhor o seu prompt, **menos o modelo vai "alucinar"** e mais consistente será a resposta.

Lembre-se: **o modelo só responde bem aquilo que é perguntado bem**.


## Princípios Fundamentais de um Bom Prompt

### ✅ 1. **Seja Claro e Objetivo**

- Use instruções diretas, sem ambiguidade.
- Especifique exatamente o que espera como resposta.

**Exemplo ruim:**  
_"Me fale um pouco sobre marketing."_  
**Exemplo bom:**  
_"Explique o conceito de marketing digital em até 3 parágrafos curtos, com foco em redes sociais."_

### ✅ 2. **Defina o Papel ou Persona**

Indicar o papel que o modelo deve assumir pode melhorar a coerência.

**Exemplo:**  
_"Você é um especialista em SEO com 10 anos de experiência. Responda de forma técnica e objetiva."_

### ✅ 3. **Especifique o Formato da Resposta**

Peça o formato exato: lista, tabela, JSON, Markdown, etc.

**Exemplo:**  
_"Responda utilizando uma tabela com as colunas: Conceito | Exemplo | Aplicação em Negócios."_

### ✅ 4. **Forneça Contexto**

Quanto mais contexto relevante, melhor a qualidade da resposta.

**Exemplo:**  
Antes de perguntar sobre "otimização de campanha", explique:  
_"Estou criando uma campanha para o Instagram, com foco em geração de leads para um SaaS de gestão financeira. Quais as melhores estratégias?"_

### ✅ 5. **Use Exemplos (Few-shot Learning)**

Quando quiser um estilo específico, **dê exemplos dentro do prompt**.

**Exemplo:**  
*"Exemplo de saída esperada:

- Título: …
- Corpo: …  
    Agora, gere um novo exemplo sobre o tema X."*

### ✅ 6. **Defina Restrições Claras**

Se você quer limitar o tamanho, o tom ou o tipo de conteúdo, deixe isso explícito.

|Exemplo de restrição|Como pedir|
|---|---|
|Tamanho|"Resposta de até 150 palavras."|
|Tom|"Use linguagem simples e amigável."|
|Tipo|"Não inclua links externos."|

### ✅ 7. **Ordem Lógica nas Instruções**

Estruture o prompt seguindo a ordem natural de raciocínio:

1. Contexto
2. Tarefa
3. Formato
4. Restrições

### ✅ 8. **Peça Revisões e Melhorias**

Se o output não for ideal, adicione camadas de revisão ao prompt.

**Exemplo:**  
_"Depois de gerar a resposta, revise para garantir que não haja termos técnicos desconhecidos para um público leigo."_

### ✅ 9. **Inclua Exemplos de Fracasso (Se necessário)**

Se você já testou um prompt que deu errado, inclua no novo prompt:  
_"Evite respostas como: [exemplo de saída indesejada]"_

### ✅ 10. **Itere Sempre**

- Faça pequenas variações.
- Compare resultados.
- Documente as versões que geram melhor desempenho.

## 📌 Checklist Rápido de Boas Práticas:

✔ Clareza de objetivo  
✔ Definição de papel/persona  
✔ Contexto suficiente  
✔ Formato de saída definido  
✔ Restrições claras  
✔ Exemplos (quando necessário)  
✔ Iteração e teste constante

## ✅ Exemplo Completo de Prompt com Boas Práticas:

> **Prompt:**  
> *"Você é um especialista em marketing digital com foco em e-commerce. Sua tarefa é criar um e-mail promocional para uma campanha de liquidação. A resposta deve conter:

1. Um título chamativo com até 10 palavras
2. Um corpo de e-mail com no máximo 150 palavras
3. Uma chamada para ação clara  
    Utilize um tom amigável e comercial. Não inclua emojis."*



<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>