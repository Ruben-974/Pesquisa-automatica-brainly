from amparos.botoes import BotaoAtualizar
from amparos.layouts import Menu_Principal

lista_perguntas, local = [], ''

window = Menu_Principal(local=local, lista_perguntas=lista_perguntas)

while True:

    event_nivel1, values_nivel1 = window.read()

    print(f'{event_nivel1}\n{values_nivel1}')

    if event_nivel1 in ('Sair', None):

        window.close()

        break

    if event_nivel1 == 'Atualizar':

        local = values_nivel1['local']

        window.close()

        lista_perguntas = BotaoAtualizar(local)

        window = Menu_Principal(local=local, lista_perguntas=lista_perguntas)

