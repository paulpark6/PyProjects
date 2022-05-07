# create an automation program of to watch a movie on xmovies8.tv website
# open website on private mode
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_arguments('--incognito')
'''
driver = webdriver.Chrome(executable_path='C:/Drivers/chromedriver.exe')
driver.get('https://xmovies8.tv/')
search = '//*[@id="onesignal-slidedown-cancel-button"]'

wait = WebDriverWait(driver,10) # waits for the search box to be present
nothanks = wait.until(EC.element_to_be_clickable((By. NAME, 'keyword-home')))
# ask user what they want to watch
movie_name = input('What movie do you want to watch?')
nothanks.send_keys(movie_name)  # TYPES INTO SERACH BOX
driver.find_element(By.XPATH, '//*[@id="hm-search"]/div/a').click() # clicks search key
driver.implicitly_wait(10) # wait for the page to load
# find the right movie

# click

# watch
