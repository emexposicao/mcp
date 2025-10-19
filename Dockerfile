# Dockerfile para deploy do servidor Em Exposição no Railway
FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema mínimas
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Define variáveis padrão
ENV PORT=5173
EXPOSE 5173

# Executa o servidor FastAPI com Uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "5173"]
