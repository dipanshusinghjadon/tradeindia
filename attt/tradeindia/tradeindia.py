#! /home/user01/miniconda3/envs/sele/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


usernameStr = 'hasan.fauwad@tradeindia.com'
passwordStr = 'trade12india'
browser = webdriver.Chrome(executable_path="/home/user01/Downloads/chromedriver.exe")
browser.maximize_window()
#browser.implicitly_wait(8)
browser.get(('https://www.tradeindia.com/login/login.html'))
time.sleep(1)
browser.find_element(By.XPATH, "//p[@class='mt-3 text-center loginWithText']").click()
username=browser.find_element(By.NAME,"email")
username.send_keys(usernameStr)
browser.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(1)
password=browser.find_element(By.NAME,"otp")
password.send_keys(passwordStr)
browser.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
# browser.execute_script("return document.body.scrollHeight")
# scroll_down = 1300
# scroll_up = 1300
# for scroll_down in range(0,1300,100):
#     browser.execute_script(f"window,scrollBy(0,{scroll_down})")
#     print(scroll_down)
#     time.sleep(1)
# for scroll_up in range(-100,-1300,-100):
#     browser.execute_script(f"window.scrollBy(0,{scroll_up})")
#     print(scroll_up)
#     time.sleep(1)
a = ActionChains(browser)
m = browser.find_element(By.XPATH,'//h2[text()="Agriculture"]')
time.sleep(2)
a.move_to_element(m).perform()
time.sleep(2)
n = browser.find_element(By.CSS_SELECTOR,'#__next > div > div > main > div > div.ti-container.bx-brd-box > div.mb-4.mb-md-4.row.pt-md-3 > div.col-xl-2.order-xl-0.mt-xl-0.mt-md-5.mt-3 > span > div > ul > li:nth-child(12) > div > div > div.row > div:nth-child(6) > a:nth-child(2)')
time.sleep(2)
a.move_to_element(n).click().perform()
time.sleep(2)
browser.execute_script("return document.body.scrollHeight")
for scroll in range(0,500,100):
    browser.execute_script(f"window,scrollTo(0,{scroll})")
    time.sleep(3)


# browser.find_element(By.XPATH,"//p[text()='Agriculture']").click()
# time.sleep(2)
# browser.find_element(By.XPATH,'//span[@class="text14"]').click()
# time.sleep(2)
# browser.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(2)
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/main/div/div[3]/div/div[1]/div/div/form/div[1]/div[1]/div/div/div[1]/input').send_keys(100)
# time.sleep(2)
# browser.find_element(By.XPATH,'//div[@class="input-wrapper"][1]').click()
# time.sleep(2)
# browser.find_element(By.XPATH,'//li[text()="Units"]').click()
# time.sleep(2)
# browser.find_element(By.XPATH,'//input[@type="number"]').send_keys(10000)
# time.sleep(1)
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/main/div/div[3]/div/div[1]/div/div/form/div[2]/div/div[2]/span/div/div/div[1]/div/div').click()
# time.sleep(1)
# browser.find_element(By.XPATH,'//li[text()="INR"]').click()
# time.sleep(1)
# browser.find_element(By.XPATH,'//button[@type="submit"]').click()
# time.sleep(2)