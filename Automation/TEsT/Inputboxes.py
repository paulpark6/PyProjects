from selenium import webdriver

driver=webdriver.Chrome(executable_path= 'C:/Drivers/chromedriver.exe')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/')
# working with the radio buttons
status=driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').click()

sunday=driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[1]/td/label')
sunday.click()

saturday=driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[7]/td/label')
saturday.click()