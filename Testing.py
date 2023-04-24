import datetime

# Import actual date from webform
date_input = "2023-02-07 03:26:24 -0000"

# Split the <date_input> to a list and extract the values of date and time separately
new_date = date_input.split(" ")
date_only = new_date[0]
time_only = new_date[1]

# Split the <date_only> to a list and extract the values separately
splitted_date = date_only.split("-")
year = int(splitted_date[0])
month = int(splitted_date[1])
day = int(splitted_date[2])

# Use the <year>, <month> and <day> variable and determine if the date falls on a weekend
# If <date_input> falls on a Fri, Sat or Sun adjust the day to reflect next week's Monday
# Else if date falls on a weekdays, adjust +1 to date
date = datetime.date(year, month, day)
output_date = ""
if date.weekday() in range(4,7):
    try:
        while date.weekday() != 0:
            day += 1
            date = datetime.date(year, month, day)
    except ValueError:
        day = 1
        month += 1
        date = datetime.date(year, month, day)

    output_date = str(date) + " " + time_only
else:
    day += 1
    date = datetime.date(year, month, day)
    output_date = str(date) + " " + time_only

print(output_date)

