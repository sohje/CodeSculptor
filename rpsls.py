# Rock-paper-scissors-lizard-Spock
import random

def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return "Error! You should give number beetwen 0-4"
    
    #list_of_strings = ['rock', 'Spock', 'paper', 'lizard', 'scissors']
    #return list_of_strings[number]

def name_to_number(name):
    # convert number to a name using if/elif/else
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return "Error! Wrong input string", name

    #list_of_strings = ['rock', 'Spock', 'paper', 'lizard', 'scissors']
    #return list_of_strings.index(name)

def rpsls(name):
    # fill in your code below
    if name not in ['rock', 'Spock', 'paper', 'lizard', 'scissors']:
        print 'Error! Wrong input string: ', name
        return
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
    modulo = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if player_number == comp_number:
       winner = "Player and computer tie!"
    elif modulo <= 2:
       winner = "Player wins!"
    elif modulo > 2:
       winner = "Computer wins!"
    else:
       winner = "universe has collapsed?"
    print "Player chooses", name
    # convert comp_number to name using number_to_name
    print "Computer chooses", number_to_name(comp_number)
    # print results
    print winner
    print 
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")