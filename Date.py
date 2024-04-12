import datetime
s=datetime.datetime.now()
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
print(current_year)
print(current_month)
print(current_day)
print(s)
my_date = datetime.date(1993, 11, 18)
to_date = datetime.date(current_year,current_month,current_day)
print(my_date)
print(to_date)
print(to_date - my_date)