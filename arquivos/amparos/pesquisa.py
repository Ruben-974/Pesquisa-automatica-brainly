
from time import sleep

def Pesquisa_Com_Driver(pergunta=str, primeira_res=(True, True), segunda_res=(True, True)):

    import selenium
    import selenium.common.exceptions

    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver

    opc = Options()
    opc.headless = True # Esconder navegador? True or False

    fim_contagem, ini_contagem = 1, 0

    resultado = {
        'sua pergunta': pergunta,
        '1 pergunta similar': '',
        '1 pergunta similar 1 resposta': '',
        '1 pergunta similar 2 resposta': '',
        '2 pergunta similar': '',
        '2 pergunta similar 1 resposta': '',
        '2 pergunta similar 2 resposta': '',
    }

    if True in segunda_res:
        
        fim_contagem = 2

    if True not in primeira_res:

        ini_contagem = 1

    if True not in primeira_res and True not in segunda_res:

        pass

    else:

        for c in range(ini_contagem, fim_contagem):

            tempo = 0

            try:

                driver = webdriver.Firefox(executable_path='arquivos/driver/geckodriver', options=opc)

            except selenium.common.exceptions.WebDriverException:

                print('O arquivo geckodrive.exe não foi encontrado, verifique a pasta "arquivos/driver/"')

            try:

                driver.get(f'https://brainly.com.br/app/ask?q={resultado["sua pergunta"]}')

            except selenium.common.exceptions.WebDriverException:

                print('Não foi possivel acessar o site, verifique a sua internet')

            else:

                while True:

                    encontrou = True

                    try:
                        
                        sleep(1)

                        driver.find_elements_by_xpath("//a[@class='sg-text sg-text--small sg-text--link sg-text--bold']")[c].click()

                        break

                    except selenium.common.exceptions.InvalidSelectorException:

                        tempo += 1

                        if tempo > 10:

                            driver.close()

                            break

                    except IndexError:

                        print(f'A {c+1}° resposta da sua pergunta não foi encontrada no brainly')

                        resultado[f'{c+1} pergunta similar'] = 'Não houve pergunta similar'

                        encontrou = False

                        break

                if tempo <= 10 and encontrou:

                    resultado[f'{c+1} pergunta similar']  = driver.find_element_by_xpath("//h1/span[1]").text

                    if c == 0:

                        inc = primeira_res

                    else:

                        inc = segunda_res

                    if inc[0]:

                        resultado[f'{c+1} pergunta similar 1 resposta'] = driver.find_elements_by_xpath("//div[@class='sg-text sg-text--break-words brn-rich-content js-answer-content']")[0].text

                    if inc[1]:

                        try:

                            resultado[f'{c+1} pergunta similar 2 resposta'] = driver.find_elements_by_xpath("//div[@class='sg-text sg-text--break-words brn-rich-content js-answer-content']")[1].text

                        except IndexError:

                            resultado[f'{c+1} pergunta similar 2 resposta'] = 'Não há segunda resposta'

            driver.close()

    return resultado


def Pesquisa_Sem_Driver(pergunta, primeira_res=(True, True), segunda_res=(True, True)):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    from googlesearch import search

    links = []

    resultado = {'sua pergunta': pergunta,
                '1 pergunta similar': '',
                '1 pergunta similar 1 resposta': '',
                '1 pergunta similar 2 resposta': '',
                '2 pergunta similar': '',
                '2 pergunta similar 1 resposta': '',
                '2 pergunta similar 2 resposta': ''}

    quest = resultado['sua pergunta'] + ' site:brainly.com.br'

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

            resultado[f'{c+1} pergunta similar'] = perg.get_text()

            for c2 in range(len(resp)):
                
                for c3 in resp[c2].find_all('p'):

                    resultado[f'{c+1} pergunta similar {c2+1} resposta'] += c3.get_text() + '\n'

                resultado[f'{c+1} pergunta similar {c2+1} resposta'] = resultado[f'{c+1} pergunta similar {c2+1} resposta'].strip()

            if resultado[f'{c+1} pergunta similar 1 resposta'] == '':
                
                resultado[f'{c+1} pergunta similar 1 resposta'] = resp[0].get_text().strip()

            if resultado[f'{c+1} pergunta similar 2 resposta'] == '':

                resultado[f'{c+1} pergunta similar 2 resposta'] = resp[1].get_text().strip()

        if primeira_res[0] == False:

            resultado['1 pergunta similar 1 resposta'] = ''

        if primeira_res[1] == False:

            resultado['1 pergunta similar 2 resposta'] = ''

        if segunda_res[0] == False:

            resultado['2 pergunta similar 1 resposta'] = ''

        if segunda_res[1] == False:

            resultado['2 pergunta similar 2 resposta'] = ''

        return resultado

        
respostas = Pesquisa_Com_Driver(pergunta='Resumo segunda guerra mundial', primeira_res=(True, True), segunda_res=(True, True))

for k, v in respostas.items():

    print(f'\033[1;32mChave:\033[m {k}\n\033[1;32mItem:\033[m {v[0:50]}\n')