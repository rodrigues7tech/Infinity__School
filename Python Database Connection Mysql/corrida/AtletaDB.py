import os
import mysql.connector
from banco import Banco
from mysql.connector import Error
import os

os.system('cls')
class AtletaDB:
    def __init__(self, banco):
        self.banco = banco
    
    def listaAtletas(self):
        try:
            sql = "SELECT * FROM atleta;"
            resultados = self.banco.cursor()
            resultados.execute(sql)
            return resultados
        except Error as e:
            print("Erro: ", e)    
        
    def insereAtletas(self, atleta):
        try:
            sql = f"INSERT INTO atleta (nome, idade) VALUES ('{atleta.nome}', '{atleta.idade}');"
            resultados = self.banco.cursor()
            resultados.execute(sql)
            self.banco.commit()
            os.system('cls')
            return resultados
        except Error as e:
            print("Erro: ", e) 
        