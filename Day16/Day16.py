#Day16, 29 November 2025, Managing Date & Times

from datetime import datetime, timedelta  #provide classes to manage date, time and duration

"""
datetime module provideds 3 classes:
datetime: date and time (year, month, day, hour, minute and seconds)
date: date(year, month, year)
timedelta: duration or difference betwee two date or datetime object
"""

#Guided Project: Project Deadline Setter
default_datetime_format = '%Y-%m-%d %H:%M:%S'

#1. Get the current date and time
start_time = datetime.now()
print(f"Current Time: {start_time.strftime(default_datetime_format)}")

#2. Defining the duration
deadline_duration = timedelta(days = 7, hours = 5, minutes = 30)

#3. Caclualte the exact deadline
deadline = start_time + deadline_duration

print(f"\nDeadline Duration: 7 Days, 5 hours, 30 minutes")
print(f"Project Deadline: {deadline.strftime(default_datetime_format)}")

#Self Project: program Tracker

#1. Define start date
program_start_date = datetime(2025, 10, 8, 0, 0, 0) #Year, Month, Date, Hour, Minutes, Seconds
program_end_date = program_start_date + timedelta(days = 30) #type is still datetime
current_date = datetime.now()

#2. Calculation
# Time elapsed
time_elapsed =  current_date - program_start_date
time_remaining = program_end_date - current_date

#3. Priting output

print(f"Total days elapsed: {time_elapsed.days}")
print(f"Total days remaining: {time_remaining}")

print(f"End Date: {program_end_date.strftime("%B %d, %Y")}")