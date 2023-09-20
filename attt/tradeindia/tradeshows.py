from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# usernameStr = 'hasan.fauwad@tradeindia.com'
# passwordStr = 'info@12india'
browser = webdriver.Chrome(executable_path="/home/user01/Downloads/chromedriver.exe")
browser.maximize_window()
browser.get(('https://www.tradeindia.com/tradeshows/'))
time.sleep(2)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/span/header/div/div/div[2]/div/a[2]/span/span/span').click()
time.sleep(2)
browser.find_element(By.XPATH,'//p[text()="Login With Email & Password"]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//input[@type="email"]').send_keys(usernameStr)
time.sleep(2)
browser.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(2)
browser.find_element(By.XPATH,'//input[@type="password"]').send_keys(passwordStr)
time.sleep(2)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/section[2]/div/div[2]/div/div[3]/button').click()
time.sleep(5)
browser.implicitly_wait(10)
all_containers = browser.get("https://www.tradeindia.com/tradeshows/all-categories.html")

for no in range(1,37):
    all_containers = browser.find_elements(By.CSS_SELECTOR,".col-md-3")
    tag = all_containers[no].find_element(By.TAG_NAME,"a")
    tag.click()
    time.sleep(5)
    # bb = tag.screenshot_as_base64()
    # with open(f"./timage{no}.png","wb") as file:
    #     file.write(bb)
    browser.back()
    time.sleep(5)
    