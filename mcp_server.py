# mcp_server.py
import os
import asyncio

from mcp import server
from mcp.tools import Tool, ToolSchema
from mcp.schemas import ToolParameter

from tools_imobiliarios import extrair_parametros_basico
from buscar_imoveis_supabase import buscar_imoveis_supabase


async def main():
    srv = server.MCPServer(name="em-exposicao", version="1.0.0")

    async def extrair_handler(query: str):
        return extrair_parametros_basico(query)

    srv.add_tool(
        Tool(
            name="extrair_parametros_basico",
            description=(
                "Extrai cidade, operação, tipo de imóvel, valores, área, dormitórios e perfil de bairro "
                "a partir de uma consulta em linguagem natural."
            ),
            schema=ToolSchema(
                parameters=[
                    ToolParameter(
                        name="query",
                        type="string",
                        description="Consulta natural. Ex.: 'Procuro apartamento até 600 mil em Florianópolis'",
                    )
                ]
            ),
            handler=extrair_handler,
        )
    )

    async def buscar_handler(parametros: dict, limite: int = 1000):
        return buscar_imoveis_supabase(parametros, limite)

    srv.add_tool(
        Tool(
            name="buscar_imoveis_supabase",
            description=(
                "Busca imóveis filtrando por cidade, operação, tipo, valor, área, dormitórios e perfil de bairro "
                "diretamente no banco Supabase."
            ),
            schema=ToolSchema(
                parameters=[
                    ToolParameter(
                        name="parametros",
                        type="object",
                        description="Parâmetros estruturados de busca (cidade, operacao, tipo_imovel, valor_minimo, etc.).",
                    ),
                    ToolParameter(
                        name="limite",
                        type="integer",
                        description="Número máximo de imóveis a retornar.",
                        default=1000,
                    ),
                ]
            ),
            handler=buscar_handler,
        )
    )

    port = int(os.getenv("PORT", "5173"))
    host = os.getenv("HOST", "0.0.0.0")
    print(f"[MCP] Starting server em-exposicao on {host}:{port}")
    await srv.start(host=host, port=port)


if __name__ == "__main__":
    asyncio.run(main())
