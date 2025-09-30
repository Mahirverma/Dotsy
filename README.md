# Dotsy

## 1. Clone the repository

```bash
git clone https://github.com/Mahirverma/Dotsy.git
cd Dotsy
```

## 2. Create a virtual environment

```bash
python -m venv .venv
.venv\activate\scripts
```
## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create environment file (.env)

```bash
APP_NAME=FastAPI KB System
APP_ENV=development

DB_HOST=localhost
DB_PORT=5432
DB_USER=[username]
DB_PASSWORD=[password]
DB_NAME=kb_db
```

## 5. Run the application
```bash
uvicorn main:app --reload
```

