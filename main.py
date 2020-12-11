from datetime import datetime, timedelta

print("\nFirst, enter the date and time you woke up.")
print("Remember, you must enter the hours in military time format.\n")

w_year = int(input("Year: "))
w_month = int(input("Month: "))
w_day = int(input("Day: "))
w_hour = int(input("\nHour: "))
w_minute = int(input("Minutes: "))

wake_time = datetime(w_year, w_month, w_day, w_hour, w_minute)

print("\nNow, enter the date and time you slept.")

s_year = int(input("Year: "))
s_month = int(input("Month: "))
s_day = int(input("Day: "))
s_hour = int(input("\nHour: "))
s_minute = int(input("Minutes: "))

sleep_time = datetime(s_year, s_month, s_day, s_hour, s_minute)

difference = wake_time - sleep_time
print("\nYour sleep time is", difference)