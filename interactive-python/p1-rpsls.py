# Rock-paper-scissors-lizard-Spock
# http://www.codeskulptor.org/#user29_R2SIOyW89k_0.py

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    if "rock" == name:
        number = 0
    elif "Spock" == name:
        number = 1
    elif "paper" == name:
        number = 2
    elif "lizard" == name:
        number = 3
    elif "scissors" == name:
        number = 4
    else:
        number = -1
        print "Sorry, '" + name + "' you squeezed into the wrong game, didn't you?"

    return number

def number_to_name(number):
    if 0 == number:
        name = "rock"
    elif 1 == number:
        name = "Spock"
    elif 2 == number:
        name = "paper"
    elif 3 == number:
        name = "lizard"
    elif 4 == number:
        name = "scissors"
    else:
        name = "Anonymous Prime"
        print "Sorry, '" + str(number) + "' is not *the* number. Try again?"

    return name


def rpsls(player_choice):
    print
    print "Player chooses", player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 5)

    comp_choice = number_to_name(comp_number)

    print "Computer chooses", comp_choice

    delta = (comp_number - player_number) % 5
    if 1 == delta or 2 == delta:
        print "Computer wins!"
    elif 3 == delta or 4 == delta:
        print "Player wins!"
    elif 0 == delta:
        print "Player and computer tie!"
    else:
        print "What does it mean, 'exact change'? "

# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
