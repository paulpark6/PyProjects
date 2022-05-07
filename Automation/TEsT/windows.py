from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:/Drivers/chromedriver.exe')
driver.get('http://demo.automationtesting.in/Windows.html')
driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()

handles = driver.window_handles
window_one = driver.window_handles[0]
window_two = driver.window_handles[1]
print('fwekojkjpewfkjnwdekjewfd')
for handle in handles:
    driver.switch_to_window(handle)
    print(handle)
    print(driver.current_window_handle)
    print(driver.title)
driver.switch_to_window(window_two)

'''
title = driver.title
if title == 'SeleniumHQ Browser Automation':
    driver.close()

'''