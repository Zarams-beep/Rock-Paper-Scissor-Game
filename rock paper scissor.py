import random

player_score = {'Tie': 0, 'Win': 0, 'Lose': 0}


def get_player_choice():
    while True:
        try:
            player_choice = int(input('Rock is 0. Paper is 1. Scissor is 2. Please enter a number between 0-2: '))
            if 0 >= player_choice and player_choice<= 2:
                return player_choice
            else:
                print('Please enter a valid number between 0 and 2.')
        except ValueError:
            print('Please enter a valid integer.')


def determine_winner(computer_choice, player_choice, word_choice):
    result=''
    if computer_choice == player_choice:
        result = 'Tie'
    elif (computer_choice == 0 and player_choice == 2) or (computer_choice == 1 and player_choice == 0) or (
            computer_choice == 2 and player_choice == 1):
        result = 'Lose'
    elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (
            player_choice == 2 and computer_choice == 0):
        result = 'Win'

    return result


def game():
    print('Welcome to my rock, paper, and scissor game!!')
    name=input('Enter name!')

    while True:
        player_choice = get_player_choice()

        computer_choice = random.randint(0, 2)
        word_choice = ['rock', 'paper', 'scissor']

        result = determine_winner(computer_choice, player_choice, word_choice)

        if result == 'Tie' or result == 'Lose' or result == 'Win':
            player_score[result] += 1
            print(
                f'Computer chose {word_choice[computer_choice]} and Player chose {word_choice[player_choice]}.\n Player You {result}. \n Tie: {player_score["Tie"]}. Win: {player_score["Win"]}. Lose: {player_score["Lose"]}.')
        start = input('Start: (y/n)').lower()
        if start != 'y':
            print(f'Good bye {name}!!')
            break    
        

game()
