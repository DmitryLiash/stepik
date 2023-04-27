import text as te
import random

def random_choise():
    value = random.randint(1, 20)
    print(te.answer)
    print(te.words_dict.get(value))

def exit() -> bool:
    print()
    print(te.exit0)
    print()
    print(te.exit1)
    answer = is_valid_num()
    return answer


def is_valid(s):
    return s.isalpha() and s in te.valid_answer

def is_valid_num():
    while True:
        n = input(te.answer2)
        if is_valid(n):
            if n in 'Yy':
                return True
            return False
        print(te.exit2)


