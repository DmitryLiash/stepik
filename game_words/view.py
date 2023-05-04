import text as te
import os
import time

def print_rulz():
    os.system('cls')
    print(te.hello_txt)
    print()
    time.sleep(6)

def display_lives(_tries):
    stages = ["\033[0;32m\U0001f90D \U0001f90D \U0001f90D \U0001f90D \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f90D \U0001f90D \U0001f90D \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f90D \U0001f90D \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f90D \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f90D \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f90D \033[0;0m",
              "\033[0;32m\U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \U0001f9E1 \033[0;0m"]
    return stages[_tries]

def print_visual_status_game(word: str, use_ch: list, use_worlds: list, lives: int):
   tem_words_list = []
   count = 0
   flag = None
   for i in range(len(word)):
      if word[i] in use_ch:
         count += 1
         tem_words_list.append(word[i])
      else:
         tem_words_list.append('_')
   os.system('cls')
   print()
   print()
   print(display_lives(lives))
   print()
   print('+' * (len(word) * 2 - 1))
   print(*tem_words_list, sep=' ') 
   print('+' * (len(word) * 2 - 1))
   print()
   print(f"{te.open_c} {use_ch}")
   print()
   print(f"{te.open_w} {use_worlds}")
   print()
   return count == len(word)
      
def print_dead(word: str):
   print()
   print(f"{te.dead}{word}")

def exit_txt():
   print()
   print(te.exit_txt)

def print_visual_won_pass(word: str, use_ch: list, use_worlds: list, lives: int):
   tem_words_list = list(word)
   os.system('cls')
   print()
   print()
   print(display_lives(lives))
   print()
   print('+' * (len(word) * 2 - 1))
   print(*tem_words_list, sep=' ') 
   print('+' * (len(word) * 2 - 1))
   print()
   print(f"{te.open_c} {use_ch}")
   print()
   print(f"{te.open_w} {use_worlds}")
   print()

   









