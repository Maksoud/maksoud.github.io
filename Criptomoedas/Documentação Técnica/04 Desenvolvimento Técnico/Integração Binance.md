# 💱 Integração Binance  
`/Documentação Técnica/04 Desenvolvimento Técnico/Integração Binance.md`  

## 1. Configuração Inicial  
### 1.1. Requisitos de API  
```python
from binance.client import Client

client = Client(
    api_key=os.getenv('BINANCE_API_KEY'), 
    api_secret=os.getenv('BINANCE_API_SECRET')
)
```

| Permissão Necessária | Descrição                  |  
|-----------------------|----------------------------|  
| `Leitura`             | Consultar candles e saldos |  
| `Trading`             | Executar ordens            |  
| ❌ `Saques`           | Não é necessário           |  

## 2. Fluxo de Dados  
### 2.1. WebSocket (Tempo Real)  
```python
from binance import ThreadedWebsocketManager

def handle_candle(msg):
    if msg['k']['x']:  # Candle fechado
        process_strategy(
            symbol=msg['s'],
            close=float(msg['k']['c']),
            volume=float(msg['k']['v'])
        )

twm = ThreadedWebsocketManager()
twm.start_kline_socket(
    callback=handle_candle, 
    symbol="BTCUSDT", 
    interval=Client.KLINE_INTERVAL_4HOUR
)
```

### 2.2. Endpoints REST Críticos  
| Método                | Descrição                     | Limite de Requisições |  
|-----------------------|-------------------------------|-----------------------|  
| `get_klines()`        | Histórico de candles (H4)     | 50/min               |  
| `create_order()`      | Enviar ordens                 | 10/s                 |  
| `get_account()`       | Consultar saldos              | 5/s                  |  

## 3. Tratamento de Erros  
### 3.1. Códigos Comuns  
```python
try:
    order = client.create_order(...)
except BinanceAPIException as e:
    if e.code == -1021:  # Timestamp inválido
        resync_server_time()
    elif e.code == -1013:  # Filtro LOT_SIZE
        adjust_quantity(order)
```

| Código | Significado                  | Ação Recomendada               |  
|--------|------------------------------|--------------------------------|  
| `-1003`| Rate limit excedido          | Esperar 60s                    |  
| `-2010`| Saldo insuficiente           | Validar capital alocado        |  
| `-1121`| Símbolo inválido             | Verificar lista de ativos      |  

## 4. Modelo de Dados Binance → PostgreSQL  
```python
# Exemplo: Salvar candle no banco
async def save_candle(candle):
    await db.execute(
        "INSERT INTO candles (symbol, open, high, low, close, volume) "
        "VALUES (:symbol, :open, :high, :low, :close, :volume)",
        {
            "symbol": candle['symbol'],
            "open": candle['open'],
            "high": candle['high'],
            "low": candle['low'],
            "close": candle['close'],
            "volume": candle['volume']
        }
    )
```

## 5. Boas Práticas  
- **Cache Local**: Armazenar candles recentes para evitar chamadas repetidas  
- **Filtros**: Respeitar `LOT_SIZE` e `PRICE_FILTER` (consultar via `get_symbol_info()`)  
- **Sincronização**: Usar `get_server_time()` para evitar problemas de timestamp  

## 6. Exemplo Completo  
```python
async def execute_trade(strategy: Strategy):
    symbol_info = client.get_symbol_info(strategy.symbol)
    min_qty = float(next(
        f['minQty'] for f in symbol_info['filters'] 
        if f['filterType'] == 'LOT_SIZE'
    ))
    
    if strategy.quantity < min_qty:
        raise ValueError(f"Quantidade abaixo do mínimo: {min_qty}")
    
    order = client.create_order(
        symbol=strategy.symbol,
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_LIMIT,
        timeInForce=Client.TIME_IN_FORCE_GTC,
        quantity=round(strategy.quantity, 8),
        price=str(strategy.target_price)
    )
    
    await save_order_to_db(order)  # Persistir no PostgreSQL
```

## 7. Monitoramento  
### 7.1. Métricas Essenciais  
```prometheus
# HELP binance_api_requests Total de requisições à API
# TYPE binance_api_requests counter
binance_api_requests_total{endpoint="klines"} 42
binance_api_requests_failed{error="rate_limit"} 3
```

## 8. Próximos Passos  
1. [Configurar WebSocket para múltiplos símbolos](#)  
2. [Implementar fallback para REST quando WebSocket falhar](#)  

---

### ✅ Checklist de Implementação  
- [ ] Validar chaves API no painel da Binance  
- [ ] Testar limites de requisições em sandbox  
- [ ] Configurar tratamento para reconexão WebSocket  

```bash
# Para testar a conexão básica:
python -c "from binance.client import Client; print(Client().get_system_status())"
```