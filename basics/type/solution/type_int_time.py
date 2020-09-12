SECOND = 1
MIN = 60 * SECOND
HOUR = 60 * MIN
DAY = 24 * HOUR

workday = 8 * HOUR
workweek = 5 * workday
workmonth = 22 * workday

print(f'Day: {DAY // SECOND} sec')
print(f'Day: {DAY // MIN} min')
print(f'Work day: {workday} sec')
print(f'Work week: {workweek // MIN} min')
print(f'Work month: {workmonth // HOUR} h')
