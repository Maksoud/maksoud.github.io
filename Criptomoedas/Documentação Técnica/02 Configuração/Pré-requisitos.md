# 📋 Pré-requisitos Técnicos
`/Documentação Técnica/02 Configuração/Pré-requisitos.md`

## 1. Requisitos Mínimos

### 1.1. Sistema Operacional
| SO         | Versão    | Notas                          |
|------------|-----------|--------------------------------|
| Linux      | Ubuntu 22.04+ | Recomendado para produção    |
| Windows    | 10/11     | Requer WSL2 para Docker        |
| macOS      | Monterey+ | Testado na arquitetura M1/M2   |

### 1.2. Hardware
| Componente | Especificação               | Observações                     |
|------------|-----------------------------|---------------------------------|
| CPU        | 4 núcleos (x86_64/ARM)      | 2.5 GHz mínimo                 |
| RAM        | 8 GB                        | 16 GB para backtesting pesado  |
| Disco      | 50 GB SSD                   | Para histórico de mercado       |

## 2. Dependências Principais

### 2.1. Pacotes Python (requirements.txt)
```text
# 🚀 Núcleo
fastapi==0.95.2          # Framework web
python-binance==1.0.19   # API Binance
apscheduler==3.9.1       # Agendamento

# 🗃️ Banco de Dados
asyncpg==0.27.0          # PostgreSQL assíncrono
sqlalchemy==2.0.15       # ORM
alembic==1.11.1          # Migrações

# 🔐 Segurança
pydantic==2.1.1          # Validação
python-dotenv==1.0.0     # Variáveis de ambiente

# ⚙️ Infra
uvicorn==0.22.0          # Servidor ASGI

# 🧪 Testes (dev)
pytest==7.3.1            # Testes unitários
pytest-asyncio==0.21.0   # Testes async
```

### 2.2. Bancos de Dados
| Sistema      | Versão | Configuração Recomendada       |
|--------------|--------|--------------------------------|
| PostgreSQL   | 15+    | 2 vCPUs, 4GB RAM, 100GB disco |
| Redis        | 7.0+   | Opcional para cache            |

## 3. Contas Externas Obrigatórias

### 3.1. Binance API
- Tipo: **Spot Trading**
- Permissões necessárias:
  - ✅ Leitura
  - ✅ Trading
  - ❌ Saques (desativado por segurança)

### 3.2. Serviços Opcionais
| Serviço       | Uso                      | Plano Gratuito        |
|---------------|--------------------------|-----------------------|
| Sentry        | Monitoramento de erros   | 5k eventos/dia       |
| Datadog       | Métricas                 | 5 hosts              |

## 4. Script de Verificação

### 4.1. check_environment.py
```python
import subprocess
import sys

def check_package(name, min_version):
    try:
        pkg = __import__(name)
        if pkg.__version__ < min_version:
            print(f"❌ {name} {pkg.__version__} (requer >= {min_version})")
            return False
        print(f"✅ {name} {pkg.__version__}")
        return True
    except ImportError:
        print(f"⚠️ {name} não instalado")
        return False

requirements = {
    "fastapi": "0.95.2",
    "python-binance": "1.0.19",
    "asyncpg": "0.27.0"
}

all_ok = all(check_package(pkg, ver) for pkg, ver in requirements.items())
sys.exit(0 if all_ok else 1)
```

Execute com:
```bash
python check_environment.py
```

## 5. Configurações Recomendadas

### 5.1. Linux (Otimização)
```bash
# Aumentar limites para conexões WebSocket
echo "fs.file-max = 2097152" >> /etc/sysctl.conf
echo "net.core.somaxconn = 65535" >> /etc/sysctl.conf
sysctl -p
```

### 5.2. Windows (WSL2)
```powershell
# Configurar memória máxima
wsl --shutdown
notepad "$env:USERPROFILE\.wslconfig"
```
Adicione:
```ini
[wsl2]
memory=8GB
swap=4GB
```

## 6. Problemas Comuns

| Sintoma                         | Causa                          | Solução                          |
|---------------------------------|--------------------------------|----------------------------------|
| `BinanceAPIException: -1021`    | Timestamp inválido             | Sincronizar relógio do sistema   |
| `asyncpg.InvalidCatalogName`    | Banco não existe               | `CREATE DATABASE criptoren;`     |
| `ImportError: pydantic_core`    | Versão incompatível            | `pip install --upgrade pydantic` |

## 7. Próximos Passos

1. [Configuração inicial do ambiente](./Setup%20Inicial.md)
2. [Primeiros passos no desenvolvimento](../01%20Visão%20Geral/Primeiros%20Passos%20no%20Desenvolvimento.md)
3. [Integração com Binance](../04%20Desenvolvimento%20Técnico/Integração%20Binance.md)

---

> **Nota**: Para ambientes de produção, considere usar:
> - `gunicorn` com 4+ workers
> - `nginx` como reverse proxy
> - Monitoramento com Prometheus+Grafana


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/02-configuracao/pre-requisitos/)

<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>
