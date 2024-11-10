[Modelos de Inteligência Artificial](<https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial>)

**Árvores de Decisão** e **Florestas Aleatórias** são métodos populares de aprendizado supervisionado usados para tarefas de **classificação** e **regressão**. Elas se destacam por sua capacidade de interpretar dados complexos de forma intuitiva e robusta, e são amplamente utilizadas em muitos campos, como **ciências de dados**, **diagnósticos médicos**, e **análise financeira**.

### 1. **Árvores de Decisão (Decision Trees)**

Uma **árvore de decisão** é um modelo de aprendizado baseado em uma estrutura de árvore. Cada nó da árvore representa uma **pergunta** ou **condição** sobre uma característica do conjunto de dados, e os **ramos** da árvore representam as **decisões** tomadas com base nessa pergunta. O objetivo final é **dividir os dados** em subgrupos cada vez menores, até que os dados estejam tão separados que uma decisão final ou predição possa ser feita.

#### Como funciona uma Árvore de Decisão?

1. **Raiz da Árvore:** A árvore começa com um **nó raiz**, que contém todos os dados de entrada.
2. **Divisões ou Splits:** Em cada nó, a árvore faz uma pergunta sobre uma característica dos dados (por exemplo, "A idade é maior que 30?"). Os dados são então divididos em dois ou mais subgrupos, dependendo da resposta (sim/não ou categorias).
3. **Nós Folha:** Os nós finais, chamados **nós folha**, contêm a decisão final ou predição (como a classificação de uma classe ou um valor numérico no caso de regressão).

#### Critérios para a Divisão (Split)

A principal tarefa ao construir uma árvore de decisão é escolher a melhor divisão (split) para cada nó. Alguns critérios comuns são:

- **Gini Impurity (Impureza de Gini):** Um critério que mede o grau de impureza de um nó. A impureza de Gini é mínima (0) quando todos os exemplos pertencem à mesma classe.
- **Entropia e Ganho de Informação:** A **entropia** mede a desordem ou incerteza nos dados. O **ganho de informação** é calculado como a redução da entropia após a divisão.
- **Erro Quadrático Médio (MSE):** Usado em tarefas de regressão, o MSE mede o erro quadrático entre as predições e os valores reais.

#### Vantagens das Árvores de Decisão

1. **Interpretação Simples:** As árvores de decisão são fáceis de entender e interpretar, pois o caminho de cada decisão pode ser traçado de cima para baixo.
2. **Versatilidade:** Elas podem ser usadas para problemas de classificação e regressão.
3. **Não precisam de normalização dos dados:** As árvores de decisão não exigem escalonamento ou normalização dos dados, o que é necessário em muitos outros algoritmos.

#### Limitações das Árvores de Decisão

1. **Overfitting:** Árvores de decisão podem crescer muito, criando modelos complexos que se ajustam excessivamente aos dados de treinamento. Isso pode levar a um mau desempenho em dados novos (generalização ruim).
2. **Instabilidade:** Pequenas mudanças nos dados podem resultar em grandes mudanças na estrutura da árvore.

### 2. **Florestas Aleatórias (Random Forests)**

As **florestas aleatórias** são uma extensão das árvores de decisão e têm como objetivo melhorar o desempenho e a robustez dos modelos. Elas são um exemplo de um algoritmo de **ensemble**, o que significa que combinam vários modelos (neste caso, várias árvores de decisão) para tomar decisões mais precisas e robustas.

#### Como funciona uma Floresta Aleatória?

1. **Ensemble de Árvores de Decisão:** Uma floresta aleatória consiste em um grande número de **árvores de decisão** individuais, onde cada árvore faz uma predição sobre os dados.
2. **Bagging (Bootstrap Aggregating):** Para cada árvore, uma amostra aleatória (com reposição) dos dados de treinamento é usada. Isso cria uma variedade entre as árvores e reduz o risco de overfitting.
3. **Seleção Aleatória de Características:** Ao construir cada árvore, a floresta aleatória também seleciona aleatoriamente um subconjunto das características (features) em cada divisão (split). Isso aumenta a diversidade das árvores e ajuda a evitar que algumas características dominem o modelo.
4. **Predição Final:** Para **classificação**, a predição final é feita com base em uma votação majoritária das árvores individuais. Para **regressão**, a predição final é a média das predições das árvores.

#### Vantagens das Florestas Aleatórias

1. **Redução do Overfitting:** Ao combinar várias árvores e usar amostras e características aleatórias, as florestas aleatórias são menos propensas a overfitting em comparação com uma única árvore de decisão.
2. **Robustez:** As florestas aleatórias são mais estáveis e robustas, pois as predições são baseadas em muitas árvores, o que reduz o impacto de outliers e variações nos dados.
3. **Versatilidade:** Assim como as árvores de decisão, as florestas aleatórias podem ser usadas para problemas de **classificação** e **regressão**.

#### Limitações das Florestas Aleatórias

1. **Complexidade:** As florestas aleatórias podem ser mais lentas para treinar e mais complexas de interpretar devido ao grande número de árvores envolvidas.
2. **Tamanho do Modelo:** Como uma floresta aleatória envolve muitas árvores de decisão, o modelo final pode ser grande e consumir mais memória e tempo para fazer predições.

### Comparação: Árvores de Decisão vs Florestas Aleatórias

|Característica|Árvores de Decisão|Florestas Aleatórias|
|---|---|---|
|**Interpretação**|Simples e intuitiva|Difícil de interpretar|
|**Risco de Overfitting**|Alto|Baixo|
|**Robustez**|Sensível a mudanças nos dados|Resistente a mudanças nos dados|
|**Precisão**|Menos precisa|Mais precisa e confiável|
|**Complexidade Computacional**|Baixa|Moderada a alta|

### Aplicações de Árvores de Decisão e Florestas Aleatórias

1. **Diagnóstico Médico:** Árvores de decisão são usadas para diagnosticar doenças com base em sintomas ou resultados de exames. Florestas aleatórias melhoram a precisão ao combinar várias árvores.
2. **Análise Financeira:** As florestas aleatórias podem ser usadas para prever riscos de crédito ou detectar fraudes em transações financeiras.
3. **Sistemas de Recomendação:** As florestas aleatórias são aplicadas para personalizar recomendações, como em sistemas de recomendação de filmes ou produtos.

### Conclusão

- **Árvores de Decisão** são uma ferramenta poderosa para classificar e prever dados de forma simples e intuitiva, mas podem sofrer de overfitting.
- **Florestas Aleatórias** são uma versão mais robusta e precisa, corrigindo muitas das limitações das árvores de decisão individuais ao combinar várias árvores em um modelo ensemble.

Esses modelos continuam sendo amplamente utilizados em várias indústrias devido à sua capacidade de lidar com dados complexos e fornecer predições confiáveis.