from model.Cliente import Cliente
from data.ClienteBd import ClienteBd
from data.Connect import Connect


class ClientesController:
    def __init__(self, cadastroCliente):
        self.view = cadastroCliente
    
        
        
    def cadastrar(self):
        nome = self.view.nome.get()
        cpf = self.view.cpf.get()
        endereco = self.view.endereco.get()
        cliente = Cliente(nome, endereco, cpf)
        if not cliente.cpfValido(cpf):
            self.view.mensagem["text"] = "CPF inválido!"
        else:
            if nome == "":
                self.view.mensagem["text"] = "Nome não pode ser vazio!"
            else:
                con = Connect()
                c, ok = con.conectar()
                if ok:
                    clientebd = ClienteBd(c)
                    clientebd.inserirCliente(cliente)
                    self.view.mensagem["text"] = "Deu tudo certo!"
                else:
                    self.view.mensagem["text"] = "Estamos tendo problemas com o banco, tente mais tarde!"
                    print("Erro: ", c)
                    
    # def listarCliente(self, listarCliente):
    #     sql = f"UPDATE clientes set nome='{listarCliente.nome}', endereco='{listarCliente.endereco}' WHERE cpf='{listarCliente.cpf}';"
    #     resultado = con.cursor()
        