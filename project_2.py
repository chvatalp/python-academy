import random
import time


def random_number():
    """Function generates 4 digits number."""
    return random.sample(range(0, 10), 4)


def bull_cow():
    """Wrapper of bull and cows game."""
    print('Hi there!')
    ran_num = random_number()
    print(ran_num)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    bulls = 0
    counter = 0
    start_time = int(time.time())

    while bulls != 4:
        counter += 1
        cows = 0
        bulls = 0
        input_num = input('Input 4 digit number, please: ')

        for i, x in enumerate(input_num):
            if int(x) == ran_num[i]:
                bulls += 1
            elif int(x) in ran_num:
                cows += 1
        print(f'There are {bulls} bull(s) and {cows} cow(s), number of '
              f'guesses: {int(counter)}.')

    end_time = int(time.time())
    total_time = end_time - start_time
    name = input('Please, enter your name: ')
    with open('leaderboard.txt', 'a+') as txt:
        txt.write(f'Name : {name} : number of guesses : {counter} '
                  f': total time : {total_time} \n')
    print('This is leaderboard sorted by name: ')
    with open('leaderboard.txt', 'r') as txt:
        board = [line.strip('\n') for line in txt.readlines()]
        print(sorted(board))
    print(f'Congratulation, {name}, you are master! It took you {int(counter)} '
          f'guess(es) '
          f'and {total_time} second(s).')


bull_cow()
