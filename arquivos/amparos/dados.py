import pandas as pd


def VerificarXlsx(local):

    conter_na_tabela = ['sua pergunta', '1 pergunta similar', '1 pergunta similar 1 resposta', '1 pergunta similar 2 resposta', '2 pergunta similar', '2 pergunta similar 1 resposta', '2 pergunta similar 2 resposta']
    contem = 0

    try:
        tabela = pd.read_excel(local)
    except FileNotFoundError:
        return 'ERRO: Caminho ou arquvio invalido'
    except ValueError:
        return 'ERRO: Arquivo inadequado'

    if 'Unnamed: 0' in tabela:
        tabela.drop('Unnamed: 0', axis=1, inplace=True)
    for c in conter_na_tabela:
        if c in tabela.keys():
            contem += 1
        else:
            return 'ERRO: Arquivo .xlsx fora dos padrões impostos pela sociedade :('
        if contem == len(conter_na_tabela):
            return True


def CriarListaPerguntas(local_xlsx):

    lista_perguntas = []

    tabela_xlsx = pd.read_excel(local_xlsx)

    # Deletar a coluna 'Unnamed: 0' ela pode atrapalhar na resolução das tarefas

    if 'Unnamed: 0' in tabela_xlsx:
        tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

    # Cria uma lista com as perguntas da tabela em .xlsx

    for c in tabela_xlsx['sua pergunta']:
        lista_perguntas.append(c)
    
    return lista_perguntas

