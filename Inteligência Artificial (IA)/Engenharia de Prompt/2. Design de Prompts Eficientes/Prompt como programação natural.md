### [Sumário](<https://maksoud.github.io/Sumário>)

# Prompt como Programação Natural: Princípios de Clareza, Contexto e Objetivo


## 📌 Introdução

No universo da **engenharia de prompt**, um dos conceitos mais poderosos é enxergar o prompt como uma forma de **"programação natural"**.

Isso significa tratar o prompt como **um código em linguagem humana**, com a mesma atenção que um programador teria ao escrever uma função de software.

A diferença?  
👉 Em vez de falar com uma máquina por meio de linguagens como Python ou JavaScript, estamos programando um **modelo de linguagem (LLM)** usando o próprio idioma (Português, Inglês etc.).


## 📐 Os 3 Princípios-Chave para um Prompt Eficiente

### ✅ 1. Clareza

**Regra:** O modelo só entende o que você pede de forma clara.

Se o prompt for vago, ambíguo ou genérico, a IA irá responder de forma igualmente imprecisa.

|❌ Ruim|✅ Bom|
|---|---|
|"Fale sobre vendas."|"Escreva um texto de até 150 palavras explicando 3 técnicas de vendas para lojas de e-commerce."|

**Dicas para garantir clareza:**

- Use frases curtas
- Evite jargões desnecessários (a menos que o público-alvo exija)
- Inclua instruções diretas como: _“Liste...”, “Explique...”, “Resuma...”_


### ✅ 2. Contexto

**Regra:** Quanto mais contexto você dá, melhor o modelo entende.

O LLM **não tem memória longa entre chamadas na API**, então **você precisa fornecer o máximo de contexto dentro do próprio prompt**.

|❌ Ruim|✅ Bom|
|---|---|
|"Me ajude a criar um texto de marketing."|"Você é um especialista em marketing digital. O público são pequenos empreendedores no setor de moda. O objetivo é vender uma nova coleção de verão. O texto deve ser breve e usar tom motivacional."|

**Exemplos de contexto que você pode fornecer:**

- Público-alvo
- Tom desejado
- Objetivo da comunicação
- Dados da empresa/produto
- Exemplos anteriores de saída desejada


### ✅ 3. Objetivo

**Regra:** O modelo precisa saber claramente **o que você espera como resultado final**.

|❌ Ruim|✅ Bom|
|---|---|
|"Fale sobre IA."|"Crie um artigo de blog com título, introdução, 3 tópicos e uma conclusão, explicando como pequenas empresas podem usar IA para melhorar o atendimento ao cliente."|

**Dicas para definição de objetivo:**

- Informe o formato esperado (ex: lista, artigo, JSON)
- Especifique se quer linguagem formal, técnica ou informal
- Defina limites de tamanho, se for relevante (número de palavras, parágrafos, tokens)


## 🛠️ Modelo de Estrutura de um Prompt Programável

```
[Persona/Contexto]: Você é um [especialista / função / perfil].
[Tarefa]: Sua tarefa é [descrição clara da tarefa].
[Formato de Saída]: Apresente o resultado em [formato esperado].
[Restrições]: Limite a resposta a [tamanho, linguagem, etc].
[Exemplo de Saída (opcional)]: Exemplo de como deve ser o output.
```


## ✅ Exemplo Completo de Prompt como Programação Natural:

> **Prompt:**  
> *"Você é um redator de marketing especializado em e-commerce. Sua tarefa é criar uma descrição de produto para um tênis esportivo. A saída deve ter:

1. Título (até 10 palavras)
2. Descrição (máximo 100 palavras)
3. Chamada para ação (1 frase direta)  
    Use linguagem inspiradora e focada em performance."*


## ✅ Conclusão

Adotar a mentalidade de **programador natural** na hora de criar prompts fará você entregar **instruções mais robustas, reutilizáveis e previsíveis**, evitando respostas incoerentes ou fora de contexto.

👉 Quanto mais o seu prompt parecer um **"briefing para um humano"**, melhor será o resultado.



<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>