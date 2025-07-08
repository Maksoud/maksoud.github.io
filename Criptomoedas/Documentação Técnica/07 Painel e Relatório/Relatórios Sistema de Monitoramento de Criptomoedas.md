## [Projeto de Gestão de Criptomoedas](<https://maksoud.github.io/Criptomoedas/Projeto%20de%20Gest%C3%A3o%20de%20Criptomoedas>)

# 📈 Relatórios Esperados – Sistema de Monitoramento de Criptomoedas


## Relatórios de Performance por Estratégia

- **Lucro/Prejuízo Total por Estratégia**
- **Quantidade total de operações por estratégia**
- **Taxa de acerto (% de operações com lucro)**
- **Lucro acumulado no período (Diário / Semanal / Mensal)**
- **Capital atualmente alocado em cada estratégia**
- **Capital total movimentado (volume operado)**


## Relatórios de Operações Individuais

- **Histórico detalhado de todas as operações (Compra/Venda)**
    - Data e hora
    - Par de moeda
    - Tipo de operação (Compra / Venda)
    - Estratégia utilizada
    - Preço de entrada
    - Preço de saída
    - Lucro ou prejuízo
    - Percentual de ganho por operação
    - Taxas pagas na operação
    - Motivo da venda (Venda por critério de estratégia / Venda programada por saída de canal / Outro motivo definido)


## Relatório de Posições Abertas

- **Lista de todas as posições atualmente abertas**
    - Data da compra
    - Preço de compra
    - Quantidade
    - Status (Dentro do canal / Fora do canal aguardando venda programada)
    - Preço alvo mínimo programado para venda
    - Tempo de exposição (dias desde a compra)


## KPIs Sugeridos

| Indicador                     | Descrição                                 |
| ----------------------------- | ----------------------------------------- |
| Total de Lucro Acumulado      | Por estratégia, período ou par            |
| % de Acerto                   | Operações lucrativas x total de operações |
| Lucro Médio por Operação      | Média de ganho                            |
| Tempo Médio de Posição Aberta | Tempo de exposição ao risco               |
| Lucro Total vs Taxas Pagas    | Para medir eficiência da operação         |


## Relatório de Posições Fora do Canal (Em Recuperação)

- Todas as posições que estão **fora do canal de operação**, mas que **ainda aguardam atingir o preço mínimo de lucro para venda**.

Campos sugeridos:

|Campo|Exemplo|
|---|---|
|Par|BTC/USDT|
|Data da Compra|2025-06-22 10:00|
|Preço de Compra|102.000 USDT|
|Preço atual|100.300 USDT|
|Preço Alvo Programado|102.300 USDT|
|Tempo fora do canal|3 dias|
|Status|Aguardando recuperação|


## Relatório Comparativo entre Estratégias

- **Comparativo de performance entre diferentes estratégias**
    - Lucro acumulado por estratégia
    - % de acerto por estratégia
    - Drawdown máximo por estratégia
    - Tempo médio de exposição das operações por estratégia


## Relatórios de Evolução Temporal

- **Gráfico de Evolução de Lucro no Tempo**
    - Linha de evolução diária, semanal ou mensal
- **Histórico de saldo de banca**
    - Exibir o crescimento ou queda do capital total ao longo do tempo
- **Histórico de Capital Alocado por Estratégia**


## Relatório de Impacto das Taxas

- **Total de taxas pagas por período**
- **% das taxas sobre o lucro total**
- **Estratégias com maior impacto de taxas**


## Relatório de Lucro por Par de Moedas

- Exibir **lucro/prejuízo acumulado por cada par de moedas operado**  
    (BTC/USDT, ETH/USDT, etc.)


## Relatório de Riscos e Exposições

- **Tempo médio de permanência de posições abertas fora do canal**
- **Quantidade de operações que precisaram de venda programada por saída de canal**
- **Tempo médio para recuperação de preço após saída de canal**

---


<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>