import time as ti
import text as te
import os


def hello() -> str:
    os.system('cls')
    print(te.hello)
    ti.sleep(2)
    print()
    print(te.u_name)
    name = input(te.u_name2)
    print()
    print(f"{te.f_name} {name} {te.f_name2}")
    ti.sleep(2)
    os.system('cls')
    return name


def question(name: str):
    os.system('cls')
    nothink = input(f"{name} {te.question}")
    print()

def load(value: int):
    for i in range(value):
        os.system('cls')
        print(f"{te.space} {'|||||' * i}")
        ti.sleep(1)
        os.system('cls')
    print(te.space_done)
    print()



