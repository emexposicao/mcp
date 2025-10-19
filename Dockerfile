# Dockerfile para deploy do servidor MCP no Railway
FROM python:3.11-slim

WORKDIR /app

# Instala apenas dependências de runtime (sem build-essential)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5173
EXPOSE 5173

CMD ["python", "mcp_server.py"]
