# 🧪 Testes Unitários  
`/Documentação Técnica/06 Testes/Testes Unitários.md`  

## 1. Estrutura Básica  
### 1.1. Organização de Arquivos  
```bash
tests/
├── unit/
│   ├── test_strategy.py       # Testes de lógica de negócio
│   ├── test_binance_integ.py  # Testes com mocks da API
│   └── conftest.py            # Fixtures compartilhadas
```

### 1.2. Exemplo Básico (Pytest)  
```python
# test_strategy.py
from app.strategies import calculate_entry

def test_entry_above_base():
    """Testa sinal de compra quando preço está 2% acima da base"""
    assert calculate_entry(base=100.0, current=102.0, threshold=2.0) is True
```

## 2. Testando Componentes Críticos  

### 2.1. Lógica de Canal de Preço  
```python
# test_strategy.py
import pytest

@pytest.mark.parametrize("base,top,current,expected", [
    (100.0, 110.0, 102.0, True),    # Dentro do canal +2%
    (100.0, 110.0, 99.0, False),     # Abaixo da base
    (100.0, 110.0, 111.0, False)     # Acima do teto
])
def test_channel_logic(base, top, current, expected):
    from app.strategies import check_price_channel
    assert check_price_channel(base, top, current) == expected
```

### 2.2. Mock de API Binance  
```python
# test_binance_integ.py
from unittest.mock import patch

def test_get_balance(mock_binance):
    with patch('binance.client.Client.get_account') as mock_api:
        mock_api.return_value = {'balances': [{'asset': 'BTC', 'free': '0.5'}]}
        balance = get_balance('BTC')
        assert balance == 0.5
```

## 3. Padrões Recomendados  

### 3.1. Convenções de Nomeação  
| Tipo de Teste          | Padrão do Nome                          |  
|------------------------|-----------------------------------------|  
| Teste Positivo         | `test_[função]_[condição]_success`      |  
| Teste de Validação     | `test_[função]_invalid_[input]_rejects` |  
| Teste de Edge Case     | `test_[função]_edge_[cenário]`          |  

### 3.2. Fixtures Comuns (`conftest.py`)  
```python
import pytest
from app.database import create_test_db

@pytest.fixture
def mock_binance():
    with patch('app.binance.client.Client') as mock:
        yield mock

@pytest.fixture(scope="module")
def test_db():
    db = create_test_db()
    yield db
    db.close()
```

## 4. Testes de Banco de Dados  
### 4.1. Teste com SQLite em Memória  
```python
# test_database.py
def test_position_creation(test_db):
    from app.models import Position
    pos = Position.create(symbol='BTCUSDT', entry_price=50000.0)
    assert pos.id is not None
```

### 4.2. Verificação de Constraints  
```python
def test_invalid_position_raises(test_db):
    with pytest.raises(ValueError):
        Position.create(symbol='INVALID', entry_price=-100.0)  # Preço negativo
```

## 5. Cobertura e CI  
### 5.1. Configuração Mínima  
```yaml
# .github/workflows/tests.yml
name: Tests
on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: pip install pytest pytest-cov
      - run: pytest --cov=app --cov-report=xml
      - uses: codecov/codecov-action@v1
```

### 5.2. Relatório de Cobertura  
```bash
pytest --cov=app --cov-report=html
```
> Abrir `htmlcov/index.html` no navegador  

## 6. Próximos Passos  
1. [Adicionar testes de integração](../06%20Testes/Simulação%20de%20Mercado.md)  
2. [Configurar CI/CD com GitHub Actions](#)  

---

### ✅ Checklist de Qualidade  
- [ ] 80%+ de cobertura para módulos críticos  
- [ ] Todos os testes devem ser independentes  
- [ ] Mockar todas chamadas externas  

```bash
# Executar testes rapidamente
pytest -xvs tests/unit/test_strategy.py
``` 

---

Este documento estabelece as bases para testes confiáveis, essenciais para um sistema de trading. Mantenha os testes sempre atualizados com as regras de negócio!