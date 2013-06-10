# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
msg = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card = []

    def __str__(self):
        cards_list = ''
        for card in self.card:
            cards_list += str(card) + ' '
        return "Hand contains " + cards_list

    def add_card(self, card):
        return self.card.append(card)

    def get_value(self):
        hand_value = 0
        aces = 0
        for i in self.card:
            hand_value += VALUES.get(i.get_rank())
            if i.get_rank() == 'A':
                aces += 1
        if (aces >= 1) and (hand_value + 10 <= 21): hand_value += 10
        return hand_value
 
    def draw(self, canvas, pos):
        for c in self.card:
            c.draw(canvas, pos)
            pos[0] += 100

# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(suit,rank) for suit in SUITS for rank in RANKS]
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        cards_list = ''
        for card in self.deck:
            cards_list += str(card) + ' '
        return "Deck contains " + cards_list

deck = Deck()
player = Hand() 
dealer = Hand()
#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score, msg
    if in_play:
        score -= 1
    deck = Deck()
    player = Hand() 
    dealer = Hand()
    msg = ''    
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = 'Hit or stand?'
    in_play = True

def hit():
    global player, dealer, deck, score, in_play, outcome, msg
   
    if in_play:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            msg = "You lose"
            outcome = 'New deal?'
            in_play = False
            score -= 1
     
def stand():
    global player, dealer, score, in_play, deck, outcome, msg
    if in_play:
        while dealer.get_value() <= 17:
            dealer.add_card(deck.deal_card())

        if dealer.get_value() > 21:
            msg = "You won"
            score += 1
        elif dealer.get_value() >= player.get_value():
            msg = "You lose"
            score -= 1
        elif player.get_value() == 21 or player.get_value() > dealer.get_value():
            msg = "You won"
            score += 1
        outcome = "New deal?"
        in_play = False
            
# draw handler    
def draw(canvas):
    global in_play, score
    
    canvas.draw_text("Blackjack", [100, 100], 50, "White")
    canvas.draw_text("Dealer", [21, 180], 34, "Black")
    canvas.draw_text("Player", [21, 380], 34, "Black")
    canvas.draw_text(msg, [350, 380], 30, "Black")
    canvas.draw_text(outcome, [350, 180], 30, "Black")
    canvas.draw_text("Score: "+str(score), [350, 100], 30, "RED")
    dealer.draw(canvas, [21, 200])
    player.draw(canvas, [21,400])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [21 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

def init():
    global outcome, in_play, player, dealer, deck, score, msg
    if in_play:
        score -= 1
    deck = Deck()
    player = Hand() 
    dealer = Hand()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = 'Hit or stand?'
    in_play = True    

init()
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()