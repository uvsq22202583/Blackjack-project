import tkinter as tk
import random
from tkinter import *

window = tk.Tk()
window.title("Blackjack Game")
window.geometry("800x600")
window.configure(bg="green")

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = [(rank, suit) for rank in ranks for suit in suits]


random.shuffle(deck)
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

card_values = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
def get_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        value += card_values[rank]
        if rank == "Ace":
            num_aces += 1
    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1
    return value

def check_for_winner():
    global player_hand, dealer_hand, game_in_progress
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    if player_value == 21:
        result_label.config(text="Blackjack! You win!")
        game_in_progress = False
    elif player_value > 21:
        result_label.config(text="Bust! You lose.")
        game_in_progress = False
    elif dealer_value == 21:
        result_label.config(text="Dealer has blackjack! You lose.")
        game_in_progress = False
    elif dealer_value > 21:
        result_label.config(text="Dealer busts! You win!")
        game_in_progress = False
    elif not game_in_progress:
        if player_value > dealer_value:
            result_label.config(text="You win!")
        elif player_value < dealer_value:
            result_label.config(text="You lose.")
        else:
            result_label.config(text="Push (tie game).")


window.mainloop()
