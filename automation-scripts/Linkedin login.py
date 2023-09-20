from timeit import repeat
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


usernamestr = "thakur.deepanshu90@gmail.com"
passwordstr = "Bhavik08"
browser = webdriver.Chrome(executable_path= "/home/user01/Downloads/chromedriver")
browser.get(('https://www.linkedin.com/login'))
username = browser.find_element(By.ID,"username")
username.click()
username.send_keys(usernamestr)
# time.sleep(5)
passwrd = browser.find_element(By.ID,"password")
passwrd.click()
passwrd.send_keys(passwordstr)
time.sleep(3)
btn = browser.find_element(By.XPATH,'//button[text()="Sign in"]')
btn.click()
browser.get("https://www.linkedin.com/feed/")
time.sleep(5)
btn = browser.find_element(By.ID,"#ember17").click()
time.sleep(2)
btn = browser.find_element(By.XPATH,'/html/body/div[6]/header/div/nav/ul/li[6]/div/div').click()
browser.close()
