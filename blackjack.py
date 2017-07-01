#a text based BlackJack game in Python
#player start out with 100 in money
#Player can hit or stand

import random

bet = 0
points = {'1':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10, 'J':10, 'Q':10, 'K':10 }
winner = False

class Player(object):
    def __init__(self, money=100):
        self.money = money
    
    def addMoney(self):
        return self.money + bet

    def loseMoney(self):
        return self.money - bet

class Cards(object):
    suits = ["Spades", "Hearts", "Diamond", "Clubs"]
    
    def create_deck(self):
        card_deck = [] 
        for item in Cards.suits:
            for x in range(1,14):
                card_deck.append(item+str(x))   
        return card_deck

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

#calculate score
#parameter - pass in either player_hand or dealer_hand
def calc_score(cards):
  sum = 0
  last_number=[item[-1] for item in cards]
  #if the last number is 0, then that's a 10 point card
  for item in last_number:
    sum += points[item]
  try:
    if last_number.index('1') >= 0 and sum > 21:
      sum = sum - 11*last_number.count('1') + 1*last_number.count('1')
      #11 and 1 are multipled by the number of times the player draws an Ace; in case player draws a second or third ace
  except:
    pass
  return sum
  
#checks if dealer has to draw (less than 17 in hand)
def dealer_draw():
  global dealer_score
  dealer_hand.append(deck[randomize()])
  deck.remove(dealer_hand[-1])
  display_hand(dealer_hand)
  dealer_score = calc_score(dealer_hand)
  return dealer_score

#if player or deal is dealt 21 on the first 2 cards
def natural_win():
  if player_score == 21 and dealer_score != 21:
    player.money = player.addMoney()
    print('You win! Your money increase to: {} '.format(player.money))
  elif dealer_score == 21 and player_score != 21:
    player.money = player.loseMoney()
    print('You lost this round. Your money decrease to: {}'.format(player.money))
  elif dealer_score == 21 and player_score == 21:
    print("It's a tie. You did not win or lose any money")

#check winning conditions
def win_condition():
  if dealer_score > 21:
    player.money = player.addMoney()
    print('Dealer busts! Player wins! Player money increase to: {} '.format(player.money))
  elif player_score > 21:
    player.money = player.loseMoney()
    print('Player busts! Dealer wins! Your money decrease to: {}.'.format(player.money))
  elif dealer_score == player_score:
    print("It's a tie. Player wins no money")
  elif dealer_score>player_score:
    player.money = player.loseMoney()
    print('Dealer wins! Your money decrease to: {}.'.format(player.money))
  elif player_score>dealer_score:
    player.money = player.addMoney()
    print('Player wins! Player money increase to: {} '.format(player.money))

def display_score():
  print('Player score is ', player_score)
  print('Dealer score is ', dealer_score)

#function to deal cards; takes in a num that indicates how many cards to deal and which person (player or dealer)
def deal_cards(num, hand):
  i=0
  while i<num:
    hand.append(deck[randomize()])
    deck.remove(hand[-1])
    i+=1
  return hand

#asks if the player wants to play again
def ask_play():
  ask_play = input('Do you want to play again? (Y/N)').upper()
  while ask_play != 'Y' and ask_play !='N':
    ask_play = (input('Please hit (Y) or stand (N) ')).upper()
  else:
    return ask_play
  
#generate new deck instance
cards_instance = Cards()
deck = cards_instance.create_deck()

#creating a new player instance
player = Player()

#######
##GAME CODE STARTS HERE! ABOVE ARE ONLY FUNCTIONS
#######

while player.money > 0: 
  player_hand = []
  dealer_hand = []
  make_bet()

  while bet > player.money: 
      try: 
        bet = int(input("You don't have that much money. Please enter an amount less than or equal to {}".format(player.money)))
      except:
        print('Please enter a number.')
        continue
  
  player_hand = deal_cards(2, player_hand)
  dealer_hand = deal_cards(2, dealer_hand)
  
  #display player and dealer's hand
  display_hand(player_hand)
  display_hand(dealer_hand)
  print('Your hand is ', player_hand)
  print("Dealer's face-up card is", dealer_hand[0]) #player only sees one card at the beginning
  print("Dealer's face-down card is", dealer_hand[1])
  
  #right after 2 cards are dealt, check if anyone won off the bat.
  #if player has 21, (a ten and an ace), player wins
  #if dealer has 21, (a ten and an ace), dealer wins
  #if both player and dealer has 21, tie; player loses no money
  
  player_score = calc_score(player_hand)
  dealer_score = calc_score(dealer_hand)
  
  if player_score == 21 or dealer_score == 21: 
    natural_win()
    if player.money > 0:
        play_again = ask_play()
        if play_again == 'N':
          break
        else:
            continue
  ##below code runs if neither player or dealer have 21 from first 2 cards
  else:
    decision = playerDecision()
    while decision != 'S':
      print('Player draws another card')
      player_hand = deal_cards(1, player_hand) #draws 1 card for the player
      display_hand(player_hand)
      player_score = calc_score(player_hand)
      print('Player hand is ', player_hand)
      if player_score > 21:
        win_condition()
        break
      decision = playerDecision()
    else: 
      print('Player decides to Stand')
      while dealer_score < 17:
        dealer_draw()
      display_score()
      win_condition()

  if player.money > 0:
      play_again = ask_play()
      if play_again == 'N':
          break

    
