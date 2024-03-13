# dateTime

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime


now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
print_date(now)    

# Time
print("********** CURRENT_TIME*******************")
current_time = time(21,40,0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print("********** CURRENT_DATE*******************")
current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

date_analysis = date(2023,3,9)
print(date_analysis.year)
print(current_date.month)
print(current_date.day)


# operation dates
year_2023 =  date(2020,8,1)
diff = year_2023
print(diff)


diff = year_2023.month
print(diff)


# Timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)

end_timedelta = timedelta(300, 100, 100, weeks=13)
print(start_timedelta)


