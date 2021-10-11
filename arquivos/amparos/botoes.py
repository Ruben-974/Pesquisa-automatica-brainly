from amparos.dados import CriarListaPerguntas, VerificarXlsx
from amparos.layouts import Mensagem_Erro

def BotaoAtualizar(local):

    """
    Parameters:

    local: Informe o local do arquivo .xlsx

    Returns:

    return CriarListaPerguntas(local): Lista com as perguntas do arquivo .xlsx
    return []: lista vazia
    
    """

    valido = VerificarXlsx(local) # Verifica se o arquico .xlsx e um arquivo valido

    if valido is True: # Se for valido retorna a lista com as perguntas
        
        return CriarListaPerguntas(local) 

    else: # Se não retorna uma mensagem de erro e uma lista vazia 

        Mensagem_Erro(valido) 

        return [] 


