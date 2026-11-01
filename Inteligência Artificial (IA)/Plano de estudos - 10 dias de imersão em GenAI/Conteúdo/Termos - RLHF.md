[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# RLHF

### 1. O que é

**RLHF** significa **Reinforcement Learning from Human Feedback**, ou **Aprendizado por Reforço a partir de Feedback Humano**.

É uma técnica usada para **alinhar o comportamento de um modelo de IA às preferências humanas**.

Enquanto o **Instruction Tuning** ensina o modelo a seguir instruções usando exemplos, o RLHF busca ensinar **quais respostas são melhores ou piores segundo avaliações humanas**.

### 2. Como funciona, de forma intuitiva

Imagine que fazemos uma pergunta ao modelo:

> "Explique o que é inteligência artificial."

O modelo produz duas respostas:

**Resposta A:** clara, objetiva e correta.  
**Resposta B:** longa, confusa e com informações desnecessárias.

Um avaliador humano pode indicar que:

> A é melhor que B.

Com muitas avaliações desse tipo, um sistema aprende a estimar **quais respostas tendem a ser preferidas pelos humanos**.

Depois, o modelo é otimizado para produzir respostas que recebam avaliações melhores.

Uma representação simplificada:

```
Modelo pré-treinado
↓  
Instruction Tuning  
↓  
Geração de respostas
↓  
Humanos avaliam as respostas
↓  
Modelo de recompensa aprende essas preferências
↓  
Reinforcement Learning ajusta o modelo
```

### 3. Um exemplo

Imagine que o usuário pergunte:

> "Explique programação para uma criança de 8 anos."

O modelo poderia produzir:

**Resposta 1:** muito técnica, cheia de termos de programação.

**Resposta 2:** usa uma comparação com LEGO e explica o conceito de forma simples.

Humanos provavelmente prefeririam a segunda.

O RLHF ajuda o sistema a aprender esse tipo de preferência:

> **Não basta produzir uma resposta possível. Queremos produzir uma resposta que seja útil, adequada e alinhada ao que as pessoas esperam.**

### 4. Por que é importante

RLHF ajudou a tornar os LLMs muito mais adequados para interação com humanos.

Ele pode melhorar aspectos como:

- seguir instruções;
- ser útil;
- ser mais claro;
- evitar respostas inadequadas;
- respeitar determinadas preferências;
- produzir respostas mais alinhadas às expectativas humanas.

### Uma distinção importante

É útil guardar esta sequência:

**Pretraining:**  
"Aprenda padrões da linguagem e do mundo presentes nos dados."

**Instruction Tuning:**  
"Aprenda a executar instruções."

**RLHF:**  
"Aprenda quais tipos de respostas os humanos tendem a preferir."

Essa sequência ajuda bastante a entender como um LLM passa de um **modelo pré-treinado** para um **assistente conversacional**.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-rlhf/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
