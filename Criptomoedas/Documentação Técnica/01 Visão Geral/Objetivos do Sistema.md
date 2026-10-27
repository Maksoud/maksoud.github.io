# **📌 Objetivo do Sistema**

`/Criptomoedas/Documentação Técnica/01 Visão Geral/Objetivos do Sistema.md`  
_(Disponível em: [correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/01-visao-geral/objetivos-do-sistema](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/01-visao-geral/objetivos-do-sistema/))_

## **1. Contexto**  
Sistema automatizado de compra e venda de criptomoedas na Binance, baseado em uma **estratégia de canal de preço** com:  
- 🛡️ Controle rigoroso de capital (alocação fixa de 20% da banca).  
- 📉 Vendas programadas apenas com lucro mínimo garantido.  
- 🔄 Segregação de lucros (não reinvestimento automático).  

## **2. Funcionalidades Principais**  
| Funcionalidade | Descrição |  
|----------------|-----------|  
| **Monitoramento H4** | Análise de candles de 4 horas para identificar canal de preço. |  
| **Compra Automática** | Entrada no mercado após valorização de +1% a +2% sobre o fundo do canal. |  
| **Venda Programada** | Saída com lucro mínimo (após queda de -1% a -2% do teto). |  
| **Gestão de Risco** | Bloqueio de vendas com prejuízo, mesmo em rompimento de canal. |  
| **Relatórios** | Histórico de operações e lucro acumulado por estratégia. |  

## **3. Requisitos Não Funcionais**  
- ⏱️ **Latência**: Resposta da API < 500ms para ordens críticas.  
- 🔒 **Segurança**: Chaves da Binance armazenadas com criptografia.  
- 📊 **Disponibilidade**: 99.5% de uptime (exceto durante manutenção).  

## **4. Exemplo de Fluxo**  
```python  
# Pseudocódigo da estratégia  
if preço_atual >= (base_canal * 1.02):  # Acionar compra  
    executar_compra()  
elif preço_atual <= (topo_canal * 0.98) and preço_atual >= preço_min_venda:  
    agendar_venda()  # Só vende com lucro!  
```  

## **5. Limitações Conhecidas**  
- ⚠️ Dependência da API Binance (sujeito a rate limits).  
- 📉 Não opera em mercados extremamente voláteis (stop-loss não é aplicável).  


---

### **🎯 Como Contribuir para Este Documento**  
1. **Edite** o arquivo `objetivo.md` para refletir mudanças no escopo.  
2. **Atualize** a seção *Limitações* conforme testes avançam.  
3. **Use tags** como `[WIP]` ou `[RFC]` para sinalizar seções em revisão.


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/01-visao-geral/objetivos-do-sistema/)

<sup><sub>
Renée Maksoud - julho de 2025
</sub></sup>
