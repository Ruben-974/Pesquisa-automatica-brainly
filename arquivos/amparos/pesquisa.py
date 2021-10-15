import selenium
import selenium.common.exceptions

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from time import sleep

def Pesquisar_Pergunta(pergunta=str, primeira_res=(True, True), segunda_res=(True, True)):

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

                driver = webdriver.Firefox(executable_path='arquivos/driver/geckodriver.exe', options=opc)

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

# Pesquisar_Pergunta(pergunta='Qual a formula da agua?', primeira_res=(False, False), segunda_res=(True, False))