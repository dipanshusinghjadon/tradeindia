from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


usernameStr = 'prakharnigam@tradeindia.com'
passwordStr = 'trade12india'
browser = webdriver.Chrome(executable_path="/home/user01/Downloads/chromedriver")
browser.get(('https://www.tradeindia.com/login/login.html'))
username=browser.find_element(By.ID,"email_mobile")
username.send_keys(usernameStr)
browser.find_element(By.ID,'lgn').click()
time.sleep(5)
password=browser.find_element(By.ID,"password")
password.send_keys(passwordStr)
browser.find_element(By.ID,'submit_email').click()
time.sleep(5)
browser.get(('https://www.tradeindia.com'))
