### [Sumário](<https://maksoud.github.io/Sumário>) > [Modelos de Inteligência Artificial](<https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial>)

# Modelo Discriminativo

Um **modelo discriminativo** é um tipo de modelo de aprendizado de máquina que se concentra em **distinguir entre diferentes classes** de dados com base em características observáveis, em vez de tentar modelar a distribuição conjunta dos dados. O objetivo principal de um modelo discriminativo é aprender a probabilidade condicional \( P(Y | X) \), ou seja, a probabilidade de que a classe \( Y \) seja a correta, dado o exemplo de dados \( X \).

### Diferença entre Modelos Discriminativos e Generativos

- **Modelos Generativos** tentam modelar a **distribuição conjunta** \( P(X, Y) \), ou seja, como os dados \( X \) e suas classes \( Y \) são gerados. Eles podem gerar novos exemplos de dados \( X \) a partir dessa distribuição.
- **Modelos Discriminativos**, por outro lado, não se preocupam em como os dados são gerados. Eles apenas aprendem uma função que diferencia as classes, ou seja, estimam \( P(Y | X) \), a probabilidade de um exemplo \( X \) pertencer a uma classe \( Y \).

### Como funciona um Modelo Discriminativo?

O foco está em aprender **fronteiras de decisão** que separam os dados de diferentes classes. Ao aprender a **classificar** os dados de entrada em suas respectivas categorias, os modelos discriminativos fazem isso diretamente, sem tentar entender como os dados foram gerados.

Por exemplo, ao usar um modelo discriminativo para classificar imagens de gatos e cachorros, o modelo não tenta aprender como imagens de gatos ou cachorros são geradas. Em vez disso, ele simplesmente aprende a distinguir características visuais que são típicas de gatos ou cachorros e usa essas informações para classificar corretamente novas imagens.