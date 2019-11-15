from random import sample
from time import time


def return_random_num():
    """Function generates 4 digits number."""
    return sample(range(0, 10), 4)


def introduction():
    """Introduction to bulls and cows , returns random number"""
    print('Hi there!')
    ran_num = return_random_num()
    print(f"{ran_num}\n"
          f"I've generated a random 4 digit number for you.\n"
          f"Let's play a bulls and cows game.")
    return ran_num


def summary(st_time, count):
    """Summary at the end of game, takes name, prints results"""
    end_time = time()
    total_time = int(end_time - st_time)

    name = input('You won! Please, enter your name: ')

    print(f'Congratulation, {name}, you are master! It took you'
          f' {int(count)} guess(es) and {total_time} second(s).')

    with open('leaderboard.txt', 'a') as txt:
        txt.write(f'Name : {name} : number of guesses : {count} : total '
                  f'time : {total_time} \n')

    print('This is leaderboard sorted by name: ')

    with open('leaderboard.txt', 'r') as txt:
        board = [line.strip('\n') for line in txt.readlines()]
        print(sorted(board))


def input_func():
    random_num = introduction()
    counter = 0
    bulls = 0
    """Takes input from player, returns bulls, cows, counter"""
    while bulls != 4:
        bulls = 0
        cows = 0
        counter += 1
        input_num = input('Input 4 digit number, please: ')

        for i, x in enumerate(input_num):
            if int(x) == random_num[i]:
                bulls += 1
            elif int(x) in random_num:
                cows += 1

        print(f'There are {bulls} bull(s) and {cows} cow(s), number of '
              f'guesses: {int(counter)}.')
    return counter


def bull_cow():
    """Wrapper of bull and cows game."""
    start_time = time()
    counter = input_func()
    summary(start_time, counter)


bull_cow()
