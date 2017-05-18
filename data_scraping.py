from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# chromedriver = "C:/Users/Roman/PycharmProjects/railway_check/TelegramAssistant/chromedriver.exe"
phantomjs = "c:/Users/Roman/PycharmProjects/railway_check/TelegramAssistant/webdrivers/phantomjs-2.1.1-windows/bin/phantomjs.exe"
driver = webdriver.PhantomJS(phantomjs)
actions = ActionChains(driver)
wait = ui.WebDriverWait(driver,10)


def find_tickets(station_from,station_till,date):
    print("Start working...")
    driver.get("http://booking.uz.gov.ua/ru/")
    #Chose station from
    station_from_input = driver.find_element_by_name("station_from")
    station_from_input.send_keys(str(station_from))
    #Нажать на что-то из выпадающего списка
    button_from = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='station_from']/div[@class='autosuggest']/ul/li")))
    button_from.click()

    #Choose station till    
    station_till_input = driver.find_element_by_name("station_till")
    station_till_input.send_keys(str(station_till))
    #Нажать на что-то из выпадающего списка
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='station_till']/div[@class='autosuggest']/ul/li"))
    button_till = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='station_till']/div[@class='autosuggest']/ul/li")))
    button_till.click()
    # Change date to date that user entered
    driver.execute_script("var date=arguments[0];document.getElementById('date_dep').value = date;",date)
    search_button = driver.find_element_by_name("search")
    #Search for trains
    actions.double_click(search_button).perform()
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='ts_res']/table/tbody").is_displayed())

    # If driver don`t find trains
    if "По заданному Вами направлению мест нет" in driver.page_source:
        return None
    else:
        #Вот это нужно доработать,что бы ещё и время показывало,и как-то красивее
        information = driver.find_elements_by_xpath("//table[@class='vToolsDataTable']/tbody/tr")
        # write_information = open('1.html','w')
        # for td in information:
        #     write_information.write('<table>')
        #     write_information.write(td.get_attribute('outerHTML').replace('<button>Выбрать</button>',''))
        #     write_information.write('</table>')
        anwser = '<table>'
        for td in information:
            anwser.append('<table>')
            anwser.append(td.get_attribute('outerHTML').replace('<button>Выбрать</button>',''))
            anwser.append('</table>')

        # for div in information:
        #     write_information.write(div.get_attribute('outerHTML').replace('<button>Выбрать</button>',''))
        #     write_information.write("<p></p>")
        # print(information.get_attribute('innerHTML'))
        driver.quit()
        return anwser

# div class="place fr"
# input class lastname,firstname
# input value = stud , innerHTML = Студенческий
# input class = stud_number 
# Кнопка купить:
# button class = complex_btn


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



