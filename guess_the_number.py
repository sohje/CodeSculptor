# "Guess the number" mini-project
import math
import random
import simplegui

num_range = 100

# define event handlers for control panel
def init():
    """ some magic """
    global secret_number, rem_guesses
    print "New game. Range is from 0 to", num_range
    secret_number = random.randrange(0,num_range)
    rem_guesses = math.ceil(math.log(num_range,2))
    print "Number of remaining guesses", rem_guesses
    print
    
def range100():
    """ button that changes range to range [0,100) and restarts """
    global num_range
    num_range = 100
    init()
        
def range1000():
    """ button that changes range to range [0,1000) and restarts """
    global num_range
    num_range = 1000
    init()
    
def get_input(guess):
    """ main game logic goes here """
    global num_range, rem_guesses
    if not guess.isdigit():
        print "Hey, guess the number please!!\n"
        return
    rem_guesses -= 1
    print "Guess was", guess
    if float(guess) == secret_number:
        print "Number of remaining guesses", rem_guesses
        print "Correct!\n"
        init()
    elif (float(guess) > secret_number and rem_guesses > 0):
        print "Number of remaining guesses", rem_guesses
        print "Lower!\n"
    elif (float(guess) < secret_number and rem_guesses > 0):
        print "Number of remaining guesses", rem_guesses
        print "Higher!\n"
    else:
        print "Number of remaining guesses", rem_guesses
        print "You ran out of guesses. The number was", secret_number
        print
        init()
        
f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

init()
f.start()