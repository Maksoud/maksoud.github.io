### [Sumário](<https://maksoud.github.io/Sumário>)

# Modelos de Inteligência Artificial

#### **[Modelo Generativo](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Modelo%20Generativo) (Generative Models):**

- **Definição:** Modelos que aprendem a modelar a distribuição de dados e são capazes de gerar novos exemplos semelhantes aos dados de treinamento.
- **Exemplos:** Redes Geradoras Adversárias (GANs), Modelos Variacionais de Autoencoder (VAE), GPT (Generative Pre-trained Transformer).
- **Aplicações:** Geração de imagens, geração de texto, síntese de voz.

Um **modelo generativo** é um tipo de modelo de aprendizado de máquina projetado para **gerar novos exemplos de dados** que seguem a mesma distribuição do conjunto de dados de treinamento. Em vez de simplesmente classificar ou fazer previsões sobre os dados (como um modelo discriminativo), o objetivo principal dos modelos generativos é **aprender a distribuição dos dados** e, em seguida, **amostrar novos dados** dessa distribuição.

**Como funciona um modelo generativo?**

Esses modelos tentam **modelar a distribuição conjunta** entre os dados de entrada (X) e os rótulos (Y) (se existirem), ou apenas a distribuição dos dados (no caso de aprendizado não supervisionado). Assim, a ideia principal é estimar a probabilidade P(X)P(X)P(X), ou P(X,Y)P(X, Y)P(X,Y) em casos supervisionados, que reflete a probabilidade de que um determinado conjunto de dados possa ser gerado por um determinado processo.

Um exemplo intuitivo seria um modelo que, após ser treinado em um grande conjunto de dados de imagens de gatos, é capaz de gerar imagens realistas de gatos que não existem no mundo real, mas que parecem seguir o padrão dos gatos no conjunto de dados de treinamento.

#### **[Modelo Discriminativo](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Modelo%20Discriminativo) (Discriminative Models):**

- **Definição:** Modelos que aprendem a distinguir entre diferentes classes de dados com base nas características presentes nos dados.
- **Exemplos:** Regressão Logística, Redes Neurais Convolucionais (CNN), Support Vector Machines (SVMs).
- **Aplicações:** Classificação de imagens, detecção de fraudes, reconhecimento de fala.

Um **modelo discriminativo** é um tipo de modelo de aprendizado de máquina que se concentra em **distinguir entre diferentes classes** de dados com base em características observáveis, em vez de tentar modelar a distribuição conjunta dos dados. O objetivo principal de um modelo discriminativo é aprender a probabilidade condicional P(Y∣X)P(Y | X)P(Y∣X), ou seja, a probabilidade de que a classe YYY seja a correta, dado o exemplo de dados XXX.

**Diferença entre Modelos Discriminativos e Generativos**

- **Modelos Generativos** tentam modelar a **distribuição conjunta** P(X,Y)P(X, Y)P(X,Y), ou seja, como os dados XXX e suas classes YYY são gerados. Eles podem gerar novos exemplos de dados XXX a partir dessa distribuição.
- **Modelos Discriminativos**, por outro lado, não se preocupam em como os dados são gerados. Eles apenas aprendem uma função que diferencia as classes, ou seja, estimam P(Y∣X)P(Y | X)P(Y∣X), a probabilidade de um exemplo XXX pertencer a uma classe YYY.

**Como funciona um Modelo Discriminativo?**

O foco está em aprender **fronteiras de decisão** que separam os dados de diferentes classes. Ao aprender a **classificar** os dados de entrada em suas respectivas categorias, os modelos discriminativos fazem isso diretamente, sem tentar entender como os dados foram gerados.

Por exemplo, ao usar um modelo discriminativo para classificar imagens de gatos e cachorros, o modelo não tenta aprender como imagens de gatos ou cachorros são geradas. Em vez disso, ele simplesmente aprende a distinguir características visuais que são típicas de gatos ou cachorros e usa essas informações para classificar corretamente novas imagens.

#### **[Redes Neurais Convolucionais](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Redes%20Neurais%20Convolucionais) (Convolutional Neural Networks - CNNs):**

- **Definição:** Redes neurais projetadas para processar dados que têm um grid-like topology, como imagens, utilizando operações de convolução.
- **Exemplos:** LeNet, AlexNet, ResNet.
- **Aplicações:** Reconhecimento de imagens, visão computacional, análise de vídeo.

São um tipo específico de rede neural projetada para processar dados com uma estrutura em grade, como imagens. As CNNs são especialmente eficazes em **tarefas de visão computacional**, como **classificação de imagens**, **detecção de objetos**, e **segmentação semântica**, porque conseguem capturar características espaciais e de padrões locais dos dados.

#### **[Redes Neurais Recorrentes](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Redes%20Neurais%20Recorrentes) (Recurrent Neural Networks - RNNs):**

- **Definição:** Redes que têm conexões recorrentes permitindo que as informações passadas afetem o processamento atual, úteis para dados sequenciais.
- **Exemplos:** LSTMs (Long Short-Term Memory), GRUs (Gated Recurrent Units).
- **Aplicações:** Processamento de linguagem natural (PLN), previsão de séries temporais, tradução automática.

São um tipo de rede neural projetada para lidar com **dados sequenciais**, onde há uma dependência temporal ou sequencial entre as entradas. Ao contrário das redes neurais tradicionais (como as CNNs), que assumem que todas as entradas são independentes, as RNNs têm a capacidade de **relembrar** informações de entradas anteriores e usá-las para influenciar a saída atual.
#### **[Modelos Bayesianos](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Modelos%20Bayesianos):**

- **Definição:** Modelos que utilizam a estatística bayesiana para inferência, considerando probabilidades condicionais.
- **Exemplos:** Redes Bayesianas, Classificador Naive Bayes.
- **Aplicações:** Diagnóstico médico, sistemas de recomendação, modelagem probabilística.

São uma classe de modelos de aprendizado de máquina baseados no **Teorema de Bayes**, que permite atualizar as probabilidades de uma hipótese à medida que mais evidências ou dados são obtidos. Esses modelos se distinguem por tratar a inferência de forma probabilística, o que significa que eles levam em consideração a **incerteza** nos dados e nas predições.

**Teorema de Bayes**

O Teorema de Bayes é a base dos modelos bayesianos. Ele define a relação entre a probabilidade condicional e a probabilidade marginal de dois eventos.

**Como funcionam os Modelos Bayesianos?**

Em um modelo bayesiano, você começa com uma **distribuição a priori**, que representa suas crenças sobre a variável de interesse antes de ver os dados. Conforme novos dados são observados, essa crença é atualizada para uma **distribuição a posteriori**, utilizando o Teorema de Bayes. Esse processo de **atualização contínua das crenças** é uma das principais características dos modelos bayesianos.

#### **[Transformers](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Transformers):**

- **Definição:** Modelos baseados em uma arquitetura de atenção que captura relacionamentos entre palavras ou elementos de dados de forma mais eficaz.
- **Exemplos:** BERT (Bidirectional Encoder Representations from Transformers), T5, GPT.
- **Aplicações:** Tradução de texto, resposta a perguntas, geração de linguagem natural.

O **Transformer** é um dos modelos mais inovadores e poderosos no campo da Inteligência Artificial, especialmente em **Processamento de Linguagem Natural (PLN)** e **visão computacional**. Introduzido pelo Google em 2017 no artigo "Attention is All You Need", o Transformer revolucionou o tratamento de dados sequenciais, substituindo as tradicionais **Redes Neurais Recorrentes (RNNs)** por um mecanismo de **atenção** altamente eficiente.

**Arquitetura do Transformer**

A principal inovação dos Transformers é o uso do mecanismo de **atenção** (attention mechanism), que permite que o modelo processe dados sequenciais de forma mais eficaz e paralela, superando a limitação das RNNs, que lidam com sequências de forma linear (uma palavra por vez). Em vez disso, os Transformers analisam todos os elementos da sequência simultaneamente, usando atenção para focar em partes relevantes do texto ou dos dados.

A arquitetura do Transformer é composta de dois blocos principais: **Codificador (Encoder)** e **Decodificador (Decoder)**. Embora a arquitetura completa do Transformer seja usada em tarefas de tradução automática, apenas o codificador é suficiente para muitas outras tarefas (como no BERT, que usa somente a parte do codificador).

#### **[Máquinas de Vetores de Suporte](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Máquinas%20de%20Vetores%20de%20Suporte%20(Support%20Vector%20Machines%20-%20SVM)) (Support Vector Machines - SVM):**

- **Definição:** Algoritmos de classificação que encontram o hiperplano de separação ideal entre classes.
- **Aplicações:** Classificação de texto, reconhecimento de padrões, bioinformática.

São um poderoso algoritmo de aprendizado supervisionado, amplamente utilizado em problemas de **classificação** e **regressão**. O SVM é particularmente eficaz em tarefas de **classificação binária**, mas também pode ser estendido para problemas multiclasse. Ele se destaca por sua capacidade de encontrar a **fronteira de decisão** ideal que separa diferentes classes de dados com **máxima margem**.

#### **[Redes Geradoras Adversárias](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Redes%20Geradoras%20Adversárias) (Generative Adversarial Networks - GANs):**

- **Definição:** Um tipo de modelo generativo composto por duas redes (geradora e discriminadora) que competem entre si para melhorar a qualidade dos dados gerados.
- **Aplicações:** Geração de imagens realistas, criação de dados sintéticos, arte gerada por IA.

São um tipo de modelo generativo que usa duas redes neurais que competem entre si em um processo chamado de **aprendizado adversarial**. Esse conceito foi introduzido por Ian Goodfellow e seus colegas em 2014, e as GANs rapidamente se tornaram uma das técnicas mais importantes em **aprendizado profundo** (deep learning) para a geração de novos dados a partir de um conjunto de dados existente.

#### **[Árvores de Decisão e Florestas Aleatórias](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Árvores%20de%20Decisão%20e%20Florestas%20Aleatórias%20(Decision%20Trees%20and%20Random%20Forests)) (Decision Trees and Random Forests):**

- **Definição:** Métodos baseados em árvores de decisão para classificação e regressão. Florestas aleatórias combinam várias árvores para melhorar a precisão.
- **Aplicações:** Diagnóstico de doenças, análise de crédito, detecção de fraudes.

São métodos populares de aprendizado supervisionado usados para tarefas de **classificação** e **regressão**. Elas se destacam por sua capacidade de interpretar dados complexos de forma intuitiva e robusta, e são amplamente utilizadas em muitos campos, como **ciências de dados**, **diagnósticos médicos**, e **análise financeira**.

1. **Árvores de Decisão (Decision Trees)**

Uma **árvore de decisão** é um modelo de aprendizado baseado em uma estrutura de árvore. Cada nó da árvore representa uma **pergunta** ou **condição** sobre uma característica do conjunto de dados, e os **ramos** da árvore representam as **decisões** tomadas com base nessa pergunta. O objetivo final é **dividir os dados** em subgrupos cada vez menores, até que os dados estejam tão separados que uma decisão final ou predição possa ser feita.

2. **Florestas Aleatórias (Random Forests)**

As **florestas aleatórias** são uma extensão das árvores de decisão e têm como objetivo melhorar o desempenho e a robustez dos modelos. Elas são um exemplo de um algoritmo de **ensemble**, o que significa que combinam vários modelos (neste caso, várias árvores de decisão) para tomar decisões mais precisas e robustas.

#### **[Redes Neurais Profundas](https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial/Redes%20Neurais%20Profundas) (Deep Neural Networks - DNN):**

- **Definição:** Redes com múltiplas camadas ocultas que aprendem representações complexas dos dados.
- **Exemplos:** Redes multicamadas (MLP), CNNs, RNNs.
- **Aplicações:** Visão computacional, processamento de linguagem, jogos baseados em IA.

São um tipo de rede neural artificial com múltiplas camadas ocultas entre a camada de entrada e a camada de saída. Essas redes são uma extensão das redes neurais simples, com o objetivo de aprender **representações hierárquicas** complexas dos dados. As DNNs são chamadas de "profundas" porque têm várias camadas ocultas, enquanto as redes neurais convencionais podem ter apenas uma ou duas.

**Aprendizado em Redes Neurais Profundas**

O processo de aprendizado em uma DNN é chamado de **treinamento supervisionado**. Ele ocorre em três etapas principais:

1. **Propagação para Frente (Forward Propagation):**
    - Os dados de entrada são processados através da rede, passando por todas as camadas ocultas até a camada de saída, onde o modelo faz uma predição.
2. **Cálculo da Função de Custo (Loss Function):**
    - A predição da rede é comparada com o valor real dos dados de treinamento, e a **função de perda** mede o erro (diferença entre a predição e o valor real). Exemplos de funções de perda incluem:
        - **Erro Quadrático Médio (MSE)** para regressão.
        - **Entropia Cruzada (Cross-Entropy)** para classificação.
3. **Retropropagação (Backpropagation):**
    - A **retropropagação** é o processo pelo qual os pesos da rede são ajustados para minimizar o erro da função de perda. Ela usa o **gradiente descendente** para atualizar os pesos, propagando o erro da camada de saída para trás, ajustando os pesos de cada camada intermediária.

Esse processo é repetido várias vezes até que o modelo alcance um erro aceitável nos dados de treinamento.

[link de compartilhamento](<https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial>)