import PySimpleGUI as sg


def Menu_Principal(local, lista_perguntas):

    layout_principal = [[sg.Input(local, key='local'), sg.FileBrowse('Browse', file_types=(("ALL Files", ".xlsx*"),)),sg.Button('Atualizar', size=(12, 0))],
        [sg.Listbox(lista_perguntas, key='pergunta', size=(68, 5), enable_events=True)],
        [sg.Button('Visualizar'), sg.Button('Editar conteudo da lista'),sg.Button('Criar arquivo'), sg.Button('Atualizar respostas'), sg.Button('Sair')]]

    return sg.Window('Menu Principal - Pesquisa Automatica v1.0', layout_principal, location=(420, 300))


def Mensagem_Erro(msg):

    layout_erro = [[sg.Text(msg)], [sg.Button('Ok')]]
    window = sg.Window('Erro - Pesquisa automatica v1.0', layout_erro)
    window.read()
    window.close()


        