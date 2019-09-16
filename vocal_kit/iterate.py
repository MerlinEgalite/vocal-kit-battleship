#!/usr/bin/env python3
from grid_update.py import grid_update_player
from vocal_kit.grid_init import *


def iterate():
    """
    _ brief: start the party player vs machine
    _ param: none
    _ return: the result of the party
    """
    winner = ''

    (grid_player, boats_player, life_player, text_player) = generate_random_grid_and_boats()    #generate the variables
    (grid_machine, boats_machine, life_machine, text_machine) = generate_random_grid_and_boats()
    print('chose the person who begin the game : the machine or you ? (the machine/me)')
    answer = input()
    count = 1
    shooting_list = []
    if answer == 'me':  #the player begins to play
        print('let us begin')
        while life_player > 0 or life_machine > 0:  #while all players have a boat not destroyed
            print('chose the position where you want to shoot')
            position = input()      #the player choose where to play
            (grid_machine, boats_machine, life_machine, text_machine) = grid_update_player(position, boats_machine, grid_machine, life_machine)     #the grid of the machone is then updated
            if life_machine == 0:
                winner = 'you'
                break   #if the player won we go out from the while
            (grid_player, boats_player, grid_screen_player, shooting_machine, text_machine) = grid_update_machine(boats_player, grid_player, count, shooting_list)  #the machine plays after the player
            shooting_list.append(shooting_machine)
            print(text_machine)
            if life_player == 0:
                winner = 'the machine'
                break       #if the machine wins we go out from the while
            count += 1      #the count is updated
    else:
        print('let us begin')
        while life_player > 0 or life_machine > 0:
            (grid_player, boats_player, grid_screen_player, shooting_machine, text_machine) = grid_update_machine(boats_player, grid_player, count, shooting_list)
            shooting_list.append(shooting_machine)
            print(text_machine)
            if life_player == 0:
                winner = 'the machine'
                break       #if the machine won we go out from the while
            print('chose the position where you want to shoot')
            position = input()
            (grid_machine, boats_machine, life_machine, text_machine) = grid_update_player(position, boats_machine, grid_machine, life_machine)
            if life_machine == 0:
                winner = 'you'
                break       #the machine plays after the player
            count += 1      #the count is updated
    return print('the winner is '+ winner)      #diplays the winner









