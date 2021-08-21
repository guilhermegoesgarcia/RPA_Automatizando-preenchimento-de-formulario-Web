#https://robocorp.com/docs/development-guide/browser/rpa-form-challenge
#https://rpaframework.org/index.html#

import pandas as pd
import timeit

from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP


# Open chrome on site
browser = Selenium()
browser.open_available_browser('http://rpachallenge.com/')  #http://rpachallenge.com/

# Download file
page = HTTP()
page.download('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx', target_file='../RPA_Automatiza-do-preenchimento-de-formulario-Web', overwrite=True)

# Click on Buttom
browser.click_button('Start')
start = timeit.timeit()

# Read data
data = pd.DataFrame()
data = pd.read_excel('/home/guilherme/PycharmProjects/RPA_Automatiza-do-preenchimento-de-formulario-Web/challenge.xlsx')

# Fill form

for index, tabela in data.iterrows():

    browser.input_text('css:input[ng-reflect-name="labelFirstName"]', tabela['First Name'])
    browser.input_text('css:input[ng-reflect-name="labelLastName"]', tabela['Last Name '])
    browser.input_text('css:input[ng-reflect-name="labelCompanyName"]', tabela['Company Name'])
    browser.input_text('css:input[ng-reflect-name="labelRole"]', tabela['Role in Company'])
    browser.input_text('css:input[ng-reflect-name="labelAddress"]', tabela['Address'])
    browser.input_text('css:input[ng-reflect-name="labelEmail"]', tabela['Email'])
    browser.input_text('css:input[ng-reflect-name="labelPhone"]', str(tabela['Phone Number']))

    # Click on Buttom
    browser.click_button('Submit')
    start = timeit.timeit()

    print(f'Processando pessoa {index+1}')

# Take Photo:
browser.capture_page_screenshot('rpachallenge.png')

# Show time
end = timeit.timeit()
print(f'Tempo decorrido: {round(end-start,6)}')







