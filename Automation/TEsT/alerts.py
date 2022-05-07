from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='C:/Drivers/chromedriver.exe')
driver.get('https://testautomationpractice.blogspot.com/')
element = driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button')
score = int(0)
final_score = int(5)
for score in range (0,3):
    element.click()
    time.sleep(2)
    user_answer = input('Yes or No?').lower()
    if user_answer == 'yes':
        driver.switch_to_alert().accept()
    elif user_answer == 'no':
        driver.switch_to_alert().dismiss()
    else:
        "???????"







