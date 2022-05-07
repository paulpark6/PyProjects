# a program to swtich windows between 3 websites
# close the website you dont need
# driver location = C:/Drivers/chromedriver.exe
# 'https://www.selenium.dev/'
# 'http://demo.automationtesting.in/Windows.html'
# 'https://www.youtube.com'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('C:/Drivers/chromedriver.exe')
driver.get('http://demo.automationtesting.in/Windows.html')
wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Tabbed"]/a/button'))).click()
driver.get('https://www.youtube.com')
handles = driver.window_handles
one = driver.window_handles[0]
two = driver.window_handles[1]

for website in handles:
    print(driver.title)
driver.switch_to_window(one)
wait.until(EC.url_to_be('https://www.youtube.com/'))
driver.find_element_by_id('search').send_keys('league')
