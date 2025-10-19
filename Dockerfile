# Dockerfile for hosting the MCP server
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \    build-essential \    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5173
EXPOSE 5173

CMD ["python", "mcp_server.py"]
