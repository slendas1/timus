import math

h, H, L = list(map(int, input().split()))

if H/2 < h:
    print(0)
else:
    sin_ = (2 * h/H) ** (1/3)
    cos_ = math.sqrt(1 - sin_ ** 2)
    print(cos_ * H/2 - cos_/sin_ * h)