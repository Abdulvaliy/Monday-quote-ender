import smtplib
import datetime as dt
import random

my_email = "your_account_goes_here@gmail.com"
password = "your_password"

now = dt.datetime.now()   # date of present moment
year = now.year
month = now.month
day_of_week = now.weekday()


with open("quotes.txt") as data:
    lines = data.readlines()
    random_quotes = random.choice(lines)
    # print(random_quotes)


if day_of_week == 0:   #if a day is monday (as 0)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="receipent_account@gmail.com",
            msg=f"Subject:Monday Motivational Quote\n\nAssalamu alaykum, Alhamdulillah for a new day, new life and "
                f"new chances. \n\n{random_quotes} "
        )

















# date_of_week = dt.datetime(year=2021, month=7, day=25)
# # print(date_of_week.weekday())    #fixed date