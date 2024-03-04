import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    chrome = webdriver.Chrome()
    URL = "https://www.elefant.ro/"
    chrome.get(URL)
    chrome.maximize_window()
    time.sleep(2)


    #elements = chrome.find_elements(By.CLASS_NAME,"form-control searchTerm js-has-overlay")
    #print(len(elements))
    #chrome.find_element(By.NAME,"SearchTerm").send_keys("IPhone14")
    #time.sleep(10)
finally:
    chrome.quit()