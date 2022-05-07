from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome('C:/Drivers/chromedriver.exe')
driver.get('https://www.youtube.com/')
driver.implicitly_wait(3)
searchBox=driver.find_element(By.XPATH, '//*[@id="search"]')
searchBox.send_keys('niga')


