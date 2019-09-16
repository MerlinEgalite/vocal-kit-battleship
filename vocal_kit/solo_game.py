#!/usr/bin/env python3
from grid_init import *
from grid_update import *
from affiche_simple import *

def is_shoot_valid(position): #tuple
    chiffre = [i for i in range(10)]
    boole = True
    if type(position) != tuple:
        return False 
    elif not (position[0] in chiffre and position[1] in chiffre):
        return False
    return True 
    
def solo_game():
    """
    _ brief: start the game, the player is alone trying to destruct the boats on a random generated grid
    _ param: none
    _ return: the issue of the game
    """
    (grid, boats) = generate_random_grid_and_boats()
    print(boats)
    life = 5
    print('The game starts, good luck ! Type \'STOP\' to stop playing')

    affiche_simple_grille(grid)

    counter = 0
    while life > 0:
        counter += 1
        position = input('Where do you want to shoot ?\n')
        if position == 'STOP':
            print("Perdu...")
            break
        if is_shoot_valid(position_to_tuple(position)):
            (boats, grid, life, text_returned) = grid_update_player(position, boats, grid, life)
        else:
            print("Not valid")
        affiche_simple_grille(grid)
    else:
        print('\nVICTORY !!!\n\nIn '+str(counter)+" tries.")

solo_game()
