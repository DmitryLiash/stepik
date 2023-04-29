import text as t
import random as r
import time as ti
import os



def is_valid_y_n_mini(ch: str) -> bool:
    return ch.isalpha() and ch in t.valid_answer

def is_valid_y_n(mystr: str, myst_final: str) -> bool:
    print()
    print(mystr)
    while True:
        print()
        ch = input(t.move)
        if is_valid_y_n_mini(ch):
            if ch in t.valid_answer_yes:
                return True
            return False
        print(myst_final)




def is_valid(s: str, a: int, b: int):
    return s.isdigit() and a <= int(s) <= b

def is_valid_num(a: int, b: int, txt1: str, txt2: str) -> int:
    while True:
        print()
        n = input(txt1)
        if is_valid(n, a, b):
            return int(n)
        print(txt2)

def generation_pi_dict_lengt_size():
    magich_chairs = ''
    length_pas_int = is_valid_num(5, 15, t.question1, t.ques1_exept)
    nums_y_n = is_valid_y_n(t.question2, t.exit1)
    abc_low = is_valid_y_n(t.question3, t.exit1)
    abc_uper = is_valid_y_n(t.question4, t.exit1)
    simbol = is_valid_y_n(t.question5, t.exit1)
    same_like_simbol = is_valid_y_n(t.question6, t.exit1)
    count_pas_int = is_valid_num(1, 100, t.question1_2, t.ques1_exept1_2)
    if nums_y_n:
        magich_chairs += t.digits
    if abc_low:
        magich_chairs += t.low_let
    if abc_uper:
        magich_chairs += t.up_let
    if simbol:
        magich_chairs += t.punct
    if same_like_simbol:
        for sim in t.spec_simbol_no:
            magich_chairs = magich_chairs.replace(sim, '')
    return magich_chairs, length_pas_int, count_pas_int

def final_generation_pi(ch_dict: str, length: int) -> str:
    creat_pass = ''
    for _ in range(length):
        creat_pass += r.choice(ch_dict)
    return creat_pass

    

def count_generation_pi(ch_dict: str, length: int, count: int):
    os.system('cls')
    for i in range(1, count + 1):
        pas_new = final_generation_pi(ch_dict, length)
        print()
        print(f"Пароль № {i}.{pas_new}")

def load(value: int):
    for i in range(value):
        os.system('cls')
        print(f"{t.space} {'|||||' * i}")
        ti.sleep(1)
        os.system('cls')
    print(t.space_done)
    print()
    
def print_hello():
    os.system('cls')
    print(t.hello)

