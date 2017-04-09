from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromedriver = "C:/Users/Roman/PycharmProjects/railway_check/TelegramAssistant/chromedriver.exe"
phantomjs = "c:/Users/Roman/PycharmProjects/railway_check/TelegramAssistant/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe"
driver = webdriver.Chrome(chromedriver)
actions = ActionChains(driver)
wait = ui.WebDriverWait(driver,100)

#Названия станций на русском
#s;dflgj
def find_tickets(station_from,station_till,date):
    print("Start working...")
    driver.get("http://booking.uz.gov.ua/ru/")
    station_from_input = driver.find_element_by_name("station_from")
    station_from_input.send_keys(str(station_from))
    # driver.save_screenshot('screenshot1.png')

    #Нажать на что-то из выпадающего списка
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='station_from']/div[@class='autosuggest']/ul/li"))
    button_from = driver.find_element_by_xpath("//div[@id='station_from']/div[@class='autosuggest']/ul/li")
    # button_from_li = button_from.find_element_by_tag_name("li")
    actions.double_click(button_from).perform()
    print(button_from.get_attribute('innerHTML'))
    
    station_till_input = driver.find_element_by_name("station_till")
    station_till_input.send_keys(str(station_till))
    #Нажать на что-то из выпадающего списка
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='station_till']/div[@class='autosuggest']/ul/li"))
    button_till = driver.find_element_by_xpath("//div[@id='station_till']/div[@class='autosuggest']/ul/li")
    actions.double_click(button_till).perform()
    print(button_till.get_attribute('innerHTML'))
    

	#Теперь дата 
	# id = date_dep --- это кнопка для календаря
	#a[class=ui-state-default]  ----  это ячейки с номерами дат в календарике. Выбирать по числу
	# class = ui-datepicker-calendar   ---- это сам календарь

    search_button = driver.find_element_by_name("search")
    actions.click(search_button).perform()
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='ts_res']/table/tbody"))

    driver.save_screenshot('screenshot.png')
    # driver.quit()


find_tickets('Киев','Кривой Рог','23.03.2017')

# if __name__ == 'main':
#     find_tickets('Киев','Кривой Рог')


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



