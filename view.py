import tkinter as tk
from view.frame_lista import FrameLista
from view.frame_detalhes import FrameDetalhes
from view.frame_coleta1 import FrameColeta
from view.frame_coleta2 import FrameColeta2
from view.frame_resumo import FrameResumo
from view.frame_excluir_avaliacao import ExcluirAvaliacao

class Inicio:
    def __init__(self,controller):
        self.root = tk.Tk()
        self.controller = controller
        self.frames = {}
        
        #Cria o Container para posicionar os frames e o coloca dentro da janela principal
        self.container = tk.Frame(self.root) 
        self.container.pack()
        
        #Instancia todas as telas e as associa ao dicionário a uma chave para fazer a troca de tela
        self.frames["coleta1"] = FrameColeta(self.container, self.controller ,self) #Indica que serão colocados dentro de container
        self.frames["coleta2"] = FrameColeta2(self.container, self.controller,self)
        self.frames["resumo"] = FrameResumo(self.container, self.controller,self)
        self.frames["lista_avaliacoes"] = FrameLista(self.container, self.controller,self)
        self.frames["detalhes_avaliacao"] = FrameDetalhes(self.container, self.controller,self)
        self.frames["excluir_avaliacao"] = ExcluirAvaliacao(self.container, self.controller,self)
        
        for frame in self.frames.values(): #<- percorre os frames e os posiciona no mesmo lugar com o tkraise na funcao trocar_tela
            frame.grid(row=0,column=0,sticky="nsew")
        
        self.tela_atual = None
        self.trocar_tela('coleta1')
   
    #Troca de tela com base na chave passada
    def trocar_tela(self,trocar):
        if trocar == "resumo":
            self.frames["resumo"].atualizar()
        elif trocar == "lista_avaliacoes":
            self.frames['lista_avaliacoes'].atualizar_lista()
                
        self.frames[trocar].tkraise()
    
    def comecar(self):
        self.root.mainloop()
    
    def mostrar_detalhes(self,avaliacao):
        self.controller.avaliacao_para_excluir = avaliacao
        self.frames['detalhes_avaliacao'].mostrar_dados(avaliacao)
        self.trocar_tela('detalhes_avaliacao')        
    
    def resetar_campos(self):
        self.frames['coleta1'].zerar_campos()
        self.frames['coleta2'].zerar_campos()        
            