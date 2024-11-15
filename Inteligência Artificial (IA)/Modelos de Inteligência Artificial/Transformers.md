### [Sumário](<https://maksoud.github.io/Sumário>) > [Modelos de Inteligência Artificial](<https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial>)

# Transformers

**Transformers** são uma arquitetura de redes neurais que revolucionou o campo do **processamento de linguagem natural (PLN)** e, mais recentemente, também **visão computacional**. Introduzida no artigo "Attention is All You Need" (2017), pelos pesquisadores da Google, a arquitetura de Transformers se destacou por resolver várias limitações das redes neurais recorrentes (RNNs), como LSTMs e GRUs, no que diz respeito à eficiência e à capacidade de lidar com dependências de longo alcance em sequências.

### Principais Componentes do Transformer

Os Transformers são baseados em um mecanismo fundamental: a **atenção**. A arquitetura é composta por **camadas de atenção** que permitem à rede aprender quais partes da entrada são mais importantes em qualquer momento do processamento. Eles utilizam um mecanismo de **atenção auto-regressiva** para processar sequências, sem precisar depender de uma estrutura sequencial como RNNs, o que possibilita **paralelizar** o treinamento de maneira eficiente.

A arquitetura Transformer pode ser dividida em dois blocos principais: **codificador** (encoder) e **decodificador** (decoder). Em alguns casos, como no modelo BERT, usa-se apenas o codificador, e em outros, como no GPT, usa-se apenas o decodificador.

#### 1. **Mecanismo de Atenção**
   - O mecanismo de **atenção** é o ponto central do Transformer. Ele permite que o modelo se concentre nas partes mais relevantes da sequência de entrada para cada tarefa específica, ao invés de tratar todos os elementos da sequência com o mesmo peso. Isso é feito através de três vetores: **query**, **key**, e **value**.
     - **Query (consulta)**: Um vetor que representa a "pergunta" que o modelo está tentando fazer sobre a sequência.
     - **Key (chave)**: Um vetor que indexa os elementos na sequência.
     - **Value (valor)**: O conteúdo associado à chave que pode ser retornado como resposta à query.

   O cálculo da atenção é feito por meio da fórmula:
   \[
   \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
   \]
   Onde \( Q \), \( K \), e \( V \) representam os vetores query, key e value, respectivamente. O softmax assegura que as pontuações de atenção somem para 1, distribuindo a importância das diferentes palavras da sequência.

#### 2. **Atenção Multi-Head (Multi-Head Attention)**
   - Em vez de calcular a atenção uma única vez, o Transformer usa **atenção multi-head**, o que significa que múltiplas "cabeças" de atenção são usadas para capturar diferentes aspectos das dependências da sequência. Cada uma dessas cabeças aprende a focar em diferentes partes da sequência, permitindo que o modelo entenda vários relacionamentos complexos ao mesmo tempo.

#### 3. **Camadas Feedforward**
   - Depois da camada de atenção, o modelo aplica uma **rede neural feedforward** (totalmente conectada) a cada posição da sequência, independentemente. Essa rede consiste em uma combinação de duas camadas densas com uma função de ativação no meio, geralmente **ReLU**.

#### 4. **Codificador (Encoder)**
   - O **encoder** é uma pilha de camadas, onde cada camada consiste em uma camada de **atenção multi-head** e uma camada **feedforward**. A entrada do encoder é a sequência de dados de entrada, geralmente palavras ou tokens. Ele gera uma representação codificada para cada elemento da sequência, levando em consideração todas as relações entre os elementos da sequência.

#### 5. **Decodificador (Decoder)**
   - O **decoder** é responsável por gerar a saída final. Ele é semelhante ao encoder, mas com uma diferença: ele utiliza a **atenção mascarada** (masked attention) para impedir que as posições futuras influenciem as previsões anteriores, tornando o processo de geração de sequência mais eficaz. Além disso, o decoder também usa a **atenção cruzada** (cross-attention) para conectar as representações geradas pelo encoder à tarefa de decodificação.

### Processamento Paralelo

Uma das maiores vantagens dos Transformers em relação às RNNs é que eles **não precisam processar as sequências de forma sequencial**. Em RNNs, cada palavra ou token de uma sequência depende das informações do token anterior, o que impede a paralelização. Já nos Transformers, como o cálculo da atenção é feito para todos os tokens ao mesmo tempo, o processamento pode ser **totalmente paralelizado**, tornando os Transformers muito mais eficientes em termos de tempo e recursos computacionais.

### Atenção Posicional

Diferentemente de RNNs, que capturam a ordem dos tokens por natureza, os Transformers não possuem essa característica automaticamente, já que processam os dados em paralelo. Para resolver isso, é adicionado um **embedding posicional** (positional encoding) aos vetores de entrada para que o modelo possa aprender a posição de cada token dentro da sequência.

### Modelos Baseados em Transformers

Desde a introdução dos Transformers, muitos modelos de PLN de última geração foram construídos com base nessa arquitetura. Aqui estão alguns exemplos de modelos famosos:

1. **BERT (Bidirectional Encoder Representations from Transformers):**
   - **Como funciona:** BERT usa a parte do **encoder** do Transformer e foi treinado de maneira bidirecional, o que significa que ele olha para o contexto à esquerda e à direita de uma palavra simultaneamente. BERT foi pré-treinado em tarefas como a **máscara de palavras** (Masked Language Model - MLM), onde o modelo tenta prever palavras ocultas no texto.
   - **Aplicações:** Compreensão de texto, classificação de texto, resposta a perguntas, análise de sentimentos.

2. **GPT (Generative Pre-trained Transformer):**
   - **Como funciona:** GPT usa apenas o **decodificador** do Transformer e é treinado de forma auto-regressiva, ou seja, a geração de palavras em uma sequência depende apenas do contexto anterior, não do futuro. GPT-3, por exemplo, é uma das maiores implementações com bilhões de parâmetros.
   - **Aplicações:** Geração de texto, tradução automática, chatbots, resumo de texto.

3. **T5 (Text-to-Text Transfer Transformer):**
   - **Como funciona:** O T5 converte todas as tarefas de PLN em um problema de **texto-para-texto**, onde tanto a entrada quanto a saída são sequências de texto. Ele utiliza tanto o encoder quanto o decoder do Transformer e foi treinado para resolver uma variedade de tarefas, como tradução, sumarização e classificação de texto.
   - **Aplicações:** Tradução automática, sumarização, geração de texto.

4. **Vision Transformer (ViT):**
   - **Como funciona:** O Vision Transformer adapta a arquitetura Transformer para tarefas de **visão computacional**, como classificação de imagens. Em vez de processar sequências de palavras, o ViT divide uma imagem em pequenos patches (blocos de imagem) e os trata como uma sequência de tokens.
   - **Aplicações:** Classificação de imagens, detecção de objetos, segmentação de imagens.

### Vantagens dos Transformers

1. **Captura de Dependências de Longo Alcance:**
   - Com o mecanismo de atenção, os Transformers podem capturar relações entre palavras distantes em uma sequência, o que é difícil para RNNs.

2. **Paralelização:** 
   - A capacidade de processar sequências inteiras de uma vez, em vez de uma palavra por vez, torna o treinamento mais rápido e eficiente.

3. **Versatilidade:**
   - A arquitetura de Transformers pode ser aplicada a uma ampla gama de tarefas de sequência, tanto em linguagem natural quanto em visão computacional.

4. **Transferência de Aprendizado:**
   - Modelos como BERT e GPT podem ser pré-treinados em grandes conjuntos de dados e depois adaptados (fine-tuned) para tarefas específicas com relativamente poucos dados rotulados.

### Limitações dos Transformers

1. **Alto Custo Computacional:**
   - Embora os Transformers sejam altamente paralelizados, a complexidade computacional aumenta com o comprimento da sequência, exigindo grandes recursos computacionais para treinamento.

2. **Dependência de Grandes Quantidades de Dados:**
   - Os modelos baseados em Transformers, especialmente os de grande porte como GPT-3, exigem **grandes quantidades de dados** para treinamento e são caros de treinar.

### Conclusão

Os Transformers são uma arquitetura revolucionária em aprendizado profundo, especialmente no processamento de linguagem natural, mas também em outros domínios. Sua capacidade de capturar dependências de longo alcance e de processar sequências de maneira paralela os torna uma escolha poderosa para muitas tarefas. Desde sua introdução, eles foram adotados em diversos modelos e são hoje uma das bases mais importantes para avanços na inteligência artificial.