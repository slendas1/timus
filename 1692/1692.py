import math
from collections import defaultdict

n = int(input())
k = math.floor((1 + math.sqrt(1 + 8 * n))/2)
d = defaultdict(list)
color = 1

print(k)
for flag1 in range(1, k + 1):
    for flag2 in range(flag1 + 1, k + 1):
        d[flag1].append(color)
        d[flag2].append(color)
        color += 1
    print(k - 1, ' '.join(map(str, d[flag1])))