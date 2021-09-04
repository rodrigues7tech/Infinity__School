from controller.ClientesController import ClientesController
from tkinter import Tk
from view.CadastroCliente import CadastroCliente

root = Tk()

cadastroCliente = CadastroCliente(root)
ClientesController(cadastroCliente)

# listarCliente = ListarCliente(root)
# ClientesController.listarCliente(listarCliente)

root.mainloop()