import os
import random

#define deck
deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

#define how to deal
def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = 'J'
        if card == 12: card = 'Q'
        if card == 13: card = 'K'
        if card == 14: card = 'A'
        hand.append(card)
    return hand

#calculate total
def total(hand):
    total = 0
    for card in hand:
        if card == 'K' or card == "Q" or card == 'J':
            total += 10
        elif card == 'A':
            if total > 11:
                total += 1
            else: 
                total += 11
        else:
            total += card
    return total

#print results
def print_results(player_hand, player2_hand):
    print('Dealer has a total of ' + str(total(player_hand)))
    print('You have a total of ' + str(total(player2_hand)))

#blackjack fucntion to check score rigth after 1st deal
def blackjack(player_hand, player2_hand):
    if total(player_hand) == 21:
        print_results(player_hand, player2_hand)
        print('{} has a Blackjack ' + ' {} wins').format(player_hand, player_hand)
    elif total(player2_hand) == 21:
        print_results(player_hand, player2_hand)
        print('{} has a Blackjack ' + ' {} wins').format(player2_hand, player2_hand)

#hit function to deal another card
def hit(hand):
    card = deck.pop()
    if card == 11: card = 'J'
    if card == 12: card = 'Q'
    if card == 13: card = 'K'
    if card == 14: card = 'A'
    hand.append(card)
    return hand

#calculate winner between two players
def calculate_winner(player_hand, player2_hand):
    #print_results(player_hand, player2_hand)
    if total(player_hand) < 21 and total(player_hand) > total(player2_hand):
        print('Dealer has a total of ' + str(total(player_hand)) + str(player_hand) + ' , Dealer wins')
    elif total(player2_hand) < 21 and total(player2_hand) > total(player_hand):
        print('You have a total of ' + str(total(player2_hand)) + str(player2_hand) + ' wins')
    elif total(player_hand) == 21:
        print_results(player_hand, player2_hand)
        print('Dealer has a Blackjack ' + str(player_hand))
    elif total(player2_hand) == 21:
        print_results(player_hand, player2_hand)
        print('You win ' + str(player2_hand))
    elif total(player_hand) > 21:
        print_results(player_hand, player2_hand)
        print('Dealer is bust ' + str(player_hand) + ' . You win!')
    elif total(player_hand) > 21:
        print_results(player_hand, player2_hand)
        print('You are bust ' + str(player2_hand))

#define replay function
def play_again():
    replay = input('Do you want to play again? (Y or N) : ').lower()
    if replay == 'y':
        dealer_hand = []
        player1_hand = []
        deck = deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
        game()
    else:
        print('You suck! Bye')
        exit()



#define main game functionality
def game():
    #start game
    choice = 0
    print("Welcome to BlackJack - Let's hope you win")

    #first deal
    dealer_hand = deal(deck)
    player1_hand = deal(deck)

    #print initial results
    print('Dealer is showing ' + str(dealer_hand[0]))
    print('You have a ' + str(player1_hand[0]) + ' and ' + str(player1_hand[1]) + ' for a total of ' + str(total(player1_hand)))

    #check blackjack
    blackjack(dealer_hand, player1_hand)


    #ask player to hit again?
    choice = input('Do you want to [H]it, [S]tay or [Q]uit?').lower()
    if choice == 'h':
        hit(player1_hand)
        while total(dealer_hand) < total(player1_hand):
            hit(dealer_hand)
        calculate_winner(dealer_hand, player1_hand)
        play_again()
    elif choice == 's':
        while total(dealer_hand) < total(player1_hand):
            hit(dealer_hand)
        calculate_winner(dealer_hand, player1_hand)
        play_again()
    elif choice == 'q':
        print('Game Aborted - You lost  1 Billion Dollars')
        exit()


if __name__ == "__main__":
    game()
