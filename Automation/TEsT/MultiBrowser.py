from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver= webdriver.Chrome('C:/Drivers/chromedriver.exe')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_elements(By.CLASS_NAME, 'text_field')
wait=WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label')))
element.click()