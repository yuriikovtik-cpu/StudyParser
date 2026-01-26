from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from parser import FindInfo
driver = webdriver.Chrome()
driver.get("https://brain.com.ua/ukr/")
findInfo = FindInfo()
time.sleep(2)

elem = driver.find_element(By.XPATH,"//div[@class='header-bottom']//input[@class='quick-search-input']")
elem.send_keys("Apple iPhone 15 128GB Black")
time.sleep(0.5)
elem.send_keys(Keys.RETURN)
time.sleep(2)

findPhone = driver.find_element(By.XPATH,"//div[@class='row']//div[@data-pid='1044347']//div[@class='br-pp-imadds']//img")
findPhone.click()
time.sleep(5)

print(findInfo.find(driver))