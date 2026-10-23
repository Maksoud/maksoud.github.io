### Sumário > Projeto de Gestão de Criptomoedas

# 📊 Requisitos Técnicos - Painel e Visualização

Este documento detalha os requisitos para o desenvolvimento de um painel visual que permita acompanhar em tempo real as operações automatizadas, o estado das estratégias e os dados de desempenho do sistema Criptoren.

---

## 🎯 Objetivos do Painel

- Exibir status atual das estratégias e posições abertas
- Permitir acompanhamento da execução da lógica automatizada
- Facilitar tomada de decisões e identificação de situações críticas

---

## 🧩 Requisitos Técnicos

### 🔹 Visualização de posições abertas

- Lista de todas as operações com status `Aberta` ou `Programada`
- Campos exibidos:
    - Par operado
    - Preço de compra
    - Preço alvo de venda (se programado)
    - Margem de lucro estimada
    - Status: Aberta / Venda Programada / Em Recuperação
    - Data da compra / Data programada de venda (se aplicável)

### 🔹 Visualização de posições encerradas

- Histórico de todas as vendas realizadas com:
    - Data e hora da venda
    - Motivo da venda (lucro, rompimento, manual)
    - Preço de venda
    - Lucro em valor e em %
    - Tempo de permanência da posição aberta

### 🔹 Status do sistema

- Conexão com WebSocket: ativa/inativa
- Estratégia ativa: sim/não
- Número de operações abertas / programadas / encerradas
- Log de eventos recentes (últimos 20 logs)

### 🔹 Filtros e navegação

- Filtro por par de moedas (ex: BTC/USDT, ETH/USDT)
- Filtro por status da operação
- Intervalo de datas
- Buscar por ID ou valor aproximado

### 🔹 Destaques visuais

- Posições "em recuperação" devem ser destacadas (ex: cor amarela)
- Operações com venda agendada próximas do alvo (ex: < 0.2% do alvo) devem ser sinalizadas
- Alertas de falhas ou bloqueios em vermelho (ex: tentativa de venda abaixo do lucro mínimo)

---

## 🧩 Requisitos de Backend para suporte ao painel

- Endpoint para listar posições abertas (com filtros)
- Endpoint para listar posições encerradas
- Endpoint para status geral do sistema
- Endpoint para logs recentes

---

## ✅ Benefícios Esperados

- Visibilidade operacional para tomada de decisão
- Diagnóstico rápido de problemas
- Transparência para validação da estratégia em tempo real

---


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/07-painel-e-relatorio/requisitos-tecnicos-painel-e-visualizacao/)

<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>