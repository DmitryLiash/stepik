up_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_eng = 'abcdefghijklmnopqrstuvwxyz'

def chec_registr(ch: str) -> bool:
    if ch == ch.lower():
        return True
    return False

abc = input().split()
new_one = []

for el in abc:
    size = len([i for i in el if i.isalpha() == True])
    mini_new = ''
    for i in range(len(el)):
        if el[i].isalpha():
            if chec_registr(el[i]):
                mini_new += low_eng[((low_eng.index(el[i])) + size) % 26]
            else:
                mini_new += up_eng[((up_eng.index(el[i])) + size) % 26]
        else: mini_new +=  el[i]
    new_one.append(mini_new)

print(*new_one, sep= ' ')