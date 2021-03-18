import requests
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import smtplib

messege=" "
'''
PrimaryEs = "http://52.9.15.66:9200/_cluster/health?pretty.com"
PrimaryEs_json = requests.get(PrimaryEs).json()
PrimaryEs_status = PrimaryEs_json['status']
print('primaryEs status=',PrimaryEs_status)
messege += 'primaryEs status='+PrimaryEs_status

PortalES = "http://52.9.15.66:9200/_cluster/health?pretty"
PortalES_json = requests.get(PortalES).json()
PortalES_status = PortalES_json['status']
print('PortalES status=',PortalES_status)
messege += 'PortalES status='+PortalES_status



MainES = "http://52.35.203.233:9200/_cluster/health?pretty"
MainES_json = requests.get(MainES).json()
MainES_status = MainES_json['status']
print('MainES status=',MainES_status)
messege += 'MainES status='+MainES_status


EmailES = "http://18.208.87.155:9200/_cluster/health?pretty"
EmailES_json = requests.get(EmailES).json()
EmailES_status = EmailES_json['status']
print('EmailES status=',EmailES_status)
messege += 'EmailES status='+EmailES_status

NLA = "http://206.81.26.0:9200/_cluster/health?pretty"
NLA_json = requests.get(NLA).json()
NLA_status = NLA_json['status']
print('NLA status=',NLA_status)
messege += 'NLA status='+NLA_status
'''



driver = webdriver.Chrome("C:/Users/HP/Downloads/chromedriver.exe")
driver.get('https://portal.mynewsdash.com/?rt=login/fLogout&logout=1')

username = "rim_team_support"
password = "12345"

driver.find_element_by_id("userName").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(password)

driver.find_element_by_id("submitBtn").click()
driver.find_element_by_id("admin_menu").click()
driver.find_element_by_xpath("/html/body/div[1]/div[23]/div/div[2]/div[6]").click()


'''feed = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.ID, '?rt=process/manageProcess'))).click()'''


messege=" "

#feed_processor
feed_processor = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[2]/table/tbody/tr[1]/td[6]')))
if (feed_processor.text != '0'):
    print ('feed_processor =',feed_processor.text)
    messege += "feed_processor ="+feed_processor.text
    


#feed_controller
feed_controller = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[2]/table/tbody/tr[2]/td[6]')))
if (feed_controller.text != '0'):
    print ('feed controller =',feed_controller.text)
    messege += "feed controller ="+feed_controller.text



#INDEX_PROCESSOR
INDEX_PROCESSOR = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[2]/table/tbody/tr[3]/td[6]')))
if (INDEX_PROCESSOR.text != '0'):
    print ('INDEX_PROCESSOR =',INDEX_PROCESSOR.text)
    messege += "INDEX_PROCESSOR ="+INDEX_PROCESSOR.text


#DAILY_FEED_CONVERTOR_CONTROLLER
DAILY_FEED_CONVERTOR_CONTROLLER = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '//html/body/div[1]/div[23]/div/form/div/div[1]/div[2]/table/tbody/tr[4]/td[6]')))
if (DAILY_FEED_CONVERTOR_CONTROLLER.text != '0'):
    print ('DAILY FEED CONVERTOR CONTROLLER =',DAILY_FEED_CONVERTOR_CONTROLLER.text)
    messege += 'DAILY FEED CONVERTOR CONTROLLER ='+DAILY_FEED_CONVERTOR_CONTROLLER.text


#dailyfeed converter processor
dailyfeed_converter_processor = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[2]/table/tbody/tr[5]/td[6]')))
if (dailyfeed_converter_processor.text != '0'):
    print ('daily feed converter processr=',dailyfeed_converter_processor.text)
    messege += 'daily feed converter processr='+dailyfeed_converter_processor.text




#LMDS_DAILY_FEED_PROCESSOR
LMDS_DAILY_FEED_PROCESSOR = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[2]/table/tbody/tr[6]/td[6]')))
if (LMDS_DAILY_FEED_PROCESSOR.text != '0'):
    print ('LMDS DAILY FEED PROCESSOR =',LMDS_DAILY_FEED_PROCESSOR.text)
    messege += 'LMDS DAILY FEED PROCESSOR ='+LMDS_DAILY_FEED_PROCESSOR.text




#BROADCAST_DAILY_FEED_PROCESSOR
BROADCAST_DAILY_FEED_PROCESSOR = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[2]/table/tbody/tr[7]/td[6]')))
if (BROADCAST_DAILY_FEED_PROCESSOR.text != '0'):
    print ('BROADCAST DAILY FEED PROCESSOR =',BROADCAST_DAILY_FEED_PROCESSOR.text)
    messege += 'BROADCAST DAILY FEED PROCESSOR ='+BROADCAST_DAILY_FEED_PROCESSOR.text


#CORE_DAILY_FEED_PROCESSOR
CORE_DAILY_FEED_PROCESSOR = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[2]/table/tbody/tr[8]/td[6]')))
if (CORE_DAILY_FEED_PROCESSOR.text != '0'):
    print ('CORE DAILY FEED PROCESSOR =',CORE_DAILY_FEED_PROCESSOR.text)
    messege += 'CORE DAILY FEED PROCESSOR =',CORE_DAILY_FEED_PROCESSOR.text



#MAIN_INDEX_CONTROLLER
MAIN_INDEX_CONTROLLER = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[3]/table/tbody/tr[1]/td[6]')))
if (MAIN_INDEX_CONTROLLER.text != '0'):
    print ('MAIN INDEX CONTROLLER =',MAIN_INDEX_CONTROLLER.text)
    messege += 'MAIN INDEX CONTROLLER ='+MAIN_INDEX_CONTROLLER.text

#MAIN_INDEX_PROCESSOR
MAIN_INDEX_PROCESSOR = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[23]/div/form/div/div[1]/div[3]/table/tbody/tr[2]/td[6]')))
if (MAIN_INDEX_PROCESSOR.text != '0'):
    print ('MAIN INDEX PROCESSOR =',MAIN_INDEX_PROCESSOR.text)
    messege += 'MAIN INDEX PROCESSOR ='+MAIN_INDEX_PROCESSOR.text


'''server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("rim.test2134@gmail.com","test@1234")
server.sendmail("rim.test2134@gmail.com","aditya.s@ninestars.in",messege)
server.quit()'''
print(messege)