# Setup Inicial

```markdown
# 🛠️ Setup Inicial  
`/Documentação Técnica/02 Configuração/Setup Inicial.md`  

## **1. Pré-requisitos**  
| Componente       | Versão  | Verificação               |
|------------------|---------|---------------------------|
| Python           | 3.10+   | `python --version`        |
| PostgreSQL       | 15+     | `psql --version`          |
| Docker           | 20.10+  | `docker --version`        |
| Git              | 2.30+   | `git --version`           |

## **2. Configuração do Ambiente**  
### **2.1. Banco de Dados (Docker)**  
```bash
docker run --name criptoren-db -e POSTGRES_PASSWORD=senha_segura -p 5432:5432 -d postgres:15
```

### **2.2. Clonar Repositório**  
```bash
git clone https://github.com/maksoud/Criptomoedas.git
cd Criptomoedas
```

### **2.3. Ambiente Virtual (Poetry)**  
```bash
poetry install  # Instala dependências
poetry shell    # Ativa o ambiente
```

## **3. Variáveis de Ambiente**  
Crie um arquivo `.env` na raiz:  
```env
# Binance
BINANCE_API_KEY=suachave
BINANCE_API_SECRET=seusegredo

# Banco de Dados
DATABASE_URL=postgresql+asyncpg://postgres:senha_segura@localhost:5432/criptoren

# Configurações Opcionais
CAPITAL_PERCENTAGE=20.0
```

## **4. Migrações do Banco**  
Execute com Alembic:  
```bash
alembic upgrade head
```

## **5. Testar Conexões**  
### **5.1. Teste Binance**  
```python
import os
from binance import AsyncClient

async def test_binance():
    client = await AsyncClient.create(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_API_SECRET'))
    print(await client.get_account())
```

### **5.2. Teste PostgreSQL**  
```python
import asyncpg

async def test_db():
    conn = await asyncpg.connect(os.getenv('DATABASE_URL'))
    print(await conn.fetch('SELECT * FROM strategies;'))
```

## **6. Iniciar o Sistema**  
```bash
uvicorn app.main:app --reload
```
Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)  

## **7. Problemas Comuns**  
| Erro                          | Solução                          |
|-------------------------------|----------------------------------|
| `ConnectionError` (Binance)   | Verifique API keys e firewall    |
| `asyncpg.InvalidPassword`     | Confira `DATABASE_URL` no .env   |
| `ImportError` (Python)        | Ative o ambiente virtual        |

## **8. Próximos Passos**  
1. [Configurar estratégia inicial](../03%20Estratégia/Regras%20do%20Canal%20de%20Preços.md)  
2. [Implementar monitoramento H4](../04%20Desenvolvimento%20Técnico/Integração%20Binance.md)  

---

### **📌 Estrutura do Projeto após Setup**  
```bash
.
├── .env
├── alembic.ini
├── app/
│   ├── main.py
│   └── binance/
│       └── client.py
└── migrations/
    └── versions/
        └── 001_initial_migration.py
```

> **Nota**: Para deploy em produção, substitua `DATABASE_URL` por uma conexão SSL e use `gunicorn` + `nginx`.

