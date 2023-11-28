s0 = input()
s1 = input()


a = s0 + '#' + s1
s1_start = len(s0) + 1


p = [0] * len(a)

for i in range(1, len(a)):
    k = p[i - 1]
    while k > 0 and a[i] != a[k]:
        k = p[k - 1]
    if a[i] == a[k]:
        k += 1
    p[i] = k

p_s1 = p[s1_start:]



if 0 in p_s1:
    print('Yes')
else:
    res = []
    i = len(p_s1) - 1
    while i >= 0:
        res.append(s1[i - p_s1[i] + 1: i + 1])
        i = i - p_s1[i]
    print('No')
    print(' '.join(res[::-1]))