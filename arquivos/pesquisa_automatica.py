
from amparos.botoes import *
from amparos.layouts import *

valido, lista_perguntas = False, []

window = Menu_Principal(local='', lista=[]) # Criando janela principal do programa

while True:

    event, values = window.read() # Abrindo a janela principal, para receber valores do usuario

    local, pergunta = values['local'], values['pergunta']
    
    Resultados_Terminal(event, values)

    window.close()

    if event in ('Sair', None): # O programa será finalizado por completo

        break

    if event == 'Atualizar': # Programa será atualizado de acordo com as informações do usuario

        valido, lista_perguntas = BotaoAtualizar(local) # Recebendo lista de perguntas do arquivo .xlsx

    if valido is True: # Opções liberadas quando o programa receber um arquivo .xlsx valido

        if event == 'Visualizar':

            BotaoVisualizar(pergunta=pergunta, local=local) # Cria interfase para visualizar o conteudo

        if event == 'Editar lista':

            lista_perguntas = BotaoEditarLista(lista_perguntas, local=local) # Cria interface do menu editar lista

        if event == 'Atualizar respostas':

            BotaoAtualizarResp(local=local)

        if event == 'Criar arquivo':

            pass
    
    elif event != 'Atualizar': # Caso o usuario tente com um arquivo invalido irá aparecer uma mensagem de erro

        Mensagem_Erro('Você deve escolher um arquivo .xlsx valido para usar essa opção!')

    window = Menu_Principal(local=local, lista=lista_perguntas)

