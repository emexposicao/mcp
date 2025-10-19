# parameters.py

# Mapeamento de cidades normalizadas para nomes usados em bairros_por_perfil
CIDADES_MAP = {
    "caxias do sul": "Caxias do Sul",
    "porto alegre": "Porto Alegre",
    "florianopolis": "Florianópolis"
}

CIDADES_DISPONIVEIS = list(CIDADES_MAP.keys())

# Mapeamento de sinônimos para cidades
CIDADES_SINONIMOS = {
    "poa": "porto alegre",
    "cxs": "caxias do sul",
    "flp": "florianopolis",
    "floripa": "florianopolis"
}

# Mapeamento de sinônimos para operações
OPERACAO_SINONIMOS = {
    "comprar": ["comprar", "adquirir", "compra"],
    "alugar": ["alugar", "aluguel", "locar"]
}

# Mapeamento de sinônimos para tipos de imóvel
TIPO_IMOVEL_SINONIMOS = {
    "casa": ["casa", "residência", "moradia", "casa geminada", "residencial", "lar", "habitação", "domicílio", "vivenda", "casa térrea", "casa unifamiliar", "casa isolada", "casa independente"],    
    "apartamento padrão": ["apartamento", "apt", "apto", "apart", "apartamento residencial", "apartamento convencional", "apartamento tradicional", "apartamento padrão", "unidade residencial", "unidade habitacional", "apartamento familiar"],    
    "apartamento compacto": ["studio", "kitnet", "quitinete", "flat", "loft", "kit", "ktnete", "kitinete", "JK", "conjugado", "apartamento compacto", "apartamento estúdio", "apartamento conjugado", "microapartamento", "apartamento pequeno", "apartamento econômico"],    
    "apartamento especial": ["cobertura", "duplex", "triplex", "penthouse", "cobertura duplex", "apartamento garden", "apartamento térreo", "apartamento com terraço", "apartamento de luxo", "apartamento premium", "apartamento exclusivo", "apartamento diferenciado"],    
    "casa em condomínio": ["casa condomínio", "casa em condomínio fechado", "casa em condomínio residencial", "casa em condomínio de casas", "residência em condomínio", "casa em condomínio horizontal", "casa em condomínio de alto padrão", "casa em condomínio de luxo", "casa em condomínio privativo"],    
    "sobrado": ["sobrado", "sobrado geminado", "sobrado em condomínio", "sobrado residencial", "casa sobrado", "casa de dois andares", "casa de dois pavimentos", "casa duplex", "casa assobradada", "casa com dois pisos", "casa com dois níveis"],    
    "comercial": ["loja", "ponto", "sala comercial", "casa comercial", "imovel comercial", "ponto comercial", "estabelecimento comercial", "espaço comercial", "salão comercial", "loja térrea", "loja de rua", "loja em shopping", "loja em galeria", "loja em centro comercial", "sala para escritório", "escritório", "consultório", "conjunto comercial", "andar corporativo", "prédio comercial", "edifício comercial"],    
    "industrial": ["industrial", "barracão", "galpão", "conjunto", "pavilhão industrial", "galpão industrial", "galpão logístico", "galpão comercial", "centro de distribuição", "CD", "armazém", "depósito", "espaço industrial", "área industrial", "parque industrial", "complexo industrial"],    
    "terreno": ["terreno", "terras", "lote", "área", "gleba", "parcela", "pedaço de terra", "terreno urbano", "terreno rural", "terreno residencial", "terreno comercial", "terreno industrial", "lote urbano", "lote residencial", "lote comercial", "área de terra", "fração de terra"],    
    "chácara": ["rancho", "chácara", "sítio de recreio", "sítio de lazer", "quinta", "propriedade rural pequena", "área de lazer rural", "chácara de recreio", "chácara de final de semana", "chácara de lazer", "pequena propriedade rural"],    
    "sítio": ["sítio", "fazendola", "pequena fazenda", "propriedade rural média", "sítio rural", "roça", "herdade", "granja", "horta", "pomar", "propriedade rural", "terra rural"],    
    "fazenda": ["fazenda", "propriedade rural grande", "latifúndio", "grande propriedade rural", "fazenda agrícola", "fazenda de criação", "fazenda de gado", "fazenda produtiva", "estância", "hacienda"],    
    "empreendimento misto": ["uso misto", "residencial e comercial", "multiuso", "mixed-use", "empreendimento híbrido", "imóvel de uso misto", "prédio de uso misto", "edifício multiuso"],    
    "imóvel na planta": ["na planta", "em construção", "em lançamento", "pré-lançamento", "em fase de obras", "em desenvolvimento", "em projeto", "futuro empreendimento"],    
    "imóvel hoteleiro": ["flat hoteleiro", "apart-hotel", "hotel residência", "condo-hotel", "condohotel", "hotel", "pousada", "resort", "hospedagem"],    
    "imóvel para temporada": ["temporada", "veraneio", "férias", "casa de praia", "casa de campo", "casa de temporada", "apartamento de temporada", "imóvel para férias", "locação por temporada"]
}


# Mapeamento de sinônimos para dormitórios
DORMITORIOS_SINONIMOS = ["quarto", "qto", "dorm", "dormitorio"]

# Mapeamento de ordenação
ORDENACAO_SINONIMOS = {
    "data": {
        "desc": ["recentes", "novos", "últimos"],
        "asc": ["antigos", "velho"]
    },
    "valor": {
        "asc": ["baratos", "menor valor", "econômico"],
        "desc": ["caros", "maior valor", "luxo"]
    },
    "dormitorios": {
        "desc": ["mais dormitórios", "mais quartos"],
        "asc": ["menos dormitórios", "menos quartos"]
    }
}


# Mapeamento de bairros por cidade
BAIRROS_POR_CIDADE = {
    "caxias do sul": [
        "Ana Rech", "Bela Vista", "Belo Horizonte", "Brandalise", "Centenário", "Centro", "Charqueadas", 
        "Cidade Nova", "Cinquentenário", "Colina Sorriso", "Cristo Redentor", "Cruzeiro", "De Lazzer", 
        "De Zorzi", "Desvio Rizzo", "Diamantino", "Esplanada", "Exposição", "Floresta", "Forqueta", 
        "Galópolis", "Industrial", "Interlagos", "Jardelino Ramos", "Jardim América", "Jardim das Hortênsias", 
        "Jardim Eldorado", "Jardim Iracema", "Kayser", "Linha 40", "Madureira", "Maestra", "Marechal Floriano", 
        "Medianeira", "Monte Bérico", "Nossa Senhora da Conceição", "Nossa Senhora da Saúde", 
        "Nossa Senhora das Graças", "Nossa Senhora de Fátima", "Nossa Senhora de Lourdes", 
        "Nossa Senhora do Rosário", "Panazzolo", "Parada Cristal", "Pedancino", "Petrópolis", "Pio X", 
        "Pioneiro", "Planalto", "Pôr do Sol", "Presidente Vargas", "Reolon", "Rio Branco", "Sagrada Família", 
        "Salgado Filho", "Samuara", "Santa Catarina", "Santa Corona", "Santa Fé", "Santa Lúcia", "Sanvitto", 
        "São Caetano", "São Ciro", "São Cristóvão", "São Giácomo", "São José", "São Leopoldo", "São Luiz", 
        "São Pelegrino", "São Victor Cohab", "São Virgílio", "Século XX", "Serrano", "Tijuca", "Universitário", 
        "Vila Lobos", "Vila Verde", "Vinhedos"
    ],
    "porto alegre": [
        "Agronomia", "Anchieta", "Arquipélago", "Auxiliadora", "Azenha", "Bela Vista", "Belém Novo", 
        "Belém Velho", "Boa Vista", "Bom Fim", "Bom Jesus", "Camaquã", "Cascata", "Cavalhada", "Centro", 
        "Chácara das Pedras", "Cidade Baixa", "Coronel Aparício Borges", "Cristal", "Cristo Redentor", 
        "Espírito Santo", "Farrapos", "Farroupilha", "Floresta", "Glória", "Guarujá", "Higienópolis", 
        "Hípica", "Humaitá", "Independência", "Ipanema", "Jardim Botânico", "Jardim Carvalho", 
        "Jardim do Salso", "Jardim Floresta", "Jardim Isabel", "Jardim Itu-Sabará", "Jardim Lindoia", 
        "Jardim São Pedro", "Lageado", "Lami", "Lomba do Pinheiro", "Marcílio Dias", "Mário Quintana", 
        "Medianeira", "Menino Deus", "Moinhos de Vento", "Mont'Serrat", "Navegantes", "Nonoai", "Partenon", 
        "Passo d'Areia", "Pedra Redonda", "Petrópolis", "Ponta Grossa", "Praia de Belas", "Protásio Alves", 
        "Restinga", "Rio Branco", "Rubem Berta", "Santa Cecília", "Santa Maria Goretti", "Santa Tereza", 
        "Santana", "Santo Antônio", "São Geraldo", "São João", "São José", "São Sebastião", "Sarandi", 
        "Serraria", "Teresópolis", "Três Figueiras", "Tristeza", "Vila Assunção", "Vila Conceição", 
        "Vila Ipiranga", "Vila Jardim", "Vila João Pessoa", "Vila Nova"
    ],
    "florianopolis": [
        "Agronômica", "Armação do Pântano do Sul", "Balneário", "Barra da Lagoa", "Bom Abrigo", 
        "Cachoeira do Bom Jesus", "Cacupé", "Campeche", "Canasvieiras", "Capoeiras", "Carianos", "Carvoeira", 
        "Centro", "Coqueiros", "Córrego Grande", "Costeira do Pirajubaé", "Daniela", "Estreito", 
        "Ingleses do Rio Vermelho", "Itacorubi", "Itaguaçu", "Jardim Atlântico", "João Paulo", "José Mendes", 
        "Jurerê Internacional", "Jurerê Tradicional", "Lagoa da Conceição", "Monte Verde", "Pantanal", 
        "Pântano do Sul", "Ponta das Canas", "Praia Brava", "Ribeirão da Ilha", "Rio Tavares", 
        "Saco dos Limões", "Saco Grande", "Sambaqui", "Santa Mônica", "Santo Antônio de Lisboa", 
        "São João do Rio Vermelho", "Tapera", "Trindade"
    ]
}

# Definição dos bairros por perfil
BAIRROS_POR_PERFIL = {
    "Caxias do Sul": {
        "centrais": ["Centro", "Cinquentenário", "Cristo Redentor", "Exposição", "Floresta", "Jardelino Ramos", "Jardim América", "Madureira", "Medianeira", "Marechal Floriano", "Nossa Senhora de Lourdes", "Panazzolo", "Pio X", "Rio Branco", "Sagrada Família", "Santa Catarina", "São Pelegrino", "São Leopoldo", "Universitário"],        
        "arborizados": ["Panazzolo", "Colina Sorriso", "Jardim América", "Pio X", "Madureira", "Exposição", "Altos do Panazzolo", "Jardim Eldorado", "Cinquentenário", "Nossa Sra. de Lourdes"],        
        "expansao": ["Desvio Rizzo", "Forqueta", "Ana Rech", "Cidade Nova", "Serrano", "Esplanada", "Salgado Filho", "São Caetano", "Fátima", "Charqueadas", "Samuara", "Planalto"],        
        "alto_padrao": ["Villagio Iguatemi", "Sanvitto", "Jardim América", "Exposição", "Panazzolo", "Madureira", "Colina Sorriso", "Altos do Panazzolo", "Cinquentenário", "Nossa Sra. de Lourdes", "Petrópolis"],        
        "industrial": ["São Ciro", "Distrito Industrial", "Desvio Rizzo", "Interlagos", "Forqueta", "Cidade Nova", "Galópolis", "Charqueadas", "Salgado Filho", "Esplanada"],        
        "tranquilo_residencial": ["Villagio Iguatemi", "Sanvitto", "Jardim América", "Exposição", "Panazzolo", "Madureira", "Colina Sorriso", "Altos do Panazzolo", "Jardim Eldorado", "Presidente Vargas", "Cinquentenário", "Pio X"],        
        "rural_proximo": ["Galópolis", "Fazenda Souza", "Santa Lúcia do Piaí", "Vila Cristina", "Vila Oliva", "Criúva", "São Virgílio da Santa Légua", "São Luiz da Sexta Légua", "Forqueta", "Ana Rech"],        
        "universitario": ["Universitário", "Petrópolis", "Centro", "Exposição", "Panazzolo", "Cinquentenário", "Pio X", "Jardim América", "Madureira", "Rio Branco"],        
        "vida_noturna": ["Centro", "São Pelegrino", "Rio Branco", "Exposição", "Cinquentenário", "Pio X", "Madureira", "Floresta", "Jardelino Ramos", "Panazzolo"],        
        "gastronomico": ["Centro", "São Pelegrino", "Exposição", "Rio Branco", "Madureira", "Cinquentenário", "Pio X", "Panazzolo", "Jardim América", "Colina Sorriso"]
    },
    
    "Florianópolis": {
        "centrais": ["Agronômica", "Centro", "Córrego Grande", "Itacorubi", "João Paulo", "José Mendes", "Monte Verde", "Pantanal", "Saco dos Limões", "Saco Grande", "Santa Mônica", "Trindade", "Carvoeira"],
        "continente": ["Balneário", "Bom Abrigo", "Capoeiras", "Coqueiros", "Estreito", "Itaguaçu", "Jardim Atlântico"],
        "praia_leste": ["Lagoa da Conceição", "Barra da Lagoa", "São João do Rio Vermelho"],
        "praia_norte": ["Cachoeira do Bom Jesus", "Cacupé", "Canasvieiras", "Daniela", "Ingleses do Rio Vermelho", "Jurerê Internacional", "Jurerê Tradicional", "Ponta das Canas", "Praia Brava", "Sambaqui", "Santo Antônio de Lisboa"],
        "praia_sul": ["Armação do Pântano do Sul", "Campeche", "Carianos", "Costeira do Pirajubaé", "Pântano do Sul", "Ribeirão da Ilha", "Rio Tavares", "Tapera"],
        "arborizados": ["Córrego Grande", "Santa Mônica", "Itacorubi", "João Paulo", "Monte Verde", "Parque São Jorge", "Saco Grande", "Lagoa da Conceição", "Campeche", "Cacupé"],        
        "alto_padrao": ["Jurerê Internacional", "Agronômica", "Centro (Beira Mar)", "Itacorubi", "Coqueiros", "Santa Mônica", "Lagoa da Conceição (Condomínios)", "Cacupé", "João Paulo", "Novo Campeche"],        
        "universitario": ["Trindade", "Pantanal", "Carvoeira", "Córrego Grande", "Santa Mônica", "Itacorubi", "Serrinha", "Saco dos Limões", "Centro", "João Paulo"],        
        "vida_noturna": ["Lagoa da Conceição", "Centro", "Jurerê Internacional", "Santo Antônio de Lisboa", "Campeche", "Rio Tavares", "Trindade", "Canasvieiras", "Ingleses", "Barra da Lagoa"],        
        "tranquilo_residencial": ["Saco Grande", "João Paulo", "Cacupé", "Santo Antônio de Lisboa", "Sambaqui", "Ratones", "Vargem Grande", "Vargem Pequena", "Monte Verde", "Córrego Grande", "Santa Mônica", "Canto da Lagoa"],        
        "gastronomico": ["Santo Antônio de Lisboa", "Coqueiros", "Centro", "Lagoa da Conceição", "Ribeirão da Ilha", "Santa Mônica", "Itacorubi", "Jurerê Internacional", "Canasvieiras", "Campeche"],        
        "ecologico": ["Campeche", "Lagoa da Conceição", "Ratones", "Costa da Lagoa", "Naufragados", "Barra da Lagoa", "Solidão", "Lagoinha do Leste", "Matadeiro", "Pântano do Sul"],        
        "industrial": ["Saco Grande", "Capoeiras", "Estreito", "Coqueiros", "Jardim Atlântico", "Monte Cristo", "Coloninha", "Abraão", "Canto", "Balneário"],        
        "expansao": ["Campeche", "Rio Tavares", "Ingleses", "Vargem Grande", "Vargem do Bom Jesus", "Canasvieiras", "Santinho", "Rio Vermelho", "Tapera", "Carianos"],        
        "rural_proximo": ["Ratones", "Rio Vermelho", "Vargem Grande", "Vargem Pequena", "Ingleses", "Santinho", "Canasvieiras", "Ribeirão da Ilha", "Pântano do Sul", "Costa da Lagoa"]
    },
    
    "Porto Alegre": {
        "zona_norte": ["Anchieta", "Arquipélago", "Auxiliadora", "Boa Vista", "Cristo Redentor", "Farrapos", "Humaitá", "Jardim Floresta", "Jardim Lindóia", "Jardim São Pedro", "Marcílio Dias", "Mário Quintana", "Navegantes", "Passo d'Areia", "Rubem Berta", "Santa Maria Goretti", "São João", "São Sebastião", "Vila Ipiranga"],
        "zona_sul": ["Belem Novo", "Belém Velho", "Camaquã", "Cascata", "Cavalhada", "Coronel Aparício Borges", "Cristal", "Espírito Santo", "Glória", "Guarujá", "Hípica", "Ipanema", "Jardim Isabel", "Lageado", "Lami", "Medianeira", "Nonoai", "Partenon", "Pedra Redonda", "Ponta Grossa", "Restinga", "Santa Tereza", "Santo Antônio", "Serraria", "Teresópolis", "Tristeza", "Vila Assunção", "Vila Conceição", "Vila Nova"],
        "zona_leste": ["Agronomia", "Bom Jesus", "Chácara das Pedras", "Jardim Botânico", "Jardim Carvalho", "Jardim do Salso", "Jardim Itu-Sabará", "Lomba do Pinheiro", "Protásio Alves", "São José", "Três Figueiras", "Vila Jardim", "Vila João Pessoa"],
        "centrais": ["Azenha", "Bela Vista", "Bom Fim", "Centro", "Cidade Baixa", "Farroupilha", "Floresta", "Higienópolis", "Independência", "Menino Deus", "Moinhos de Vento", "Mont'Serrat", "Petrópolis", "Praia de Belas", "Rio Branco", "Santana", "Santa Cecília"],        
        "arborizados": ["Petrópolis", "Menino Deus", "Jardim Botânico", "Bela Vista", "Três Figueiras", "Auxiliadora", "Moinhos de Vento", "Boa Vista", "Vila Assunção", "Chácara das Pedras", "Jardim Europa", "Mont'Serrat"],        
        "orla_guaiba": ["Belém Novo", "Ipanema", "Tristeza", "Vila Assunção", "Pedra Redonda", "Guarujá", "Cristal", "Ponta Grossa", "Serraria", "Lami", "Praia de Belas", "Menino Deus", "Centro Histórico", "Navegantes", "Humaitá"],        
        "alto_padrao": ["Boa Vista", "Mont'Serrat", "Chácara das Pedras", "Bela Vista", "Três Figueiras", "Moinhos de Vento", "Higienópolis", "Petrópolis", "Auxiliadora", "Cristal (novos empreendimentos)", "Vila Assunção", "Jardim Europa", "Menino Deus"],        
        "universitario": ["Bom Fim", "Partenon (PUCRS)", "Cidade Baixa", "Farroupilha (UFRGS)", "Agronomia (UFRGS)", "Jardim Botânico", "Santa Cecília", "Santana", "Petrópolis", "Rio Branco"],        
        "vida_noturna": ["Cidade Baixa", "Moinhos de Vento", "Bom Fim", "Floresta (4º Distrito)", "São Geraldo (4º Distrito)", "Auxiliadora", "Centro Histórico", "Independência", "Rio Branco", "Menino Deus"],        
        "tranquilo_residencial": ["Jardim Isabel", "Cristo Redentor", "Vila Conceição", "Passo d'Areia", "Jardim Lindoia", "Vila Ipiranga", "Higienópolis", "Boa Vista", "Tristeza", "Pedra Redonda", "Jardim Itu", "Jardim Sabará", "Três Figueiras", "Vila Assunção"],        
        "historico_cultural": ["Centro Histórico", "Bom Fim", "Cidade Baixa", "Floresta", "Navegantes", "Menino Deus", "Independência", "Rio Branco", "Moinhos de Vento", "Santana"],        
        "expansao_zona_sul": ["Hípica", "Restinga", "Ponta Grossa", "Cavalhada", "Aberta dos Morros", "Belém Velho", "Serraria", "Lageado", "Lomba do Pinheiro", "Agronomia", "Campo Novo", "Chapéu do Sol"],        
        "comercial": ["Centro Histórico", "Azenha", "Floresta", "Passo d'Areia", "Menino Deus", "Nonoai", "Cristo Redentor", "Praia de Belas", "Moinhos de Vento", "São Geraldo", "Navegantes", "Sarandi"],        
        "industrial": ["Sarandi", "Humaitá", "Navegantes", "São Geraldo", "Anchieta", "Farrapos", "São João", "Passo d'Areia", "Rubem Berta", "Partenon"],        
        "gastronomico": ["Moinhos de Vento", "Cidade Baixa", "Bom Fim", "Centro Histórico", "Menino Deus", "Auxiliadora", "Floresta (4º Distrito)", "Petrópolis", "Mont'Serrat", "Três Figueiras"],        
        "rural_proximo": ["Belém Novo", "Lami", "Chapéu do Sol", "Extrema", "Lageado", "Hípica", "Aberta dos Morros", "Lomba do Pinheiro", "Agronomia", "Ponta Grossa"]
    }
}

# Mapeamento de sinônimos para perfis
PERFIL_SINONIMOS = {
    "centrais": ["central", "zona central", "regiao central", "area central", "centro", "centro da cidade", "meio da cidade", "coração da cidade", "centro urbano", "núcleo urbano", "área urbana central"],    
    "zona_norte": ["norte", "zona norte", "regiao norte", "area norte", "parte norte", "setor norte", "área setorial norte", "norte da cidade"],
    "zona_sul": ["sul", "zona sul", "regiao sul", "area sul", "parte sul", "setor sul", "area setorial sul", "sul da cidade"],
    "zona_leste": ["leste", "zona leste", "regiao leste", "area leste", "parte leste", "setor leste", "area setorial leste", "leste da cidade"],
    "continente": ["regiao continental", "parte continental", "área continental", "zona continental", "região do continente", "regiao_continental"],
    "alto_padrao": ["nobre", "regiao nobre", "bairro nobre", "alto padrao", "de luxo", "premium", "sofisticado", "exclusivo", "elite", "classe alta", "área vip", "área privilegiada", "requintado", "upscale", "prime"],
    "praia_norte": ["praia do norte", "praias do norte", "litoral norte", "costa norte", "orla norte", "beira-mar norte", "balneário norte", "frente para o mar norte"],    
    "praia_leste": ["praia do leste", "praias do leste", "litoral leste", "costa leste", "orla leste", "beira-mar leste", "balneário leste", "frente para o mar leste"],    
    "praia_sul": ["praia do sul", "praias do sul", "litoral sul", "costa sul", "orla sul", "beira-mar sul", "balneário sul", "frente para o mar sul"],    
    "arborizados": ["verde", "arborizado", "com natureza", "com árvores", "área verde", "bosque", "parque", "jardim", "com vegetação", "ecológico", "com praças", "com parques", "com mata", "com bosque"],    
    "tranquilo_residencial": ["tranquilo", "residencial", "familiar", "calmo", "sossegado", "pacato", "silencioso", "sem movimento", "dormitório", "área residencial", "zona residencial", "bairro dormitório", "área familiar", "sem barulho", "sem agitação"],    
    "industrial": ["industrial", "zona industrial", "distrito industrial", "polo industrial", "setor industrial", "cidade industrial", "área industrial", "parque industrial", "região de fábricas", "área de indústrias"],    
    "expansao": ["em expansao", "nova regiao", "crescimento", "em desenvolvimento", "emergente", "área nova", "recém-desenvolvido", "em valorização", "novo polo", "área promissora", "região em crescimento", "bairro planejado"],    
    "rural_proximo": ["zona rural", "rural", "interior", "campo", "chácara", "sítio", "fazenda", "estância", "rancho", "área rural", "área de chácaras", "condomínio rural", "loteamento rural", "área campestre", "região agrícola"],    
    "universitario": ["universitario", "perto da faculdade", "estudante", "vida academica", "campus", "próximo à universidade", "área universitária", "polo educacional", "região de estudantes", "próximo ao campus", "vila universitária"],    
    "vida_noturna": ["agitado", "vida noturna", "bares", "baladas", "boemio", "badalado", "movimentado", "festivo", "noturno", "área de entretenimento", "região de bares", "polo gastronômico noturno", "área de lazer noturno", "boêmio"],    
    "gastronomico": ["gastronomico", "restaurantes", "culinaria", "polo gastronomico", "área gastronômica", "setor gastronômico", "região de restaurantes", "praça de alimentação", "rua dos restaurantes", "corredor gastronômico", "centro gastronômico"],    
    "ecologico": ["ecologico", "natureza", "trilhas", "preservado", "sustentavel", "reserva", "ambiental", "verde", "conservação", "área de preservação", "parque ecológico", "reserva natural", "área de conservação", "mata preservada"],    
    "orla_guaiba": ["orla", "beira do guaiba", "vista para o guaiba", "margem do guaíba", "beira-rio", "orla do guaíba", "calçadão do guaíba", "frente para o guaíba", "pôr do sol no guaíba", "borda d'água"],    
    "historico_cultural": ["historico", "cultural", "patrimonio", "centro antigo", "cidade antiga", "parte antiga", "núcleo histórico", "centro histórico", "cidade velha", "bairro histórico", "patrimônio histórico", "área tombada", "região histórica"],    
    "expansao_zona_sul": ["zona sul em expansao", "novos bairros zona sul", "expansao sul", "crescimento zona sul", "desenvolvimento zona sul", "nova zona sul", "sul em crescimento", "região sul em expansão", "polo sul em desenvolvimento"],    
    "comercial": ["comercial", "comercio", "lojas", "area comercial", "centro comercial", "polo comercial", "setor comercial", "quadra comercial", "distrito comercial", "corredor comercial", "shopping", "galeria", "área de negócios", "empresarial"],    
    "condominio_fechado": ["condomínio fechado", "condomínio de casas", "condomínio residencial", "condomínio de alto padrão", "residencial privativo", "condomínio exclusivo", "área residencial fechada", "condomínio de luxo", "condomínio clube"],    
    "loteamento": ["loteamento", "loteamento fechado", "loteamento aberto", "loteamento de acesso controlado", "condomínio de lotes", "loteamento residencial", "loteamento planejado", "loteamento urbanizado"],    
    "conjunto_habitacional": ["conjunto habitacional", "COHAB", "BNH", "conjunto residencial popular", "habitação popular", "residencial popular", "conjunto de casas populares", "núcleo habitacional", "residencial público"],    
    "prefixos_bairros": ["vila", "jardim", "parque", "conjunto", "residencial", "recanto", "bosque", "vale", "colina", "portal", "morada", "cidade", "bairro"],    
    "distritos": ["distrito", "arraial", "povoação", "povoado", "arredores", "região", "setor", "quadra", "área", "zona", "núcleo", "polo"],    
    "beira_mar": ["orla", "beira-mar", "praia", "litoral", "costeira", "balneário", "beira da praia", "frente para o mar", "pé na areia", "costa", "praia urbana", "praia particular"]
}