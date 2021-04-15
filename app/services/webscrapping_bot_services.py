from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

class Bot:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    # def set_verify(self):
    #     if not self.sorted_verify:
    #         self.sorted_verify = True
    #         return self.sorted_verify


    def get_items(self):
        try:

            self.driver.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/')
            page_source = self.driver.page_source
            parser = BeautifulSoup(page_source, 'html.parser')
            items = parser.select('li[ng-repeat="dezena in resultado.listaDezenas "]')
            items_frases = parser.select('p[ng-repeat="faixaPremiacao in resultado.listaRateioPremio"]')
            values = []
            frases = []
            [values.append(int(item.text)) for item in items]
            [frases.append(frase) for frase in items_frases]
            result = str(values).replace(']',"").replace('[',"")
            return result, frases
        except:
            return False





def get_ms_result():
    bot = Bot()
    return bot.get_items()
