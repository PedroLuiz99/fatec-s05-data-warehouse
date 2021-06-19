from pygrametl.datasources import CSVSource

from db_connection import dw_conn_wrapper
from schema import dim_grupo_voo, dim_data, dim_empresa, dim_aeroporto, origin_mapping, destination_mapping, \
    fact_measures, fato_voo, column_mapping


def main():
    first_line = True
    data = CSVSource(open('./assets/resumo_anual_2021-JANEIRO.csv', 'r', 16384, encoding='latin1'), delimiter=';',
                     fieldnames=column_mapping)
    
    print("-- Started ETL Process --")
    for row in data:
        if first_line:
            first_line = False
            continue
            
        print(f"Processing row {data.line_num}...")

        row['id_aeroporto_origem'] = dim_aeroporto.ensure(row, namemapping=origin_mapping)
        row['id_aeroporto_destino'] = dim_aeroporto.ensure(row, namemapping=destination_mapping)
        row['id_empresa'] = dim_empresa.ensure(row)
        row['id_data'] = dim_data.ensure(row)
        row['id_grupo_voo'] = dim_grupo_voo.ensure(row)
        row['horas_voadas'] = float(row['horas_voadas'].replace(",", ".")) if row['horas_voadas'] != '' else 0

        for measure in fact_measures:
            if measure not in ['horas_voadas', 'natureza']:
                row[measure] = int(row[measure]) if row[measure] != '' else 0

        fato_voo.insert(row)
    
    print("Commiting changes...")
    dw_conn_wrapper.commit()
    dw_conn_wrapper.close()
    
    print("-- ETL Process successfully finished! --")


if __name__ == '__main__':
    main()
