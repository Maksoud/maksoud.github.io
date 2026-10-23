### Sumário > Projeto de Gestão de Criptomoedas

# 📋 Requisitos Técnicos - Logs e Auditoria

Este documento apresenta os requisitos e estruturas necessárias para garantir **transparência**, **rastreabilidade** e **confiabilidade** das operações realizadas automaticamente pelo sistema Criptoren.

---

## 🎯 Objetivos dos Logs

- Rastrear decisões automáticas do sistema (compra, venda, rompimento)
- Fornecer histórico detalhado para auditoria técnica e estratégica
- Permitir identificação de falhas ou comportamentos inesperados

---

## 🧩 Requisitos Técnicos

### 🔹 Registro de eventos

- Cada ação tomada pelo sistema deve ser registrada com:
    
    - Timestamp UTC preciso
    - Tipo do evento (INFO, ALERT, ERROR)
    - Categoria (COMPRA, VENDA, ESTRATEGIA, SISTEMA)
    - Mensagem legível por humanos
    - ID da operação vinculada (quando aplicável)

### 🔹 Tipos de eventos esperados

- Início e fim da execução do sistema
- Conexão/Desconexão com WebSocket
- Estratégia ativada/desativada
- Compra realizada / venda realizada
- Venda programada após rompimento
- Bloqueio de venda por falta de lucro
- Tentativas inválidas (ex: sem fundo definido, sem saldo, erro de API)

### 🔹 Modelo de dados sugerido (`Log`)

- `id` (auto-incremento)
- `data_evento` (datetime)
- `tipo` (enum: INFO, ALERT, ERROR)
- `categoria` (texto: COMPRA, VENDA, etc.)
- `mensagem` (texto)
- `operacao_id` (opcional)

### 🔹 Integração com painel de monitoramento

- Os logs devem ser visualizados em ordem cronológica
- Filtros por tipo, categoria e operação
- Destaque para ALERTs e ERRORs

### 🔹 Persistência

- Todos os logs devem ser salvos no banco PostgreSQL
- Rotina para limpeza periódica ou exportação para arquivo

### 🔹 Logs estratégicos obrigatórios

- Motivo da venda (lucro, rompimento, desativação)
- Justificativa do não acionamento da venda (ex: abaixo do valor mínimo)
- Alterações nos parâmetros da estratégia (com histórico)

---

## ✅ Benefícios Esperados

- Melhora na confiabilidade e manutenção do sistema
- Base sólida para tomada de decisão e ajuste da estratégia
- Transparência total das decisões automatizadas

---


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/06-testes/requisitos-tecnicos-logs-e-auditoria/)

<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>