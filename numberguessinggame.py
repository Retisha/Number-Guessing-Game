import random


number = random.randint(1, 9)
chances = 5
tries = 0

while(tries < 5):
    guess = int(input('guess a number between 1 and 9'))
    if guess == number:
        print('CONGRATULATIONS YOU WON!!!')
        break
    elif guess < number:
        print('your guess was too low, guess a number higher than ', guess)
    else:
        print('your number was too high, guess a number lower than ', guess)

    tries = tries+1


if(tries >= 5):
    print('you lose!!, the number is ', number)
