
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
        [sg.Listbox(lista, key='pergunta', size=(68, 5))],
        [sg.Button('Visualizar'), sg.Button('Editar lista'),sg.Button('Criar arquivo'), sg.Button('Atualizar respostas'), sg.Button('Sair')]]

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

    # Caso os caracters da pergunta for > 70 ira diminuir o tamanho para 70 caracters, para visualizar na bar

    if len(conteudo["sua pergunta"]) > 70:
        window = sg.Window(f'{conteudo["sua pergunta"][:70]}... - Pesquisa automatica v1.0', layout)
    
    elif len(conteudo["sua pergunta"]) <= 70:
        window = sg.Window(f'{conteudo["sua pergunta"]} - Pesquisa automatica v1.0', layout)

    window.read()
    window.close()

# Cria a janela de Editar lista

def Editar_Lista(lista):

    """
    Parameters:

        lista: Mostra os itens da lista na janela do programa

    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()
    """

    layout = [[sg.Button('Adicionar pergunta'), sg.Button('Editar pergunta / conteudo'), 
            sg.Button('Deletar pergunta / conteudo')],
            [sg.Listbox(lista, key='pergunta', size=(68, 5))],
            [sg.Button('Visualizar'), sg.Button('Cancelar')]]

    return sg.Window('Editar lista - Pesquisa automatica v1.0', layout)

# Janela que recebe uma pergunta

def Recebe_Pergunta():

    """
    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()
    """

    layout = [[sg.Input(key='adicionar_pergunta')],
             [sg.Button('Adicionar'), sg.Button('Cancelar')]]

    return sg.Window('Adicionar pergunta - Pesquisa Automatica v1.0', layout)

# Janela que recebe sim ou não para deletar a pergunta

def Janela_deletar(pergunta):
    """
    Parameters:

        pergunta: Necessario para mostrar a sua pergunta na janela

    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()

    """

    if len(pergunta) > 35:

        pergunta = pergunta[:35]

    layout = [[sg.Text(f'Deletar pergunta / conteudo da pergunta:\n'
               f'{pergunta} ...')],
              [sg.Button('Sim'), sg.Button('Não')]]

    return sg.Window('Deletar pergunta - Pesquisa automatica v1.0', layout)

# Janela para editar conteudo da pergunta escolhida

def Menu_Editar(conteudo, pergunta):
    """
    Parameters:

        conteudo: recebe uma lista expesifica para mostrar o conteudo

        pergunta: Necessario para mostrar a sua pergunta na janela

    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()

    """

    if len(pergunta) > 70:

        pergunta = pergunta[:70]

    layout = [[sg.Text('Sua pergunta')],
        [sg.Multiline(conteudo['sua pergunta'], key='sua pergunta', size=(104, 2))],
        [sg.Text('1° Pergunta similar'), sg.Text(f'{" " * 65}2° Pergunta similar')],
        [sg.Multiline(conteudo['1 pergunta similar'], key='1 pergunta similar', size=(50, 2)),
        sg.Multiline(conteudo['2 pergunta similar'], key='2 pergunta similar', size=(50, 2))],
        [sg.Text('1° Resposta similar'), sg.Text(f'{" " * 64}1° Resposta similar')],
        [sg.Multiline(conteudo['1 pergunta similar 1 resposta'], key='1 pergunta similar 1 resposta', size=(50, 5)),
        sg.Multiline(conteudo['2 pergunta similar 1 resposta'], key='2 pergunta similar 1 resposta', size=(50, 5))],
        [sg.Text('2° Resposta similar'), sg.Text(f'{" " * 64}2° Resposta similar')],
        [sg.Multiline(conteudo['1 pergunta similar 2 resposta'], key='1 pergunta similar 2 resposta', size=(50, 5)),
        sg.Multiline(conteudo['2 pergunta similar 2 resposta'], key='2 pergunta similar 2 resposta', size=(50, 5))],
        [sg.Button('Salvar'), sg.Button('Cancelar')]]

    return sg.Window(f'{pergunta} - Pesquisa automatica v1.0', layout)
    
# Janela para salvar alterações 

def Confirmar_Alterações():

    """
    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()

    """

    layout = [[sg.Text('Deseja salvar as alterações?')],
              [sg.Button('Sim'), sg.Button('Não')]]

    return sg.Window('Confirmar', layout)

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


