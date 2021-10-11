from amparos.botoes import BotaoAtualizar
from amparos.layouts import Menu_Principal

lista_perguntas, local = [], ''

window = Menu_Principal(local=local, lista=lista_perguntas) # Criando janela principal do programa

while True:

    event, values = window.read() # Abrindo a janela principal, para receber valores do usuario

    print(f'{event}\n{values}')

    if event in ('Sair', None): # O programa será finalizado por completo

        window.close()

        break

    if event == 'Atualizar': # Programa será atualizado de acordo com as informações do usuario

        local = values['local']

        window.close()

        lista_perguntas = BotaoAtualizar(local) # Recebendo lista de perguntas do arquivo .xlsx

        window = Menu_Principal(local=local, lista=lista_perguntas) # Criando janela principal do programa

