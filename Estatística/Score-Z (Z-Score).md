O score-Z, também conhecido como escore padronizado ou z-score, é uma medida que descreve a posição de um valor em relação à média de um conjunto de dados, expressa em termos de desvios padrão. Ele indica quantos desvios padrão um valor está acima ou abaixo da média.
## **Fórmula do Score-Z**

A fórmula para calcular o score-Z de um valor 𝑥 é:
![[16.png]]

Onde:

- 𝑍 é o score-Z,
- 𝑥 é o valor individual,
- 𝜇 é a média do conjunto de dados,
- 𝜎 é o desvio padrão do conjunto de dados.

## **Interpretação do Score-Z**

- **Z = 0**: O valor _x_ é igual à média.
- **Z positivo**: O valor _x_ está acima da média.
- **Z negativo**: O valor _x_ está abaixo da média.
- **|Z| > 2 ou |Z| > 3**: O valor _x_ está a mais de 2 ou 3 desvios padrão da média, o que pode indicar um outlier, dependendo do contexto.

## **Exemplo Prático**

Vamos calcular o score-Z para um conjunto de dados. Suponha que temos os seguintes dados de pontuações de um teste: 70, 75, 80, 85, 90, 95, 100.

1. **Calcule a média (𝜇):**
    ![[17.png]]
2. **Calcule o desvio padrão (𝜎):** Primeiro, calcule a soma das diferenças ao quadrado em relação à média:
    ![[18.png]]
    Soma das diferenças ao quadrado:
    ![[19.png]]
    Variância (para uma população):
    ![[20.png]]
    Desvio padrão:
    ![[21.png]]
3. **Calcule o score-Z para uma pontuação específica, por exemplo, 90:**
    ![[22.png]]
    Portanto, a pontuação de 90 está 0.5 desvios padrão acima da média.

## **Aplicação do Score-Z na Ciência de Dados**

1. **Identificação de Outliers** Valores com score-Z acima de 2 ou abaixo de -2 são frequentemente considerados outliers. Isso ajuda a detectar anomalias nos dados.
    
    **Exemplo:** Em um conjunto de dados de alturas, valores com score-Z muito alto ou baixo podem indicar erros de medição ou indivíduos excepcionalmente altos ou baixos.
    
2. **Padronização de Dados** Padronizar dados significa transformar os valores para que tenham média 0 e desvio padrão 1. Isso é útil para comparações e para algoritmos de machine learning que se beneficiam de dados em uma escala comum.
    
    **Exemplo:** Em uma análise de várias métricas de desempenho, padronizar os dados permite comparar diferentes métricas na mesma escala.
    
3. **Detecção de Anomalias** Em modelos de detecção de fraudes ou manutenção preditiva, scores-Z podem ser usados para identificar comportamentos anômalos.
    
    **Exemplo:** Em transações financeiras, scores-Z altos podem indicar transações fraudulentas.

## **Exemplo Complementar**

Imagine que você está analisando o tempo de resposta de um servidor em milissegundos: 120, 115, 130, 150, 110, 170, 125.

1. **Calcule a média (𝜇):**
    ![[23.png]]
2. **Calcule o desvio padrão (𝜎):** Primeiro, calcule a soma das diferenças ao quadrado em relação à média:
    ![[24.png]]
    Soma das diferenças ao quadrado:
    ![[25.png]]
    Variância (para uma população):
    ![[26.png]]
    Desvio padrão:
    ![[27.png]]
3. **Calcule o score-Z para um tempo de resposta específico, por exemplo, 150 ms:**
    ![[28.png]]
    Portanto, o tempo de resposta de 150 ms está aproximadamente 0.94 desvios padrão acima da média.

## **Conclusão**

O score-Z é uma ferramenta poderosa e versátil para analistas e cientistas de dados. Ele permite a padronização de dados, identificação de outliers, comparação de valores de diferentes distribuições e detecção de anomalias. Compreender como calcular e interpretar scores-Z é fundamental para análises precisas e informadas em diversas aplicações estatísticas e de machine learning.