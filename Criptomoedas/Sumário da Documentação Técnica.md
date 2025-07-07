# 📚 **Sumário da Documentação Técnica - Criptoren**

Um sistema de negociação automatizada de criptomoedas com estratégia baseada em canal de preço, controle de capital e vendas programadas com lucro.

---

### 1. [**Documentação Técnica da Arquitetura e Funcionalidades do MVP**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Documenta%C3%A7%C3%A3o%20t%C3%A9cnica%20da%20arquitetura%20e%20funcionalidades%20do%20MVP)

- Estrutura geral do projeto (pastas e módulos)
- Componentes implementados no MVP
- Visão de backend, banco de dados, estratégia e WebSocket
- Fluxo de execução principal

---
## 📘 Visão Geral

### 2. [**Backlog do Produto**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Backlog%20de%20Produto%20-%20Criptoren)

Documenta funcionalidades já entregues e tarefas pendentes, com foco na maturidade incremental do sistema.

---

## 🧠 Estratégia e Operação

### 3. [**Estratégia Operacional**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Detalhamento%20T%C3%A9cnico%20-%20Estrat%C3%A9gia%20Operacional)

- Lógica completa da estratégia Canal de Preço
- Compra após valorização sobre o fundo
- Venda após desvalorização do topo com lucro mínimo
- Regras de segurança e programação de vendas após rompimento

---

## 🛡️ Logs e Auditoria

### 4. [**Logs Auditoria**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Logs%20e%20Auditoria)

- Registro detalhado de eventos da estratégia
- Modelo de dados para log com categorias e tipos
- Integração com painel e persistência

---

## 📊 Painel e Visualização

### 5. [**Painel Visualização**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Painel%20e%20Visualiza%C3%A7%C3%A3o)

- Exibição de posições abertas e encerradas
- Status de estratégias, WebSocket e alertas
- Filtros, indicadores e destaques visuais

---

## ⚙️ Configurações e Parâmetros

### 6. [**Configurações Parâmetros**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Configura%C3%A7%C3%B5es%20e%20Par%C3%A2metros%20da%20Estrat%C3%A9gia)

- Estrutura da entidade `Estrategia`
- Parâmetros configuráveis por par de moeda
- CRUD, ativação e persistência das configurações

---

## 🧪 Testes Automatizados

### 7. [**Testes Automatizados**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Testes%20Automatizados)

- Testes unitários da lógica de operação
- Testes de integração com WebSocket e banco
- Verificação de persistência e APIs

---

## 📈 Relatórios Estratégicos e Analíticos

### 8. [**Relatórios Estratégicos e Analíticos**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Relat%C3%B3rios%20Estrat%C3%A9gicos%20e%20Anal%C3%ADticos)

- Relatórios de performance por estratégia e por operação
- KPIs como lucro acumulado, drawdown, tempo médio de exposição
- Comparativo entre estratégias, pares de moedas e impacto de taxas
- Painéis de posições abertas, fora do canal e evolução da banca

---


<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>