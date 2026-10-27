## Teste de Hipóteses

O teste de hipóteses é uma metodologia estatística usada para tomar decisões sobre uma população com base em dados amostrais. Ele ajuda a determinar se há evidências suficientes para rejeitar uma hipótese inicial (hipótese nula) em favor de uma hipótese alternativa.
## Componentes do Teste de Hipóteses

1. **Hipótese Nula (H0)**: A hipótese inicial que assume que não há efeito ou diferença. É o ponto de partida para o teste.
2. **Hipótese Alternativa (H1 ou Ha)**: A hipótese que sugere a existência de um efeito ou diferença. É o que tentamos provar.
3. **Nível de Significância (α)**: A probabilidade de rejeitar a hipótese nula quando ela é verdadeira. Comumente, valores de 0.05, 0.01, e 0.10 são usados.
4. **Estatística de Teste**: Uma medida calculada a partir dos dados amostrais que é usada para decidir entre H0 e H1.
5. **Valor-P (P-Value)**: A probabilidade de obter um resultado tão extremo quanto o observado, assumindo que a hipótese nula é verdadeira.
6. **Decisão**: Com base no valor-p e no nível de significância, decidimos se rejeitamos ou não a hipótese nula.
## Passos para Realizar um Teste de Hipóteses

1. **Formular as Hipóteses**
    - H0: Não há diferença (ou efeito).
    - H1: Há diferença (ou efeito).
2. **Escolher o Nível de Significância (α)**
    - Comumente, 0.05 é usado.
3. **Calcular a Estatística de Teste**
    - Dependendo do teste, pode ser *t-*teste, *z-*teste, _χ_2-teste, etc.
4. **Determinar o Valor-P**
    - Calcular a probabilidade de observar a estatística de teste sob H0.
5. **Tomar uma Decisão**
    - Se o valor-p < α, rejeitar H0.
    - Se o valor-p ≥ α, não rejeitar H0.
## Tipos Comuns de Testes de Hipóteses

1. **Teste 𝑡-teste para uma média**
2. **Teste 𝑡-teste para duas médias**
3. **Teste 𝜒2-teste para independência**
4. **Teste 𝑧-teste para proporções**
## Exemplos de Testes de Hipóteses

## Exemplo 1: **Teste 𝑡-teste para uma Média**

**Problema:** Suponha que a média populacional de uma característica seja 50. Uma amostra de 30 elementos tem uma média de 52 e um desvio padrão de 5. Queremos testar se a média populacional é diferente de 50 ao nível de significância de 0.05.

1. **Formular as Hipóteses**
    - H0:
   ![[42.png]]
    
    - H1:
    ![[43.png]]
    
2. **Escolher o Nível de Significância (α)**
    - α = 0.05
3. **Calcular a Estatística de Teste**
    ![[44.png]]
4. **Determinar o Valor-P**
    - Usando uma tabela \( t \) ou software estatístico, encontramos que para (formula em imagem) e 29 graus de liberdade, o valor-p é aproximadamente 0.036.
        ![[45.png]]
5. **Tomar uma Decisão**
    - Como o valor-p (0.036) < α (0.05), rejeitamos H0.

Portanto, há evidências suficientes para sugerir que a média populacional é diferente de 50.

## Exemplo 2: Teste $𝜒2$-teste para Independência

**Problema:** Suponha que queremos testar se há uma associação entre gênero e preferência de produto em uma pesquisa. Temos a tabela de contingência a seguir:

|          | Produto A | Produto B | Total |
| -------- | --------- | --------- | ----- |
| Homens   | 30        | 10        | 40    |
| Mulheres | 20        | 40        | 60    |
| Total    | 50        | 50        | 100   |

1. **Formular as Hipóteses**
    - H0: Não há associação entre gênero e preferência de produto.
    - H1: Há associação entre gênero e preferência de produto.
2. **Escolher o Nível de Significância (α)**
    - α = 0.05
3. **Calcular a Estatística de Teste** $𝜒2$
    - Calcular as frequências esperadas:
        ![[46.png]]
    - Calcular $𝜒2$:
        ![[47.png]]
4. **Determinar o Valor-P**
    - Com 1 grau de liberdade (df = (r-1)(c-1) = 1), usando uma tabela $𝜒2$ ou software estatístico, encontramos que o valor-p é muito pequeno (< 0.001).
5. **Tomar uma Decisão**
    - Como o valor-p < α (0.05), rejeitamos H0.

Portanto, há evidências suficientes para sugerir que há uma associação entre gênero e preferência de produto.

## Conclusão

Os testes de hipóteses são ferramentas essenciais para cientistas de dados e analistas de dados. Eles permitem que se faça inferências sobre populações a partir de dados amostrais, ajudando a validar teorias e tomar decisões baseadas em dados. Compreender os conceitos, tipos e passos dos testes de hipóteses é fundamental para conduzir análises estatísticas robustas e precisas.


[link de compartilhamento](https://correiarodrigues.com.br/notas/estatistica/teste-de-hipoteses/)

<sup><sub>
Renée Maksoud - julho de 2024
</sub></sup>
