from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome(executable_path= "/home/user01/Downloads/chromedriver")
browser = Chrome()
browser.get('https://www.browserstack.com/')
print(browser.title)
browser.close()