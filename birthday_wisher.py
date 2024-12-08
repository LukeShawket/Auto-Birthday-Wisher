import datetime
import pandas
import smtplib


my_mail = "example@example.com"
my_password = "examplepassword"

# Your local directory should contain 2 different files:
# 1) birthdays.csv - this file should contain 4 different column: name,email,month,day
# 2) wish.txt - this is a mail content.
birthday_wish = "wish.txt"

today_month = datetime.datetime.now().month
today_day = datetime.datetime.now().day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

# creating a new dictionary that contains birthday as key
birthday_dict = {(key["month"], key["day"]) : (key["name"], key["email"]) for index, key in data.iterrows()}
if today in birthday_dict:
    persons_name = birthday_dict[today][0]
    persons_email = birthday_dict[today][1]
    with open(birthday_wish) as file:
        content = file.read()
        personalized_content = content.replace("[NAME]", persons_name)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_mail, password=my_password)
        connection.sendmail(from_addr=my_mail, to_addrs=persons_email, msg=f"Subject:Happy Birthday\n\n"
                                                                            f"{personalized_content}")

