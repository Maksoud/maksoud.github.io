# 📌 Estratégia Inicial: Canal de Preço com Controle de Capital e Venda Programada com Lucro


## 🎯 Objetivo

Executar operações dentro de um canal de preço pré-estabelecido, priorizando entradas com maior probabilidade de acerto e saídas controladas, utilizando uma **parcela fixa da banca** e **preservando o capital principal**. Os lucros não são reinvestidos automaticamente, permanecendo segregados para controle e proteção de capital.


## ⚙️ Parâmetros Operacionais

|Parâmetro|Valor/Descrição|
|---|---|
|**Timeframe de Análise**|Gráfico de 4 horas (H4)|
|**Canal de Preço**|Base: 100.489 / Teto: 110.626|
|**Capital Alocado**|20% do saldo disponível (valor fixo por estratégia)|
|**Lucro**|Não reinvestido — permanece separado do capital de operação|
|**Taxas de Operação**|Consideradas no cálculo do preço mínimo de venda|
|**Critério de Compra**|Valorização de +1% a +2% sobre o fundo do canal (configurável)|
|**Critério de Venda**|Queda de -1% a -2% a partir do topo, com lucro acima das taxas|


## 📈 Regras de Compra (Entrada)

- A entrada só ocorrerá **após uma valorização relevante sobre o ponto mínimo do canal**.
- Evita compras em momentos de lateralização ou queda contínua.
- A valorização mínima pode ser definida pelo operador (ex.: +2% sobre o fundo mais recente).


## 📉 Regras de Venda (Saída)

- A venda será programada **somente se o preço estiver acima do valor de compra + taxas**, com um lucro mínimo configurável.
- Preferencialmente realizada após uma desvalorização percentual a partir do topo do canal (ex.: -2%), mas sempre respeitando o critério de lucro mínimo.
- **Nunca será executada a mercado com prejuízo.**
- Em caso de rompimento do canal, o preço de venda assumirá o menor lucro + taxas para ser programado, garantindo com isso que vendas não sejam esquecidas ou realizadas com valor menor futuramente.


## 💰 Gestão de Capital

- O capital destinado à estratégia é fixo e configurável (ex.: 20% da banca).
- Os lucros gerados são acumulados à parte, **não aumentam o capital de operação automaticamente**.
- O valor da banca pode ser recalculado periodicamente para ajustar o capital alocado.
- É necessário manter um saldo de BNB (moeda da Binance) afim de garantir uma taxa mais atrativa nas operações.


## 🧠 Exemplo Prático

- **Banca Total:** 10.000 USDT
- **Capital Alocado para Estratégia:** 2.000 USDT
- **Compra:** após valorização de 2% sobre o fundo (ex.: de 100.000 → 102.000)
- **Venda:** após queda de 2% a partir do topo (ex.: de 110.000 → 107.800), desde que acima do preço de compra + taxas


## 🗂️ Campos no Sistema

|Campo|Tipo|Exemplo|
|---|---|---|
|Nome da Estratégia|Texto|Canal H4 - Controle de Capital|
|Par Operado|Seleção|BTC/USDT|
|Capital Alocado (%)|Número|20|
|Considera Lucros?|Booleano|Não|
|Limite Inferior (Base)|Decimal|100.489|
|Limite Superior (Teto)|Decimal|110.626|
|% Valorização para Compra|Decimal|2|
|% Desvalorização para Venda|Decimal|2|
|Preço Mínimo para Venda|Cálculo|Compra + Taxas + Lucro mínimo|


## ✅ Benefícios da Estratégia

- **Redução de riscos:** Ao não reinvestir lucros, o capital principal é protegido.
- **Maior assertividade:** Entradas apenas após sinais consistentes de valorização.
- **Saídas controladas:** Venda somente com lucro efetivo e programado.


## 🚫 Problema Evitado

Evita a exposição indefinida de capital em posições que saíram do canal sem uma estratégia de saída.  
**Não há venda imediata no prejuízo**, nem mesmo após rompimentos do canal.


## 🔁 Fluxo Operacional

| Etapa | Ação                                                            |
| ----- | --------------------------------------------------------------- |
| 1     | Operador configura a estratégia                                 |
| 2     | Sistema monitora os preços via WebSocket (Binance)              |
| 3     | Identifica valorização sobre o fundo → Registra a compra        |
| 4     | Acompanha a posição (dentro ou fora do canal)                   |
| 5     | Se o preço atingir o alvo de venda com lucro → Registra a venda |
| 6     | Atualiza os relatórios e painéis                                |


## 🧩 Monitoramento de Posições Abertas

Toda compra realizada será registrada com:

- Par de moeda, quantidade, preço, taxas, data/hora
- Estratégia vinculada
- Status da operação: `Aberta`, `Venda Programada`, ou `Encerrada`

### Quando o preço sair do canal:

- A posição **não será encerrada imediatamente**
- O sistema agendará uma **venda futura programada com lucro mínimo esperado**


## 📤 Venda por Saída de Canal (Lucro Programado)

|Situação|Ação|
|---|---|
|Preço rompe o canal (teto ou base)|Sistema verifica se há posição aberta vinculada|
|Preço ainda está abaixo do valor mínimo de venda|Sistema registra que está "fora do canal" e agenda venda futura|
|Preço atinge o alvo mínimo com lucro|Venda é executada e registrada como "Venda programada com lucro"|


## 🗄️ Campos Específicos para Controle

|Campo|Tipo|Exemplo|
|---|---|---|
|Status da Posição|Enum|Aberta / Programada / Encerrada|
|Preço Alvo de Venda|Decimal|102.300 USDT|
|Motivo da Venda|Texto|Saída de canal|
|Data da Saída do Canal|Datetime|2025-06-22 14:00|
|Data da Venda Programada|Datetime|2025-06-22 14:03|
|Margem de Lucro Mínimo|Percentual|0,5%|


## 🔄 Exemplo de Execução

1. Compra BTC/USDT a 102.000 USDT
2. Preço cai para 100.300 USDT → **Sai do canal**
3. Sistema calcula preço alvo mínimo: 102.300 USDT
4. Preço volta a subir → atinge 102.350 USDT
5. Venda é executada com lucro e marcada como **"Venda pós-saída de canal"**


## 🔒 Regras Essenciais do Sistema

- ❌ Nunca vender com prejuízo após saída de canal
- ✅ Toda saída de canal gera **venda programada com lucro mínimo**
- ✅ Relatórios destacam posições "em recuperação" aguardando venda
- ✅ Transparência total das operações em aberto, encerradas e programadas



<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>