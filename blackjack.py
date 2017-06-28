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

    def loseMoney(self):
        return self.money - bet

class Cards(object):
    suits = ["Spades", "Hearts", "Diamond", "Clubs"]

    #points = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
    
    def create_deck(self):
        card_deck = [] 
        for item in Cards.suits:
            for x in range(1,14):
                card_deck.append(item+str(x))   
        return card_deck

#generate new deck instance
cards_instance = Cards()
deck = cards_instance.create_deck()
print(cards_instance.create_deck())

#creating a new player instance
player = Player()


#Ask player to make bet before game starts
def make_bet():
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

#function for player to input decision - hit or stand
def playerDecision():
    decision = (input('Do you want to hit (H) or stand (S)? ')).upper()
    while decision != 'S' and decision !='H':
        decision = (input('Please hit (H) or stand (S) ')).upper()
    else:
        return decision

#pick a random number
def randomize():
    return random.randint(0, len(deck)-1)

#function display Jack, Queen, and King; pass in parameter either player's hand or dealer's hand
def display_hand(cards_in_hand):
    for idx in range(len(cards_in_hand)):
        if cards_in_hand[idx][-2:] == '11':
            cards_in_hand[idx] = cards_in_hand[idx][:-2] + 'J'
        elif cards_in_hand[idx][-2:] == '12':
            cards_in_hand[idx] = cards_in_hand[idx][:-2] + 'Q'
        elif cards_in_hand[idx][-2:] == '13':
            cards_in_hand[idx] = cards_in_hand[idx][:-2] + 'K'

#function to calculate player and dealer's score right after two cards are dealt to see if anyone has 21
#paramters - pass in either the dealer's hand or the player's hand
#card_one = player_hand[0]
#card_two = player_hand[1]
def score_after_deal(card_one, card_two):
    if card_one[-1] == '1' and (card_two[-1] == 'J' or card_two[-1] == 'Q' or card_two[-1] == 'K' or card_two[-2] == '10'):
        total_points = 21
        return total_points
    elif card_two[-1] == '1' and (card_one[-1] == 'J' or card_one[-1] == 'Q' or card_one[-1] == 'K' or card_one[-2] == '10'):
        total_points = 21
        return total_points
    else:
        return "Not 21."

#######
##GAME CODE STARTS HERE! ABOVE ARE ONLY FUNCTIONS
#######

make_bet()

#deals out card (removes each card from the deck list as it is dealt so no dubplicate cards will be dealt)
player_hand = [deck[randomize()]]
deck.remove(player_hand[0])
dealer_hand = [deck[randomize()]]
deck.remove(dealer_hand[0])
player_hand.append(deck[randomize()])
deck.remove(player_hand[1])
dealer_hand.append(deck[randomize()])

#display player and dealer's hand
display_hand(player_hand)
display_hand(dealer_hand)
print('Your hand is ', player_hand)
print("Dealer's face-up card is", dealer_hand[0]) #player only sees one card at the beginning

#right after 2 cards are dealt, check if anyone one off the bat.
#if player has 21, (a ten and an ace), player wins
#if dealer has 21, (a ten and an ace), dealer wins
#if both player and dealer has 21, tie; player loses no money

player_score = score_after_deal(player_hand[0], player_hand[1])
dealer_score = score_after_deal(dealer_hand[0], dealer_hand[1])

if player_score == 21 and dealer_score != 21:
    print('You win! Your money increase to: ', player.addMoney())
elif dealer_score == 21 and player_score != 21:
    print('You lost this round. You money decrease to: ', player.loseMoney())
elif dealer_score == 21 and player_score == 21:
    print("It's a tie. You did not win or lose any money")
else:
    decision = playerDecision()
    print('Player decision is ', decision)
