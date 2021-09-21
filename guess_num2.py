import random

def guess_the_number():
    l = list(range(1, 11))
    num_l = random.choice(l)
    guess_num = num_l
    g = input('enter the guess number, '+ 'numbers are from {}: '.format(l))
    while True:
        if g.isnumeric() == False:
            print(f'yo this is for numbers not for {g}')
            g = input('enter the guess number ' + 'numbers are from {}: '.format(l))
        elif g.isnumeric() == True:
            if int(g) == guess_num:
                print('you got the number congratulations')
                print(guess_num)
                break
            else:
                print('sorry try again')
                # print(guess_num)
                g = input('enter the guess number: ')
                continue
        elif g.isspace():
            print('you know that this is a game for numbers and not spaces')
            g = input('enter the guess number ' + 'numbers are from {}: '.format(l))


guess_the_number()

