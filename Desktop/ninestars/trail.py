from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#import pandas as pd
#driver = webdriver.Chrome("C:/Users/HP/Downloads/chromedriver.exe")

options = Options()
options.headless = True
CHROMEDRIVER_PATH="C:/Users/HP/Downloads/chromedriver.exe"
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
driver.get('https://trial.mynewsdash.com/?rt=login/fLogout&logout=1')

username = "ns_rim_team"
password = "12345"

driver.find_element_by_id("userName").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("submitBtn").click()





element2 = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/nav/div[1]/div[2]/ul[1]/li[3]/a')))
if (element2.text == 'Stories'):
    print ('login successful')
else:
    print('login unsuccessfull')