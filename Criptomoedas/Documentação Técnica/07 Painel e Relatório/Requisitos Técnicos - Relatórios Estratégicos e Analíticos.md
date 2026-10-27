# 📈 Requisitos Técnicos - Relatórios Estratégicos e Analíticos

Este documento consolida os requisitos para geração de relatórios estratégicos, táticos e analíticos no sistema Criptoren. Os relatórios têm como objetivo oferecer visão de desempenho, risco, oportunidade e eficiência da estratégia de negociação automatizada.

---

## 🎯 Objetivos Gerais

- Medir performance por estratégia e por operação
- Avaliar exposição ao risco e eficiência das execuções
- Oferecer subsídio para tomada de decisão e ajustes estratégicos
- Permitir rastreabilidade completa das operações

---

## 📊 Relatórios por Tipo

### 1. **Relatórios de Performance por Estratégia**

- Lucro/Prejuízo total
- Quantidade total de operações
- Taxa de acerto (% operações com lucro)
- Lucro acumulado (Diário / Semanal / Mensal)
- Capital atualmente alocado
- Volume total operado
- **Taxa de recuperação de posições fora do canal**
- **Tempo médio de recuperação após rompimento**

### 2. **Relatórios de Operações Individuais**

- Histórico detalhado (data, par, tipo, preço entrada/saída, lucro, % ganho, taxas)
- Motivo da venda (estratégia, rompimento, outro)
- **Data de saída do canal (se aplicável)**
- **Preço máximo/mínimo durante a exposição**
- **Lucro potencial não realizado**

### 3. **Relatório de Posições Abertas**

- Data e preço de compra
- Quantidade e status (dentro/fora do canal)
- Preço alvo mínimo programado
- Tempo de exposição
- **Preço atual e % até o alvo**
- **Drawdown atual da operação**

### 4. **KPIs Estratégicos Sugeridos**

|Indicador|Descrição|
|---|---|
|Total de Lucro Acumulado|Por estratégia, período ou par|
|% de Acerto|Lucro x Total|
|Lucro Médio por Operação|Média de ganho|
|Tempo Médio Posição Aberta|Tempo de exposição|
|Lucro Total vs Taxas Pagas|Eficiência líquida|
|Drawdown Médio por Operação|Perda não realizada|
|% de Posições Fora do Canal|Exposição fora da estratégia|
|Tempo Médio de Recuperação|Após rompimento|

### 5. **Relatório de Posições Fora do Canal (Em Recuperação)**

- Par, data de compra, preço compra, preço atual
- Preço alvo programado, tempo fora do canal
- **Histórico de tentativas de venda bloqueadas**
- **Status de proximidade do alvo (ex: chegou perto e não vendeu)**

### 6. **Relatório Comparativo entre Estratégias**

- Lucro acumulado
- % de acerto
- Drawdown máximo
- Tempo médio de exposição
- **% de vendas por rompimento**
- **Lucro médio por tipo de venda**

### 7. **Relatórios de Evolução Temporal**

- Gráfico de evolução de lucro (diário, semanal, mensal)
- Histórico de saldo da banca
- Histórico de capital alocado por estratégia
- **Evolução do número de operações abertas/encerradas**
- **Gráfico de exposição agregada diária**

### 8. **Relatório de Impacto das Taxas**

- Total de taxas pagas por período
- % das taxas sobre lucro
- Estratégias com maior impacto relativo das taxas
- **Simulações com taxas alternativas**

### 9. **Relatório de Lucro por Par de Moedas**

- Lucro/prejuízo por par operado (BTC/USDT, ETH/USDT, etc.)

### 10. **Relatório de Riscos e Exposições**

- Tempo médio fora do canal
- Quantidade de vendas programadas por rompimento
- Tempo médio de recuperação
- Total de capital exposto em posições fora do canal
- Maior drawdown individual e em sequência

---

## 🛠️ Requisitos Técnicos

- Endpoints para exportação em CSV e visualização em frontend
- Cálculo automático com base nas tabelas de operações, logs e estratégias
- Atualização contínua com base nas posições em tempo real

---


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/07-painel-e-relatorio/requisitos-tecnicos-relatorios-estrategicos-e-analiticos/)

<sup><sub>
Renée Maksoud - julho de 2025
</sub></sup>