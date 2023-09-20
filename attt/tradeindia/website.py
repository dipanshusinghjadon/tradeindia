#! /home/user01/miniconda3/envs/sele/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains


usernameStr = 'hasan.fauwad@tradeindia.com'
passwordStr = 'info@12india'
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
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/section[2]/div/div[2]/div/div[3]/button').click()
time.sleep(2)
browser.get(('https://www.tradeindia.com'))
browser.execute_script("return document.body.scrollHeight")
scroll_down = 300
#scroll_up = 1300
for scroll_down in range(0,150,50):
    browser.execute_script(f"window,scrollBy(0,{scroll_down})")
    print(scroll_down)
    time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/main/div/div[1]/div[1]/div[2]/span/div/a/span').click()
time.sleep(2)
# categories = browser.find_element(By.CSS_SELECTOR,'#__next > div > div > main > div > div > div.row.mt-3 > div:nth-child(1) > div > div.cat-det-wrp > a').click()
# time.sleep(4)
categories = ["Agriculture", "Apparel & Fashion", "Automobile", "Brass Hardware & Components", "Chemicals",
              "Computer Hardware & Software", "Construction & Real Estate", "Consumer Electronics", 
              "Electronics & Electrical Supplies", "Energy & Power", "Environment & Pollution", 
              "Food & Beverage", "Furniture", "Gifts & Crafts", "Health &  Beauty", "Home Supplies",
              "Home Textiles & Furnishings","Hospital & Medical Supplies","Hotel Supplies & Equipment",
              "Industrial Supplies","Jewelry & Gemstones","Leather & Leather Products","Machinery",
              "Mineral & Metals","Office & School Supplies","Packaging & Paper","Pharmaceuticals",
              "Pipes, Tubes & Fittings","Plastics & Products","Printing & Publishing","Scientific & Laboratory Instruments",
              "Security & Protection","Sports & Entertainment","Telecommunications","Textiles & Fabrics","Toys","Transportation"]

# Loop through the categories and click on each one
for i,category in enumerate(categories):
    # Wait for the category element to be clickable
    if i != 0 and i % 15 == 0:
        # print("#####")
        browser.execute_script(f"window.scrollBy(0,1500)")

    category_element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, category)))
    
    # Click on the category element
    category_element.click()
        
    # Wait for the page to load
    WebDriverWait(browser, 5).until(EC.title_contains(category))
    time.sleep(3)
    browser.back()
    time.sleep(5)

# scroll_down = 50
# #scroll_up = 1300
# for scroll_down in range(0,50,10):
#     browser.execute_script(f"window,scrollBy(0,{scroll_down})")
#     print(scroll_down)
#     time.sleep(1)

