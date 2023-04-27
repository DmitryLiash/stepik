import random
ex = 0
f1 = 0
s2 = 0 
t3 = 0
f4 = 0
f5 = 0
s6 = 0
s7 = 0
e8 = 0
while ex < 1000000:
    l = 1; r = 100
    n = (l + r)  //  2
    num = random.randint(l, r)
    c = 0
    while True:
        c += 1
        if n > num:
            r = n - 1
            n = (l + r) // 2
        elif n < num:
            l = n + 1
            n = (l + r)  //  2
        elif n == num:
            ex += 1
            if c == 1:
                f1 += 1
            elif c == 2:
                s2 += 1
            elif c == 3:
                t3 += 1
            elif c == 4:
                f4 += 1
            elif c == 5:
                f5 += 1
            elif c == 6:
                s6 += 1
            elif c == 7:
                s7 += 1
            elif c == 8:
                e8 += 1
            break
print(f"1-{f1}_2-{s2}_3-{t3}_4-{f4}_5-{f5}_6-{s6}_7-{s7}_8-{e8}")
