# tools_imobiliarios.py
import re
import unicodedata
import json
from parameters_dict import *


def get_parameters_dict():
    """
    Retorna o dicionário completo com todas as definições e mapeamentos imobiliários.
    Este conteúdo é o mesmo do parameters.py original, mantido integralmente.
    """
    return {
        "CIDADES_MAP": CIDADES_MAP,
        "CIDADES_DISPONIVEIS": CIDADES_DISPONIVEIS,
        "CIDADES_SINONIMOS": CIDADES_SINONIMOS,
        "OPERACAO_SINONIMOS": OPERACAO_SINONIMOS,
        "TIPO_IMOVEL_SINONIMOS": TIPO_IMOVEL_SINONIMOS,
        "DORMITORIOS_SINONIMOS": DORMITORIOS_SINONIMOS,
        "ORDENACAO_SINONIMOS": ORDENACAO_SINONIMOS,
        "BAIRROS_POR_CIDADE": BAIRROS_POR_CIDADE,
        "BAIRROS_POR_PERFIL": BAIRROS_POR_PERFIL,
        "PERFIL_SINONIMOS": PERFIL_SINONIMOS
    }


def normalizar_texto(texto: str) -> str:
    """
    Normaliza o texto para facilitar comparações:
    - Converte para minúsculas
    - Remove acentos e caracteres especiais
    """
    if not texto:
        return ""
    texto = texto.lower().strip()
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')


def extrair_parametros_basico(query: str) -> dict:
    """
    Realiza uma extração local e determinística dos parâmetros de busca
    a partir de uma consulta em linguagem natural.
    Ideal para fallback quando o LLM não é utilizado.
    """
    dados = get_parameters_dict()
    resultado = {
        "cidade": None,
        "operacao": None,
        "tipo_imovel": None,
        "dormitorios": None,
        "valor_minimo": None,
        "valor_maximo": None,
        "bairro": None,
        "perfil_bairro": None,
        "ordenar_por": "data",
        "ordenar_direcao": "desc"
    }

    q = normalizar_texto(query)

    # CIDADE
    for key, nome in dados["CIDADES_MAP"].items():
        if key in q or normalizar_texto(nome) in q:
            resultado["cidade"] = nome
            break
    if not resultado["cidade"]:
        for sinonimo, cidade in dados["CIDADES_SINONIMOS"].items():
            if sinonimo in q:
                resultado["cidade"] = dados["CIDADES_MAP"].get(cidade, cidade)
                break

    # OPERAÇÃO
    for op, termos in dados["OPERACAO_SINONIMOS"].items():
        if any(t in q for t in termos):
            resultado["operacao"] = op
            break

    # TIPO DE IMÓVEL
    for tipo, termos in dados["TIPO_IMOVEL_SINONIMOS"].items():
        if any(t in q for t in termos):
            resultado["tipo_imovel"] = tipo
            break

    # DORMITÓRIOS
    dorm = re.search(r"(\d+)\s*(quarto|dormitorio|dorm|qto)", q)
    if dorm:
        resultado["dormitorios"] = int(dorm.group(1))

    # VALORES
    valor_regex = re.findall(r"(\d+[\.,]?\d*)\s*(milhao|mil|reais|k)?", q)
    valores_num = []
    for v, unidade in valor_regex:
        vnum = float(v.replace(",", "."))
        if unidade == "milhao":
            vnum *= 1_000_000
        elif unidade in ("mil", "k"):
            vnum *= 1_000
        valores_num.append(vnum)
    if len(valores_num) == 1:
        resultado["valor_maximo"] = valores_num[0]
    elif len(valores_num) >= 2:
        resultado["valor_minimo"], resultado["valor_maximo"] = valores_num[:2]

    # PERFIL DE BAIRRO
    for perfil, termos in dados["PERFIL_SINONIMOS"].items():
        if any(t in q for t in termos):
            resultado["perfil_bairro"] = perfil
            break

    # ORDENACAO
    for campo, direcoes in dados["ORDENACAO_SINONIMOS"].items():
        for direcao, termos in direcoes.items():
            if any(t in q for t in termos):
                resultado["ordenar_por"] = campo
                resultado["ordenar_direcao"] = direcao
                break

    return resultado


def parametros_to_json(parametros: dict) -> str:
    """Converte o resultado em JSON formatado."""
    return json.dumps(parametros, ensure_ascii=False, indent=2)


# Exemplo de uso rápido
if __name__ == "__main__":
    exemplo = "Quero comprar uma casa de 3 dormitórios até 700 mil em Florianópolis, nas praias do sul"
    print(parametros_to_json(extrair_parametros_basico(exemplo)))
