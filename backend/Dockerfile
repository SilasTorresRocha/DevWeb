FROM python:3.10-slim

WORKDIR /app

# Instala as dependências leves
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos da aplicação
COPY . .

EXPOSE 8000

# Executa o servidor FastAPI na porta fornecida pela hospedagem
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]