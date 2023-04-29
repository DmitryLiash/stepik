import model as m
import time as t
import text as te
import os 

def start():
    m.print_hello()
    print()
    while True:
        elements_str, size, count = m.generation_pi_dict_lengt_size()
        m.load(5)
        m.count_generation_pi(elements_str, size, count)
        if m.is_valid_y_n(te.ques_exit, te.exit2):
            break
        os.system('cls')


