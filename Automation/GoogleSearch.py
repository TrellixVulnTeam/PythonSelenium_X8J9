import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("Drivers\\chromedriver.exe")
driver.get('http://newtours.demoaut.com/')
time.sleep(5)
elem = driver.find_element_by_name("userName")
elem.send_keys("mercury")
elem = driver.find_element_by_name("password")
elem.send_keys("mercury")
elem.send_keys(Keys.RETURN)
driver.close()
driver.quit()