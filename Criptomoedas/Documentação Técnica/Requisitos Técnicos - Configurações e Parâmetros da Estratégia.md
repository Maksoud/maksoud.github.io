# ⚙️ Requisitos Técnicos - Configurações e Parâmetros da Estratégia

Este documento descreve os requisitos necessários para gerenciar de forma dinâmica e persistente as configurações operacionais das estratégias utilizadas no sistema Criptoren.

---

## 🎯 Objetivos das Configurações

- Permitir personalização de parâmetros por par de moeda
- Garantir persistência e recuperação das configurações
- Facilitar ajustes operacionais sem necessidade de alteração de código

---

## 🧩 Requisitos Técnicos

### 🔹 Estrutura do modelo `Estrategia`

- `id`: identificador único
- `nome`: nome da estratégia (ex: Canal H4 - BTC)
- `par`: par operado (ex: BTC/USDT)
- `capital_alocado`: percentual fixo da banca (ex: 20%)
- `considera_lucro`: booleano
- `limite_inferior`: decimal (ex: 100000)
- `limite_superior`: decimal (ex: 110000)
- `pct_valorizacao_compra`: decimal (ex: 2.0)
- `pct_desvalorizacao_venda`: decimal (ex: 2.0)
- `lucro_minimo`: decimal (ex: 0.5)
- `ativo`: booleano
- `data_criacao`: datetime
- `data_atualizacao`: datetime

### 🔹 Funcionalidades esperadas

-  Criar, editar, listar e remover estratégias
-  Ativar/desativar estratégia sem excluir
-  Aplicar estratégia ativa em tempo real na lógica operacional
-  Validar unicidade por par ativo (um par, uma estratégia ativa)

### 🔹 Persistência e atualização

- Toda alteração deve atualizar `data_atualizacao`
- Estratégias ativas devem ser mantidas em cache ou memória para desempenho
- Estratégia atual deve ser recarregada ao reiniciar a aplicação

### 🔹 Interface administrativa (futura)

- Formulário para edição dos parâmetros
- Validação de campos com limites permitidos (ex: lucro mínimo ≥ 0.1%)
- Confirmação de ativação única por par

---

## ✅ Benefícios Esperados

- Flexibilidade para adaptação a diferentes cenários de mercado
- Maior controle e auditoria sobre mudanças de estratégia
- Possibilidade de múltiplos testes A/B com diferentes parâmetros

---


<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>