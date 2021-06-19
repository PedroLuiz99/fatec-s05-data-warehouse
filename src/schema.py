from pygrametl.tables import Dimension, FactTable

column_mapping = (
    "sigla_empresa",
    "nome_empresa",
    "nacionalidade_empresa",
    "ano",
    "mes",
    "sigla_aeroporto_origem",
    "nome_aeroporto_origem",
    "uf_aeroporto_origem",
    "regiao_aeroporto_origem",
    "pais_aeroporto_origem",
    "continente_aeroporto_origem",
    "sigla_aeroporto_destino",
    "nome_aeroporto_destino",
    "uf_aeroporto_destino",
    "regiao_aeroporto_destino",
    "pais_aeroporto_destino",
    "continente_aeroporto_destino",
    "natureza",
    "nome_grupo_voo",
    "passageiros_pagos",
    "passageiros_gratis",
    "carga_paga_kg",
    "carga_gratis_kg",
    "correio_kg",
    "ask", "rpk", "atk", "rtk",
    "combustivel",
    "distancia_voada",
    "decolagens",
    "carga_paga_km",
    "carga_gratis_km",
    "correio_km",
    "assentos",
    "payload",
    "horas_voadas",
    "bagagem_km"
)

origin_mapping = {
    "sigla_aeroporto": "sigla_aeroporto_origem",
    "nome_aeroporto": "nome_aeroporto_origem",
    "uf_aeroporto": "uf_aeroporto_origem",
    "regiao_aeroporto": "regiao_aeroporto_origem",
    "pais_aeroporto": "pais_aeroporto_origem",
    "continente_aeroporto": "continente_aeroporto_origem"
}

destination_mapping = {
    "sigla_aeroporto": "sigla_aeroporto_destino",
    "nome_aeroporto": "nome_aeroporto_destino",
    "uf_aeroporto": "uf_aeroporto_destino",
    "regiao_aeroporto": "regiao_aeroporto_destino",
    "pais_aeroporto": "pais_aeroporto_destino",
    "continente_aeroporto": "continente_aeroporto_destino"
}

# dimensoes e fato
dim_empresa = Dimension(
    name='dim_empresa',
    key='id_empresa',
    attributes=['nome_empresa', 'nacionalidade_empresa'],
)

dim_aeroporto = Dimension(
    name='dim_aeroporto',
    key='id_aeroporto',
    attributes=["sigla_aeroporto",
                "nome_aeroporto",
                "uf_aeroporto",
                "regiao_aeroporto",
                "pais_aeroporto",
                "continente_aeroporto"
                ],
)

dim_grupo_voo = Dimension(
    name='dim_grupo_voo',
    key='id_grupo_voo',
    attributes=['nome_grupo_voo']
)

dim_data = Dimension(
    name='dim_data',
    key='id_data',
    attributes=['ano', 'mes']
)

fact_measures = ["natureza", "passageiros_pagos", "passageiros_gratis",
                 "correio_kg", "ask", "rpk", "atk", "rtk", "combustivel", "distancia_voada", "decolagens",
                 "carga_paga_km", "carga_gratis_km", "carga_paga_kg", "carga_gratis_kg", "correio_km", "assentos",
                 "payload", "horas_voadas", "bagagem_km"]

fato_voo = FactTable(
    name='fato_voo',
    keyrefs=['id_aeroporto_origem', 'id_aeroporto_destino', 'id_empresa', 'id_data', 'id_grupo_voo'],
    measures=fact_measures
)