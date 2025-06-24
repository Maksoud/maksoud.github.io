
### Objetivo da Estratégia

Operar dentro de um canal de preço previamente identificado, buscando maximizar a assertividade das entradas e saídas, utilizando uma parcela fixa do capital da banca, e **não reinvestindo os lucros gerados nas operações**.

### Parâmetros Operacionais

|Parâmetro|Valor|
|---|---|
|**Timeframe de Análise**|Gráfico de 4 horas (H4)|
|**Canal de Preço**|Mínimo: 100.489 / Máximo: 110.626|
|**Capital Alocado**|20% da banca disponível (valor fixo, sem reinvestimento de lucros)|
|**Cálculo de Lucro**|Lucros gerados nas operações não são incorporados ao capital de operação (lucro separado)|
|**Taxas**|Considerar as taxas de operação da Binance ao calcular os limites de venda|
### Regras de Compra (Entrada)

- A compra será disparada **apenas quando houver uma valorização significativa** a partir do **menor valor registrado dentro do canal no período recente**.
- O operador busca com isso **evitar compras em movimento lateral ou de queda contínua**, e só entrar após sinais de reversão positiva.
- Exemplo de critério (ajustável no sistema futuramente):
    - **% de valorização mínima** a partir do fundo: Exemplo: +1% ou +2% (definível por configuração).

### Regras de Venda (Saída)

- A venda será disparada quando houver uma **desvalorização percentual a partir do topo mais recente dentro do canal**, desde que:
    1. O valor atual **seja maior que o preço da compra + taxas** (para evitar saídas no prejuízo).
    2. Exemplo de critério de saída:
        - **Queda de -1% ou -2% a partir do topo**, ajustável via sistema.

### Gestão de Capital

- Capital **fixo por estratégia:** 20% da banca.
- Lucros acumulados **não são reaplicados**. O capital base permanece o mesmo até nova configuração.
- Caso o capital da banca sofra variação (por saques ou perdas em outras estratégias), o valor de 20% pode ser recalculado periodicamente.

Suponha:

- Banca atual: **10.000 USDT**
- Capital para a estratégia: **2.000 USDT**
- Compra: ocorre se o preço sobe **2% a partir do fundo das últimas horas no canal**.
- Venda: ocorre se o preço cai **2% a partir do topo**, desde que respeite o mínimo de lucro (superando taxas).

### Possíveis Campos no Sistema para essa Estratégia:

| Campo                            | Tipo     | Exemplo                        |
| -------------------------------- | -------- | ------------------------------ |
| Nome da Estratégia               | Texto    | Canal H4 - Controle de Capital |
| Par Operado                      | Seleção  | BTC/USDT                       |
| Capital Alocado (%)              | Número   | 20 (saldo da banca na config.) |
| Considera Lucros?                | Booleano | Não                            |
| Limite Inferior (Base)           | Número   | 100.489                        |
| Limite Superior (Teto)           | Número   | 110.626                        |
| % Valorização Mínima para Compra | Número   | 2                              |
| % Desvalorização para Venda      | Número   | 2                              |
| Critério de Venda Mínima         | Cálculo  | Preço Compra + Taxas           |
### Benefícios dessa Estratégia:

- **Proteção de Capital:** Uso de apenas uma parcela fixa da banca.
- **Evita operações impulsivas:** Entradas somente após confirmação de valorização.
- **Realização de Lucros Controlada:** Saídas programadas considerando oscilações de curto prazo dentro do canal.

### Problema Evitado:

Evitar a permanência de posições compradas abertas indefinidamente quando o preço **sai do canal de operação**, deixando o capital exposto ao risco sem uma saída programada.

### Relação entre Estratégia, Operações e Relatório

Estratégia → Gera → Operações → Gera → Relatórios

### Etapas

| Etapa | Ação                                                        |
| ----- | ----------------------------------------------------------- |
| 1     | Operador configura estratégia                               |
| 2     | Sistema monitora preço via Binance API                      |
| 3     | Sistema avalia critérios de entrada                         |
| 4     | Se critérios atingidos → Registra compra                    |
| 5     | Sistema acompanha posição (dentro ou fora do canal)         |
| 6     | Se preço atingir o alvo de venda com lucro → Registra venda |
| 7     | Sistema atualiza relatórios                                 |

---
### Nova Regra de Monitoramento: **Controle de Posições Abertas**

#### Para cada compra realizada (real ou simulada), o sistema deverá:

- Registrar os seguintes dados:
    - Par de moeda
    - Preço de compra
    - Quantidade
    - Data/hora
    - Taxas
    - Estratégia vinculada
    - Status da operação: **Aberta** ou **Encerrada**
- Manter a posição **marcada como "aberta"** até que:
    1. Uma venda seja executada de forma programada pela estratégia (ex: queda de % a partir do topo, dentro do canal), ou
    2. Uma venda de emergência (forçada) seja registrada caso o preço **ultrapasse o limite inferior ou superior do canal**.

### Nova Regra de Saída: **Venda por Saída de Canal (Stop Fora do Canal)**

Sempre que o preço da moeda **sair dos limites do canal (abaixo da base ou acima do teto)**, e existirem compras abertas associadas àquela estratégia/par, o sistema deverá:

**Jamais realizar uma venda no prejuízo só porque o preço saiu do canal.**

✅ Toda posição aberta só será encerrada com uma venda **acima do preço de compra + taxa mínima de lucro**. **Mesmo que o preço da moeda saia do canal de operação (rompa o teto ou a base), o sistema não fará venda imediata a preço de mercado.**  
✅ Se o preço estiver fora do canal, a estratégia deverá **registrar uma venda com o mínimo lucro esperado**. A estratégia será: **registrar uma venda futura, programada, no mínimo lucro esperado**, considerando o preço de compra + taxas + lucro mínimo.

### Regra de Gestão para Saída de Canal

|Situação|Ação|
|---|---|
|O preço rompe o limite inferior (base) ou superior (teto) do canal|O sistema verifica se há posições abertas daquela estratégia/par|
|Existe posição aberta e o preço atual ainda está abaixo do valor de venda com lucro|O sistema registra internamente que aquela posição está “fora do canal” e **agenda uma venda futura com o preço alvo mínimo de lucro**|
|O preço posteriormente atinge o valor de venda programado|A venda é executada e registrada com o status "Venda programada após saída do canal com lucro mínimo"|
### Campos Extras Necessários na Base de Dados:

|Campo|Tipo|Exemplo|
|---|---|---|
|Status da Posição|Enum|Aberta / Venda Programada / Encerrada|
|Motivo da Venda|Texto|Venda programada por saída do canal|
|Preço alvo da venda|Decimal|Exemplo: 102.300 USDT|
|Data da saída do canal|Datetime|Quando a cotação saiu do canal|
|Data de programação da venda|Datetime|Quando o sistema registrou a venda programada|
|Condição mínima de lucro|Decimal (ou %)|Exemplo: 0,5% acima do preço de compra + taxas|
### Fluxo Exemplo de Evento:

1. **Compra feita:**  
    Par BTC/USDT a 102.000 USDT.
2. **Cotação atual:**  
    Preço cai e rompe o limite inferior do canal: chega a 100.300 USDT.
3. **Ação do sistema:**  
    Detecta que há uma posição aberta fora do canal → Sistema calcula:  
    "Preço de venda mínima aceitável = Preço de compra + taxas + lucro mínimo = 102.300 USDT"
4. **Venda programada:**  
    O sistema registra a **venda programada**.
5. **Quando o preço atinge o alvo:**  
    Exemplo: o preço sobe para 102.350 USDT → **Venda é executada e registrada**.
6. **Resultado:**  
    O relatório da estratégia mostrará que a venda foi **pós saída de canal**, mas sempre **com lucro**.

### Novos Comportamentos Obrigatórios no Sistema:

- Sistema **nunca** executa vendas no prejuízo por rompimento de canal.
- Toda saída de canal dispara uma programação automática de venda com lucro mínimo.
- Possibilidade de listar no painel:  
    ✅ "Posições fora do canal aguardando venda com lucro mínimo".



<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>