import smtplib, ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import logging
from _datetime import datetime

class LogGen:

    @staticmethod
    def loggen():
        timestr = datetime.now().strftime("%d-%m-%Y--%I:%M %p")
        date = datetime.now().strftime("%d-%m")
        day = datetime.now().strftime("%a")
        logger = logging.getLogger()
        '''if(day=="Mon"):
            fhandler = logging.FileHandler(filename="/home/admin7/Documents/Housekeeping_logs/Attendence-" + date + ".log", mode="a")'''

        fhandler = logging.FileHandler(filename="/home/admin7/Documents/Housekeeping_logs/Attendence-"+timestr+".log",
                                       mode="w")
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

    def send_mail(self):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "mailkartikey3101@gmail.com"  # Enter your address
        receiver_email = "kartikeygupta@tradeindia.com"  # Enter receiver address
        password = "#google#1997"
        message = """Subject: SCRIPT STOPPED

        The login script stopped please update password.
        """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


options = Options()
options.headless = True
log = LogGen.loggen()
holiday_lst=["01 Jan","26 Jan","18 Mar","11 Aug","15 Aug","24 Oct","25 Oct"]
date = datetime.now().strftime("%d %b")
log.info("Welcome Kartikey")
if(date in holiday_lst):
    pass
else:
    driver = webdriver.Chrome(executable_path="/home/admin7/Downloads/chromedriver_linux64/chromedriver",options=options)
    driver.get("http://housekeeping.tradeindia.com/housekeeping/")
    log.info("Housekeeping URL opened")
    driver.maximize_window()
    log.info("Window Maximized")
    driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div[3]/form/div[1]/input").send_keys("I-HONOIDA33036")
    log.info("Username Entered Properly")
    driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div[3]/form/div[2]/input").send_keys("madras@.income")
    log.info("Password Entered Properly")
    driver.find_element(By.NAME,"Login").click()
    log.info("Login Button Pressed")
    try:
            
        driver.find_element(By.XPATH,"//*[text()='Sorry! The Employee code or Password you entered is incorrect, Please go back and try again.']")
        log.info("PASSWORD EXPIRED. Please update it.")
        mail = LogGen()
        mail.send_mail()
    except:

        try:
            driver.get("http://housekeeping.tradeindia.com/housekeeping/")
            time.sleep(1)
            log.info("Screen Refreshed")
            driver.get("http://housekeeping.tradeindia.com/housekeeping/")
            time.sleep(1)
            log.info("Screen Refreshed")
            driver.get("http://housekeeping.tradeindia.com/housekeeping/")
            time.sleep(1)
            log.info("Screen Refreshed")
            driver.get("http://housekeeping.tradeindia.com/housekeeping/my_area/attendance_report.html")
            log.info("You are at attendence page")
            time.sleep(1)
            txt = driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[1]").text
            log.info("Welcome Message Obtained")
            log.info(txt)
            if("Welcome" in txt):
                driver.find_element(By.NAME,"submit").click()
                log.info("Attendence Submit button pressed")
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                log.info("Page scrolled to bottom")
                txt2 = driver.find_element(By.XPATH,"/html/body/div[2]/table[3]").text
                print(txt2)
                log.info(txt2)

        except NoSuchElementException:
            timestr = datetime.now().strftime("%d-%m-%Y--%I:%M %p")
            driver.save_screenshot("/home/admin7/Documents/Attendence/Attendence-" + timestr + ".png")
            log.info("Screenshot generated")
            mail = LogGen()
            mail.send_mail()
            driver.close()

        driver.get("http://housekeeping.tradeindia.com/intranet_logoff.html")
        time.sleep(2)
        log.info("User Logged Out from HouseKeeping")
        driver.close()
