from banco import Banco
from AtletaDB import AtletaDB
from Atleta import Atleta
import os

os.system('cls')
conexao = Banco()
con = conexao.conectar()
a = AtletaDB(con)

nome = input("Nome: ")
idade = input("Idade: ")
atleta = Atleta(nome, idade)
resultado = a.insereAtletas(atleta)
r = a.listaAtletas()
if atleta != None:
    for r1 in r:
        print("Nome: ", r1[1])
        print("Idade: ", r1[2])