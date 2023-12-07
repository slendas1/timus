def stage(i):
    k = 0
    while i % 2 == 0:
        i = i >> 1
        k += 1
    return k
    

def count_degree_k(l, r, k):
    count = r - l + 1 >> k

    if stage(r - l + 1) >= k:
        return count
    
    rem1 = l & (1 << k) - 1
    rem2 = r & (1 << k) - 1
    if rem1 == 0:
        return count + 1
    
    if rem2 < rem1:
        return count + 1
    return count

def run(a, b):
    if b < a:
        a, b = b, a
    res = 0
    if b - a >= 2:
        for i in range(30, 1, -1):
            res += 2 * (count_degree_k(a + 1, b - 1, i) - count_degree_k(a + 1, b - 1, i + 1)) * (i - 1) 
    res += max(stage(a) - 1, 0)
    res += max(stage(b) - 1, 0)

    if a == b:
        res = 0


    return res

a, b = list(map(int, input().split()))
print(run(a, b))