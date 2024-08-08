import datetime

day, month = map(int, input().split())
date = datetime.date(2009, month, day)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_of_week = days_of_week[date.weekday()]

print(day_of_week)
