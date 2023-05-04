import text as te
import random
import view as v


def get_world() -> str:
    words = te.words_list[random.randint(1, 50)].upper()
    return words

def rus_check(u_input: str):
    n = len([i for i in u_input if i in te.up_rus])
    return n == len(u_input)


def check_len_abc(input: str, word: str) -> bool:
    return len(input) == len(word) and input.isalpha() or len(input) == 1 and input.isalpha()


def chech_abc(ch: str) -> bool:
    return len(ch) == 1  # and ch in te.up_rus

def words_change_checker(word: str, lives: int, use_word: list, use_ch: list):
    ch = ''
    check_word = ''
    win = False
    while True:
        print()
        u_input = input(te.enter_checker).upper()
        if rus_check(u_input):
            if check_len_abc(u_input, word):
                if chech_abc(u_input):
                    if u_input not in use_ch:
                        if u_input in word:
                            ch += u_input
                            return win, lives, check_word, ch
                        else:
                            ch += u_input
                            lives += -1
                            return win, lives, check_word, ch
                    else:
                        print(te.enter_error)
                else:
                    if u_input not in use_word:
                        if u_input == word:
                            win = True
                            return win, lives, check_word, ch
                        else:
                            check_word += u_input
                            lives += -1
                            return win, lives, check_word, ch
                    else:
                        print(te.enter_error_w)
            else:
                print(te.enter_error_1st)
        else:
                print(te.enter_error_1st)

def is_valid_y_n_mini(ch: str) -> bool:
    return ch.isalpha() and ch in te.valid_answer

def is_valid_y_n() -> bool:
    print()
    print(te.exit_yes_no)
    while True:
        print()
        ch = input(te.move)
        if is_valid_y_n_mini(ch):
            if ch in te.valid_answer_yes:
                return True
            return False
        print(te.yes_no_error)

def clear():
    lives = 6
    word = get_world().upper()
    use_words = []
    use_ch = []
    win = None
    win2 = None
    return lives, word, use_words, use_ch, win, win2
