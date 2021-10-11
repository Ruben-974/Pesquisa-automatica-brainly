
from amparos.botoes import *
from amparos.layouts import *

lista_perguntas, local, valido = [], '', False

window = Menu_Principal(local=local, lista=lista_perguntas) # Criando janela principal do programa

while True:

    event, values = window.read() # Abrindo a janela principal, para receber valores do usuario
    local = values['local']

    Resultados_Terminal(event, values)

    if event in ('Sair', None): # O programa será finalizado por completo

        window.close()

        break

    if event == 'Atualizar': # Programa será atualizado de acordo com as informações do usuario

        window.close()

        valido, lista_perguntas = BotaoAtualizar(local) # Recebendo lista de perguntas do arquivo .xlsx

        window = Menu_Principal(local=local, lista=lista_perguntas)

    if valido is True: # Opções liberadas quando o programa receber um arquivo .xlsx valido

        if event == 'Visualizar':

            window.close()

            if len(values['perguntas']) == 0: # Se o ususario não selecionou nenhum item da lista

                Mensagem_Erro('Escolha uma pergunta antes de selecionar essa opção!') # Mensagem de erro

            else: # Se selecionou o item

                BotaoVisualizar(pergunta=values['perguntas'][0], local=local) # Cria interfase para visualizar o conteudo

            window = Menu_Principal(local=local, lista=lista_perguntas)

        if event == 'Editar conteudo da lista':
            pass

        if event == 'Criar arquivo':
            pass

        if event == 'Atualizar respostas':
            pass
    
    # Caso o usuario tente mesmo sem um arquivo valido irá aparecer uma mensagem de erro

    elif event != 'Atualizar': 

        window.close()

        Mensagem_Erro('Você deve escolher um arquivo .xlsx valido para usar essa opção!')

        window = Menu_Principal(local=local, lista=lista_perguntas)

