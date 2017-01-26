import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from  selenium.webdriver.remote.webelement import WebElement

from robobrowser import RoboBrowser


driver = webdriver.Firefox()

def open_search_page():
    driver.get("http://booking.uz.gov.ua/ru/")
    form = driver.find_element_by_class_name('train_search')
    print(form)




if __name__ == 'main':
    open_search_page()


'''br = RoboBrowser(user_agent='user_agent=Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')

br.open('http://booking.uz.gov.ua/ru/')
form=br.get_form(class_='train_search')

form['station_id_from'].value='2204001'
form['station_id_till'].value='2200001'
form['station_from'].value = 'Харьков'
form['station_till'].value = 'Киев'
form['date_dep'].value ='16.10.2016'
form['time_dep_till'].value = 0
br.submit_form(form,True)
br.select('button')

table_of_trains=br.select('table')[0]
#print(table_of_trains)


'''



