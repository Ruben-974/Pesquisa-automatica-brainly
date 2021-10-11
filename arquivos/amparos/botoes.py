from amparos.dados import *
from amparos.layouts import *

# Executar quando o botão "Atualizar" for chamado

def BotaoAtualizar(local):

    """
    Parameters:

        local: Informe o local do arquivo .xlsx

    Returns:

        return True, CriarListaPerguntas(local):

            True: Retorna verdadeiro pois o arquivo .xlsx e valido

            CriarListaPerguntas(local): Como a o arquivo e valido, o programa irá pegar os as perguntas do arquivo


        return False, []:

            False: Retorna falso pois o arquivo .xlsx e invalido

            []: Como o arquivo e invalido, o programa irá retornar uma lista vazia
    
    """

    valido = VerificarXlsx(local) # Verifica se o arquico .xlsx e um arquivo valido

    if valido is True: # Se for valido retorna a lista com as perguntas
        
        return True, CriarListaPerguntas(local) 

    else: # Se não retorna uma mensagem de erro e uma lista vazia 

        Mensagem_Erro(valido) 

        return False, [] 

# Executar quando o botão "Visualizar" for chamado

def BotaoVisualizar(pergunta, local):

    '''
    Parameters:

        pergunta: Pergunta que você deseja analisar o conteudo 

        local: Local do arquivo .xlsx (Valido)
        
    '''

    conteudo = DicionarioComConteudo(pergunta=pergunta, local=local)

    Visualizar_Conteudo(conteudo)
