from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path='C:/Drivers/chromedriver.exe')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/')

drop_down=driver.find_element_by_id('RESULT_RadioButton-9')
Select(drop_down).select_by_visible_text('Afternoon')
all_options=Select(drop_down).options

for option in all_options:      # this will write down all the options
    print(option.text)

print(len(all_options))         # this will coudn the options available






