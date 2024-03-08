import pyodbc
import configparser

def get_database_config(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    return config['database']

def connect_to_database(config):
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};' \
                        f'SERVER={config["server"]};' \
                        f'DATABASE={config["database"]};' \
                        f'UID={config["username"]};' \
                        f'PWD={config["password"]};' \
                        f'Trusted_Connection=no;'
    return pyodbc.connect(connection_string)

def commit_transaction(connection):
    connection.commit()

def close_cursor(cursor):
    cursor.close()

def close_connection(connection):
    connection.close()