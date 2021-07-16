def verificaCategoria(categoria):
    if categoria == "musculação" or categoria == "crossfit" or categoria == "spinning":
        return categoria
    else:
        print("Categoria inválida!")
        return ""
class Aula:
    def __init__(self, duracao, categoria, instrutor, alunos):
        self.duracao = duracao
        self.categoria =  verificaCategoria(categoria)
        self.instrutor = instrutor
        self.__alunos = alunos
        
    @property
    def alunos(self):
        for a in self.__alunos:
            print(a.nome)
            
    @alunos.setter
    def alunos(self, novoAluno):
        self.__alunos.append(novoAluno)
        
    