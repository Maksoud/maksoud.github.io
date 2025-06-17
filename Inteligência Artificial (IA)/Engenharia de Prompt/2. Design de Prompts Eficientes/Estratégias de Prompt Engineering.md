### [Sumário](<https://maksoud.github.io/Sumário>)

# Estratégias de Prompt Engineering: Chain of Thought, Zero-Shot, Few-Shot e Instruções Aninhadas

## 📌 Introdução

Além de escrever prompts claros, o engenheiro de prompt pode aplicar **estratégias avançadas de prompting** para melhorar a qualidade das respostas de um LLM.

Essas estratégias ajudam o modelo a:

- Raciocinar melhor
- Generalizar melhor para tarefas novas
- Responder com mais contexto
- Diminuir erros e alucinações

A seguir, vamos detalhar 4 das mais importantes:


## 1️⃣ Zero-shot Prompting (Prompt sem exemplo)

### ✅ O que é:

O modelo recebe **apenas uma instrução clara**, sem nenhum exemplo de como a resposta deve ser.

### ✅ Exemplo:

> **Prompt:**  
> _"Resuma o seguinte texto em até 3 frases."_

**📌 Quando usar:**

- Tarefas simples
- Quando o modelo já tem bom desempenho na tarefa
- Quando você quer economizar tokens

**✅ Vantagem:**  
Rápido e econômico

**❌ Limitação:**  
Mais chance de respostas vagas ou genéricas em tarefas complexas


## 2️⃣ Few-shot Prompting (Prompt com alguns exemplos)

### ✅ O que é:

O prompt inclui **exemplos explícitos de input e output**, para ensinar o modelo como responder.

### ✅ Exemplo:

> **Prompt:**

```
Exemplo 1:
Entrada: "Gato"
Saída: "Um animal de estimação doméstico que costuma miar."

Exemplo 2:
Entrada: "Maçã"
Saída: "Uma fruta geralmente vermelha ou verde, com sabor adocicado."

Agora, responda para:
Entrada: "Cachorro"
```

**📌 Quando usar:**

- Quando o modelo precisa aprender o formato ou o tom desejado
- Tarefas que envolvem estilo, formato específico ou tipo de linguagem

**✅ Vantagem:**  
Gera respostas mais controladas e consistentes

**❌ Limitação:**  
Gasta mais tokens (mais caro)  
Requer curadoria dos exemplos


## 3️⃣ Chain of Thought (Cadeia de Pensamento)

### ✅ O que é:

O prompt orienta o modelo a **raciocinar passo a passo antes de dar a resposta final**, especialmente útil para **problemas de lógica, matemática ou interpretação complexa**.

### ✅ Exemplo:

> **Prompt:**  
> _"Resolva o problema a seguir passo a passo:  
> Se Maria tem 3 maçãs e compra mais 2, quantas ela tem no total?"_

**Saída esperada:**

```
Passo 1: Maria tem 3 maçãs.
Passo 2: Ela compra mais 2 maçãs.
Passo 3: 3 + 2 = 5.
Resposta final: Maria tem 5 maçãs.
```

**📌 Quando usar:**

- Problemas de lógica
- Cálculos matemáticos
- Raciocínio analítico
- Perguntas que exigem várias etapas de pensamento

**✅ Vantagem:**  
Melhora a precisão em problemas complexos  
Força o modelo a "pensar antes de responder"

**❌ Limitação:**  
Respostas mais longas  
Consome mais tokens


## 4️⃣ Instruções Aninhadas (Nested Instructions)

### ✅ O que é:

Criar prompts com **várias camadas de instrução dentro de um único prompt**, geralmente com **etapas internas** ou **regras específicas para cada parte da resposta**.

### ✅ Exemplo:

> **Prompt:**  
> *"Sua tarefa tem 3 etapas:

1. Leia o texto a seguir.
2. Identifique os principais tópicos em forma de lista.
3. Escreva um resumo de até 100 palavras.  
    Não avance para a etapa seguinte sem concluir a anterior."*

**📌 Quando usar:**

- Tarefas multifásicas
- Quando você precisa controlar o fluxo da resposta
- Relatórios, análises, resumos com critérios claros

**✅ Vantagem:**  
Controle detalhado sobre o comportamento do modelo  
Evita que o LLM pule etapas ou misture formatos

**❌ Limitação:**  
Pode ser sensível à ordem das instruções  
Requer testes e refinamento


## ✅ Comparativo das Estratégias:

|Estratégia|Complexidade|Consumo de Tokens|Melhor uso|
|---|---|---|---|
|Zero-shot|Baixa|Baixo|Tarefas simples|
|Few-shot|Média|Médio|Controle de estilo e formato|
|Chain of Thought|Alta|Médio-Alto|Problemas que exigem raciocínio|
|Instruções Aninhadas|Alta|Alto|Tarefas com múltiplas etapas|


## ✅ Conclusão:

Como engenheiro de prompt, sua habilidade será **saber escolher e combinar essas estratégias** conforme o contexto da aplicação empresarial:

- Para tarefas rápidas: Zero-shot
- Para formatação e estilo: Few-shot
- Para lógica: Chain of Thought
- Para tarefas complexas: Instruções Aninhadas



<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>