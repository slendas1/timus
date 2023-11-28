arr = list(map(int, input().split()))

min_ = 0
max_ = 0
strike = False
spare = False

for i in range(len(arr)):
    min_ += arr[i]
    max_ += arr[i]

if arr[-2] == 10 and arr[-1] > 20:
    min_ += 10


for i in range(len(arr) - 3):
    if arr[i] == 10:
        max_ += arr[i + 1]
        if arr[i + 1] == 10:
            max_ += arr[i + 2]

if arr[-3] == 10:
    max_ += arr[-2]
    if arr[-2] == 10:  
        max_ += min(arr[-1], 10)  
  
if arr[-2] == 10:
    max_ += min(arr[-1], 20)

print(min_, max_)