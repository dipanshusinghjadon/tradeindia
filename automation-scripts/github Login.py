from selenium import webdriver
from selenium.webdriver.common.by import By
import time

usernamestr = "thakur.deepanshu90@gmail.com"
passwordstr = "#dipanshu1992"
# browser = webdriver.Chrome(executable_path= "/home/user01/Downloads/chromedriver")
browser = webdriver.Chrome()
browser.get(('https://github.com/login'))
username = browser.find_element(By.ID,"login_field")
username.click()
username.send_keys(usernamestr)
# time.sleep(5)
passwrd = browser.find_element(By.ID,"password")
passwrd.click()
passwrd.send_keys(passwordstr)
btn = browser.find_element(By.CLASS_NAME,"js-sign-in-button")
btn.click()
browser.get("https://github.com/dipanshusinghjadon/testing")
browser.get("https://github.com/dipanshusinghjadon/testing/blob/master/test.py")
