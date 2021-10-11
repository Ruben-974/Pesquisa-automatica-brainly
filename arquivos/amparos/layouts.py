
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

    layout = [[sg.Input(local, key='local'), sg.FileBrowse('Browse', file_types=(("ALL Files", ".xlsx*"),)),sg.Button('Atualizar', size=(12, 0))],
        [sg.Listbox(lista, key='perguntas', size=(68, 5), enable_events=True)],
        [sg.Button('Visualizar'), sg.Button('Editar conteudo da lista'),sg.Button('Criar arquivo'), sg.Button('Atualizar respostas'), sg.Button('Sair')]]

    return sg.Window('Menu Principal - Pesquisa Automatica v1.0', layout, location=(420, 300))

# Cria uma janela de erro "Personalizada" :D

def Mensagem_Erro(msg):

    """
    Parameters:

        msg: Mensagem de erro que será visualizada
    
    """

    layout = [[sg.Text(msg)], [sg.Button('Ok')]]
    window = sg.Window('Erro - Pesquisa automatica v1.0', layout)
    window.read()
    window.close()

# Cria uma janela para visualizar o conteudo sobre a pergunta

def Visualizar_Conteudo(conteudo):

    '''
    Parameters:

        conteudo: Recebe um dicionario expesifico e cria uma janela para visualizar o seu conteudo

    '''

    layout = [[sg.Multiline(

        f'\n- Sua pergunta - \n\n'
        f'{conteudo["sua pergunta"]}\n\n'
        f' - 1° Resposta - \n\n'
        f'{conteudo["1 pergunta similar 1 resposta"]}\n\n'
        f' - 2° Resposta - \n\n'
        f'{conteudo["1 pergunta similar 2 resposta"]}\n\n'
        f' - 3° Resposta - \n\n'
        f'{conteudo["2 pergunta similar 1 resposta"]}\n\n'
        f' - 4° Resposta - \n\n'
        f'{conteudo["2 pergunta similar 2 resposta"]}',
        size=(90, 25))], [sg.Button('Ok')]]

    # Caso os caracters da pergunta for > 70 longo ira diminuir o tamanho para 70 caracters, para visualização na Bar

    if len(conteudo["sua pergunta"]) > 70:
        window = sg.Window(f'{conteudo["sua pergunta"][:70]}... - Pesquisa automatica v1.0', layout)
    
    elif len(conteudo["sua pergunta"]) <= 70:
        window = sg.Window(f'{conteudo["sua pergunta"]} - Pesquisa automatica v1.0', layout)

    window.read()
    window.close()

# Um print "especial" para visualizar oque está acontecendo no terminal enquanto o programa e executado

def Resultados_Terminal(event, values):
    '''
    Parameters:

        event: Evento retordado quando acontece alguma ação na janela

        values: Valores que foram enviados pelo usuario

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