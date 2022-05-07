'''
 Paul Park
 Monday, June 22nd, 2020
 My first Rock Paper Scissors Game
'''

# import random
import time
from random import randint

# list of options
options = ["rock", "paper", "scissors"]
#           0    ,   1    ,     2
count_trys = 0
count_total = 0
# computer plays
computer = options[randint(0, 2)]

user = input("Welcome to my first game\nRock Paper Scissors.... \nShoot!!!\nYour Choice: ").lower()
print("Computer chose: ", computer)
# is there a way to not write all 6 possible ways for the user and computer to give answer?
if computer == user:
    print("Draw!")
    count_total += 1
elif user == "rock" and computer == "paper":
    print("GG.\nYou lost")
    count_total += 1
elif user == "rock" and computer == "scissors":
    print("You won!")
    count_trys += 1
    count_total += 1
elif user == "paper" and computer == "rock":
    print("You won!")
    count_trys += 1
    count_total += 1
elif user == "paper" and computer == "scissors":
    print("GG.\nYou lost")
    count_total += 1
elif user == "scissors" and computer == "rock":
    print("GG.\nYou lost")
    count_total += 1
elif user == "scissors" and computer == "paper":
    print("You won!")
    count_total += 1
    count_trys += 1
else:
    print("Sorry I cant understand that...")
final = input("One more? ('y' or'n') \n").lower()
while final == 'y':
    computer = options[randint(0, 2)]

    user = input("Rock Paper Scissors.... \nShoot!!!\nYour Choice: ").lower()
    print("Computer chose: ", computer)
    # is there a way to not write all 6 possible ways for the user and computer to give answer?
    if computer == user:
        print("Draw!")
        count_total += 1
    elif user == "rock" and computer == "paper":
        print("GG.\nYou lost")
        count_total += 1
    elif user == "rock" and computer == "scissors":
        print("You won!")
        count_trys += 1
        count_total += 1
    elif user == "paper" and computer == "rock":
        print("You won!")
        count_trys += 1
        count_total += 1
    elif user == "paper" and computer == "scissors":
        print("GG.\nYou lost")
        count_total += 1
    elif user == "scissors" and computer == "rock":
        print("GG.\nYou lost")
        count_total += 1
    elif user == "scissors" and computer == "paper":
        print("You won!")
        count_total += 1
        count_trys += 1
    else:
        input("Sorry I cant understand that...")
        exit()
    final = input("One more? ('y' or'n') \n").lower()
while final == "n":
    print("Good game!")
    print("you have won ", count_trys, " games out of ", count_total)
    average = (count_trys / count_total) * 100
    print("your accuracy is", average, "%")
    press_enter = input("press enter to quit!")
    exit()
