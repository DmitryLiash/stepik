import text as te
import model as m
import view as vi
import time
import os

def start():
    vi.print_rulz()
    lives = 6     
    use_words = []
    use_ch = []
    word = m.get_world().upper()
    win = None
    win2 = None
    while lives >= 0:
        win = vi.print_visual_status_game(word, use_ch, use_words, lives)
        print()
        if lives == 0:
            vi.print_dead(word)
            if m.is_valid_y_n():
                vi.exit_txt()
                time.sleep(3)
                os.system('cls')
                quit()
            else:
                lives, word, use_words, use_ch, win, win2 = m.clear()
                continue
        if win == True or win2 == True:
            vi.print_visual_won_pass(word, word, use_words, lives)
            print(f'{te.win}{6 - lives}')
            if m.is_valid_y_n():
                vi.exit_txt()
                time.sleep(3)
                os.system('cls')
                quit()
            else:
                lives, word, use_words, use_ch, win, win2 = m.clear()
                continue
        
        win2, lives, temp_use_world, temp_use_ch  = m.words_change_checker(word, lives, use_words, use_ch)
        
        if len(temp_use_world) > 0:
            use_words.append(temp_use_world)
        if len(temp_use_ch) > 0:
            use_ch.append(temp_use_ch)
    



