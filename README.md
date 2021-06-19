# Fatec - Data Warehouse project
Projeto para a disciplina de Data Warehouse do quinto semestre, lecionada pela professora Patricia Belin Ribeiro.

Este projeto utiliza como base uma base de dados extraída da ANAC. Você pode consultar a fonte original dos dados [aqui](https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/dados-estatisticos/dados-estatisticos).

## Dependências
Este projeto foi desenvolvido para ser usado com o `Docker` e `Docker Compose`, portanto, tenha-os instalados para execução do mesmo.

Caso não deseje utilizar o Docker (o que eu não recomendo), é necessário instalar os seguintes pacotes:
* PostgreSQL Server 13
* Python 3.6 ou superior
* Pip
* psycopg2 → `pip install psycopg2` ou `pip install psycopg2-binary`
* pygrametl → `pip install pygrametl`

## Executando o projeto
### Via Docker
Renomeie o arquivo `.env-example` na raiz do projeto para `.env`

Construa e suba a stack do docker com o seguinte comando (lembre-se de estar dentro da pasta do projeto):
```shell
docker-compose up --build -d
```
O Docker subirá dois containeres: Um para o banco de dados Postgres e outro com o código do ETL que carregará os dados para dentro do banco de dados.

O banco de dados estará de pé e alimentado automaticamente dentro de alguns segundos após a finalização do comando. Ele estará disponível para acesso na porta `5432` com as credenciais que estão no arquivo `.env`.

### Sem docker (não recomendado)
Considerando que você tenha uma instância Postgres em execução e com um usuário e banco de dados criado para o projeto, aplique o arquivo `src/dw_tables.sql` para criação das tabelas necessárias para armazenar os dados. 

Em seguida exporte as seguintes variáveis no seu shell:
```shell
export POSTGRES_USER=<usuario do banco>
export POSTGRES_PASSWORD=<senha do usuario>
export POSTGRES_DB=<nome do banco>
export POSTGRES_HOST=<host do banco - se estiver na sua máquina utilize localhost>
export POSTGRES_PORT=<porta do banco, por padrão 5432>
```

Após isso entre na pasta `src` com o comando:
```shell
cd src
```

E execute o ETL manualmente:
```shell
python ./etl.py
```

Em alguns segundos o CSV será carregado para a base de dados.

> Sim, eu sei que tem gambiarras nesse projeto, mas o prazo está apertado =)
