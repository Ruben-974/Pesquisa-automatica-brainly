import selenium
import selenium.common.exceptions

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from time import sleep

opc = Options()
opc.headless = True # Esconder navegador? True or False

encontrou, tempo, resultado = True, 0, {}

resultado['sua pergunta'] = 'dkjfklsdjfkldsjfokdsjkdfjds'

try:

    driver = webdriver.Firefox(executable_path='arquivos/driver/geckodriver.exe', options=opc)

except selenium.common.exceptions.WebDriverException:

    print('O arquivo geckodrive.exe não foi encontrado, verifique a pasta "arquivos/driver/"')

else:

    try:

        driver.get(f'https://brainly.com.br/app/ask?q={resultado["sua pergunta"]}')

    except selenium.common.exceptions.WebDriverException:

        print('Não foi possivel acessar o site, verifique a sua internet')

    else:

        while True:

            try:
                
                sleep(1)

                driver.find_elements_by_xpath("//a[@class='sg-text sg-text--small sg-text--link sg-text--bold']")[0].click()

                break

            except selenium.common.exceptions.InvalidSelectorException:

                tempo += 1

                if tempo == 10:

                    break

            except IndexError:

                print('A resposta da sua pergunta não foi encontrada no brainly')

                encontrou = False

                break

        if tempo <= 10 and encontrou:

            resultado['resposta similar']  = driver.find_element_by_xpath("//h1/span[1]").text

            respostas = driver.find_elements_by_xpath("//div[@class='sg-text sg-text--break-words brn-rich-content js-answer-content']")

            resultado['primeira resposta'] = respostas[0].text

            try:

                resultado['segunda resposta']  = respostas[1].text

            except IndexError:

                resultado['segunda resposta'] = 'Não há segunda resposta'

            driver.close()

            print(tempo)

            for k, i in resultado.items():
                print(f'Chave: {k}\nItem: {i}')

driver.close()
