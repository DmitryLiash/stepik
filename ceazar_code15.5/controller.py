import model as m
import view as v
import text as t
import time
import os


def start():
    v.hello_print()
    while True:
        flag = m.is_valid_choise(t.cho_start, t.cho_mid, t.cho_end)
        value_secret = m.is_valid_secret(t.sec_start, t.sec_mid, t.sec_end)
        if flag:
            m.programm_on_of1(value_secret)
        else:
            m.programm_on_of2(value_secret)
        
        if m.is_valid_choise(t.exit, t.exit2, t.exit3):
            v.goodbye()
            break
        else:
            os.system('cls')
            continue
            
        
        