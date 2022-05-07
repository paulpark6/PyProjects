# switching frames and clicking on different links inside the frame
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/Drivers/chromedriver.exe')
driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')
frame1 = 'packageListFrame'
frame2 = 'packageFrame'
frame3 = 'classFrame'

driver.switch_to_frame(frame1)  # switched to frame 1
driver.find_element(By. XPATH, '/html/body/div[2]/ul/li[5]/a').click()



driver.switch_to_default_content()  # switched to default

driver.switch_to_frame(frame2)  # switched to frame 2
driver.find_element_by_xpath('/html/body/div/ul[1]/li[1]/a/span').click()

driver.switch_to_default_content()  # switched to default

driver.switch_to_frame(frame3)  # switched to frame 3
driver.find_element_by_xpath('/html/body/div[1]/ul/li[4]/a').click()












