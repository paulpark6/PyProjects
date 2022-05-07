# website link: https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/
# chrome driver path: C:/Drivers/chromedriver.exe
# before getting the link of the website
# ask the user if they are male or female
# list all the drop down options and select one of the option
# select the option for the user
# list the number of options then make the user to pick one
# select the option in the webpage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = 'C:/Drivers/chromedriver.exe')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/')
# ask the user for his / her gender and makes it into all lower case.
user_gender = input('Welcome to my form!\nAre you male or female?\nType male or female here: ').lower()

drop_down_butten = 'drop_down'  # class name of the butten

wait = WebDriverWait(driver, 3)

if user_gender == 'male':

    male = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label')))
    male.click()
else:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q26"]/table/tbody/tr[2]/td/label'))).click()
# after clicking on the gender moves on to dropdown options

drop_down_options = Select(driver.find_element(By.CLASS_NAME, 'drop_down')).options
print('there are', len(drop_down_options) -1 , 'options')    # -1 because the blank counts as an option too

for drop_down_option in drop_down_options:
    print(drop_down_option.text)        # .text will show the text file of the options.

user_option = input('What option do you want from above?\n Type here: ').lower()

if user_option == 'morning':
    print('morning')
    Select(driver.find_element(By.CLASS_NAME, 'drop_down')).select_by_index(1)
elif user_option == 'afternoon':
    print('afternoon')
    Select(driver.find_element(By.CLASS_NAME, 'drop_down')).select_by_index(2)
elif user_option == 'evening':
    print('evening')
    Select(driver.find_element(By.CLASS_NAME, 'drop_down')).select_by_index(3)

