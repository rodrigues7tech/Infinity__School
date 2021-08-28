import mysql.connector
from mysql.connector import Error
import os

os.system('cls')
class Banco:
    def __init__(self):
        pass
    
    def conectar(self):
        try:
            con = mysql.connector.connect(
                host = 'localhost',
                database = 'corrida',
                user = 'root',
                password = 'aluno99'
            )
            if con.is_connected():
                db_info = con.get_server_info()
                print('Conectou ao mysql versão: ', db_info)
                return con
        except Error as e:
            print("Erro na conexão mysql: ", e)