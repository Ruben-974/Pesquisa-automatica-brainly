
import PySimpleGUI as sg

# --=-=-- Janelas de Navegação --=-=--

def Menu_Principal(local, lista): # Cria janela principal do programa

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

def Editar_Lista(lista): # Cria a janela de Editar lista

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

    return sg.Window('Editar lista - Pesquisa automatica v1.0', layout, location=(420, 300))

def Atualizar_respostas():

    """
    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()
    """

    layout = [[sg.Radio('Atualizar tudo', key='Tudo', group_id='radio_1')],
        [sg.Radio('Atualizar o necessario', key='Necessario', group_id='radio_1', default=True)],
        [sg.Radio('Atualização personalizada', key='Personalizado', group_id='radio_1')],
        [sg.Button('Ok'), sg.Button('Cancelar')]]

    return sg.Window('Atualizar respostas - Pesquisa automatica v1.0', layout, location=(420, 300))

# --=-=-- Janelas de Modificação --=-=--

def Menu_Editar(conteudo, pergunta): # Janela para editar conteudo da pergunta escolhida
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

    return sg.Window(f'{pergunta} - Pesquisa automatica v1.0', layout, location=(420, 300))
 
def Recebe_Pergunta(): # Janela que recebe uma pergunta

    """
    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()
    """

    layout = [[sg.Input(key='adicionar_pergunta')],
             [sg.Button('Adicionar'), sg.Button('Cancelar')]]

    return sg.Window('Adicionar pergunta - Pesquisa Automatica v1.0', layout, location=(420, 300))

def Janela_deletar(pergunta): # Janela que recebe sim ou não para deletar a pergunta
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

    return sg.Window('Deletar pergunta - Pesquisa automatica v1.0', layout, location=(420, 300))

# --=-=-- Janelas de Visualização --=-=--

def Mensagem_Erro(msg): # Cria uma janela de erro "Personalizada" :D

    """
    Parameters:

        msg: Mensagem de erro que será visualizada
    
    """

    layout = [[sg.Text(msg)], [sg.Button('Ok')]]
    window = sg.Window('Erro - Pesquisa automatica v1.0', layout, location=(420, 300))
    window.read()
    window.close()

def Visualizar_Conteudo(conteudo): # Cria uma janela para visualizar o conteudo sobre a pergunta

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
        window = sg.Window(f'{conteudo["sua pergunta"][:70]}... - Pesquisa automatica v1.0', layout, location=(420, 300))
    
    elif len(conteudo["sua pergunta"]) <= 70:
        window = sg.Window(f'{conteudo["sua pergunta"]} - Pesquisa automatica v1.0', layout, location=(420, 300))

    window.read()
    window.close()
 
# --=-=-- Janelas de Confirmação --=-=--

def Confirmar_Alterações(): # Janela para salvar alterações 

    """
    Returns:

        return sg.Window(...): Todas infomações necessarias para iniciar a janela com .read()

    """

    layout = [[sg.Text('Deseja salvar as alterações?')],
              [sg.Button('Sim'), sg.Button('Não')]]

    return sg.Window('Confirmar', layout, location=(420, 300))

# --=-=-- Outras demonstrações --=-=--

def Resultados_Terminal(event, values): # Visualizar oque está acontecendo no terminal

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


