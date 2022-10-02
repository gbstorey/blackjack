############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def player_add_card():
  """Draws a random equal probability card with replacement from the deck and adds it to the player's hand."""
  player_cards.append(cards[random.randint(0,len(cards)-1)])

def dealer_add_card():
  """Draws a random equal probability card with replacement from the deck and adds it to the dealer's hand."""
  dealer_cards.append(cards[random.randint(0,len(cards)-1)])

def player_ace_replacement():
  """Replaces a player's 11 with a 1 to avoid a bust."""
  ace_index=player_cards.index(11)
  player_cards[ace_index]=1

def dealer_ace_replacement():
  """Replaces the dealer's 11 with a 1 to avoid a bust."""
  ace_index=dealer_cards.index(11)
  dealer_cards[ace_index]=1

drawing=True
greater_seventeen=False
playing=True

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  while playing==True:
    from art import logo
    print(logo)
    player_cards=[]
    player_add_card()
    player_add_card()
    player_score=sum(player_cards)
    dealer_cards=[]
    dealer_add_card()
    dealer_add_card()
    print(f"Your cards: {player_cards}, current score:{player_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    while drawing==True:
      choice = input("Type 'y' to get another card, type 'n' to pass: ")
      if choice == "y":
        player_add_card()
        player_score=sum(player_cards)
        print(f"Your cards: {player_cards}, Current score: {player_score}")
      else:
        drawing=False
      if player_score > 21 and 11 in player_cards:
        print("Your ace becomes a 1 to avoid busting.")
        player_ace_replacement()
        player_score=sum(player_cards)
        print(f"Your cards: {player_cards}, Current score: {player_score}")
      if player_score > 21:
        print("You bust. Dealer wins.")
        playing=False
        drawing=False

    if playing==True:
      if sum(dealer_cards) >= 17:
        greater_seventeen=True
      while greater_seventeen==False:
        dealer_add_card()
        if sum(dealer_cards) >= 17:
          greater_seventeen=True
      dealer_score=sum(dealer_cards)
      if sum(dealer_cards) > 21 and 11 in dealer_cards:
        dealer_ace_replacement()
        dealer_score=sum(dealer_cards)
      if sum(dealer_cards) > 21:
        print(f"Computer cards: {dealer_cards}, Current score: {dealer_score}")
        print("Dealer busts. You win!")
        playing=False
      
    if playing==True:
      print(f"Computer cards: {dealer_cards}, Current score: {dealer_score}")
      if sum(player_cards) > sum(dealer_cards):
        print("Congratulations! You win!")
      elif sum(player_cards) == sum(dealer_cards):
        print("Draw.")
      else:
        print("Dealer wins.")
    playing=False
    if input("Would you like to play again? Type 'y' or 'n': ")=='y':
      playing=True
      drawing=True
    os.system('cls')
