from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from re import sub, search
# chromedriver = "C:/Users/Roman/PycharmProjects/railway_check/TelegramAssistant/chromedriver.exe"
phantomjs = "c:/Users/Roman/PycharmProjects/railway_check/TelegramAssistant/webdrivers/phantomjs-2.1.1-windows/bin/phantomjs.exe"
# driver = webdriver.Chrome(chromedriver)
driver = webdriver.PhantomJS(phantomjs)
actions = ActionChains(driver)
wait = ui.WebDriverWait(driver,10)

#Нужно допилить
def clear_text(string):
    string = sub("<.*?>"," ",string)
    string = string.strip()
    return string

def find_tickets(station_from, station_till, date):
    print("Start working...")
    driver.get("http://booking.uz.gov.ua/ru/")
    # Read 'station from' city 
    station_from_input = driver.find_element_by_name("station_from")
    station_from_input.send_keys(str(station_from))
    # Wait until city will be in dropdown list
    button_from = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//div[@id='station_from']/div[@class='autosuggest']/ul/li")
            )
        )
    # Choose station from city
    button_from.click()

    #  Read 'station till' city
    station_till_input = driver.find_element_by_name("station_till")
    station_till_input.send_keys(str(station_till))
    # Wait until city will be in dropdown list
    wait.until(lambda driver: driver.find_element_by_xpath(
            "//div[@id='station_till']/div[@class='autosuggest']/ul/li")
        )
    button_till = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,
                "//div[@id='station_till']/div[@class='autosuggest']/ul/li")
            )
        )
    # Choose station till city
    button_till.click()

    # Change date to date that user entered
    driver.execute_script(
        "var date=arguments[0];document.getElementById('date_dep').value = date;", date
        )
    search_button = driver.find_element_by_name("search")
    #Search for trains
    actions.double_click(search_button).perform()
    # wait.until(EC.text_to_be_present_in_element((By.ID, 'ts_res'),'None'))
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='ts_res']").is_displayed())
    try:
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='ts_res']/table/tbody").is_displayed())
    # If driver don`t find trains
    except TimeoutException:
        return "Я не нашёл билетов.Попробуй позже"
    else:
        anwser = []
        # Вот это нужно доработать,что бы ещё и время показывало,и как-то красивее
        information = driver.find_elements_by_xpath("//table[@class='vToolsDataTable']/tbody/tr")
        for tr in information:
            tr = tr.get_attribute('innerHTML')
            train_number = tr.split('<td class="num">')[1].split('</td>')[0]
            date = tr.split('<td class="date">')[1].split('</td>')[0]
            duration = tr.split('<td class="dur">')[1].split('</td>')[0]
            places = tr.split('<td class="place">')[1].split('</td>')[0]
            train_number, date, dur, places = map(
                lambda string: clear_text(string),
                [train_number, date, duration, places]
                )
            # Appending new avaliable train information
            anwser.append({
                'train_number': train_number,
                'date': date,
                'duration': duration,
                'places': places
                })
        driver.quit()
        print('End work')
        return anwser

if __name__ == '__main__':
    result = find_tickets('Киев', "Харьков", "24.05.2017")
    