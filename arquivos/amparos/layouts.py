# Bribriotecas utilizadas

import PySimpleGUI as sg

# Cria janela principal do programa

def Menu_Principal(local, lista):

    """
    Parameters:

        local: Ficará na barra de busca da janela

        lista: Mostra os itens da lista na janela do programa

    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()
    
    """

    layout_principal = [[sg.Input(local, key='local'), sg.FileBrowse('Browse', file_types=(("ALL Files", ".xlsx*"),)),sg.Button('Atualizar', size=(12, 0))],
        [sg.Listbox(lista, key='perguntas', size=(68, 5), enable_events=True)],
        [sg.Button('Visualizar'), sg.Button('Editar conteudo da lista'),sg.Button('Criar arquivo'), sg.Button('Atualizar respostas'), sg.Button('Sair')]]

    return sg.Window('Menu Principal - Pesquisa Automatica v1.0', layout_principal, location=(420, 300))


# Cria uma janela de erro "Personalizada" :D

def Mensagem_Erro(msg):

    """
    Parameters:

        msg: Mensagem de erro que será visualizada
    
    """

    layout_erro = [[sg.Text(msg)], [sg.Button('Ok')]]
    window = sg.Window('Erro - Pesquisa automatica v1.0', layout_erro)
    window.read()
    window.close()


def Resultados_Terminal(event, values):
    '''
    Temporario, somente para ajudar no desenvolvimento
    '''
    print('-'*150)
    print(f'\n\033[1;34mEVENTO: \033[1;33m{event}\033[m')

    try:

        for k, v in values.items():
            print()
            print(f'\033[1;34mCHAVE: \033[1;33m{k}\033[m')
            print(f'\033[1;34mVALOR: \033[1;33m{v}\033[m')

    except:

        pass