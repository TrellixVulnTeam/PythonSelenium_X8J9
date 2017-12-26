import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\nmelo\\QATools\\Python\\PythonSelenium\\Automation\\Drivers\\chromedriver.exe")
driver.get("http://www.google.com")
time.sleep(5)
assert 'Google' in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("Pyton")
elem.send_keys(Keys.RETURN)
driver.close()
driver.quit()

