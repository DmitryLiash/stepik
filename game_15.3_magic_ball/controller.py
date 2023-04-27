import view as v
import model as m


def start():
    user_name = v.hello()
    while True:
        v.question(user_name)
        v.load(7)
        m.random_choise()
        flag = m.exit()
        if flag:
            break
        continue
