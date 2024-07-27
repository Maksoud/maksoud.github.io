# **Média (Média Aritmética)**

A média, também conhecida como média aritmética, é uma medida de tendência central que representa o valor médio de um conjunto de dados. Ela é calculada somando todos os valores e dividindo pelo número total de valores.

### **Fórmula**

Para um conjunto de dados 𝑥1,𝑥2,…,𝑥𝑛:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/841573b6-4c76-4425-a611-1b87b21d254f/Untitled.png)

Onde:

- 𝑥ˉ é a média aritmética,
- 𝑛 é o número de observações,
- 𝑥𝑖 são os valores individuais.

### **Exemplo**

Considere o conjunto de dados: 4, 8, 6, 5, 3.

1. Calcule a soma dos valores: 4+8+6+5+3=26
    
2. Divida a soma pelo número de valores:
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/c7825855-b369-4fa2-b317-4dda4f61ab02/Untitled.png)
    

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
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/2f92a157-0922-4379-91f1-9ea3774d2bd7/Untitled.png)
    

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
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/5f87f891-d521-436f-ad78-2a28166ef674/Untitled.png)
    
2. Note que a média (227.400) é muito maior que a maioria dos salários devido ao outlier (1.000.000).
    

## **Exemplo de Mediana Resistente a Outliers**

Usando o mesmo conjunto de dados ordenado: 30.000, 32.000, 35.000, 40.000, 1.000.000.

1. Ordene os valores: 30.000, 32.000, 35.000, 40.000, 1.000.000.
2. Encontre o valor central: 35.000.

A mediana é 35.000, que é mais representativa dos salários típicos na empresa, sem ser influenciada pelo outlier.

## **Conclusão**

Tanto a média quanto a mediana são importantes medidas de tendência central usadas em análise de dados. A média é útil para dados simétricos e completos, enquanto a mediana é preferida para dados com outliers ou distribuições assimétricas. Compreender quando usar cada uma é crucial para análises precisas e significativas na ciência de dados.