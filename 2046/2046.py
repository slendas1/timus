n = int(input())

def day_to_int(day):
    if day == 'Tuesday':
        return 0
    if day == 'Thursday':
        return 1
    return 2

def add_spaces(s):
    return s + ' ' * max(10 - len(s), 0)

def add_rows(splits, max_len):
    for split_ in splits:
        len_ = len(split_)
        for i in range(len_ + 1, max_len + 1):
            split_.append(' ' * 10)
    return splits

def indents(subject):
    split_ = []
    s = ''
    for word in subject.split():
        if s == '':
            s += word
        elif len(s + ' ' + word) > 10:
            split_.append(add_spaces(s))
            s = word
        else:
            s = s + ' ' + word

    split_.append(add_spaces(s))

    return split_

def transform(subjects):
    max_len = 0
    res = []
    for i in range(len(subjects)):
        split_ = indents(subjects[i])
        max_len = max(max_len, len(split_))
        res.append(split_)

    return add_rows(res, max_len)

main = [[''] * 3 for _ in range(4)]

for i in range(n):
    subject = input()
    day, lecture = input().split()
    day = day_to_int(day)
    lecture = int(lecture)
    main[lecture - 1][day] = subject


s = ('+' + '-' * 10) * 3 + '+'
for lecture in range(4):
    print(s)
    splits = transform(main[lecture])
    for s1, s2, s3 in zip(splits[0], splits[1], splits[2]):
        print('|' + s1 + '|' + s2 + '|' + s3 + '|')
print(s)