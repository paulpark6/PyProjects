from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('C:/Drivers/chromedriver.exe')
driver.get('https://www.sitebuilderreport.com/free-website-builders')


links = driver.find_elements(By.CLASS_NAME, "cta")
print(len(links))

for link in links:
    print(link.text)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Wix.c').click()

