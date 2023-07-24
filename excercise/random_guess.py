import random
print('Please guess a random number between 1 and 100 \n')
guess_limit = 5
while guess_limit > 0:
    guess_limit = guess_limit - 1
    nm = input();
    g = random.randint(0, 101)
    #print(g)
    if nm == 'q':
        break
    if g < int(nm):
        print(f'Your guess is too high.')
    elif g > int(nm):
        print('Your guess is low')
    else:
        print('HEY you got it')
