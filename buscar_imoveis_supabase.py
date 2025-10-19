# buscar_imoveis_supabase.py
"""
Funções para buscar imóveis diretamente no Supabase,
adaptadas para uso como Tool no Agent Builder.
Mantém toda a lógica original do app.py (sem Streamlit).
"""

import os
import json
import unicodedata
import pandas as pd
from datetime import datetime, timezone
from supabase import create_client, Client
from parameters_dict import *
from tools_imobiliarios import normalizar_texto


# === CONFIGURAÇÃO DE CONEXÃO SUPABASE ===
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise EnvironmentError("Variáveis SUPABASE_URL e SUPABASE_KEY não configuradas.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# === FUNÇÃO PRINCIPAL ===
def buscar_imoveis_supabase(parametros: dict, limite: int = 1000) -> list:
    """
    Executa a busca de imóveis conforme os parâmetros informados.

    Parâmetros esperados (todos opcionais):
        cidade, operacao, tipo_imovel, dormitorios,
        valor_minimo, valor_maximo,
        area_minima, area_maxima,
        bairro, perfil_bairro,
        ordenar_por, ordenar_direcao

    Retorna: lista de imóveis (JSON-ready)
    """
    conditions = []

    # CIDADE
    if parametros.get("cidade"):
        cidade = normalizar_texto(parametros["cidade"])
        conditions.append(f"unaccent(cidade) ILIKE '%{cidade}%'")

    # OPERAÇÃO
    if parametros.get("operacao"):
        operacao = normalizar_texto(parametros["operacao"])
        conditions.append(f"unaccent(operacao) ILIKE '%{operacao}%'")

    # TIPO IMÓVEL
    if parametros.get("tipo_imovel"):
        tipo = normalizar_texto(parametros["tipo_imovel"])
        conditions.append(f"unaccent(tipo) ILIKE '%{tipo}%'")

    # DORMITÓRIOS
    if parametros.get("dormitorios"):
        conditions.append(f"dormitorios = {parametros['dormitorios']}")

    # VALORES
    if parametros.get("valor_minimo"):
        conditions.append(f"valor >= {parametros['valor_minimo']}")
    if parametros.get("valor_maximo"):
        conditions.append(f"valor <= {parametros['valor_maximo']}")

    # ÁREAS
    if parametros.get("area_minima"):
        conditions.append(f"area >= {parametros['area_minima']}")
    if parametros.get("area_maxima"):
        conditions.append(f"area <= {parametros['area_maxima']}")

    # BAIRRO / PERFIL
    cidade_norm = normalizar_texto(parametros.get("cidade", ""))
    cidade_chave = CIDADES_MAP.get(cidade_norm)

    if cidade_chave and (parametros.get("bairro") or parametros.get("perfil_bairro")):
        if parametros.get("perfil_bairro"):
            perfil = parametros["perfil_bairro"]
            if cidade_chave in BAIRROS_POR_PERFIL and perfil in BAIRROS_POR_PERFIL[cidade_chave]:
                bairros_perfil = BAIRROS_POR_PERFIL[cidade_chave][perfil]
                bairros_normalizados = [normalizar_texto(b) for b in bairros_perfil]
                bairros_str = ",".join([f"'{b}'" for b in bairros_normalizados])
                conditions.append(f"lower(unaccent(bairro)) IN ({bairros_str})")
        elif parametros.get("bairro"):
            bairro_input = normalizar_texto(parametros["bairro"])
            conditions.append(f"unaccent(bairro) ILIKE '%{bairro_input}%'")

    # MONTAGEM DO SQL
    where_clause = " AND ".join(conditions) if conditions else "TRUE"
    sql_query = f"SELECT * FROM imoveis WHERE {where_clause}"

    # ORDENAÇÃO
    if parametros.get("ordenar_por"):
        criterio = parametros["ordenar_por"]
        direcao = parametros.get("ordenar_direcao", "desc")
        order_field = {
            "data": "datapublicacao",
            "valor": "valor",
            "dormitorios": "dormitorios"
        }.get(criterio, "datapublicacao")
        sql_query += f" ORDER BY {order_field} {'DESC' if direcao == 'desc' else 'ASC'}"
    else:
        sql_query += " ORDER BY datapublicacao DESC"

    # LIMITE
    sql_query += f" LIMIT {limite}"

    # EXECUÇÃO
    try:
        response = supabase.rpc("buscar_imoveis", {"query": sql_query}).execute()
        data = response.data or []

        # Ajuste de datas e formatação
        for item in data:
            if "datapublicacao" in item and item["datapublicacao"]:
                item["datapublicacao"] = str(item["datapublicacao"]).split("T")[0]
        return data

    except Exception as e:
        return {"erro": str(e), "query": sql_query}


# === FUNÇÃO AUXILIAR ===
def buscar_imovel_por_id(imovel_id: int):
    """Busca um imóvel específico pelo ID."""
    try:
        response = supabase.table("imoveis").select("*").eq("id", imovel_id).execute()
        if response.data:
            return response.data[0]
        return None
    except Exception as e:
        return {"erro": str(e)}
