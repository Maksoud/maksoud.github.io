# 📚 **Sumário da Documentação Técnica - Criptoren**

Um sistema de negociação automatizada de criptomoedas com estratégia baseada em canal de preço, controle de capital e vendas programadas com lucro.

---
```text
/Criptomoedas
├── /Documentação Técnica
│   ├── /01 Visão Geral
│   │   ├── Arquitetura.md
│   │   └── Objetivos do Sistema.md
│   └── /02 Configuração
│   │   ├── Pré-requisitos.md
│   │   └── Setup Inicial.md
│   └── /03 Estratégia
│   │   ├── Regras do Canal de Preços.md
│   │   └── Fluxo Operacional.md
│   └── /04 Desenvolvimento Técnico
│   │   ├── API Reference.md
│   │   ├── Modelagem de Dados.md
│   │   └── Integração Binance.md
│   └── /05 Gestão de Risco
│   │   ├── Controle de Capital.md
│   │   └── Failover Strategies.md
│   └── /06 Testes
│   │   ├── Testes Unitários.md
│   │   └── Simulação de Mercado.md
│   └── /07 Painel e Relatório
│   │   ├── Performance_por_Estrategia.md
│   │   ├── Operacoes_Individuais.md
│   │   ├── Posicoes_Abertas.md
│   │   ├── KPIs.md
│   │   ├── Posicoes_Fora_Canal.md
│   │   ├── Comparativo_Estrategias.md
│   │   ├── Evolucao_Temporal.md
│   │   ├── Impacto_Taxas.md
│   │   ├── Lucro_Par_Moedas.md
│   │   └── Riscos_Exposicoes.md
```
#### **1. Visão Geral**

- 1.1. [Objetivo do Sistema](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/01%20Vis%C3%A3o%20Geral/Objetivos%20do%20Sistema) → 
    _Estratégia de canal de preço com controle de capital na Binance._
    
- 1.2. [Arquitetura](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/01%20Vis%C3%A3o%20Geral/Arquitetura) → 
    _Diagrama de componentes (FastAPI, PostgreSQL, Binance API)._

#### **2. Configuração do Ambiente**

- 2.1. Pré-requisitos → 
    *Python 3.10+, Docker, Binance API Keys.*
    
- 2.2. Setup Inicial → 
- docs/02_configuracao/setup.md`]  
    _Passo a passo para `docker-compose up` e instalação de dependências._

#### **3. Estratégia de Negócio**

- 3.1. Regras do Canal de Preço → 
    _Parâmetros (base, teto, % alvo) e exemplos matemáticos._
    
- 3.2. Fluxo Operacional → 
    _Diagrama de sequência (compra → monitoramento → venda)._

#### **4. Desenvolvimento Técnico**

- 4.1. API Reference → 
    _Endpoints FastAPI (métodos, schemas, exemplos)._
    
- 4.2. Modelagem de Dados → 
    _DER PostgreSQL e relação com classes Python._
    
- 4.3. Integração Binance → 
    _WebSocket, tratamento de erros, rate limits._

#### **5. Gestão de Risco**

- 5.1. Controle de Capital → 
    _Cálculo de 20% da banca e segregação de lucros._
    
- 5.2. Failover Strategies → 
    _O que fazer se a Binance API falhar?_

#### **6. Testes**

- 6.1. Testes Unitários → 
    _Exemplo: `pytest tests/test_channel_strategy.py`._
    
- 6.2. Simulação de Mercado → 
    _Backtesting com dados históricos._

#### **7. Relatórios**

- 7.1. Deploy Local → 
    _Configuração de `docker-compose.prod.yml`._
    
- 7.2. Cloud (AWS/Heroku) → 
    _CI/CD com GitHub Actions._


---

1. [**Documentação Técnica da Arquitetura e Funcionalidades do MVP**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Documenta%C3%A7%C3%A3o%20t%C3%A9cnica%20da%20arquitetura%20e%20funcionalidades%20do%20MVP)
2. [**Backlog do Produto**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Backlog%20de%20Produto%20-%20Criptoren)
3. [**Estratégia Operacional**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Detalhamento%20T%C3%A9cnico%20-%20Estrat%C3%A9gia%20Operacional)
4. [**Logs Auditoria**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Logs%20e%20Auditoria)
5. [**Painel Visualização**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Painel%20e%20Visualiza%C3%A7%C3%A3o)
6. [**Configurações Parâmetros**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Configura%C3%A7%C3%B5es%20e%20Par%C3%A2metros%20da%20Estrat%C3%A9gia)
7. [**Testes Automatizados**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Testes%20Automatizados
8. [**Relatórios Estratégicos e Analíticos**](https://maksoud.github.io/Criptomoedas/Documenta%C3%A7%C3%A3o%20T%C3%A9cnica/Requisitos%20T%C3%A9cnicos%20-%20Relat%C3%B3rios%20Estrat%C3%A9gicos%20e%20Anal%C3%ADticos)

---


<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>