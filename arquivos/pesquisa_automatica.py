from amparos.botoes import BotaoAtualizar
from amparos.layouts import Menu_Principal, Mensagem_Erro

def mostrar(event, values):
    print('-'*150)
    print(f'\n\033[1;34mEVENTO: \033[1;33m{event}\033[m')

    try:

        for k, v in values.items():
            print()
            print(f'\033[1;34mCHAVE: \033[1;33m{k}\033[m')
            print(f'\033[1;34mVALOR: \033[1;33m{v}\033[m')

    except:

        pass

lista_perguntas, local, valido = [], '', False

window = Menu_Principal(local=local, lista=lista_perguntas) # Criando janela principal do programa

while True:

    event, values = window.read() # Abrindo a janela principal, para receber valores do usuario

    mostrar(event, values)

    if event in ('Sair', None): # O programa será finalizado por completo

        window.close()

        break

    if event == 'Atualizar': # Programa será atualizado de acordo com as informações do usuario

        local = values['local']

        window.close()

        valido, lista_perguntas = BotaoAtualizar(local) # Recebendo lista de perguntas do arquivo .xlsx

        window = Menu_Principal(local=local, lista=lista_perguntas)

    if valido is True: # Serão liberadas quando o programa receber um arquivo .xlsx valido

        if event == 'Visualizar' and len(values['perguntas']) != 0:
            pass

        if event == 'Editar conteudo da lista':
            pass

        if event == 'Criar arquivo':
            pass

        if event == 'Atualizar respostas':
            pass
    
    # Caso o usuario tente mesmo sem um arquvi valido irá aparece uma mensagem de erro

    elif event != 'Atualizar': 

        window.close()

        Mensagem_Erro('Você deve escolher um arquivo .xlsx valido para usar essa opção!')

        window = Menu_Principal(local=local, lista=lista_perguntas)

