# Importando as Bribrioteca :D

import selenium.common.exceptions
import PySimpleGUI as sg
import pandas as pd
import os

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from amparos.dados import VerificarXlsx

# Criando variaveis

lista_perguntas = []
valido = False
local = ''

# Função para criar Layouts (botões/funções e sua janela)


def layouts(layout=str):

    global layout_menu_principal, layout_menu_editar_conteudo_lista, window_nivel1, window_nivel2, window_nivel3

    if layout == 'layout_menu_principal':
        layout_menu_principal = [[sg.Input(local,
            key='local'), sg.FileBrowse('Browse', key='browse', file_types=(("ALL Files", ".xlsx*"),)),
            sg.Button('Atualizar', size=(12, 0), key='atualizar')],
            [sg.Listbox(lista_perguntas, key='pergunta', size=(68, 5), enable_events=True)],
            [sg.Button('Visualizar'),
             sg.Button('Editar conteudo da lista', key='editar_conteudo_lista'),
             sg.Button('Criar arquivo'), sg.Button('Atualizar respostas'), sg.Button('Sair')]]

        window_nivel1 = sg.Window('Menu Principal - Piriiê v1.0', layout_menu_principal, location=(420, 300))

    if layout == 'layout_menu_editar_conteudo_lista':
        layout_menu_editar_conteudo_lista = [[sg.Button('Adicionar pergunta'), 
                                              sg.Button('Editar pergunta / conteudo'),
                                              sg.Button('Deletar pergunta / conteudo')],
                                             [sg.Listbox(lista_perguntas, key='pergunta', size=(68, 5))],
                                             [sg.Button('Visualizar'), sg.Button('Cancelar')]]

        window_nivel2 = sg.Window('Editar conteudo da lista - Piriiê v1.0', layout_menu_editar_conteudo_lista)

    if layout == 'layout_atualizar_respostas':

        layout_atualizar_respostas = [[sg.Radio('Atualizar tudo', key='atualizar_tudo', group_id='radio_1')],
        [sg.Radio('Atualizar o necessario', key='atualizar_o_necessario', group_id='radio_1', default=True)],
        [sg.Radio('Atualização personalizada', key='atualizacao_personalizada', group_id='radio_1')],
        [sg.Button('Ok'), sg.Button('Cancelar')]]

        window_nivel2 = sg.Window('Atualizar respostas - Piriiê v1.0', layout_atualizar_respostas)
# Função que irar escrever os Events e Values de acordo com o seu nivel


def monstrar_resultados(nivel=0, events=str, values=dict):

    if nivel == 0:
        txt = ''
    else:
        txt = f'_nivel{nivel}'

    print("\n" * 10)
    print(f'event{txt}: \033[1;34m{events}\033[m\n')
    try:
        for k, v in values.items():

            print(f"values{txt}['\033[1;33m{k}\033[m']: \033[1;34m{v}\033[m")

    except AttributeError:
        pass


layouts('layout_menu_principal')

# Sistema de repetição para o usuario escolher um botão

while True:

    # Chamando os valores da primeira janela e os mostradno na tela do ternimal

    event_nivel1, values_nivel1 = window_nivel1.read()

    monstrar_resultados(1, event_nivel1, values_nivel1)

    # Se a resposta for None ou 'Sair' a 1° janela ira fechar e a execução do programa será finalizada

    if event_nivel1 in (None, 'Sair'):
        window_nivel1.close()
        break

    # Se a resposta for 'atualizar', o programa irá trazer as informações do arquivo .xlsx para o programa atual

    elif event_nivel1 == 'atualizar':

        # Criando variaveis ou as rezetando

        local = values_nivel1['local']
        lista_perguntas = []

        # Função que ira verificar se o caminho e valido e se o arquivo tem condições de ser usado no programa atual
        
        valido = VerificarXlsx(local)

        # Se o arquivo for valido o programa irá abrir o arquivo

        if valido is True:

            tabela_xlsx = pd.read_excel(local)

            # Deletar a coluna 'Unnamed: 0' ela pode atrapalhar na resolução das tarefas

            if 'Unnamed: 0' in tabela_xlsx:
                tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

            # Cria uma lista com as perguntas da tabela em .xlsx

            for c in tabela_xlsx['sua pergunta']:
                lista_perguntas.append(c)

        # Se o arquivo for invalido, o programa irá mostrar uma mensagem de erro

        else:

            layout_msg_erro = [[sg.Text(valido)], [sg.Button('Ok', key='ok')]]
            window_nivel2 = sg.Window('Erro - Piriiê v1.0', layout_msg_erro)
            window_nivel2.read()
            window_nivel2.close()

        # Independente da resposta (valido is True or valido is False) o programa irá rezetar a janela principal

        window_nivel1.close()
        layouts('layout_menu_principal')

    # Se o arquivo for valido, as opções (Visualizar / Editar conteudo da lista / Criar arquivo / Atualizar respostas) serão liberadas

    elif valido is True:

        # Se a o opção for 'Visualizar'

        if event_nivel1 == 'Visualizar':

            # Fecha a janela do menu principal do programa e logo cria o seu layout novamente

            window_nivel1.close()

            layouts('layout_menu_principal')

            # Declarando variavel ou a rezetando

            dici = {}

            # Tratamento de erro, caso o usuario não selecionar nenhum item da lista

            try:

                # Verificando se algum item da lista foi selecionado

                pergunta = values_nivel1['pergunta'][0]

            except IndexError:

                # Caso não tiver seleção o programa irá mostrar uma mensagem de erro

                layout_msg_erro = [[sg.Text('Você deve selecionar uma pergunta para escolher essa opção!')],
                                   [sg.Button('Ok', key='ok')]]

                window_nivel2 = sg.Window('Erro - Piriiê v1.0', layout_msg_erro)
                event_nivel2, values_nivel2 = window_nivel2.read()

                if event_nivel2 in (None, 'ok'):
                    window_nivel2.close()

            # Se não ocorrer nenhum erro

            else:

                # Sistema para verificar os dados sobre a pergunta escolhida pelo usuario

                for c in range(len(tabela_xlsx['sua pergunta'])):

                    # Buscando a mesma pergunta no arquivo .xlsx, para trazer os dados sobre essa pergunta

                    if tabela_xlsx.loc[c]['sua pergunta'] == pergunta:

                        # Adicionando os dados no dicionario

                        for key in tabela_xlsx.keys():
                            dici[key] = tabela_xlsx.loc[c][key]

                        # Encerrando o sistema de repetição, ele não e mais necessario  :(

                        break

                # Criando layout para visualizar o conteudo da pergunta escolhida

                layout_visualizar_conteudo = [[sg.Multiline(f'\n- Sua pergunta - \n\n'
                                                            f'{dici["sua pergunta"]}\n\n'
                                                            f' - 1° Resposta - \n\n'
                                                            f'{dici["1 pergunta similar 1 resposta"]}\n\n'
                                                            f' - 2° Resposta - \n\n'
                                                            f'{dici["1 pergunta similar 2 resposta"]}\n\n'
                                                            f' - 3° Resposta - \n\n'
                                                            f'{dici["2 pergunta similar 1 resposta"]}\n\n'
                                                            f' - 4° Resposta - \n\n'
                                                            f'{dici["2 pergunta similar 2 resposta"]}',
                                                            size=(90, 25))], [sg.Button('Ok')]]

                # Se a pergunta for maior que 70 caracteres, irá ocorer um fatiamneto

                if len(dici["sua pergunta"]) > 70:

                    window_nivel2 = sg.Window(f'{dici["sua pergunta"][:70]}... - Piriiê v1.0',
                                              layout_visualizar_conteudo)

                # Se for menor ou igual a 70 caracteres, irá manter a pergunta original

                elif len(dici["sua pergunta"]) <= 70:
                    window_nivel2 = sg.Window(f'{dici["sua pergunta"]} - Piriiê v1.0', layout_visualizar_conteudo)

                # Abrindo e fechando a janela de visualização

                window_nivel2.read()
                window_nivel2.close()

        # Se a opção for 'editar_conteudo_lista'

        elif event_nivel1 == 'editar_conteudo_lista':

            # Fecha a janela do menu principal do programa e logo cria o seu layout novamente

            window_nivel1.close()
            layouts('layout_menu_principal')

            # Cria layout da proxima janela

            layouts('layout_menu_editar_conteudo_lista')

            # Sistema de repetição para receber respotas do usuario

            while True:

                # Recebendo informações do usuario e as mostrando no terminal (por enquanto)

                event_nivel2, values_nivel2 = window_nivel2.read()
                monstrar_resultados(2, event_nivel2, values_nivel2)

                # Se a resposta for None ou 'Cancelar', fechará a janela 'editar conteudo da lista'
                # e voltará a o menu principal

                if event_nivel2 in (None, 'Cancelar'):

                    # Fechando a janela e acabando com o sistema de repetição

                    window_nivel2.close()
                    break

                # Se a resposta for 'Visualizar'

                elif event_nivel2 == 'Visualizar':

                    # Fecha a janela do menu principal do programa e logo cria o seu layout novamente

                    window_nivel2.close()
                    layouts('layout_menu_editar_conteudo_lista')

                    # Criando ou rezetando variaveis

                    dici = {}

                    try:

                        # Verificando se algum item da lista foi selecionado

                        pergunta = values_nivel2['pergunta'][0]

                    except IndexError:

                        # Caso não tiver seleção o programa irá mostrar uma mensagem de erro

                        layout_msg_erro = [[sg.Text('Você deve selecionar uma pergunta para escolher essa opção!')],
                                           [sg.Button('Ok', key='ok')]]

                        window_nivel3 = sg.Window('Erro - Piriiê v1.0', layout_msg_erro)
                        window_nivel3.read()
                        window_nivel3.close()

                    # Se não ocorrer nenhum erro

                    else:

                        # Sistema para verificar os dados sobre a pergunta escolhida pelo usuario

                        for c in range(len(tabela_xlsx)):

                            # Buscando a mesma pergnta no arquivo .xlsx, para trazer os dados sobre essa pergunta

                            if tabela_xlsx.loc[c]['sua pergunta'] == pergunta:

                                # Adicionando os dados no dicionario

                                for key in tabela_xlsx.keys():
                                    dici[key] = tabela_xlsx.loc[c][key]

                                # Encerrando o sistema de repetição, ele não e mais necessario  :(

                                break

                        # Criando layout para visualizar o conteudo da pergunta escolhida

                        layout_visualizar_conteudo = [[sg.Multiline(f'\n- Sua pergunta - \n\n'
                                                                    f'{dici["sua pergunta"]}\n\n'
                                                                    f' - 1° Resposta - \n\n'
                                                                    f'{dici["1 pergunta similar 1 resposta"]}\n\n'
                                                                    f' - 2° Resposta - \n\n'
                                                                    f'{dici["1 pergunta similar 2 resposta"]}\n\n'
                                                                    f' - 3° Resposta - \n\n'
                                                                    f'{dici["2 pergunta similar 1 resposta"]}\n\n'
                                                                    f' - 4° Resposta - \n\n'
                                                                    f'{dici["2 pergunta similar 2 resposta"]}',
                                                                    size=(90, 25))], [sg.Button('Ok')]]

                        # Se a pergunta for maior que 70 caracteres, irá occorer um fatiamneto

                        if len(dici["sua pergunta"]) > 70:
                            window_nivel3 = sg.Window(f'{dici["sua pergunta"][:70]}... - Piriiê v1.0',
                                                      layout_visualizar_conteudo)

                        # Se for menor ou igual a 70 caracteres, irá manter a pergunta original

                        elif len(dici["sua pergunta"]) <= 70:
                            window_nivel3 = sg.Window(f'{dici["sua pergunta"]} - Piriiê v1.0',
                                                      layout_visualizar_conteudo)

                        # Abrindo e fechando a janela de visualização

                        window_nivel3.read()
                        window_nivel3.close()

                # Se a resposta for 'Adicionar pergunta'

                elif event_nivel2 == 'Adicionar pergunta':

                    # Fecha a janela editar conteudo da lita e logo cria o seu layout novamente

                    window_nivel2.close()
                    layouts('layout_menu_editar_conteudo_lista')

                    # Criando layout da janele adicionar pergunta

                    layout_adicionar_pergunta = [[sg.Input(key='adicionar_pergunta')],
                                                 [sg.Button('Adicionar'), sg.Button('Cancelar')]]

                    window_nivel3 = sg.Window('Adicionar pergunta - Piriiê v1.0', layout_adicionar_pergunta)

                    # Sistema de repetição para receber a resposta do usuario

                    while True:

                        # Criando janela e recebendo respostas do usuario e mostrando os resultados no terminal
                        # (por enquanto)

                        event_nivel3, values_nivel3 = window_nivel3.read()
                        monstrar_resultados(3, event_nivel3, values_nivel3)

                        # Se a resposta do usuario for None ou 'Cancelar'

                        if event_nivel3 in (None, 'Cancelar'):

                            # Irá fechar a janela e quebrar os istema de repetição
                            # (volta para a janela "aditar conteudo da lista")

                            window_nivel3.close()
                            break

                        # Se a resposta for 'Adicionar'

                        elif event_nivel3 == 'Adicionar':

                            # Criando ou rezetando variaveis

                            columns = []

                            # Adicionadno o nome das colunas na lista 'columns'

                            for key in tabela_xlsx.keys():
                                columns.append(key)

                            # Criando um DadaFrame e adicionadno as colunas (de acordo com as colunas do arquivo .xlsx)

                            # Obs: Estou usando o DataFrame pois não consegui somar ou subtrair linhas
                            # Diretamente no arquivo .xlsx, somente analizar e alterar o que ja existe

                            tabela = pd.DataFrame(columns=columns)

                            # Adicionando as linhas no DataFrame (de acordo com as linhas do arquivo .xlsx)

                            for linha in range(len(tabela_xlsx)):
                                tabela.loc[linha] = [tabela_xlsx.loc[linha][columns[0]]] + [
                                                        tabela_xlsx.loc[linha][columns[1]]] + [
                                                        tabela_xlsx.loc[linha][columns[2]]] + [
                                                        tabela_xlsx.loc[linha][columns[3]]] + [
                                                        tabela_xlsx.loc[linha][columns[4]]] + [
                                                        tabela_xlsx.loc[linha][columns[5]]] + [
                                                        tabela_xlsx.loc[linha][columns[6]]]

                            # Adiciondo sua pergunta na lista de perguntas

                            tabela.loc[len(tabela)] = [values_nivel3['adicionar_pergunta']] + [''] * 6

                            # Salvando dados do DataFrame no aruquivo .xlsx, ou melhor,
                            # Substituindo o arquivo existente com a nova pergunta

                            tabela.to_excel(local)

                            # Fechando a janela "Adicionar perguntas"

                            window_nivel3.close()

                            # Criando ou rezetadno variaveis

                            lista_perguntas = []

                            # Abrindo arquivo .xlsx

                            tabela_xlsx = pd.read_excel(local)

                            # Apagando tabela 'Unnamed: 0', pois ela e sempre criada quando salvamos nosso arquivo .xlsx

                            if 'Unnamed: 0' in tabela_xlsx:
                                tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

                            # Adicionando a suas perguntas a lista 'lista_perguntas'
                            # Isso para atualizar a lista dos layouts

                            for c in tabela_xlsx['sua pergunta']:
                                lista_perguntas.append(c)

                            # Criando Layouts e fechando janelas

                            layout_menu_editar_conteudo_lista = [
                                [sg.Button('Adicionar pergunta'), sg.Button('Editar pergunta / conteudo'),
                                 sg.Button('Deletar pergunta / conteudo')],
                                [sg.Listbox(lista_perguntas, key='pergunta', size=(68, 5))],
                                [sg.Button('Visualizar'), sg.Button('Cancelar')]]

                            layouts('layout_menu_principal')

                            window_nivel2.close()

                            window_nivel2 = sg.Window('Editar conteudo da lista - Piriiê v1.0',
                                                      layout_menu_editar_conteudo_lista)

                # Se a resposta for 'Deletar pergunta / conteudo'

                elif event_nivel2 == 'Deletar pergunta / conteudo':

                    # Fechando janela 'Editar conteudo da lista' e criando seu layout

                    window_nivel2.close()
                    layouts('layout_menu_editar_conteudo_lista')

                    try:

                        # Verificando se algum item da lista foi selecionado

                        pergunta = values_nivel2['pergunta'][0]

                    except IndexError:

                        # Caso não tiver selecionado o programa irá mostrar uma mensagem de erro

                        layout_msg_erro = [[sg.Text('Você deve selecionar uma pergunta para escolher essa opção!')],
                                           [sg.Button('Ok', key='ok')]]

                        window_nivel3 = sg.Window('Erro - Piriiê v1.0', layout_msg_erro)
                        window_nivel3.read()
                        window_nivel3.close()

                    # Se não ocorrer nenhum erro

                    else:

                        # Se a pergunta tiver mais de 35 caracteres, irá ocorrer um fatiamento até 35 caracteres

                        if len(pergunta) >= 35:

                            # Cria layout para a janela "Deletar pergunta"

                            layout_adicionar_pergunta = [[sg.Text(f'Deletar pergunta / conteudo da pergunta:\n'
                                                                  f'{pergunta[:35]} ...')],
                                                         [sg.Button('Sim'), sg.Button('Não')]]

                        # Se tiver menos de 35 caracteres, irá manter a pergunta original

                        else:

                            # Cria layout para a janela "Deletar pergunta"

                            layout_adicionar_pergunta = [[sg.Text(f'Deletar pergunta / conteudo da pergunta:\n'
                                                                  f'{pergunta}')],
                                                         [sg.Button('Sim'), sg.Button('Não')]]

                        # Cria janela "Deletar perguntas"

                        window_nivel3 = sg.Window('Deletar pergunta - Piriiê v1.0', layout_adicionar_pergunta)

                        # Sistema de repetição para receber respostas do usuario

                        while True:

                            # Recebendo valores do usuario e as escrevendo no terminal (por enquanto)

                            event_nivel3, values_nivel3 = window_nivel3.read()
                            monstrar_resultados(3, event_nivel3, values_nivel3)

                            # Se a resposta for None ou 'Não'

                            if event_nivel3 in (None, 'Não'):

                                # Fecha a janela 'Deletar pergunta' e retornarar a janela "Editar conteudo da lista"
                                # E terminarar o sistema de repetição

                                window_nivel3.close()
                                break

                            # Se a resposta for 'Sim'

                            elif event_nivel3 == 'Sim':

                                # Irá abrir o arquivo .xlsx

                                tabela_xlsx = pd.read_excel(local)

                                # Apagando tabela 'Unnamed: 0', pois ela e sempre criada quando salvamos o arquivo .xlsx

                                if 'Unnamed: 0' in tabela_xlsx:
                                    tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

                                # Criando ou rezetando variaveis

                                columns = []

                                # Adicioando a 'columns' o nome das colunas do arquivo .xlsx

                                for key in tabela_xlsx.keys():
                                    columns.append(key)

                                # Criando um DataFrame com o nome das colunas do arquivo .xlsx

                                tabela = pd.DataFrame(columns=columns)

                                # Adicioando linhas do arquivo .xlsx no DataFrame
                                # Tendo assim uma copia identica do arquivo .xlsx
                                # Porém agora posso adicionar ou apagar linhas

                                for linha in range(len(tabela_xlsx)):
                                    tabela.loc[linha] = [tabela_xlsx.loc[linha][columns[0]]] + [
                                        tabela_xlsx.loc[linha][columns[1]]] + [tabela_xlsx.loc[linha][columns[2]]] + [
                                                            tabela_xlsx.loc[linha][columns[3]]] + [
                                                            tabela_xlsx.loc[linha][columns[4]]] + [
                                                            tabela_xlsx.loc[linha][columns[5]]] + [
                                                            tabela_xlsx.loc[linha][columns[6]]]

                                # Sistema para apagar a pergunta escolhida

                                for linha in range(len(tabela['sua pergunta'])):

                                    # Se 'sua pergunda' da linha atual for igual a pergunta que o usuario deseja apagar

                                    if tabela.loc[linha]['sua pergunta'] == pergunta:

                                        # Apaga a linha e encerra o sistema de repetição

                                        tabela = tabela.drop(linha)

                                        break

                                # Substitui o arquivo antigo pelo novo (com a pergunta excluida)

                                tabela.to_excel(local)

                                # Fecha a janela "Deletar pergunta"

                                window_nivel3.close()

                                # Criando ou rezetando variaveis

                                lista_perguntas = []

                                # Abrindo o arquivo .xlsx

                                tabela_xlsx = pd.read_excel(local)

                                # Apagando tabela 'Unnamed: 0', pois ela e sempre criada quando salvamos o arquivo .xlsx

                                if 'Unnamed: 0' in tabela_xlsx:
                                    tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

                                # Adicioando as perguntas do arquivo .xlsx na lista 'lista_perguntas'
                                # Isso para atualizar a lista dos layouts

                                for c in tabela_xlsx['sua pergunta']:
                                    lista_perguntas.append(c)

                                # Criando Layouts e fechando janelas

                                layout_menu_editar_conteudo_lista = [
                                    [sg.Button('Adicionar pergunta'), sg.Button('Editar pergunta / conteudo'),
                                     sg.Button('Deletar pergunta / conteudo')],
                                    [sg.Listbox(lista_perguntas, key='pergunta', size=(68, 5))],
                                    [sg.Button('Visualizar'), sg.Button('Cancelar')]]

                                layouts('layout_menu_principal')

                                window_nivel2.close()

                                window_nivel2 = sg.Window('Editar conteudo da lista - Piriiê v1.0',
                                                          layout_menu_editar_conteudo_lista)

                # Se a resposta for 'Editar pergunta / conteudo'

                elif event_nivel2 == 'Editar pergunta / conteudo':
                    
                    # Criando ou rezetadno variaveis

                    dici = {}

                    # Fechando janela 'Editar conteudo da lista' e criando seu layout

                    window_nivel2.close()
                    layouts('layout_menu_editar_conteudo_lista')

                    try:

                        # Verificando se algum item da lista foi selecionado

                        pergunta = values_nivel2['pergunta'][0]
                        pergunta_original = values_nivel2['pergunta'][0]

                    except IndexError:

                        # Caso não tiver selecionado o programa irá mostrar uma mensagem de erro

                        layout_msg_erro = [[sg.Text('Você deve selecionar uma pergunta para escolher essa opção!')],
                                           [sg.Button('Ok', key='ok')]]

                        window_nivel3 = sg.Window('Erro - Piriiê v1.0', layout_msg_erro)
                        window_nivel3.read()
                        window_nivel3.close()

                    # Se não ocorrer nenhum erro

                    else:

                        # Sistema para verificar os dados sobre a pergunta escolhida pelo usuario

                        for c in range(len(tabela_xlsx)):

                            # Buscando a mesma pergnta no arquivo .xlsx, para trazer os dados sobre essa pergunta

                            if tabela_xlsx.loc[c]['sua pergunta'] == pergunta:

                                # Adicionando os dados no dicionario

                                for key in tabela_xlsx.keys():
                                    dici[key] = tabela_xlsx.loc[c][key]

                                # Encerrando o sistema de repetição, ele não e mais necessario  :(

                                break
                        
                        layout_editar_conteudo = [[sg.Text('Sua pergunta')],
                            [sg.Multiline(dici['sua pergunta'], key='sua pergunta', size=(104, 2))],
                            [sg.Text('1° Pergunta similar'), sg.Text(f'{" " * 65}2° Pergunta similar')],
                            [sg.Multiline(dici['1 pergunta similar'], key='1 pergunta similar', size=(50, 2)),
                            sg.Multiline(dici['2 pergunta similar'], key='2 pergunta similar', size=(50, 2))],
                            [sg.Text('1° Resposta similar'), sg.Text(f'{" " * 64}1° Resposta similar')],
                            [sg.Multiline(dici['1 pergunta similar 1 resposta'], key='1 pergunta similar 1 resposta', size=(50, 5)),
                            sg.Multiline(dici['2 pergunta similar 1 resposta'], key='2 pergunta similar 1 resposta', size=(50, 5))],
                            [sg.Text('2° Resposta similar'), sg.Text(f'{" " * 64}2° Resposta similar')],
                            [sg.Multiline(dici['1 pergunta similar 2 resposta'], key='1 pergunta similar 2 resposta', size=(50, 5)),
                            sg.Multiline(dici['2 pergunta similar 2 resposta'], key='2 pergunta similar 2 resposta', size=(50, 5))],
                            [sg.Button('Salvar'), sg.Button('Cancelar')]]

                        # Se a pergunta for maior que 70 caracteres, irá occorer um fatiamneto

                        if len(dici["sua pergunta"]) > 70:
                            window_nivel3 = sg.Window(f'{dici["sua pergunta"][:70]}... - Piriiê v1.0',
                                                      layout_editar_conteudo)

                        # Se for menor ou igual a 70 caracteres, irá manter a pergunta original

                        elif len(dici["sua pergunta"]) <= 70:
                            window_nivel3 = sg.Window(f'{dici["sua pergunta"]} - Piriiê v1.0',
                                                      layout_editar_conteudo)

                        while True:

                            # Recebendo informações do usuario e as mostrando no terminal (por enquanto)

                            event_nivel3, values_nivel3 = window_nivel3.read()
                            monstrar_resultados(3, event_nivel3, values_nivel3)

                            # Se a resposta for None ou 'Cancelar', fechará a janela 'Editar pergunta / conteudo' e voltará a a janela 'Editar conteudo da lista'

                            if event_nivel3 in (None, 'Cancelar'):

                                # Fechando a janela e acabando com o sistema de repetição

                                window_nivel3.close()
                                break

                            elif event_nivel3 == 'Salvar':

                                layout_msg_confirmação = [[sg.Text('Deseja salvar as alterações?')],
                                                          [sg.Button('Sim'), sg.Button('Não')]]

                                window_nivel4 = sg.Window('Confirmar', layout_msg_confirmação)

                                event_nivel4, values_nivel4 = window_nivel4.read()

                                if event_nivel4 in (None, 'Não'):

                                    window_nivel4.close()

                                if event_nivel4 == 'Sim':

                                    window_nivel4.close()

                                    # Criando ou rezetando variaveis

                                    pergunta = values_nivel3['sua pergunta']

                                    # Irá abrir o arquivo .xlsx

                                    tabela_xlsx = pd.read_excel(local)

                                    # Apagando tabela 'Unnamed: 0', pois ela e sempre criada quando salvamos o arquivo .xlsx

                                    if 'Unnamed: 0' in tabela_xlsx:
                                        tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

                                    # Criando ou rezetando variaveis

                                    columns = []

                                    # Adicioando a 'columns' o nome das colunas do arquivo .xlsx

                                    for key in tabela_xlsx.keys():
                                        columns.append(key)

                                    # Criando um DataFrame com o nome das colunas do arquivo .xlsx

                                    tabela = pd.DataFrame(columns=columns)

                                    # Adicioando linhas do arquivo .xlsx no DataFrame
                                    # Tendo assim uma copia identica do arquivo .xlsx
                                    # Porém agora posso adicionar ou apagar linhas

                                    for linha in range(len(tabela_xlsx)):
                                        tabela.loc[linha] = [tabela_xlsx.loc[linha][columns[0]]] + [
                                                                tabela_xlsx.loc[linha][columns[1]]] + [
                                                                tabela_xlsx.loc[linha][columns[2]]] + [
                                                                tabela_xlsx.loc[linha][columns[3]]] + [
                                                                tabela_xlsx.loc[linha][columns[4]]] + [
                                                                tabela_xlsx.loc[linha][columns[5]]] + [
                                                                tabela_xlsx.loc[linha][columns[6]]]

                                    for linha in range(len(tabela_xlsx)):

                                        if tabela.loc[linha]['sua pergunta'] == pergunta_original:

                                            for key in range(len(tabela.keys())):

                                                tirar_quebra_linha = values_nivel3[columns[key]]
                                                tirar_quebra_linha = tirar_quebra_linha[::-1].replace('\n', '', 1)
                                                tirar_quebra_linha = tirar_quebra_linha[::-1]

                                                tabela.loc[linha][columns[key]] = tirar_quebra_linha

                                            tabela.to_excel(local)
                                            
                                            # Criando ou rezetando variaveis

                                            lista_perguntas = []

                                            # Abrindo o arquivo .xlsx

                                            tabela_xlsx = pd.read_excel(local)

                                            # Apagando tabela 'Unnamed: 0', pois ela e sempre criada quando salvamos o arquivo .xlsx

                                            if 'Unnamed: 0' in tabela_xlsx:
                                                tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

                                            # Adicioando as perguntas do arquivo .xlsx na lista 'lista_perguntas'
                                            # Isso para atualizar a lista dos layouts

                                            for c in tabela_xlsx['sua pergunta']:
                                                lista_perguntas.append(c)

                                            window_nivel3.close()

                                            layouts('layout_menu_principal')

                                            layout_menu_editar_conteudo_lista = [
                                        [sg.Button('Adicionar pergunta'), sg.Button('Editar pergunta / conteudo'),
                                        sg.Button('Deletar pergunta / conteudo')],
                                        [sg.Listbox(lista_perguntas, key='pergunta', size=(68, 5))],
                                        [sg.Button('Visualizar'), sg.Button('Cancelar')]]

                                            window_nivel2.close()

                                            window_nivel2 = sg.Window('Editar conteudo da lista - Piriiê v1.0',layout_menu_editar_conteudo_lista)

        # Se a opção for 'Atualizar respostas'

        elif event_nivel1 == 'Atualizar respostas':  

            # Fecha a janela do menu principal do programa e logo cria o seu layout novamente

            window_nivel1.close()
            layouts('layout_menu_principal')

            # Cria layout da proxima janela

            layouts('layout_atualizar_respostas')

            # Sistema de repetição para receber respotas do usuario

            while True:

                # Recebendo informações do usuario e as mostrando no terminal (por enquanto)

                event_nivel2, values_nivel2 = window_nivel2.read()
                monstrar_resultados(2, event_nivel2, values_nivel2)

                if event_nivel2 in (None, 'Cancelar'):

                    # Fechando a janela e acabando com o sistema de repetição

                    window_nivel2.close()
                    break

                elif event_nivel2 == 'Ok':

                    # Irá abrir o arquivo .xlsx

                    tabela_xlsx = pd.read_excel(local)

                    # Apagando tabela 'Unnamed: 0', pois ela e sempre criada quando salvamos o arquivo .xlsx

                    if 'Unnamed: 0' in tabela_xlsx:
                        tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

                    # Criando ou rezetando variaveis

                    columns = []

                    # Adicioando a 'columns' o nome das colunas do arquivo .xlsx

                    for key in tabela_xlsx.keys():
                        columns.append(key)

                    # Criando um DataFrame com o nome das colunas do arquivo .xlsx

                    tabela = pd.DataFrame(columns=columns)

                    # Adicioando linhas do arquivo .xlsx no DataFrame
                    # Tendo assim uma copia identica do arquivo .xlsx
                    # Porém agora posso adicionar ou apagar linhas

                    for linha in range(len(tabela_xlsx)):
                        tabela.loc[linha] = [tabela_xlsx.loc[linha][columns[0]]] + [
                            tabela_xlsx.loc[linha][columns[1]]] + [tabela_xlsx.loc[linha][columns[2]]] + [
                                                tabela_xlsx.loc[linha][columns[3]]] + [
                                                tabela_xlsx.loc[linha][columns[4]]] + [
                                                tabela_xlsx.loc[linha][columns[5]]] + [
                                                tabela_xlsx.loc[linha][columns[6]]]

                    opc = Options()
                    opc.headless = True
                    driver = webdriver.Firefox(options=opc)

                    if values_nivel2['atualizar_tudo'] is True:
                        print('atualizar_tudo')
                        

                    elif values_nivel2['atualizar_o_necessario'] is True:
                        print('atualizar_o_necessario')

                    elif values_nivel2['atualizacao_personalizada'] is  True:
                        print('atualizacao_personalizada')

                    print(tabela)


                #elif: event_nivel2

    # Se o arquivo não for valido, irá mostrar uma mensagem de erro

    else:

        # Com exceção da opção 'atualizar'

        if event_nivel1 != 'atualizar':

            # Mensagem de erro, abrir e fachar a janela, criar layout

            layout_msg_erro = [
                [sg.Text('Você deve escolher um arquivo .xlsx (Dentro dos padrões)\npara escolher essa opção!')],
                [sg.Button('Ok', key='ok')]]

            window_nivel2 = sg.Window('Erro - Piriiê v1.0', layout_msg_erro)

            window_nivel2.read()
            window_nivel2.close()

            