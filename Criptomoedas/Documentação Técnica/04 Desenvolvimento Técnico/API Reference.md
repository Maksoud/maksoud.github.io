# 📡 API Reference  
`/Documentação Técnica/04 Desenvolvimento Técnico/API Reference.md`  

## 1. Endpoints Principais  

### **1.1 Estratégias**  
| Método | Endpoint                | Descrição                          | Parâmetros (Body) |
|--------|-------------------------|------------------------------------|-------------------|
| `POST` | `/strategies`           | Cria nova estratégia de canal      | `{symbol, base_price, top_price, buy_threshold, sell_threshold, capital_percentage}` |
| `PATCH`| `/strategies/{id}`      | Atualiza parâmetros                | `{min_profit, is_active}` |
| `GET`  | `/strategies/active`    | Lista estratégias ativas           | - |

**Exemplo Request**:  
```python
import httpx

response = httpx.post(
    "http://localhost:8000/strategies",
    json={
        "symbol": "BTCUSDT",
        "base_price": 100489.00,
        "top_price": 110626.00,
        "buy_threshold": 1.5,
        "sell_threshold": 1.8,
        "capital_percentage": 20.0
    }
)
```

### **1.2 Ordens**  
| Método | Endpoint                | Descrição                          | 
|--------|-------------------------|------------------------------------|
| `POST` | `/orders/buy`           | Executa compra programada          | 
| `POST` | `/orders/sell`          | Executa venda imediata             |
| `GET`  | `/orders/scheduled`     | Lista vendas agendadas             |

**Exemplo Response**:  
```json
{
    "order_id": "abc123",
    "symbol": "BTCUSDT",
    "type": "buy",
    "quantity": 0.5,
    "price": 102000.00,
    "status": "filled"
}
```

---

## 2. Integração Binance  

### **2.1 WebSocket (Preços em Tempo Real)**  
```python
from binance import ThreadedWebsocketManager

def handle_socket_message(msg):
    if msg['e'] == 'kline' and msg['k']['x']:  # Candle fechado H4
        process_candle(msg['k'])

twm = ThreadedWebsocketManager(api_key, api_secret)
twm.start_kline_socket(callback=handle_socket_message, symbol="BTCUSDT", interval="4h")
```

### **2.2 REST API (Ordens)**  
**Métodos Essenciais**:  
```python
from binance.client import Client

client = Client(api_key, api_secret)

# Compra limitada
client.create_order(
    symbol="BTCUSDT",
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_LIMIT,
    timeInForce=Client.TIME_IN_FORCE_GTC,
    quantity=0.5,
    price="102000.00"
)

# Consulta saldo
client.get_asset_balance(asset='USDT')
```

---

## 3. Modelos Pydantic  
### **OrderSchema**  
```python
from pydantic import BaseModel

class OrderCreate(BaseModel):
    strategy_id: int
    symbol: str
    quantity: float
    type: Literal["buy", "sell"]

    class Config:
        json_schema_extra = {
            "example": {
                "strategy_id": 1,
                "symbol": "BTCUSDT",
                "quantity": 0.5,
                "type": "buy"
            }
        }
```

---

## 4. Códigos de Status  
| Código | Descrição                  | Ação Recomendada               |
|--------|----------------------------|--------------------------------|
| `429`  | Rate limit excedido        | Esperar 1 minuto               |
| `418`  | IP banido temporariamente  | Trocar IP ou aguardar 24h      |
| `200`  | Sucesso                    | Processar resposta normalmente |

---

## 5. Exemplo Completo  
**`app/api.py`**:  
```python
from fastapi import APIRouter

router = APIRouter()

@router.post("/strategies")
async def create_strategy(strategy: StrategyCreate):
    """Registra nova estratégia no banco de dados"""
    db_strategy = await save_strategy(strategy)
    return {"id": db_strategy.id}

@router.post("/orders/buy")
async def create_buy_order(order: OrderCreate):
    """Dispara ordem de compra na Binance"""
    if not await check_balance(order.symbol, order.quantity):
        raise HTTPException(400, "Saldo insuficiente")
    
    binance_order = await binance_create_order(
        symbol=order.symbol,
        side="BUY",
        quantity=order.quantity
    )
    return binance_order
```

---

## 6. Testando os Endpoints  
### **6.1 Localmente**  
```bash
curl -X POST "http://localhost:8000/strategies" \
  -H "Content-Type: application/json" \
  -d '{"symbol":"BTCUSDT","base_price":100489.00,"top_price":110626.00}'
```

### **6.2 Swagger UI**  
Acesse: `http://localhost:8000/docs`  

---

## 7. Próximos Passos  
1. [Monitoramento de desempenho](../07%20Painel%20e%20Relatório/Performance_por_Estrategia.md)  
2. [Configuração de segurança](../05%20Gestão%20de%20Risco/Failover%20Strategies.md)  

---

### ✅ Checklist de Implementação  
- [ ] Testar todos endpoints com `pytest`  
- [ ] Configurar rate limiting (100 requests/min)  
- [ ] Documentar erros personalizados  
