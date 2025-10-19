# server.py
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from tools_imobiliarios import extrair_parametros_basico
from buscar_imoveis_supabase import buscar_imoveis_supabase

# Inicializa o app FastAPI
app = FastAPI(
    title="Em Exposição API",
    description="Serviço que expõe ferramentas de extração e busca de imóveis para o Agent Builder.",
    version="1.0.0"
)

# CORS liberado (para o Agent Builder e testes externos)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    """Rota raiz de verificação."""
    return {"status": "ok", "message": "Servidor Em Exposição ativo."}


@app.post("/extrair_parametros_basico")
def api_extrair_parametros_basico(payload: dict = Body(...)):
    """
    Extrai cidade, operação, tipo de imóvel, valor, área, dormitórios e perfil de bairro
    de uma consulta em linguagem natural.
    """
    query = payload.get("query", "")
    try:
        result = extrair_parametros_basico(query)
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.post("/buscar_imoveis_supabase")
def api_buscar_imoveis_supabase(payload: dict = Body(...)):
    """
    Busca imóveis filtrando por cidade, operação, tipo, valor, área, dormitórios e perfil de bairro
    diretamente no banco Supabase.
    """
    parametros = payload.get("parametros", {})
    limite = payload.get("limite", 1000)
    try:
        result = buscar_imoveis_supabase(parametros, limite)
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

