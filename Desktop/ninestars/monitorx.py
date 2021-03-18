from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import smtplib


driver = webdriver.Chrome("C:/Users/HP/Downloads/chromedriver.exe")
driver.get('http://monitorx.mynewsdash.com/login.html')

username = "sterwin.p@ninestars.in"
password = "sterwin"


driver.find_element_by_id("email").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("pwd").send_keys(password)

driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/form/input").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div/div/div[4]/i").click()
driver.find_element_by_xpath("/html/body/div[7]/a[4]/i").click()


feed_processor = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/table/tbody/tr[1]/th[2]')))
print ('BACKUP DATA =',feed_processor.text)


driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a/div").click()

feed_processor1 = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[1]/th[2]')))
print ('WEEKLY BACKUP DATA =',feed_processor1.text)
