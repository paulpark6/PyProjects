# program to skip ads on youtube automatically

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome("C:/Drivers/chromedriver.exe")

driver.get("https://www.youtube.com")
wait = WebDriverWait(driver, 3)


while True:
    try:
        skip = driver.find_element_by_class_name('ytp-ad-skip-button-container')
        skip_now = wait.until(EC.element_to_be_clickable((skip)))
        skip_now.click()
        print("skipped!")
    except:
        continue
        print("continued")
