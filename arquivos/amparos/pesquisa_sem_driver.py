
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from googlesearch import search
from time import sleep

pergunta = 'resumo segunda guerra mundial'
primeira_res = (True, False)
segunda_res = (False, False)

links = []

inc, fim = 0, 2

respostas = {'sua pergunta': pergunta,
             '1 pergunta similar': '',
             '1 pergunta similar 1 resposta': '',
             '1 pergunta similar 2 resposta': '',
             '2 pergunta similar': '',
             '2 pergunta similar 1 resposta': '',
             '2 pergunta similar 2 resposta': ''}

quest = respostas['sua pergunta'] + ' site:brainly.com.br'

if True not in primeira_res and True not in segunda_res:

    quant = 0

elif True in primeira_res and True in segunda_res:

    quant = 2

else:

    quant = 1

if quant == 1:

    if True in primeira_res:

        inc = 0

    else:

        inc = 1

print(quant, inc)

if quant != 0:

    for l in search(quest, tld='co.in', start=inc, num=quant, pause=15, user_agent='Mozilla/5.0'):

        links.append(l)

    print(links)

    exit()

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

    for k, v in respostas.items():

        print(f'Chave: {k}\n\nItem: {v}\n')

