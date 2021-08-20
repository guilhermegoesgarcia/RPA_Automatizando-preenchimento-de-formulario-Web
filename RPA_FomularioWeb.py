import pandas as pd

from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP

browser = Selenium()
browser.open_available_browser('http://rpachallenge.com/')

page = HTTP()
page.download('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx',target_file='../RPA_Automatizando-preenchimento-de-formulario-Web', overwrite=True)







