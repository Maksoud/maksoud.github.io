A regressão é uma técnica estatística usada para modelar e analisar a relação entre uma variável dependente e uma ou mais variáveis independentes. É amplamente utilizada em ciência de dados e análise de dados para prever valores, identificar tendências e entender as relações entre variáveis.

### Tipos de Regressão

1. **Regressão Linear Simples**
2. **Regressão Linear Múltipla**
3. **Regressão Logística**
4. **Regressão Polinomial**
5. **Regressão Ridge e Lasso**

## 1. Regressão Linear Simples

A regressão linear simples modela a relação entre duas variáveis: uma dependente e uma independente. A relação é representada por uma linha reta.

**Equação:**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/7d28dbee-93eb-49e7-ab07-9601054d1a97/Untitled.png)

Onde:

- _y_ é a variável dependente,
- 𝑥 é a variável independente,
- 𝛽0 é o intercepto,
- 𝛽1 é o coeficiente de inclinação,
- 𝜖 é o erro.

**Exemplo:** Suponha que você queira prever o preço de venda de uma casa com base em sua área. A equação da regressão pode ser ajustada usando dados históricos de preços de casas e suas áreas.

## 2. Regressão Linear Múltipla

A regressão linear múltipla estende a regressão linear simples para incluir duas ou mais variáveis independentes.

**Equação:**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/0eecba0f-bd18-4f6c-9765-58ba4869c377/Untitled.png)

Onde:

- _y_ é a variável dependente,
- 𝑥1,𝑥2,…,𝑥𝑛 são as variáveis independentes,
- 𝛽0 é o intercepto,
- 𝛽1,𝛽2,…,𝛽𝑛 são os coeficientes das variáveis independentes,
- 𝜖 é o erro.

**Exemplo:** Suponha que você queira prever o preço de venda de uma casa com base em sua área, número de quartos e idade. A equação da regressão pode ser ajustada usando dados históricos de preços de casas e essas características.

## 3. Regressão Logística

A regressão logística é usada quando a variável dependente é categórica, geralmente binária (0 ou 1). É útil para modelar a probabilidade de um evento ocorrer.

**Equação:**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/a61fe3f6-b30c-4bba-af22-40627b81109e/Untitled.png)

Onde:

- _p_ é a probabilidade do evento ocorrer,
- 𝑥1,𝑥2,…,𝑥𝑛 são as variáveis independentes,
- 𝛽0,𝛽1,𝛽2,…,𝛽𝑛 são os coeficientes das variáveis independentes.

**Exemplo:** Suponha que você queira prever se um cliente fará uma compra (1) ou não (0) com base em suas características demográficas e comportamento de navegação.

## 4. Regressão Polinomial

A regressão polinomial é usada quando a relação entre a variável dependente e as variáveis independentes é melhor representada por uma função polinomial.

**Equação:**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/1e923148-a8a8-4b00-984b-d151f5de6ed0/Untitled.png)

Onde:

- _y_ é a variável dependente,
- 𝑥 é a variável independente,
- 𝛽0,𝛽1,𝛽2,…,𝛽𝑛 são os coeficientes,
- 𝜖 é o erro.

**Exemplo:** Suponha que você queira prever a receita de vendas com base no orçamento de marketing, onde a relação é curvilínea.

## 5. Regressão Ridge e Lasso

Estas são técnicas de regressão regularizadas que adicionam penalidades aos coeficientes da regressão linear para prevenir overfitting.

**Regressão Ridge:** Adiciona uma penalidade aos coeficientes.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/8e601377-ac60-42d7-b660-56c6f8135707/Untitled.png)

**Regressão Lasso:** Adiciona uma penalidade aos coeficientes.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/2ed42047-4a53-4500-a702-da41ee38eb6b/Untitled.png)

**Exemplo:** Estas técnicas são úteis quando se trabalha com um grande número de variáveis independentes e se deseja um modelo mais simples e generalizável.

## Exemplos de Aplicações de Regressão

### Exemplo 1: Regressão Linear Simples

**Problema:** Você tem dados sobre a área de casas e seus preços de venda e quer prever o preço de uma casa com base em sua área.

**Dados:**

|Área (m²)|Preço (R$)|
|---|---|
|50|200,000|
|60|240,000|
|70|280,000|
|80|320,000|
|90|360,000|

**Solução:**

1. Ajustar a linha de regressão.
    
2. Equação ajustada:
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/1ffc6a6c-10bd-4952-91e4-56b26ce7b410/Untitled.png)
    

Portanto, se uma casa tem 75 m², o preço estimado seria:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/f0e9ee6c-7a39-45dd-b7d4-e89d22cba3cc/Untitled.png)

## Exemplo 2: Regressão Logística

**Problema:** Você quer prever se um cliente comprará (1) ou não (0) com base em sua idade e renda.

**Dados:**

|Idade|Renda (R$)|Compra|
|---|---|---|
|22|20,000|0|
|25|25,000|0|
|47|45,000|1|
|52|50,000|1|
|46|46,000|1|

**Solução:**

1. Ajustar o modelo de regressão logística.
    
2. Equação ajustada:
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/1c89c980-5c07-4e54-a8e1-b15c80cae14c/Untitled.png)
    

Portanto, para um cliente de 30 anos com renda de 30,000, a probabilidade de compra seria:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9d60bff0-fe0b-4ea2-8172-325712f68e66/3c6cc953-3f1a-48af-b581-12778b2a5797/Untitled.png)

## Conclusão

A regressão é uma ferramenta poderosa na estatística e ciência de dados para modelar relações entre variáveis e fazer previsões. Compreender os diferentes tipos de regressão e suas aplicações permite aos cientistas de dados e analistas de dados abordar uma ampla gama de problemas analíticos e tomar decisões informadas com base nos dados.