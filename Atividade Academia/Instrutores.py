def verificaTurno(turno):
    if turno == "matutino" or turno == "vespertino" or turno == "noturno":
        return turno
    else:
        print("turno inválido!")
        return ""
    
def verificaCategoria(categoria):
    if categoria == "musculação" or categoria == "crossfit" or categoria == "spinning":
        return categoria
    else:
        print("Categoria inválida!")
        return ""


class Instrutores:
    def __init__(self, codigo, nome, dataNasc, salario, turno, cref, categoria):
        self.codigo = codigo
        self.nome = nome
        self.dataNasc = dataNasc
        self.__salario = salario
        self.__turno = verificaTurno(turno)
        self.cref = cref
        self.__categoria =  verificaCategoria(categoria)
        
    # GETTERS E SETTERS
    @property
    def salario(self):
        return "O salário do Instrutor é: " + str(self.__salario)
    
    @salario.setter
    def salario(self, novoSalario):
        print("Não é possível atribuir um novo salário!")
        return
    
    @property
    def turno(self):
        return "O turno do Instrutor é: " + self.__turno
    
    @turno.setter
    def turno(self, novoTurno):
        self.__turno = verificaTurno(novoTurno)
        
        
    @property
    def categoria(self):
        return "A categoria do instrutor é: " + self.__categoria
    
    @categoria.setter
    def categoria(self, novaCategoria):
        self.__categoria = verificaCategoria