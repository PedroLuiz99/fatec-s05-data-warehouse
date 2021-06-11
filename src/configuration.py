import csv
import argparse
import configparser

# TODO: Este arquivo será usado para gerenciar as configs de ambiente no futuro, não está pronto


class DBConfiguration:
    host: str
    port: str
    user: str
    password: str
    schema: str

    @classmethod
    def load(cls, db_host: str, db_port: str, db_user: str, db_password: str, db_schema: str) -> None:
        cls.host = db_host
        cls.port = db_port
        cls.user = db_user
        cls.password = db_password
        cls.schema = db_schema


class ConfigFileParser:
    @classmethod
    def _get_config_parser(cls):
        return configparser.ConfigParser()

    @classmethod
    def parse_config_file(cls, config_file: str):
        config = cls._get_config_parser()
        config.read(config_file)
        return dict(config['default'])


class DBConfigLoader:
    @staticmethod
    def load(config_file):
        DBConfiguration.load(**ConfigFileParser.parse_config_file(config_file))


class DB:
    def __init__(self, configuration: DBConfiguration):
        self.configuration = configuration

    def connect(self):
        pass


def parse_cli_arguments():
    parser = argparse.ArgumentParser(description="ETL Script")
    parser.add_argument("-c", "--args-file", help="Configuration file location", action='store', dest='config_file',
                        required=False, default="./settings.ini")
    parser.add_argument("-f", "--file", help="CSV file to import", action="store", dest="csv_file", required=True)
    parser.add_argument("-e", "--encoding", help="CSV file encoding", action="store", dest="encoding", required=False,
                        default='latin1')
    return parser.parse_args()


def read_csv_file(file: str, encoding: str):
    with open(file, 'r', encoding=encoding) as csv_file:
        raw_content = csv.DictReader(csv_file, delimiter=';')
        formatted_content = [dict(line) for line in raw_content if raw_content.line_num > 0]

    return formatted_content

#
# if __name__ == '__main__':
#     args = parse_cli_arguments()
#     DBConfigLoader.load(args.config_file)
#
#     content = read_csv_file(args.csv_file, args.encoding)
