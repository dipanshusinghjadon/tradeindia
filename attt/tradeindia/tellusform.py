#! /home/user01/miniconda3/envs/sele/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


usernameStr = 'deep.mala@tradeindia.com'
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
n = browser.find_element(By.CSS_SELECTOR,'#__next > div > div > main > div > div.ti-container.bx-brd-box > div.mb-4.mb-md-4.row.pt-md-3 > div.col-xl-2.order-xl-0.mt-xl-0.mt-md-5.mt-3 > span > div > ul > li:nth-child(10) > div > div > div.row > div:nth-child(2) > a:nth-child(2) > p')
time.sleep(2)
a.move_to_element(n).click().perform()
time.sleep(3)

browser.find_element()

# topcat = ["Tulsi Tea","Ginger Tea","Masala Green Tea","Instant Masala Tea"]

# for i,category in enumerate(top_cat):
#     # Wait for the category element to be clickable
#     if i != 0 and i % 4 == 0:
#         print("#####")
#         browser.execute_script(f"window.scrollBy(0,1500)")

# category_element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, topcat)))
    
#     # Click on the category element
# category_element.click()
    
# # Wait for the page to load
# WebDriverWait(browser, 5).until(EC.title_contains(category))
# time.sleep(3)
# browser.back()
# time.sleep(5)



# browser.execute_script("return document.body.scrollHeight")
# for scroll in range(0,1500,300):
#     browser.execute_script(f"window,scrollTo(0,{scroll})")
#     time.sleep(3)


