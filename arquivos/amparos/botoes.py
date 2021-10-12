
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

    if pergunta == []: # Se o ususario não selecionou nenhuma pergunta

        Mensagem_Erro('Escolha uma pergunta antes de selecionar essa opção!') # Mensagem de erro

    else:

        conteudo = DicionarioComConteudo(pergunta=pergunta[0], local=local)

        Visualizar_Conteudo(conteudo)

# Executar quando o botão "Editar Lista" for chamado

def BotaoEditarLista(lista, local):

    window = Editar_Lista(lista)

    while True:

        event, values = window.read()

        pergunta = values['pergunta']

        if event in (None, 'Cancelar'):

            window.close()

            break

        if event == 'Visualizar':

            window.close()

            BotaoVisualizar(pergunta=pergunta, local=local) # Cria interfase para visualizar o conteudo

            window = Editar_Lista(lista)
