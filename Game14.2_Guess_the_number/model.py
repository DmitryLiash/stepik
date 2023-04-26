import text as t
import random



def add_name():
    name = input(t.enter_name)
    return name

def choice() -> int:
    print(t.nums_rulz_choice)
    value = input(t.choice)
    try:
        value = int(value)
        if 0 < value < 5:
            return value
        else:
            value = 5
            return value
    except:
        value = 5
        return value

def rulz_real(lvl: int):
    lvl_dict = {1:'голове', 2:'правом бедре', 3:'левой кисти', 4: 'голове'\
        , 12:'голове', 9:'правом бедре', 6:'левой кисти'}
    print()
    print(f'{t.real_rulz} {lvl_dict.get(lvl)} {t.real_rulz2}')
    return lvl

def enother_lvl_random() -> int:
    value = random.randrange(6, 13, 3)
    print()
    print(f"У тебя {value} попыток")
    return value


def game(lvl: int):
    value = random.randrange(101)
    count = 0
    while count < lvl:
        print()
        user_value = int(input('Введите число: '))
        if user_value == value:
            return True, value
        elif user_value > value:
            print('Не верно. Загаданное число меньше')
            count += 1
            print(f'У вас осталось {lvl - count} попыток')
        elif user_value < value:
            print('Не верно. Загаданное число больше')
            count += 1
            print(f'У вас осталось {lvl - count} попыток')
        else:
            print('хаха, число от 1 до 100 включительно')
            print(f'У вас осталось {lvl - count} попыток')
    return False, value



def won_game(value: int) -> bool:
    print(f'{t.won_value} {value}.')
    print()
    print(t.won_knife)
    print()

def choise_knife(body: int):
    body_dict = {1:'голову', 2:'правоe бедро', 3:'левую кисть', 4: 'голову'\
        , 12:'голову', 9:'правоу бедро', 6:'левую кисть'}
    print()
    print(f"{t.won_choise} {body_dict.get(body)},\n{t.won_choise2}")
    print()
    value = input('Введите действие: ')
    try:
        value = int(value)
        if 0 < value < 4:
            return value
        else:
            value = 5
            return value
    except:
        value = 5
        return value

    

        

