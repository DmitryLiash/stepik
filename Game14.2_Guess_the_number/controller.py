import view as v
import model as m
import time
import os

def start():
    os.system('cls')
    v.wake_up()
    time.sleep(3)
    print()
    v.wake_up2()
    time.sleep(2)
    v.name_print()
    time.sleep(1)
    print()
    name = m.add_name()
    print()
    v.hello_print(name)
    print()
    v.rulz_game()
    print()
    value_choice = m.choice()
    v.slep_before()
    flag = None
    value = None
    body_part = None
    if value_choice == 1:
        print()
        body_part = m.rulz_real(value_choice)
        flag, value = m.game(12)
    elif value_choice == 2:
        print()
        body_part = m.rulz_real(value_choice)
        flag, value = m.game(9)
    elif value_choice == 3:
        print()
        body_part = m.rulz_real(value_choice)
        flag, value = m.game(6)
    elif value_choice == 4:
        v.exit_lol()
        time.sleep(2)
        print()
        body_part = m.rulz_real(value_choice)
        time.sleep(1)
        flag, value = m.game(12)
    else:
        v.simbol_enother()
        print()
        rand_lvl = m.enother_lvl_random()
        print()
        body_part = m.rulz_real(rand_lvl)
        flag, value = m.game(rand_lvl)
       
        
    
    if flag:
        time.sleep(1)
        os.system('cls')
        m.won_game(value)
        time.sleep(3)
        new_choice = m.choise_knife(body_part)
        if new_choice == 1:
            os.system('cls')
            print(v.operration(body_part))
            time.sleep(5)
            v.rip()
            time.sleep(9)
        elif new_choice == 2:
            v.print_load(6)
            time.sleep(1)
            os.system('cls')
            v.sound_dead()
            time.sleep(1)
            v.rip()
            time.sleep(6)
        elif new_choice == 3:
            v.makgaver(5, body_part)
            time.sleep(8)
            os.system('cls')
            v.sound_dead()
            time.sleep(1)
            v.rip()
            time.sleep(6)
        else:
            v.f_u()
            v.print_load(6)
            time.sleep(1)
            os.system('cls')
            v.sound_dead()
            time.sleep(1)
            v.rip()
            time.sleep(6)
    else:
        time.sleep(1)
        os.system('cls')
        v.print_value_secret(value)
        print()
        v.print_load(5)
        v.sound_dead()
        time.sleep(1)
        v.rip()
        time.sleep(7)
