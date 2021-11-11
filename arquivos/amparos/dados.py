
from numpy import NaN, nan
import pandas as pd

from amparos.pesquisa import Pesquisa_Sem_Driver, Pesquisa_Com_Driver

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
            return 'ERRO: Arquivo .xlsx fora dos padrões'

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

# Cria DataFrame da tebala .xlsx

def CriarDataFrame(local):

    colunas, linhas = [], []

    # Criando tabela_xlsx e tirando a coluna 'Unnamed: 0'

    tabela_xlsx = pd.read_excel(local)

    if 'Unnamed: 0' in tabela_xlsx:

        tabela_xlsx.drop('Unnamed: 0', axis=1, inplace=True)

    # Buscando o nome das colunas no arquivo .xlsx

    for coluna in tabela_xlsx.keys():
        colunas.append(coluna)

    # Adicionando colunas em um DataFrame
    
    tabela = pd.DataFrame(columns=colunas)

    # Adicionado as linhas no Dataframe 

    for linha in range(len(tabela_xlsx)):
        for coluna in colunas:
            linhas.append(tabela_xlsx.loc[linha][coluna])

        tabela.loc[linha] = linhas
        linhas = []
    
    return tabela

# Adiciona a nova pergunta desejada

def AdicionarPerguntaLista(pergunta, local):

    """
    Parameters:

        pergunta: Recebe a pergunta que você deseja adicionar na lista de perguntas

        local: Recebe o local do arquivo .xlsx (valido)
    
    """

    tabela = CriarDataFrame(local=local)
    
    # Adiciondo sua pergunta na tabela
 
    tabela.loc[len(tabela)] = [pergunta] + [''] * 6

    # Salvando a tabela como arquivo original (Com as informações anteriores e com a pergunta recem adicionada)

    tabela.to_excel(local)

# Deleta a pergunta e o conteudo desejado

def DeletarPergunta(pergunta, local):

    """
    Parameters:

        pergunta: Recebe a pergunta que você deseja apadar da lista de perguntas

        local: Recebe o local do arquivo .xlsx (valido)
    
    """

    tabela = CriarDataFrame(local)

    for linha in range(len(tabela['sua pergunta'])):

        # Se 'sua pergunda' da linha atual for igual a pergunta que o usuario deseja apagar

        if tabela.loc[linha]['sua pergunta'] == pergunta:

            # Apaga a linha e encerra o sistema de repetição e salva isso no arquivo .xlsx

            tabela = tabela.drop(linha)

            tabela.to_excel(local)

            break
    
# Salva o conteudo alterado no menu de edição

def SalvarConteudo(conteudo, local, pergunta):
    
    '''
    Parameters: 

        conteudo: Dicionario com as alterações

        local: local do arquivo .xlsx (Valido)

        pergunta: Pergunta que o ususario deseja alterar

    '''

    tabela = CriarDataFrame(local=local)

    for linha in range(len(tabela)):

        # Busca a sua pergunta na tabela e altera o conteudo

        if tabela.loc[linha]['sua pergunta'] == pergunta:
            
            for key in tabela.loc[linha].keys():
                
                tabela.loc[linha][key] = conteudo[key]

            # Salva a tabela alterada

            tabela.to_excel(local)

            break
    
def PerguntaParaAtualizar(pergunta, local, atualizar='tudo'):

    conteudo = DicionarioComConteudo(pergunta=pergunta, local=local)

    if atualizar == 'tudo':

        conteudo = Pesquisa_Com_Driver(pergunta=conteudo['sua pergunta'])

        print(conteudo, '\n\n')
    
    if atualizar == 'necessario':

        sem_resp = []
        result = []
        verificar = ['1 pergunta similar 1 resposta', '1 pergunta similar 2 resposta', 
                     '2 pergunta similar 1 resposta', '2 pergunta similar 2 resposta']

        for k, v in conteudo.items():

            if type(v) != str:

                sem_resp.append(k)

        for i in range(len(verificar)):

            if verificar[i] in sem_resp:

                result.append(True)

            else:

                result.append(False)

        new_conteudo = Pesquisa_Com_Driver(pergunta=conteudo['sua pergunta'], primeira_res=(result[0], result[1]), segunda_res=(result[2], result[3]))

        for k, v in new_conteudo.copy().items():

            if v != '':

                conteudo[k] = v

    SalvarConteudo(conteudo=conteudo, local=local, pergunta=pergunta)
        
        
