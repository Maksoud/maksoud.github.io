# 📌 Detalhamento Técnico - Estratégia Operacional

Este documento contém a descrição técnica dos requisitos relacionados à execução da estratégia "Canal de Preço com Controle de Capital e Venda Programada com Lucro". Ele serve como guia para o desenvolvimento progressivo da lógica de negociação automatizada no Criptoren.

---

## 🎯 Objetivo da Estratégia

- Comprar após valorização de X% sobre o fundo do canal
- Vender após desvalorização de Y% a partir do topo, com lucro mínimo garantido
- Em caso de rompimento do canal para baixo, programar venda com lucro mínimo (sem prejuízo)

---

## 📋 Requisitos Técnicos

### 🧩 Detecção de rompimento para baixo do canal

- Detectar se o preço atual está abaixo do limite inferior (`limite_inferior`) da estratégia
- Marcar operação como "fora do canal"
- Registrar campo `data_saida_canal`

### 🧩 Programar venda futura com lucro mínimo após rompimento

- Calcular `preco_alvo_venda` = valor_compra + 0.5% + taxas
- Registrar `data_venda_programada` no momento do rompimento
- Garantir que a venda só ocorra com lucro

### 🧩 Campos adicionais obrigatórios (modelo Operacao)

- `preco_alvo_venda` (decimal)
- `data_saida_canal` (datetime)
- `data_venda_programada` (datetime)
- `motivo_venda` (texto)
- `margem_lucro_minimo` (decimal)

### 🧩 Garantias da Estratégia

- Nunca vender com prejuízo
- Toda compra deve originar uma venda futura (imediata ou programada)
- Vendas com `motivo_venda='Saída do canal'` devem ser destacadas

### 🧩 Configurações parametrizáveis por estratégia

- % valorização para compra (ex: 2%)
- % desvalorização para venda (ex: 2%)
- % lucro mínimo (ex: 0.5%)
- Limite inferior e superior do canal
- Capital alocado fixo

---


<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>