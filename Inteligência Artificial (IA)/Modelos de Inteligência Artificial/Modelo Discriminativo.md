### [Sumário](<https://maksoud.github.io/Sumário>) > [Modelos de Inteligência Artificial](<https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial>)

# Modelo Discriminativo

Um **modelo discriminativo** é um tipo de modelo de aprendizado de máquina que se concentra em **aprender as fronteiras de decisão** que separam diferentes classes de dados ou em prever um valor de saída com base em variáveis de entrada. Esses modelos trabalham diretamente com a **probabilidade condicional \( P(Y|X) \)**, onde:
- \( X \) são os dados de entrada (como características ou atributos de um exemplo).
- \( Y \) é o rótulo ou classe que queremos prever.

### Diferença entre Modelos Discriminativos e Generativos

A principal diferença entre modelos discriminativos e generativos está no que eles aprendem:

- **Modelos Generativos:** Aprendem a **distribuição conjunta** \( P(X, Y) \), ou seja, como os dados \( X \) e os rótulos \( Y \) são gerados. Isso permite que eles também possam gerar novos dados \( X \).
- **Modelos Discriminativos:** Focam exclusivamente em aprender \( P(Y|X) \), que é a probabilidade de \( Y \) dado \( X \), para prever a classe ou saída correta com base nas características de entrada.

Por exemplo:
- Um modelo generativo para identificar gatos em imagens pode tentar aprender como "imagens de gatos" são geradas.
- Um modelo discriminativo apenas aprenderá a distinguir "gato" de "não-gato" diretamente.

### Como Funcionam os Modelos Discriminativos?

Modelos discriminativos trabalham aprendendo **fronteiras de decisão** que melhor separam as diferentes classes. Essa fronteira é construída com base nas características dos dados, e o modelo ajusta seus parâmetros para minimizar os erros de classificação.

O aprendizado é feito geralmente por meio de **minimização de uma função de perda (loss function)** que mede o erro entre as previsões do modelo e os rótulos reais.

### Exemplos de Modelos Discriminativos

1. **Regressão Logística:**
   - **Como funciona:** É um modelo linear que estima a probabilidade condicional de uma amostra pertencer a uma classe, usando a função logística (sigmoide). É frequentemente usado para problemas de classificação binária.
   - **Exemplo:** Determinar se um e-mail é "spam" ou "não-spam".
   - **Fronteira de decisão:** A fronteira é linear, separando as classes com base nas características de entrada.

2. **Support Vector Machines (SVM):**
   - **Como funciona:** Encontra um **hiperplano ótimo** que separa as classes no espaço de características. Ele maximiza a margem (distância) entre o hiperplano e os pontos mais próximos de cada classe (os chamados vetores de suporte).
   - **Exemplo:** Classificar imagens como "gato" ou "cachorro".
   - **Fronteira de decisão:** Pode ser linear ou não-linear, dependendo do uso de **kernels** para transformar os dados.

3. **Redes Neurais (em tarefas discriminativas):**
   - **Como funciona:** Redes neurais treinadas para tarefas de classificação ou regressão aprendem \( P(Y|X) \) usando camadas ocultas para mapear características de entrada para saídas. Redes profundas podem capturar relações complexas nos dados.
   - **Exemplo:** Classificar imagens em várias categorias, como em uma competição de ImageNet.

4. **Árvores de Decisão e Florestas Aleatórias:**
   - **Como funcionam:** As árvores de decisão criam uma estrutura hierárquica onde os dados são divididos iterativamente com base em critérios como entropia ou ganho de informação. Florestas Aleatórias combinam várias árvores para melhorar a robustez.
   - **Exemplo:** Determinar se um cliente irá pagar um empréstimo ou não.
   - **Fronteira de decisão:** Não-linear, ajustada automaticamente pelo particionamento dos dados.

5. **Transformers (em tarefas discriminativas):**
   - **Como funciona:** Em tarefas como classificação de texto ou análise de sentimento, modelos baseados em **Transformers** (como BERT) aprendem \( P(Y|X) \) usando representações de atenção que capturam o contexto das características de entrada.

### Vantagens dos Modelos Discriminativos

1. **Precisão Direta:**
   - Como os modelos discriminativos aprendem \( P(Y|X) \) diretamente, eles geralmente são mais precisos em tarefas de classificação e predição em comparação com modelos generativos.

2. **Eficiência Computacional:**
   - Por não precisar modelar \( P(X) \) (como os modelos generativos), os modelos discriminativos tendem a ser mais simples e rápidos de treinar.

3. **Melhor Generalização:**
   - Eles se concentram em ajustar as fronteiras de decisão, o que pode melhorar a capacidade de generalizar para dados não vistos.

4. **Simplicidade em Tarefas Discriminativas:**
   - Para tarefas como classificação, eles são mais fáceis de implementar e interpretar do que modelos generativos.

### Desvantagens dos Modelos Discriminativos

1. **Incapacidade de Gerar Dados:**
   - Modelos discriminativos não podem gerar novos exemplos \( X \), pois não aprendem \( P(X) \), apenas \( P(Y|X) \).

2. **Requerem Muitos Dados Rotulados:**
   - Como se concentram em tarefas supervisionadas, eles exigem dados rotulados em grandes quantidades para treinar adequadamente.

3. **Não Lidam Bem com Incertezas de \( X \):**
   - Se houver incertezas ou ruídos significativos nos dados de entrada, os modelos discriminativos podem ter dificuldades, já que não modelam \( P(X) \).

### Aplicações Comuns dos Modelos Discriminativos

1. **Classificação de Texto:**
   - Exemplo: Análise de sentimentos (classificar avaliações como positivas ou negativas).
2. **Reconhecimento de Imagens:**
   - Exemplo: Identificar objetos em imagens, como gatos, carros ou pessoas.
3. **Predição em Séries Temporais:**
   - Exemplo: Prever se um cliente continuará assinando um serviço com base em padrões de uso.
4. **Detecção de Fraudes:**
   - Exemplo: Determinar se uma transação é legítima ou fraudulenta.

### Comparação com Modelos Generativos

| Característica          | Modelos Generativos                   | Modelos Discriminativos          |
|-------------------------|----------------------------------------|-----------------------------------|
| **Aprendizado**         | \( P(X, Y) \)                         | \( P(Y|X) \)                     |
| **Foco**                | Gerar dados e classificar             | Classificação ou predição        |
| **Treinamento**         | Mais complexo                         | Mais simples                     |
| **Capacidade de Geração** | Sim                                  | Não                               |
| **Eficiência Computacional** | Mais lento devido à modelagem de \( P(X) \) | Mais rápido devido à modelagem direta de \( P(Y|X) \) |

### Conclusão

Os **modelos discriminativos** são uma escolha poderosa para tarefas que exigem **classificação** ou **regressão** direta, sendo amplamente utilizados em problemas supervisionados. Sua simplicidade e precisão os tornam ideais para muitas aplicações práticas. No entanto, eles não são indicados para tarefas que exigem geração de dados ou uma compreensão detalhada de como os dados foram gerados. Para essas tarefas, modelos generativos são mais adequados.

<sup><sub>
Renée Maksoud - outubro de 2024
</sub></sup>