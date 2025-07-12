from controller import Controller
from view.view import Inicio 
from model import BancoMongodb

'''
MAIN inicia  o programa
'''
def main():
    model = BancoMongodb()
    controller = Controller(model , None)
    view = Inicio(controller)
    view.controller = controller
    controller.definir_tela(view)
    view.comecar()
    
if __name__ == "__main__":
    App = main()