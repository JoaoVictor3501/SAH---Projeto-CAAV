from model import BancoMongodb
#Importa as views e o model que se comunica com o banco(Mongodb) 
'''
Classe responsável por controllar a aplicação
Gerencia as telas , se comunica com o model e a view
'''
class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
        self.dados_avaliacao = {} 
    
    def definir_tela(self,view):
        self.view = view
        
    def trocar_tela(self):
        self.trocar_tela('coleta1')      
           
    #Atualiza os dados temporários no dicionário com os dados da tela 1 e 2 (coleta1 , coleta2)
    def salvar_parcial(self,dados):
        self.dados_avaliacao.update(dados)
    
    #Trata avaliacao antes de salvar
    def avaliacao_completa(self):
        sucesso , mensagem = self.model.tratar_dados(self.dados_avaliacao)
        return {'sucesso': sucesso , 'mensagem': mensagem}    
    
    #Salva avaliacao    
    def salvar_(self):
        sucesso , mensagem = self.model.salvar_avaliacao(self.dados_avaliacao)
        return {'sucesso': sucesso , 'mensagem': mensagem}    

    #Valida e salva a avaliacao se estiver correta (todos os campos estiverem preenchidos corretamente)
    def enviar_avaliacao(self):
        resultado = self.avaliacao_completa()
        if not resultado['sucesso']:
            return resultado
        return self.salvar_()
    
    #Retorna os dados para a tela resumo 
    def exibir_dados(self):
        return self.dados_avaliacao
    
    #Pega todas as avaliacoes do banco  
    def pegar_lista_avaliacoes(self):
        return self.model.lista_avaliacoes()
    
    #Pega a avaliação selecionada para excluir
    def pegar_avaliacao_para_excluir(self):
        return getattr(self, "avaliacao_para_excluir", None)
    
    #Exclui a avaliação , atualiza a lista e volta para tela de lista
    def excluir_avaliacao(self, email_digitado):
        avaliacao = self.pegar_avaliacao_para_excluir()
        if not avaliacao:
            return None
        _id = avaliacao.get("_id")
        
        return self.model.excluir_por_email(email_digitado, _id)   
            