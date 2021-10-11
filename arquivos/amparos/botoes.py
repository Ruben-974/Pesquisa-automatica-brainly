from amparos.dados import CriarListaPerguntas, VerificarXlsx
from amparos.layouts import Mensagem_Erro

def BotaoAtualizar(local):

    valido = VerificarXlsx(local)

    if valido is True:
        
        return CriarListaPerguntas(local)

    else:

        Mensagem_Erro(valido)

        return []


