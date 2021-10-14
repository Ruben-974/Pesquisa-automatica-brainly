import selenium
import selenium.common.exceptions

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from time import sleep

opc = Options()
opc.headless = True # Esconder navegador? True or False

tempo = 0
resultado = {}

resultado['sua pergunta'] = 'Oque foi a revolução francesa?'

try:

    driver = webdriver.Firefox(executable_path='arquivos/driver/geckodriver.exe', options=opc)

except selenium.common.exceptions.WebDriverException:

    print('O arquivo geckodrive.exe não foi encontrado, verifique a pasta "arquivos/driver/"')

else:

    driver.get(f'https://brainly.com.br/app/ask?q={resultado["sua pergunta"]}')

    while True:

        try:
            sleep(1)

            driver.find_element_by_xpath("//div[@class='sg-box sg-box--light sg-box--padding-m sg-box--border-color-gray-secondary-lightest sg-box--border SearchResultsSection__layout--2Ya_t LayoutBox__box--1H22h']/div[1]/div[@class='sg-content-box__content sg-content-box__content--spaced-bottom-xlarge']/div[1]/div[1]/div[1]/a[1]").click()

            break

        except:

            tempo += 1

            if tempo > 10:
                break

    if tempo < 10:

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

    else:

        print('houve um erro')
        driver.close()
