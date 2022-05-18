##################### Normal Starting Project ######################

import pandas
from datetime import datetime
import random
import smtplib

MAIL = "xxx@gmail.com"
PASSWORD = "1234567890"

today = datetime.now()
today_tuple = (today.day, today.month)

data = pandas.read_csv("birthdays.csv")
bdays_dict = {(data_row.day, data_row.month): data_row for (index, data_row) in data.iterrows()}

if today_tuple in bdays_dict:
    bday_person = bdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(MAIL, PASSWORD)
    #     connection.sendmail(from_addr=MAIL, 
    #     to_addrs=bday_person["email"], 
    #     msg=f"Subject:Happy Birthday!\n\n{contents}")
    print(contents)
    




