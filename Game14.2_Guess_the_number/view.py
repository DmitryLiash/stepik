import text as t
import time 
import os
import random
def wake_up():
    print(t.wake_up1)

def wake_up2():
    print(t.wake_up2)

def name_print():
    print(t.u_name)

def hello_print(name):
    print(f'{t.main_menu1} {name} {t.main_menu2}')

def rulz_game():
    print(t.rulz_game)

def exit_lol():
    print()
    print(t.exit_lol)

def simbol_enother():
    print()
    print(t.enother_simbol)

# def rulz_real():
#     print(t.real_rulz)

def print_load(ran: int):
    for i in range(1, ran + 1):
        print(f"Вы ждете, вы дрожите{' Хнык ' * i}")
        time.sleep(1)

def slep_before():
    os.system('cls')
    print(t.after_choice_s)
    time.sleep(3)
    print()
    print(t.after_choice_w)

def print_value_secret(value: int):
    print(f'Хммм.. Правильный ответ был {value}')

def rip():
    rip_dict = {1: t.dead_1, 2: t.dead_2, 3: t.dead_3, 4: t.dead_4}
    print()
    print(rip_dict.get(random.randint(1,4)))

def sound_dead():
    print()
    print(t.sound_dead)

def operration(boddy_part: int):
    body_dict = {1:'голову', 2:'правоe бедро', 3:'левую кисть', 4: 'голову'\
        , 12:'голову', 9:'правое бедро', 6:'левую кисть'}
    print(f"{t.operation_1} {body_dict.get(boddy_part)}.\n{t.operation_2}")
    print()
    print(t.no_god_no)

def f_u():
    print()
    print(t.f_u)

def makgaver(ran: int, boody: int):
    body_dict = {1:'голову', 2:'правоe бедро', 3:'левую кисть', 4: 'голову'\
        , 12:'голову', 9:'правое бедро', 6:'левую кисть'}
    print(f"{t.lol1} {body_dict.get(boody)} {t.lol2}")
    print()
    time.sleep(2)
    print()
    print(t.lol3)
    print()
    time.sleep(2)
    for i in range(1, ran + 1):
        print(f"{' ХА-' * i}")
        time.sleep(1)
    print()
    print(t.lol4)
    
    

    
