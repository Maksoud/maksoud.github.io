[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Instruction Tuning

### 1. O que é

**Instruction Tuning** é uma técnica usada para **adaptar um modelo pré-treinado para seguir instruções dadas por humanos**.

O modelo já aprendeu padrões de linguagem durante o pré-treinamento. O instruction tuning ensina o modelo a transformar esses conhecimentos em respostas mais adequadas a comandos, perguntas e tarefas.

Em termos simples:

> **Pretraining:** aprende linguagem e padrões.  
> **Instruction tuning:** aprende a seguir instruções.

### 2. Como funciona, de forma intuitiva

Depois do pré-treinamento, podemos apresentar ao modelo muitos exemplos no formato:

**Instrução:**

> Explique o que é fotossíntese para uma criança.

**Resposta esperada:**

> Fotossíntese é o processo pelo qual as plantas usam luz do Sol para produzir seu próprio alimento...

O processo é repetido com milhares ou milhões de exemplos de instruções e respostas.

Com isso, os parâmetros do modelo são ajustados para que ele aprenda padrões como:

> "Quando alguém me dá uma instrução, devo tentar executar aquela tarefa e responder de acordo com ela."

Isso é diferente do pré-treinamento, no qual o objetivo principal é aprender padrões da linguagem a partir dos dados.

### 3. Um exemplo

Um modelo pré-treinado pode receber:

> "Escreva um resumo deste texto."

Mas não necessariamente terá sido otimizado para obedecer a esse tipo de comando.

Depois do instruction tuning, ele tende a responder de maneira muito mais apropriada:

> "Claro. Aqui está um resumo: ..."

Outro exemplo:

> **Instrução:** Traduza o texto para português.  
> **Texto:** _The weather is beautiful today._

O modelo ajustado para seguir instruções entende que deve **executar a tarefa solicitada**, produzindo:

> "O tempo está bonito hoje."

### 4. Por que é importante

Instruction tuning foi fundamental para transformar LLMs de modelos que simplesmente aprendem e geram texto em modelos muito mais úteis como **assistentes**.

Ele ajuda o modelo a:

- seguir comandos;
- responder perguntas;
- resumir textos;
- traduzir;
- classificar informações;
- gerar diferentes tipos de conteúdo;
- respeitar formatos solicitados.

Uma distinção importante para sua preparação:

**Pretrained Model → aprende padrões gerais**

**Instruction Tuned Model → é adaptado para seguir instruções**

E existe ainda uma etapa relacionada chamada **RLHF (Reinforcement Learning from Human Feedback)**, que busca melhorar o comportamento do modelo usando avaliações humanas. Isso é relacionado ao instruction tuning, mas é um processo diferente.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-instruction-tuning/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
