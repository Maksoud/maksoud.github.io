Como Cientista de Dados, é essencial conhecer as principais fórmulas do Excel que podem ajudar no tratamento e análise dos dados. Aqui estão algumas das fórmulas mais úteis, divididas por categorias:

### 1. Fórmulas Estatísticas

- **MÉDIA/AVERAGE**: Calcula a média aritmética de um conjunto de valores.
    
    ```
    =MÉDIA(intervalo)
    ```
    
- **MEDIANA/MEDIAN**: Calcula a mediana de um conjunto de valores.
    
    ```
    =MEDIANA(intervalo)
    ```
    
- **DESVPAD/STDEV**: Calcula o desvio padrão de um conjunto de valores (para uma amostra).
    
    ```
    =DESVPAD(intervalo)
    ```
    
- **VAR.P**: Calcula a variância de uma população.
    
    ```
    =VAR.P(intervalo)
    ```
    
- **VAR.A/VAR.S**: Calcula a variância de uma amostra.
    
    ```
    =VAR.A(intervalo)
    ```
    
- **MÁXIMO/MAX**: Retorna o maior valor em um conjunto de valores.
    
    ```
    =MÁXIMO(intervalo)
    ```
    
- **MÍNIMO/MIN**: Retorna o menor valor em um conjunto de valores.
    
    ```
    =MÍNIMO(intervalo)
    ```
    
- **CONT.VALORES/COUNT**: Conta o número de células que contém números em um intervalo.
    
    ```
    =CONT.VALORES(intervalo)
    ```
    

### 2. Fórmulas de Pesquisa e Referência

- **PROCV/VLOOKUP**: Procura um valor na primeira coluna de uma tabela e retorna um valor na mesma linha de uma coluna especificada.
    
    ```
    =PROCV(valor_procurado, intervalo_tabela, número_coluna, [procurar_intervalo])
    ```
    
- **ÍNDICE/INDEX**: Retorna o valor de uma célula em um intervalo especificado por um número de linha e coluna.
    
    ```
    =ÍNDICE(intervalo, número_linha, [número_coluna])
    ```
    
- **CORRESP/MATCH**: Retorna a posição relativa de um item em um intervalo que corresponde a um valor especificado.
    
    ```
    =CORRESP(valor_procurado, intervalo_procurado, [tipo_correspondência])
    ```
    

### 3. Fórmulas Lógicas

- **SE/IF**: Executa um teste lógico e retorna um valor se o teste for verdadeiro e outro valor se for falso.
    
    ```
    =SE(teste_lógico, valor_se_verdadeiro, valor_se_falso)
    ```
    
- **E/AND**: Verifica se todas as condições são verdadeiras.
    
    ```
    =E(condição1, condição2, ...)
    ```
    
- **OU/OR**: Verifica se alguma das condições é verdadeira.
    
    ```
    =OU(condição1, condição2, ...)
    ```
    

### 4. Fórmulas de Manipulação de Texto

- **CONCATENAR/CONCAT**: Junta vários textos em uma única célula.
    
    ```
    =CONCATENAR(texto1, texto2, ...)
    ```
    
- **ESQUERDA/LEFT**: Retorna o número especificado de caracteres do início de uma cadeia de texto.
    
    ```
    =ESQUERDA(texto, [número_caracteres])
    ```
    
- **DIREITA/RIGHT**: Retorna o número especificado de caracteres do final de uma cadeia de texto.
    
    ```
    =DIREITA(texto, [número_caracteres])
    ```
    
- **EXT.TEXTO/MID**: Retorna um número específico de caracteres de uma cadeia de texto, começando na posição especificada.
    
    ```
    =EXT.TEXTO(texto, início, número_caracteres)
    ```
    

### 5. Fórmulas de Data e Hora

- **HOJE/TODAY**: Retorna a data atual.
    
    ```
    =HOJE()
    ```
    
- **AGORA/NOW**: Retorna a data e hora atuais.
    
    ```
    =AGORA()
    ```
    
- **DIAS/DAYS**: Calcula o número de dias entre duas datas.
    
    ```
    =DIAS(data_final, data_inicial)
    ```
    
- **MÊS/MONTH**: Retorna o mês de uma data.
    
    ```
    =MÊS(data)
    ```
    
- **ANO/YEAR**: Retorna o ano de uma data.
    
    ```
    =ANO(data)
    ```
    
- **DIA/DAY**: Retorna o dia de uma data.
    
    ```
    =DIA(data)
    ```
    

### 6. Fórmulas de Finanças

- **VF/FV**: Calcula o valor futuro de um investimento com base em pagamentos periódicos e constantes e uma taxa de juros constante.
    
    ```
    =VF(taxa, número_períodos, pagamento, [valor_presente], [tipo])
    ```
    
- **VP/PV**: Calcula o valor presente de um investimento com base em pagamentos periódicos e constantes e uma taxa de juros constante.
    
    ```
    =VP(taxa, número_períodos, pagamento, [valor_futuro], [tipo])
    ```
    

### 7. Fórmulas de Análise de Dados

- **TENDÊNCIA/TREND**: Retorna valores ao longo de uma linha de tendência linear.
    
    ```
    =TENDÊNCIA(known_y's, [known_x's], [new_x's], [const])
    ```
    
- **CRESCIMENTO/GROWTH**: Retorna valores ao longo de uma curva de crescimento exponencial.
    
    ```
    =CRESCIMENTO(known_y's, [known_x's], [new_x's], [const])
    ```
    

---

# **Símbolos de Curinga**

1. **Asterisco (*)**
    - **Uso:** Representa qualquer sequência de caracteres (inclusive nenhum caractere).
    - **Exemplo:** Se você quiser filtrar todas as entradas que começam com "Mar", você pode usar "Mar*". Isso retornará "Marcos", "Maria", "Marinha", etc.
2. **Interrogação (?)**
    - **Uso:** Representa um único caractere qualquer.
    - **Exemplo:** Se você quiser filtrar todas as entradas que têm exatamente quatro letras e começam com "M", você pode usar "M???". Isso retornará "Mark", "Mike", etc.
3. **Tilde (~)**
    - **Uso:** Usado antes de um asterisco (*) ou interrogação (?) para tratá-los como caracteres literais em vez de curingas.
    - **Exemplo:** Se você quiser filtrar entradas que contenham exatamente o caractere "_", você pode usar "~_". Isso retornará células que contêm o caractere asterisco.

## **Exemplos de Uso em Filtros**

### **Exemplo 1: Usando o Asterisco (*)**

- **Objetivo:** Filtrar todas as entradas que contêm a palavra "data" em qualquer posição.
- **Critério de Filtro:** **`data*`**
- **Resultados Esperados:** "Database", "Big data", "Metadata", etc.

### **Exemplo 2: Usando a Interrogação (?)**

- **Objetivo:** Filtrar todas as entradas que têm exatamente cinco caracteres e terminam com "s".
- **Critério de Filtro:** **`????s`**
- **Resultados Esperados:** "Moses", "James", etc.

### **Exemplo 3: Usando a Tilde (~)**

- **Objetivo:** Filtrar todas as entradas que contêm exatamente o caractere "?".
- **Critério de Filtro:** **`~?`**
- **Resultados Esperados:** "What?", "Question?", etc.

## **Aplicação em Filtros de Dados**

Imagine que você tem uma lista de produtos e quer aplicar filtros avançados:

* Produto
* DataAnalyzer
* BigDataTool
* Metadata
* DataQuest
* Info?Tool
* Simple*Star

1. **Filtrar produtos que contêm "Data" em qualquer parte do nome:**
    - **Critério:** **`Data*`**
    - **Resultados:** "DataAnalyzer", "BigDataTool", "Metadata", "DataQuest"
2. **Filtrar produtos que têm exatamente 9 caracteres:**
    - **Critério:** **`?????????`**
    - **Resultados:** "DataQuest"
3. **Filtrar produtos que contêm exatamente o caractere "*":**
    - **Critério:** **`~*`**
    - **Resultados:** "Simple*Star"

---

# Fórmulas BD

No Excel, existem várias fórmulas avançadas de banco de dados (BD) que são extremamente úteis para realizar análises de dados complexas. Essas fórmulas ajudam a extrair, sumarizar e analisar dados com base em critérios específicos. Aqui estão algumas das principais fórmulas BD, juntamente com exemplos de uso:

### BDPROCV (DGET)

A função **BDPROCV** retorna um único valor de um campo de registro que atende a critérios específicos em um banco de dados.

**Sintaxe:**

```
=BDPROCV(base_de_dados, campo, critérios)
```

**Exemplo:** Suponha que você tenha uma tabela de funcionários com colunas "Nome", "Departamento" e "Salário". Você deseja encontrar o salário do funcionário chamado "João".

|Nome|Departamento|Salário|
|---|---|---|
|João|Vendas|5000|
|Ana|RH|6000|
|Pedro|TI|5500|

Critérios (em células separadas):

Nome

---

João

---

Fórmula:

```
=BDPROCV(A1:C4, "Salário", E1:E2)
```

Resultado: 5000

### BDMÉDIA (DAVERAGE)

A função **BDMÉDIA** retorna a média dos valores em um campo de registros no banco de dados que atende aos critérios especificados.

**Sintaxe:**

```
=BDMÉDIA(base_de_dados, campo, critérios)
```

**Exemplo:** Calcule a média dos salários no departamento de "Vendas".

Critérios (em células separadas):

Departamento

---

Vendas

---

Fórmula:

```
=BDMÉDIA(A1:C4, "Salário", E1:E2)
```

Resultado: 5000

### BDSOMA (DSUM)

A função **BDSOMA** retorna a soma dos valores em um campo de registros no banco de dados que atende aos critérios especificados.

**Sintaxe:**

```
=BDSOMA(base_de_dados, campo, critérios)
```

**Exemplo:** Some os salários dos funcionários no departamento de "TI".

Critérios (em células separadas):

Departamento

---

TI

---

Fórmula:

```
=BDSOMA(A1:C4, "Salário", E1:E2)
```

Resultado: 5500

### BDMÁX (DMAX)

A função **BDMÁX** retorna o valor máximo em um campo de registros no banco de dados que atende aos critérios especificados.

**Sintaxe:**

```
=BDMÁX(base_de_dados, campo, critérios)
```

**Exemplo:** Encontre o salário máximo no departamento de "RH".

Critérios (em células separadas):

Departamento

---

RH

---

Fórmula:

```
=BDMÁX(A1:C4, "Salário", E1:E2)
```

Resultado: 6000

### BDMÍN (DMIN)

A função **BDMÍN** retorna o valor mínimo em um campo de registros no banco de dados que atende aos critérios especificados.

**Sintaxe:**

```
=BDMÍN(base_de_dados, campo, critérios)
```

**Exemplo:** Encontre o salário mínimo no departamento de "Vendas".

Critérios (em células separadas):

Departamento

---

Vendas

---

Fórmula:

```
=BDMÍN(A1:C4, "Salário", E1:E2)
```

Resultado: 5000

### BDVAR (DVAR)

A função **BDVAR** retorna a variância dos valores em um campo de registros no banco de dados que atende aos critérios especificados.

**Sintaxe:**

```
=BDVAR(base_de_dados, campo, critérios)
```

**Exemplo:** Calcule a variância dos salários no departamento de "TI".

Critérios (em células separadas):

Departamento

---

TI

---

Fórmula:

```
=BDVAR(A1:C4, "Salário", E1:E2)
```

Resultado: 0 (já que há apenas um registro em "TI")

### BDVARP (DVARP)

A função **BDVARP** retorna a variância de uma população dos valores em um campo de registros no banco de dados que atende aos critérios especificados.

**Sintaxe:**

```
=BDVARP(base_de_dados, campo, critérios)
```

**Exemplo:** Calcule a variância da população dos salários no departamento de "RH".

Critérios (em células separadas):

Departamento

---

RH

---

Fórmula:

```
=BDVARP(A1:C4, "Salário", E1:E2)
```

Resultado: 0 (já que há apenas um registro em "RH")

### BDCONTAR (DCOUNTA)

A função **BDCONTAR** conta o número de células que não estão vazias em um campo de registros no banco de dados que atendem aos critérios especificados.

**Sintaxe:**

```
=BDCONTAR(base_de_dados, campo, critérios)
```

**Exemplo:** Conte o número de funcionários no departamento de "Vendas".

Critérios (em células separadas):

Departamento

---

Vendas

---

Fórmula:

```
=BDCONTAR(A1:C4, "Nome", E1:E2)
```

Resultado: 1

---
