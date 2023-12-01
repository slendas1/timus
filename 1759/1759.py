from datetime import datetime, timedelta

n = int(input())

def str_to_date(date):
    parts = list(map(int, date.split('.')))[::-1]
    return datetime(*parts)

max_ = timedelta(0)
ind = 1
end = datetime.now()
for i in range(n):
    dates = dates = list(map(str_to_date, input().split()))
    
    if (dates[2] - dates[0]).days > max_.days:
        max_ = dates[2] - dates[0]
        ind = i + 1
        end = dates[2]
    elif (dates[2] - dates[0]).days == max_.days and dates[2] < end:
        ind = i + 1
        end = dates[2]
print(ind)