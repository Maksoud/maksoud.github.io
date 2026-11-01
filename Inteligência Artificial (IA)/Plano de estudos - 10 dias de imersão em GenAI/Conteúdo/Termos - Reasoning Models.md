[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Reasoning Models

### 1. O que é

**Reasoning Models**, ou **modelos de raciocínio**, são modelos de IA projetados ou treinados para lidar melhor com problemas que exigem **várias etapas de raciocínio antes de chegar a uma resposta**.

Enquanto um LLM tradicional pode responder principalmente com base nos padrões aprendidos, um reasoning model é otimizado para dedicar mais processamento à resolução de problemas complexos.

Isso é especialmente útil em:
- matemática;
- programação;
- lógica;
- planejamento;
- análise de problemas complexos;
- tomada de decisão com várias etapas.

### 2. Como funciona, de forma intuitiva

Imagine a diferença entre estas duas perguntas:

> **"Qual é a capital da França?"**

É uma pergunta simples. Basta recuperar uma informação conhecida.

Agora:

> **"Tenho 3 projetos, 5 pessoas disponíveis, diferentes níveis de experiência e vários prazos. Como devo distribuir as pessoas para minimizar atrasos?"**

Aqui é necessário:
1. entender as restrições;
2. identificar os recursos disponíveis;
3. comparar alternativas;
4. considerar consequências;
5. chegar a uma conclusão.

Um reasoning model é projetado para ser melhor nesse segundo tipo de problema.

Uma forma simplificada de visualizar:

**Pergunta → análise do problema → múltiplas etapas de raciocínio → conclusão → resposta**

O ponto importante é que **o modelo pode gastar mais computação para resolver o problema antes de produzir a resposta final**.

### 3. Um exemplo

Considere:

> João tem o dobro da idade de Maria. Daqui a 5 anos, a soma das idades será 40. Quantos anos eles têm hoje?

Um modelo precisa estabelecer relações:

- João = 2 × Maria
- daqui a 5 anos, João + Maria = 40
- resolver as equações
- verificar o resultado

Um modelo de raciocínio tende a ser mais adequado para esse tipo de problema porque foi otimizado para **resolver problemas em múltiplas etapas**, não apenas para produzir uma continuação linguisticamente provável.

### 4. Por que é importante

Reasoning models são importantes porque ampliam o tipo de tarefa que os LLMs conseguem realizar de maneira confiável.

A principal diferença conceitual é:

**LLM tradicional:**

> "Qual resposta é mais provável neste contexto?"

**Reasoning model:**

> "Como posso trabalhar este problema em etapas para chegar a uma solução melhor?"

Isso não significa que reasoning models sejam infalíveis. Eles também podem cometer erros ou até produzir conclusões incorretas.

Outro ponto importante: **reasoning model não significa necessariamente que o modelo tenha uma "mente" ou consciência que raciocina como um ser humano**. É uma categoria de modelos e técnicas de treinamento/inferência voltadas para melhorar a resolução de problemas complexos.

### Um conceito complementar

Um termo que você provavelmente encontrará associado a isso é **test-time compute**.

A ideia é simples: em vez de sempre usar a mesma quantidade de processamento para responder, o sistema pode **usar mais computação durante a inferência para problemas que exigem mais raciocínio**.

Isso cria uma relação importante:

**Mais esforço computacional durante a inferência → potencialmente melhor desempenho em problemas complexos → maior custo e/ou latência.**


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-reasoning-models/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
