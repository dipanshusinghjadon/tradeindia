import toml
import re
import argparse
import datetime as dt
from random import randint
from io import StringIO

import pandas as pd
import requests as req

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

CREDS = toml.load("./creds.toml")
MAX_OUT_TIME = "19:00:00"
ENDPOINT = "SAMAY MADI NEEDS TO BE PLACED HERE"

class AttendanceDetailsFetch:
    URL = "https://housekeeping.tradeindia.com"
    BINARY_EXECUTABLE_PATH = './chromedriver'

    def __init__(self,**month_and_year) -> None:
        self.browser = webdriver.Chrome(executable_path=self.BINARY_EXECUTABLE_PATH)

        if month_and_year:
            for k,v in month_and_year.items():
                setattr(self,k,v)
        else:
            time = dt.datetime.now()
            self.month = time.strftime("%b")
            self.year = str(time.year)
    
    def login(self):
        self.browser.get(self.URL)
        
        username_field = self.browser.find_element(By.NAME,"username")
        username_field.send_keys(CREDS.get("USERNAME"))

        password_field = self.browser.find_element(By.NAME,"password")
        password_field.send_keys(CREDS.get("PASSWORD")+Keys.ENTER)

        for i in range(5):
            self.browser.get(self.URL)

    def route_to_attendance(self):
        my_area = self.browser.find_element(By.LINK_TEXT,"My Area")
        my_area.click()

        attendance_report = self.browser.find_element(By.LINK_TEXT,"Attendance Report")
        attendance_report.click()

        user_id_dropdown = self.browser.find_element(By.NAME,"user_id")

        emp_id = re.findall("\d+",CREDS.get("USERNAME"))

        if not emp_id:
            return
        
        user_id_selector = Select(user_id_dropdown)
        user_id_selector.select_by_value(emp_id[0])

        year_dropdown = self.browser.find_element(By.NAME,"year")
        
        year_selector = Select(year_dropdown)
        year_selector.select_by_value(self.year)

        month_dropdown = self.browser.find_element(By.NAME,"month")
        
        month_selector = Select(month_dropdown)
        month_selector.select_by_visible_text(self.month.title())

        submit = self.browser.find_element(By.NAME,"submit")
        submit.click()

    def fetch_attendance_record(self):
        attendance_table = self.browser.find_element(By.XPATH,"/html/body/div[2]/table[3]")
        return attendance_table.text

    def __del__(self):
        self.browser.quit()


class DataProcessor:
    updatable_records = {}

    def __init__(self,str_data):
        self.df = pd.read_csv(
            StringIO(str_data),
            sep=" ",
            usecols="Date In Out Hrs Neg_or_Pos".split(),
            index_col="Date",
            skip_blank_lines=True,
            skipfooter=1,
            engine="python"
        )

    @staticmethod
    def calc_neg_mins(time_string):
        time_list = time_string.strip("-").split(":")
        total_mins = int(time_list[0])*60
        total_mins += int(time_list[1])
        total_mins += float(f"0.{time_list[-1]}")
        
        return total_mins

    
    def find_negative_dates(self):
        for row in self.df.iterrows():
            data = row[-1]
            date = row[0]

            if data['Neg_or_Pos'] and '-' in data['Neg_or_Pos']:
                neg_mins = self.calc_neg_mins(data['Neg_or_Pos'])

                if neg_mins > 10:
                    self.updatable_records[date] = data,neg_mins
        
        return self.updatable_records,sum([record[-1] for record in self.updatable_records.values()])/60

    def correct_attendance(self):
        if not self.correct_attendance:
            raise Exception("Please find negative attendance dates first")

        sorted_neg_records = dict(sorted(self.updatable_records.items(),key=lambda record:record[-1][-1],reverse=True))

        for date,details in sorted_neg_records.items():
            details = details[0]
            if not details['Out']:
                out_time = dt.datetime.strptime(f"18:{randint(1,60)}:{randint(1,60)}","%H:%M:%S%")
            else:
                out_time = dt.datetime.strptime(details['Out'],"%H:%M:%S")
            
            max_out_time = dt.datetime.strptime(MAX_OUT_TIME,"%H:%M:%S")
            
            difference = (max_out_time - out_time).seconds / 60

            temp_time = dt.timedelta(
                minutes = randint(int(difference - 5), int(difference)),
                seconds = randint(1,60)
            )

            self.hit_attendance_correction_api(
                date = date,
                old_out_time = out_time.strftime("%H:%M:%S"),
                new_out_time = (out_time + temp_time).strftime("%H:%M:%S")
            )

    @staticmethod
    def hit_attendance_correction_api(date,old_out_time,new_out_time):
        print(F"CORRECTING ATTENDANCE FOR {date} FROM {old_out_time} TO {new_out_time}")
#        req.get(
#            ENDPOINT.format_map(
#                dict(
#                    DATE = date,
#                    USERNAME = CREDS.get("USERNAME"),
#                    TIME = new_out_time            
#                )
#            )
#        )


if __name__ == '__main__':

    parser=argparse.ArgumentParser()

    parser.add_argument(
        "-month", 
        help = "month of which attendance needs to be fetched", 
        default = dt.datetime.now().strftime("%b"),
        choices="jan feb mar apr may jun jul aug sep oct nov dec".title().split()
    )

    parser.add_argument(
        "-year", 
        help = "year of which attendance needs to be fetched", 
        default = dt.datetime.now().year,
    )

    args=parser.parse_args()

    month_and_year = {}

    if args.month:
        month_and_year['month'] = args.month
    
    if args.year:
        month_and_year['year'] = str(args.year)

    fetcher_obj = AttendanceDetailsFetch(**month_and_year)
    fetcher_obj.login()
    fetcher_obj.route_to_attendance()
    attendance_records = fetcher_obj.fetch_attendance_record()

    dp = DataProcessor(attendance_records.replace("Remarks","Neg_or_Pos"))
    updatable_records,_ = dp.find_negative_dates()
    dp.correct_attendance()
