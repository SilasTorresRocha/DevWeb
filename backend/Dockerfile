FROM python:3.10-slim

WORKDIR /app

# Instala as dependências leves
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos da aplicação
COPY . .

EXPOSE 8000

# Executa o servidor FastAPI com Uvicorn e auto-reload ativado
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

