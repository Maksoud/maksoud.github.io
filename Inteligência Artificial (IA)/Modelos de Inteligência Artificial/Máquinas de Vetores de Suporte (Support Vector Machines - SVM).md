### [Sumário](<https://maksoud.github.io/Sumário>) > [Modelos de Inteligência Artificial](<https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial>)

# Máquinas de Vetores de Suporte (Support Vector Machines - SVM)

As **Máquinas de Vetores de Suporte (SVM - Support Vector Machines)** são um poderoso algoritmo de aprendizado supervisionado, amplamente utilizado em problemas de **classificação** e **regressão**. O SVM é particularmente eficaz em tarefas de **classificação binária**, mas também pode ser estendido para problemas multiclasse. Ele se destaca por sua capacidade de encontrar a **fronteira de decisão** ideal que separa diferentes classes de dados com **máxima margem**.

### Intuição e Funcionamento do SVM

O objetivo principal de uma SVM é encontrar o **hiperplano** que melhor separa as diferentes classes no espaço de características. O hiperplano ideal é aquele que tem a **maior margem** possível entre as duas classes, ou seja, o que está mais distante dos pontos mais próximos de cada classe. Esses pontos próximos são chamados de **vetores de suporte**.

#### Componentes Chave:

1. **Hiperplano:**
   - O hiperplano é uma superfície que separa os dados em duas categorias. Em duas dimensões, o hiperplano é uma linha reta, mas em três ou mais dimensões, é um plano ou uma superfície.
   - Em problemas de classificação binária, o SVM encontra o hiperplano que maximiza a distância entre os pontos de dados mais próximos de cada classe, chamados de **vetores de suporte**.
   - O hiperplano pode ser representado por:
     \[
     w \cdot x + b = 0
     \]
     Onde \( w \) é o vetor normal ao hiperplano, \( x \) é o vetor de características, e \( b \) é o viés (bias).

2. **Margem:**
   - A **margem** é a distância entre o hiperplano e os vetores de suporte. O SVM busca maximizar essa margem, tornando a separação entre as classes o mais clara possível. A ideia é que uma margem maior resulte em um melhor poder de generalização, ou seja, o modelo será mais robusto a novos dados.

3. **Vetores de Suporte:**
   - Os **vetores de suporte** são os pontos de dados mais próximos ao hiperplano, que têm influência direta na posição do hiperplano. Esses pontos são críticos para a construção da SVM, pois eles definem a margem. Se removêssemos os vetores de suporte, o hiperplano seria alterado.

### Classificação Linear e Não Linear

#### 1. **SVM Linear:**
   - Em casos onde os dados são **linearmente separáveis**, o SVM pode encontrar um **hiperplano linear** que separa perfeitamente as classes. Isso significa que é possível traçar uma linha (ou plano em dimensões superiores) que divide os dados de forma clara.
   - Exemplo: Separar pontos vermelhos de pontos azuis em um gráfico 2D com uma linha reta.

#### 2. **SVM Não Linear e Kernel Trick:**
   - Quando os dados **não são linearmente separáveis** (ou seja, não podem ser divididos por uma linha reta), o SVM utiliza uma técnica chamada **Kernel Trick**.
   - O **Kernel Trick** transforma os dados para um **espaço de maior dimensão**, onde eles se tornam linearmente separáveis. O kernel, então, permite que o SVM trabalhe em dimensões mais altas sem aumentar a complexidade computacional.
   - Exemplo: Imagine dados que formam um círculo no plano 2D. Um SVM linear não pode separá-los, mas ao usar um kernel (como o **RBF - Radial Basis Function** ou **kernel polinomial**), os dados são mapeados para uma dimensão superior onde uma separação linear é possível.

Os kernels mais usados incluem:
- **Kernel Linear:** Usado quando os dados são linearmente separáveis.
- **Kernel Polinomial:** Transforma os dados para uma dimensão superior onde pode ser mais fácil encontrar a separação.
- **RBF (Radial Basis Function):** Um kernel altamente flexível que cria uma separação em formas circulares.

### Função de Custo e Margem Suave (Soft Margin)

Nem sempre os dados são perfeitamente separáveis, então o SVM usa o conceito de **margem suave (soft margin)**, permitindo que alguns pontos de dados estejam do "lado errado" do hiperplano. Para lidar com esses casos, o SVM introduz um **parâmetro de regularização (C)**, que controla o trade-off entre a maximização da margem e a minimização de erros de classificação.

- **C Alto:** O modelo tenta classificar todos os pontos corretamente, o que pode levar ao overfitting (ajuste excessivo).
- **C Baixo:** O modelo permite mais erros de classificação, o que pode resultar em melhor generalização.

### SVM para Classificação Multiclasse

O SVM foi inicialmente projetado para problemas de **classificação binária**. No entanto, ele pode ser estendido para problemas de **classificação multiclasse** usando duas abordagens principais:

1. **Um contra Todos (One-vs-All):** O SVM treina um classificador para cada classe, distinguindo-a de todas as outras. No final, a classe com a maior confiança é escolhida.
2. **Um contra Um (One-vs-One):** O SVM treina um classificador para cada par de classes. Para um problema com \( n \) classes, isso resulta em \( \frac{n(n-1)}{2} \) classificadores.

### Aplicações de SVM

1. **Classificação de Texto e Análise de Sentimentos:**
   - O SVM é amplamente utilizado em problemas de **classificação de texto**, como detecção de spam, análise de sentimentos, e categorização de documentos, onde as características são normalmente vetores de alta dimensão.
   
2. **Reconhecimento de Imagens:**
   - O SVM também é aplicado em **visão computacional** para tarefas de reconhecimento de padrões e classificação de imagens, especialmente quando as características de imagem são extraídas por métodos como **HOG** ou **SIFT**.

3. **Detecção de Fraudes:**
   - SVM é eficaz em detectar padrões anômalos em dados financeiros, sendo utilizado em sistemas de **detecção de fraudes** para identificar transações fraudulentas.

4. **Diagnóstico Médico:**
   - Em diagnósticos médicos, o SVM é usado para classificar doenças com base em conjuntos de dados clínicos, ajudando a prever se um paciente tem ou não uma determinada condição.

### Vantagens do SVM

1. **Efetivo em espaços de alta dimensão:** O SVM funciona muito bem com dados que possuem um grande número de dimensões (número de características), tornando-o ideal para tarefas como classificação de texto.
2. **Versatilidade com kernels:** Usando o Kernel Trick, o SVM pode lidar com problemas lineares e não lineares de maneira eficiente.
3. **Bom para dados com uma clara separação de classes:** O SVM é ótimo quando há uma distinção clara entre as classes.

### Desvantagens do SVM

1. **Complexidade Computacional:** Em grandes conjuntos de dados, o treinamento de um SVM pode ser lento, especialmente em problemas com muitos exemplos de treinamento.
2. **Dificuldade na seleção de kernel e ajuste de parâmetros:** A escolha do kernel correto e dos parâmetros adequados (como o valor de C e do kernel) pode ser difícil e requer experimentação.
3. **Suscetível a Outliers:** O SVM pode ser sensível a outliers nos dados, o que pode afetar a posição do hiperplano de decisão.

### Conclusão

As **Máquinas de Vetores de Suporte (SVMs)** são uma técnica poderosa para **classificação** e **regressão**, especialmente útil em problemas de classificação binária com dados de alta dimensão. Elas oferecem alta flexibilidade através do uso de kernels e são conhecidas por encontrar a fronteira de decisão ideal com uma margem máxima entre as classes. Apesar de suas desvantagens, como a complexidade em grandes conjuntos de dados, o SVM continua sendo uma ferramenta amplamente utilizada em aprendizado de máquina devido à sua eficácia e versatilidade.