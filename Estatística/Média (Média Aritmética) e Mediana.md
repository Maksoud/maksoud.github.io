# **Média (Média Aritmética)**

A média, também conhecida como média aritmética, é uma medida de tendência central que representa o valor médio de um conjunto de dados. Ela é calculada somando todos os valores e dividindo pelo número total de valores.

### **Fórmula**

Para um conjunto de dados 𝑥1,𝑥2,…,𝑥𝑛:
![[12.png]]

Onde:

- 𝑥ˉ é a média aritmética,
- 𝑛 é o número de observações,
- 𝑥𝑖 são os valores individuais.

### **Exemplo**

Considere o conjunto de dados: 4, 8, 6, 5, 3.

1. Calcule a soma dos valores: 4+8+6+5+3=26
2. Divida a soma pelo número de valores:
    ![[13.png]]

Portanto, a média aritmética é 5.2.

### **Aplicação da Média**

- **Análise de Performance**: Usada para calcular a média de vendas, temperaturas, notas de alunos, etc.
- **Comparação de Grupos**: Ajuda a comparar o desempenho médio entre diferentes grupos ou períodos.

# **Mediana**

A mediana é outra medida de tendência central que representa o valor central de um conjunto de dados ordenado. Se o número de observações for ímpar, a mediana é o valor do meio. Se for par, é a média dos dois valores centrais.

### **Passos para Calcular a Mediana**

1. **Ordene os valores em ordem crescente.**
2. **Encontre o valor central.**
    - Se o número de observações _n_ for ímpar, a mediana é o valor no meio.
    - Se _n_ for par, a mediana é a média dos dois valores centrais.

### **Exemplo 1: Número Ímpar de Observações**

Conjunto de dados: 3, 5, 8, 12, 14.

1. Ordene os valores: 3, 5, 8, 12, 14.
2. Encontre o valor central: 8.

Portanto, a mediana é 8.

### **Exemplo 2: Número Par de Observações**

Conjunto de dados: 3, 5, 7, 8, 12, 14.

1. Ordene os valores: 3, 5, 7, 8, 12, 14.
2. Encontre os dois valores centrais: 7 e 8.
3. Calcule a média dos valores centrais:
    ![[14.png]]

Portanto, a mediana é 7.5.

## **Aplicação da Mediana**

- **Análise de Dados Assimétricos**: A mediana é menos sensível a outliers e valores extremos, tornando-a útil para conjuntos de dados assimétricos.
- **Dados de Renda e Preços**: Frequentemente usada em estudos de renda e preços de imóveis, onde os dados podem ser altamente variáveis e conter outliers.

## **Comparação entre Média e Mediana**

- **Média**: Leva em conta todos os valores e pode ser influenciada por outliers. Útil para dados simétricos e quando todos os valores são relevantes.
- **Mediana**: Representa o valor central e não é afetada por outliers. Útil para dados assimétricos ou quando há outliers significativos.

# **Exemplos Complementares**

## **Exemplo de Média Influenciada por Outliers**

Considere um conjunto de salários em uma pequena empresa: 30.000, 32.000, 35.000, 40.000, 1.000.000.

1. Calcule a média:
    ![[15.png]]
2. Note que a média (227.400) é muito maior que a maioria dos salários devido ao outlier (1.000.000).

## **Exemplo de Mediana Resistente a Outliers**

Usando o mesmo conjunto de dados ordenado: 30.000, 32.000, 35.000, 40.000, 1.000.000.

1. Ordene os valores: 30.000, 32.000, 35.000, 40.000, 1.000.000.
2. Encontre o valor central: 35.000.

A mediana é 35.000, que é mais representativa dos salários típicos na empresa, sem ser influenciada pelo outlier.

## **Conclusão**

Tanto a média quanto a mediana são importantes medidas de tendência central usadas em análise de dados. A média é útil para dados simétricos e completos, enquanto a mediana é preferida para dados com outliers ou distribuições assimétricas. Compreender quando usar cada uma é crucial para análises precisas e significativas na ciência de dados.


[link de compartilhamento](https://correiarodrigues.com.br/notas/estatistica/media-media-aritmetica-e-mediana/)

<sup><sub>
Renée Maksoud - julho de 2024
</sub></sup>
