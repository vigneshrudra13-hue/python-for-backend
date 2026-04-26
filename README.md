# python-for-backend
1. learning python

## Environment variables

Create a `.env` file in the project root with any secrets or configuration values. Example:

```
API=REPLACE_WITH_YOUR_API_KEY
```

Do not commit `.env` to version control — use `.env.example` instead. The project includes `env_loader.py` which automatically loads `.env` on import; retrieve values with:

```python
from env_loader import get
api_key = get('API')
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

Run the test loader:

```bash
python env_test.py
```

