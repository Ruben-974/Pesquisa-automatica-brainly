
import pandas as pd

# Verifica se o arquico .xlsx e um arquivo valido

def VerificarXlsx(local):

    """
    Parameters:
    
        local: Arquivo .xlsx para ser analisado

    Returns:

        return 'ERRO: Caminho ou arquvio invalido': Mensagem

        return 'ERRO: Arquivo inadequado': Mensagem

        return 'ERRO: Arquivo .xlsx e fora dos padrões': Mensagem

        return True: Se o caminho e o arquivo estiver correto
    
    """

    conter_na_tabela = ['sua pergunta', '1 pergunta similar', '1 pergunta similar 1 resposta', '1 pergunta similar 2 resposta', '2 pergunta similar', '2 pergunta similar 1 resposta', '2 pergunta similar 2 resposta']

    contem = 0

    try:

        tabela = pd.read_excel(local)

    except FileNotFoundError:

        return 'ERRO: Caminho ou arquivo invalido'

    except ValueError:

        return 'ERRO: Arquivo inadequado'

    # Deletar a coluna 'Unnamed: 0' ela e sempre crianda quando abrimos um arquivo .xlsx

    if 'Unnamed: 0' in tabela:
        tabela.drop('Unnamed: 0', axis=1, inplace=True)

    # Verifiando se há as colunas necessarias

    for c in conter_na_tabela:
        if c in tabela.keys():
            contem += 1
        else:
            return 'ERRO: Arquivo .xlsx e fora dos padrões'

        # Se o arquivo tiver as colunas necessarias

        if contem == len(conter_na_tabela):
            return True

# Cria uma lista com as pergunta do arquivo .xlsx

def CriarListaPerguntas(local_xlsx):

    """
    Parameters:

        local_xlsx: Local do arquivo .xlsx dentro dos padrões

    Returns:

        return lista_perguntas: Lista com todas as perguntas do arquivo .xlxs

    """

    lista_perguntas = []

    tabela_xlsx = pd.read_excel(local_xlsx)

    # Deletar col 'Unnamed: 0' ela e sempre crianda quando abrimos um arquivo .xlsx

    if 'Unnamed: 0' in tabela_xlsx:
        tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

    # Cria uma lista com as perguntas da tabela em .xlsx

    for c in tabela_xlsx['sua pergunta']:
        lista_perguntas.append(c)
    
    return lista_perguntas

# Analisando conteudo sobre a pergunta desejada

def DicionarioComConteudo(pergunta, local):

    """
    Parameters:

        pergunta: Será buscada no arquivo .xlsx e retornará suas respostas correspondente

        local: Local do arquivo .xlsx para buscar sobre a sua pergunta

    Returns:

        conteudo: Retorna um dicionario espesifico com o conteudo sobre a sua pergunta
    """

    conteudo, tabela_xlsx = {}, pd.read_excel(local)

    if 'Unnamed: 0' in tabela_xlsx:

        tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

    # Buscando a sua pergunta no arquivo .xlsx, para trazer os dados sobre

    for c in range(len(tabela_xlsx['sua pergunta'])): 

        if tabela_xlsx.loc[c]['sua pergunta'] == pergunta: # Buscando a sua pergunta dentre as outras

            # Adicionando os dados no dicionario

            for key in tabela_xlsx.keys():

                conteudo[key] = tabela_xlsx.loc[c][key] 

            return conteudo
