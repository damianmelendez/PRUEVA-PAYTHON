#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
import random

def get_opponent_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, opponent_choice):
    if player_choice == opponent_choice:
        return 'tie'
    elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
         (player_choice == 'scissors' and opponent_choice == 'paper') or \
         (player_choice == 'paper' and opponent_choice == 'rock'):
        return 'player'
    else:
        return 'opponent'

def play_game():
    player_score = 0
    opponent_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        opponent_choice = get_opponent_choice()
        print(f"Opponent chose: {opponent_choice}")

        winner = determine_winner(player_choice, opponent_choice)

        if winner == 'player':
            player_score += 1
            print("You win this round!")
        elif winner == 'opponent':
            opponent_score += 1
            print("You lose this round!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Final Scores - You: {player_score}, Opponent: {opponent_score}")
            break

if __name__ == '__main__':
    play_game()





