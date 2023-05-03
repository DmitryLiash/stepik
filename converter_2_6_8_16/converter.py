import os

def check_code_type():
    while True:
        print()
        code = input('Введите тип исходного кода(2, 4, 8, 16): ')
        if code in ['2', '4', '8']:
            return True,  int(code)
        elif code in ['16']:
            return False, int(code)
        else:
            print()
            print('Ошибка ввода. Введите 2, 4, 8, 16 ')
            print()

def checker_2_code(value: str) -> bool:
    count = 0
    for i in range(len(value)):
        if value[i] in '01':
            count += 1
    return count == len(value)

def converter_2_4_8_to_10(code: int) -> int:
    while True:
        print()
        value = input(f'Введите число в {code} коде: ')
        answer = 0
        if checker_2_code(value):
            for i in range(len(value)):
                    answer += int(value[i]) * int(code) ** (len(value) - 1 - i)
            print()
            print('Ответ:')
            print(answer)
            break
        else:
            print('ошибка ввода числа')

def checker_16_code(value: str) -> bool:
    count = 0
    for i in range(len(value)):
        if value[i] in '0123456789ABCDEF':
            count += 1
    return count == len(value)

def create_16_code(value: str) -> list:
    value_list = []
    code_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }
    for el in value:
        if el in code_dict.keys():
            value_list.append(code_dict.get(el))
        else:
            value_list.append(int(el))
    return value_list   


def converter_16_to_10(code: int) -> int:
    while True:
        print()
        value = input('Введите число в 16 коде: ')
        answer = 0
        if checker_16_code(value):
            value_list = create_16_code(value)
            for i in range(len(value_list)):
                answer += value_list[i] * int(code) ** (len(value) - 1 - i)
            print()
            print('Ответ:')
            print(answer)
            break
        else:
            print('ошибка ввода числа')

def is_valid(s: str):
    return s.isalpha() and s in 'YyNn'

def is_valid_num():
    while True:
        n = input('Введите ваше действие: ')
        if is_valid(n):
            if n in 'Yy':
                return True
            return False
        print('Ошибка ввода( Y - Выход, N - продолжить)')

def exit() -> bool:
    print()
    print('Хотите выйти или продолжить( Y - Выход, N - продолжить )')
    answer = is_valid_num()
    return answer
        


while True:
    flag, code = check_code_type()
    if flag:
        converter_2_4_8_to_10(code)
    else:
        converter_16_to_10(code)
    if exit():
        os.system('cls')
        break
    else:
        continue