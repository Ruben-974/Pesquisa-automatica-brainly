
from amparos.dados import *
from amparos.layouts import *

# Executar quando o botão "Atualizar" for chamado

def BotaoAtualizar(local):

    """
    Parameters:

        local: Informe o local do arquivo .xlsx

    Returns:

        return True, CriarListaPerguntas(local):

            True: Retorna verdadeiro pois o arquivo .xlsx e valido

            CriarListaPerguntas(local): Como a o arquivo e valido, o programa irá pegar os as perguntas do arquivo


        return False, []:

            False: Retorna falso pois o arquivo .xlsx e invalido

            []: Como o arquivo e invalido, o programa irá retornar uma lista vazia
    
    """

    valido = VerificarXlsx(local) # Verifica se o arquico .xlsx e um arquivo valido

    if valido is True: # Se for valido retorna a lista com as perguntas
        
        return True, CriarListaPerguntas(local) 

    else: # Se não retorna uma mensagem de erro e uma lista vazia 

        Mensagem_Erro(valido) 

        return False, [] 

# Executar quando o botão "Visualizar" for chamado

def BotaoVisualizar(pergunta, local):

    '''
    Parameters:

        pergunta: Pergunta que você deseja analisar o conteudo 

        local: Local do arquivo .xlsx (Valido)

    '''

    if pergunta == []: # Se o ususario não selecionou nenhuma pergunta

        Mensagem_Erro('Escolha uma pergunta antes de selecionar essa opção!') # Mensagem de erro

    else:

        conteudo = DicionarioComConteudo(pergunta=pergunta[0], local=local)

        Visualizar_Conteudo(conteudo)

# Executar quando o botão "Editar Lista" for chamado

def BotaoEditarLista(lista, local):

    window = Editar_Lista(lista)

    while True:

        event, values = window.read()

        pergunta = values['pergunta']

        if event in (None, 'Cancelar'):

            window.close()

            return lista

        if event == 'Visualizar':

            window.close()

            BotaoVisualizar(pergunta=pergunta, local=local) # Cria interfase para visualizar o conteudo

            window = Editar_Lista(lista)

        if event == 'Adicionar pergunta':

            window.close()

            lista = BotaoAddPergunta(lista=lista, local=local)

            window = Editar_Lista(lista)

        if event == 'Deletar pergunta / conteudo':

            window.close()

            lista = BotaoDellPergCont(pergunta=pergunta, local=local, lista=lista)

            window = Editar_Lista(lista)
        
        if event == 'Editar pergunta / conteudo':

            window.close()

            lista = BotaoEditPergCont(pergunta=pergunta, local=local, lista=lista)

            window = Editar_Lista(lista)

# Executar quando o botão "Adicionar pergunta" for chamado

def BotaoAddPergunta(lista, local):

    """
    Parameters:

        local: Local do arquivo .xlsx (Valido)

    Returns:

        return CriarListaPerguntas(local): Retorna a lista de perguntas atualizada com a nova pergunta adicionada

    """

    # Abrindo a janela e recebendo valores

    window = Recebe_Pergunta()

    while True:

        event, values = window.read()

        Resultados_Terminal(event=event, values=values)

        if event in ('Cancelar', None): # Cancela a janela

            window.close()

            return lista

        if event == 'Adicionar':

            if values['adicionar_pergunta'] == '': # Não e possival adicionar uma pergunta vazia

                window.close()

                Mensagem_Erro('Você deve digitar uma pergunta') # Mesagem de erro

                window = Recebe_Pergunta()

            else:

                window.close()

                AdicionarPerguntaLista(pergunta=values['adicionar_pergunta'], local=local) # Add pergunta na lista

                return CriarListaPerguntas(local)

# Executar quando o botão "Deletar pergunta / conteudo" for chamado

def BotaoDellPergCont(pergunta, lista, local):

    '''
    Parameters:

        pergunta: pergunta (e conteudo) que o ususario deseja apagar da lista de pergunta

        local: local do arquivo .xlsx (valido)

    Returns:

        return CriarListaPerguntas(local): Retorna uma lista atualizada com a pergunta deletada
    '''

    if pergunta == []: # Verifica se alguma pergunta foi selecionada

        Mensagem_Erro('Escolha uma pergunta da lista para deletar')

        return lista

    else:

        # Cria uma janela esprando a resposta do ususario Sim ou não (ou None)

        window = Janela_deletar(pergunta[0])

        while True:

            event, values = window.read()

            if event in ('Não', None):

                window.close() # Fecha a janela

                return lista

            if event == 'Sim': # Deleta a pergunta desejada
                
                window.close()

                DeletarPergunta(pergunta=pergunta[0], local=local)

                return CriarListaPerguntas(local)
    
# Executar quando o botão "Editar pergunta / conteudo" for chamado

def BotaoEditPergCont(pergunta, local, lista):

    if pergunta == []: # Caso o usuario não selecione uma pergunta

        Mensagem_Erro('Escolha uma pergunta da lista para editar')

        return lista

    else:

        conteudo_atual = DicionarioComConteudo(pergunta[0], local)

        window = Menu_Editar(conteudo=conteudo_atual, pergunta=pergunta[0])

        while True:

            # Cria um janela mostrando o conteudo original

            event, conteudo_alterado = window.read()

            # Cancela as alterações

            if event in ('Cancelar', None):

                window.close()

                return lista

            if event == 'Salvar':

                window.close()

                # Confirma as alterações

                window = Confirmar_Alterações()

                event, values = window.read()

                if event == 'Sim':

                    window.close()

                    # Salva as alterações

                    SalvarConteudo(conteudo=conteudo_alterado, local=local, pergunta=pergunta[0])

                    # Retorna uma lista atualizada pois o usuario pode alterar a pergunta que esta na lista

                    return CriarListaPerguntas(local)

                if event == 'Não':

                    window.close()

                    window = Menu_Editar(conteudo=conteudo_alterado, pergunta=pergunta[0])

