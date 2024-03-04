import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    chrome = webdriver.Chrome()
    URL = 'https://formy-project.herokuapp.com/form'
    # Navigam spre URL-ul de mai sus.
    chrome.get(URL)
    time.sleep(2)
    # Maximizam fereastra driver-ului (Chrome)
    chrome.maximize_window()
    # Gasiti si completati campul 'First Name'.
    firstNameInput = chrome.find_elements(By.ID, 'first-name')
    firstNameInput.send_keys('Victor')
    # Gasiti si completati campul 'Last Name'.
    #lastNameInput = chrome.find_elements(By.CSS_SELECTOR,'input[placeholder='Enter last name']')
    #lastNameInput.send_keys('Manuel')
    # Gasiti si completati campul 'Job Title'.
    #jobTitleInput = chrome.find_elements(By.XPATH,'//div[3]/input[contains(@type,'text')]')
    #// div[2] / input[contains( @ type, 'radio')]
finally:
    time.sleep(3)
    chrome.quit()
