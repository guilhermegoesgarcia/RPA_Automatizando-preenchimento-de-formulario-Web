import pandas as pd
import timeit

from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP


class RPA_FormWeb():

    def __init__(self):
        self.browser = Selenium()
        self.page = HTTP()
        self.data = pd.DataFrame()

    def open_site(self, site: str):
        self.browser.open_available_browser(site)

    def download_file(self, web_download: str):
        self.page.download(web_download,
                           target_file='../RPA_Automatiza-do-preenchimento-de-formulario-Web', overwrite=True)

    def click_button(self, name_button: str):
        self.browser.click_button(name_button)

    def read_data(self, ):
        self.data = pd.read_excel(
            '/home/guilherme/PycharmProjects/RPA_Automatiza-do-preenchimento-de-formulario-Web/challenge.xlsx')

    def fill_form(self):
        for index, tabela in self.data.iterrows():
            self.browser.input_text('css:input[ng-reflect-name="labelFirstName"]', tabela['First Name'])
            self.browser.input_text('css:input[ng-reflect-name="labelLastName"]', tabela['Last Name '])
            self.browser.input_text('css:input[ng-reflect-name="labelCompanyName"]', tabela['Company Name'])
            self.browser.input_text('css:input[ng-reflect-name="labelRole"]', tabela['Role in Company'])
            self.browser.input_text('css:input[ng-reflect-name="labelAddress"]', tabela['Address'])
            self.browser.input_text('css:input[ng-reflect-name="labelEmail"]', tabela['Email'])
            self.browser.input_text('css:input[ng-reflect-name="labelPhone"]', str(tabela['Phone Number']))

            self.click_button('Submit')

    def take_photo(self):
        self.browser.capture_page_screenshot('rpachallenge.png')

    def time_on(self):
        self.start = timeit.timeit()
        return self.start

    def time_off(self):
        self.end = timeit.timeit()
        return print(f'Tempo decorrido: {round(self.end - self.start, 6)}')


def exec_RPA():
    projeto = RPA_FormWeb()
    projeto.time_on()
    projeto.open_site('http://rpachallenge.com/')
    projeto.download_file('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx')
    projeto.click_button('Start')
    projeto.read_data()
    projeto.fill_form()
    projeto.take_photo()
    projeto.time_off()


exec_RPA()