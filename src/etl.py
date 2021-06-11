import psycopg2
import pygrametl
from pygrametl.datasources import CSVSource
from pygrametl.tables import Dimension, FactTable

# TODO: Refatorar e limpar arquivo, esta é uma versão inicial
# TODO: tratativa de campos vazios

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
    "grupo_voo",
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
    "carga_gratis_kg",
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

dw_string = "host='localhost' dbname='dw' user='dwuser' password='dwpass'"
dw_pgconn = psycopg2.connect(dw_string)
dw_conn_wrapper = pygrametl.ConnectionWrapper(connection=dw_pgconn)

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

dim_data = Dimension(
    name='dim_data',
    key='id_data',
    attributes=['ano', 'mes']
)

fato_voo = FactTable(
    name='fato_voo',
    keyrefs=['id_aeroporto_origem', 'id_aeroporto_destino', 'id_empresa', 'id_data'],
    measures=["natureza", "grupo_voo", "passageiros_pagos", "passageiros_gratis",
              "correio_kg", "ask", "rpk", "atk", "rtk", "combustivel", "distancia_voada", "decolagens",
              "carga_paga_km", "carga_gratis_kg", "correio_km", "assentos", "payload", "horas_voadas", "bagagem_km"]
)

data = CSVSource(open('./../assets/resumo_anual_2021-JANEIRO.csv', 'r', 16384, encoding='latin1'), delimiter=';',
                 fieldnames=column_mapping)


def parse_distance_float(row):
    row['horas_voadas'] = float(row['horas_voadas'].replace(",", ".") or 0)


def main():
    first_line = True
    for row in data:
        if first_line:
            first_line = False
            continue

        row['id_aeroporto_origem'] = dim_aeroporto.ensure(row, namemapping=origin_mapping)
        row['id_aeroporto_destino'] = dim_aeroporto.ensure(row, namemapping=destination_mapping)
        row['id_empresa'] = dim_empresa.ensure(row)
        row['id_data'] = dim_data.ensure(row)
        parse_distance_float(row)
        fato_voo.insert(row)

    dw_conn_wrapper.commit()
    dw_conn_wrapper.close()


if __name__ == '__main__':
    main()
