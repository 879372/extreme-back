# Extreme Software — Backend

API independente em Django + Django REST Framework para clientes, autenticação administrativa e evolução do painel.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

A API REST de clientes fica em `http://localhost:8000/api/clients/`, o login do painel em `http://localhost:8000/api/auth/login/` e o Django Admin em `http://localhost:8000/admin/`.

Use no site as mesmas credenciais criadas com `createsuperuser`.

## Produção

- API: `https://extreme-api-production-b938.up.railway.app`
- Health check: `https://extreme-api-production-b938.up.railway.app/health/`
- Banco: PostgreSQL privado no Railway

O deploy executa automaticamente as migrações e a coleta de arquivos estáticos antes de iniciar o Gunicorn. No frontend da Vercel, configure:

```env
NEXT_PUBLIC_API_URL=https://extreme-api-production-b938.up.railway.app
```
