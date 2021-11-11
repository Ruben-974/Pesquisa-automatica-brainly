
from time import sleep


from time import sleep

def Pesquisa_Sem_Driver(pergunta, primeira_res=(True, True), segunda_res=(True, True)):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    from googlesearch import search

    links = []

    respostas = {'sua pergunta': pergunta,
                '1 pergunta similar': '',
                '1 pergunta similar 1 resposta': '',
                '1 pergunta similar 2 resposta': '',
                '2 pergunta similar': '',
                '2 pergunta similar 1 resposta': '',
                '2 pergunta similar 2 resposta': ''}

    quest = respostas['sua pergunta'] + ' site:brainly.com.br'

    for l in search(quest, tld='co.in', num=2, stop=2, pause=10, user_agent='Mozilla/5.0'):

        links.append(l)

    if True not in segunda_res:

        del links[1]

    if True not in primeira_res:

        del links[0]

    print(links)

    if links != []:

        for c in range(len(links)):

            sleep(5)

            html = Request(links[c], headers={'User-Agent': 'Mozilla/5.0'})

            html = urlopen(html).read()

            html = BeautifulSoup(html, 'html.parser')

            resp = html.findAll('div', {'class': 'brn-qpage-next-answer-box__content'})

            perg = html.find('span', {'class': 'sg-text sg-text--large sg-text--bold sg-text--break-words brn-qpage-next-question-box-content__primary'})

            respostas[f'{c+1} pergunta similar'] = perg.get_text()

            for c2 in range(len(resp)):
                
                for c3 in resp[c2].find_all('p'):

                    respostas[f'{c+1} pergunta similar {c2+1} resposta'] += c3.get_text() + '\n'

                respostas[f'{c+1} pergunta similar {c2+1} resposta'] = respostas[f'{c+1} pergunta similar {c2+1} resposta'].strip()

            if respostas[f'{c+1} pergunta similar 1 resposta'] == '':
                
                respostas[f'{c+1} pergunta similar 1 resposta'] = resp[0].get_text().strip()

            if respostas[f'{c+1} pergunta similar 2 resposta'] == '':

                respostas[f'{c+1} pergunta similar 2 resposta'] = resp[1].get_text().strip()

        if primeira_res[0] == False:

            respostas['1 pergunta similar 1 resposta'] = ''

        if primeira_res[1] == False:

            respostas['1 pergunta similar 2 resposta'] = ''

        if segunda_res[0] == False:

            respostas['2 pergunta similar 1 resposta'] = ''

        if segunda_res[1] == False:

            respostas['2 pergunta similar 2 resposta'] = ''

        return respostas


respostas = Pesquisa_Sem_Driver(pergunta='Qual a formula da agua?', primeira_res=(True, True), segunda_res=(True, True))
        
for k, v in respostas.items():

    print(f'\033[1;32mChave:\033[m {k}\n\033[1;32mItem:\033[m {v[0:50]}\n')

