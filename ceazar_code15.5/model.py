import text as t


def is_valid_choise_min(ch: str) -> bool:
    return ch.isdigit() and 1 <= int(ch) <= 2

def is_valid_choise(start_str: str, midl_str: str, end_str: str) -> bool:
    print()
    print()
    print(start_str)
    while True:
        print()
        ch = input(midl_str)
        if is_valid_choise_min(ch):
            if int(ch) == 1:
                return True
            return False
        print(end_str)

def is_valid_secret_min(ch: str) -> bool:
    return ch.isdigit() and int(ch) != 0

def is_valid_secret(start_str: str, midl_str: str, end_str: str) -> int:
    print()
    print(start_str)
    while True:
        print()
        ch = input(midl_str)
        if is_valid_secret_min(ch):
            return int(ch)
        print(end_str)

def chec_lang(ch: str) -> bool:
    if ch.lower() in t.low_eng:
        return True
    return False

def chec_registr(ch: str) -> bool:
    if ch == ch.lower():
        return True
    return False

def programm_on_of1(value: int):  # True -zashifr
    print()
    text = input(t.inp_txt)
    for i in range(len(text)):
        if text[i].isalpha():
            if chec_lang(text[i]): 
                if chec_registr(text[i]):
                    print(t.low_eng[((t.low_eng.index(text[i])) + value) % 26], end= '')
                else:
                    print(t.up_eng[((t.up_eng.index(text[i])) + value) % 26], end= '')
            else:
                if chec_registr(text[i]):
                    print(t.low_rus[((t.low_rus.index(text[i])) + value) % 32], end= '')
                else:
                    print(t.up_rus[((t.up_rus.index(text[i])) + value) % 32], end= '')
        else: print(text[i], end='')

def programm_on_of2(value: int):   # False - rashifr
    print()
    text = input(t.inp_txt)
    for i in range(len(text)):
        if text[i].isalpha():
            if chec_lang(text[i]): 
                if chec_registr(text[i]):
                    print(t.low_eng[((t.low_eng.index(text[i])) - value) % 26], end= '')
                else:
                    print(t.up_eng[((t.up_eng.index(text[i])) - value) % 26], end= '')
            else:
                if chec_registr(text[i]):
                    print(t.low_rus[((t.low_rus.index(text[i])) - value) % 32], end= '')
                else:
                    print(t.up_rus[((t.up_rus.index(text[i])) - value) % 32], end= '')
        else: print(text[i], end='')
    
    
    


