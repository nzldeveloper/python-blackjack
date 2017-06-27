#a text based BlackJack game in Python
#player start out with 100 in money
#Player can hit or stand

import random

bet = 0

class Player(object):
    def __init__(self, money=100):
        self.money = money
    
    def addMoney(self):
        return self.money + bet

class Cards(object):
    suits = ["Spades", "Hearts", "Diamond", "Clubs"]
    
    #keeping the points in tuple allows first value of tuple to be the card, and second value to be the points
    points = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10), ('J', 10), ('Q',10), ('K', 10)]
    
    def createDeck(self):
        card_deck = [] 
        for item in Cards.suits:
            for x in range(1,14):
                card_deck.append(item+str(x))   
        return card_deck

#generate new deck instance
deck = Cards()
print(deck.createDeck())

#Ask player to make bet before game starts
def makeBet():
    global bet
    while True:
        try:
            bet = int(input('Please enter how much you wish to bet: '))
        except:
            print("Please enter a number.")
            continue
        else:
            break
    return bet

#function to randomize the cards drawn
def randomizeDraw():
    suit = deck.suits[random.randint(0, 3)]
    card = str(deck.points[random.randint(0, 12)][0])
    hand = suit+card
    return hand

#function for player to input decision - hit or stand
def playerDecision():
    decision = (input('Do you want to hit (H) or stand (S)? ')).upper()
    while decision != 'S' and decision !='H':
        decision = (input('Please hit (H) or stand (S) ')).upper()
    else:
        return decision

print('Player decision is ', playerDecision())

#function to calculate player score depending on decision
#def calcPlayerScore(decision):
    

#function to calculate the dealer hand

    
#creating a new player instance
player = Player()

#creating variables for player hand and dealer hand
dealer_hand = [randomizeDraw(), randomizeDraw()]
player_hand = [randomizeDraw(), randomizeDraw()]

makeBet()
print('The dealer has ', dealer_hand[0]) #can only see one of dealer's cards
print('Your hand is ', player_hand)
decision = playerDecision()
#if decision == 'S':
    

print(player.addMoney())
