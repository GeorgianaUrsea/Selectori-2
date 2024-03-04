import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    chrome= webdriver.Chrome()
    #navigam spre URL de mai sus
    URL= 'https://formy-project.herokuapp.com/form'
    chrome.get(URL)
    time.sleep(2)
    #maximizam fereastra driverului (chrome)
    chrome.maximize_window()
    #gasiti si completati campul firstname
    firstNameInput= chrome.find_element(By.ID,'first-name')
    firstNameInput.send_keys("Ursea")
    #gasiti si completati campul lastname: tag[atribut="value" structura unui CSS SELECTOR
    lastNameInput=chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"')
    lastNameInput.send_keys("Georgiana")
    #gasiti si completati campul job title FOLOSIND UN SELECTOR XPATH
    jobTitleInput=chrome.find_element(By.XPATH,'//div[3]/input[contains(@type,"text")]')
    jobTitleInput.send_keys("Tester")
    #faceti click pe optiunea pe optiunea Highschool din Highest level of education
    '''chrome.find_element()
    highschoollevel=chrome.find_element(By.XPATH,'//div[2]/input[contains(@type,\'radio\')]
    jobTitleInput.click()'''
    #alegem gender
    #chrome.find_element(By.CSS_SELECTOR,'#checkbox-2').click()

    #SELECTATI OPTIUNEA 2-4 ANI DE EXPERIENTA FOLOSIND OBIECTUL SELECT DIN SELENIUM
    years_dropdown=Select(chrome.find_element(By.ID,'select-menu'))
    years_dropdown.select_by_value('2')
    #selectati ziua in curs
    chrome.find_element(By.ID,"datepicker").click()
    time.sleep(3)
    chrome.find_element(By.CSS_SELECTOR, '[class=\'today day\']').click()







finally:
    time.sleep(3)
    chrome.quit()
