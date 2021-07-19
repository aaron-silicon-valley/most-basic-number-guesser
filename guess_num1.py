import random


l = list(range(1, 11))
num_l = random.choice(l)

guess_num = num_l


g = input('enter the guess number '+ 'numbers are from {}: '.format(l))
while True:
  if int(g) == guess_num:
    print('you got the number congratulations')
    print(guess_num)
    break
  else:
    print('sorry try again')
    # print(guess_num)
    g = input('enter the guess number: ')
    continue

