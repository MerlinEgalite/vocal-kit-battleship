from random import choice , shuffle
import random
import numpy as np


#!/usr/bin/env python3
from grid_init import generate_random_grid_and_boats, tuple_to_position, position_to_tuple


def Playable_position(x,y,grid):
    liste=[0,1,2,3,4,5,6,7,8,9]
    if (x in liste and y in liste) and (grid[x,y]=='Water' or grid[x,y]=='Boat'):
        return True
    else :
        return False

def tuple_to_position(n):
    return((chr(n[0]+65) + str(n[1]+1)))

def position_to_tuple(n):
    return((ord(n[0])-65,int(n[1:])-1))


def AI_shoot(grid_player,count,shooting_list):
    grid=grid_player

    #Sélection de la position de Tir par un disjonction de cas qui suit la logique d'un joueur normal

    if count==1: #Cas d'initialisation : 1er Tir du Computer
        x_1,y_1=random.randint(0,9),random.randint(0,9)
        shooting_list.append((None,(x_1,y_1)))
        return tuple_to_position((x_1,y_1))

    if count==2: #Cas d'initialisation : 2éme Tir du Computer

        last_hit=shooting_list[0]

        if last_hit[0]==True:

            case_last_hit=last_hit[1]

            #Cas ou on Force à jouer autour de la case touché

            Haut=(case_last_hit[0]-1,case_last_hit[1])
            Bas=(case_last_hit[0]+1,case_last_hit[1])
            Droite=(case_last_hit[0],case_last_hit[1]+1)
            Gauche=(case_last_hit[0],case_last_hit[1]-1)
            possibilite={"haut":Haut, "bas":Bas,"gauche":Gauche,"droit":Droite}
            print (possibilite)

            #Test pour savoir si les cases autours sont "jouables" (donc ou on n'a pas deja tiré et dans le terrain)

            if case_last_hit[0]==0 or (grid[possibilite["haut"]]=='Missed' or grid[possibilite["haut"]]=='Sunk' or grid[possibilite["haut"]]=='Touched' ):  #Test Haut de terrain
                del possibilite["haut"]
                print (possibilite)
            if case_last_hit[0]==9 or (grid[possibilite["bas"]]=='Missed' or grid[possibilite["bas"]]=='Sunk' or grid[possibilite["bas"]]=='Touched' ): #Test Bas de terrain
                del possibilite["bas"]
                print (possibilite)
            if case_last_hit[1]==0 or (grid[possibilite["gauche"]]=='Missed' or grid[possibilite["gauche"]]=='Sunk'or grid[possibilite["gauche"]]=='Touched' ): #Test Droite de terrain
                del possibilite["gauche"]
                print (possibilite)
            if case_last_hit[1]==9 or (grid[possibilite["droit"]]=='Missed' or grid[possibilite["droit"]]=='Sunk' or grid[possibilite["droit"]]=='Touched' ): #Test Gauche de terrain
                del possibilite["droit"]
                print (possibilite)
            choix=choice(list(possibilite.keys()))
            return (tuple_to_position(possibilite[choix]))



        if last_hit[0]==False:

            #On abandonne le choix logique et on selectionne une position au hasard

            possibilite=[]
            for x in range (10):
                for y in range (10):
                    if Playable_position(x,y,grid)==True :
                        possibilite.append((x,y))
                    if possibilite==[]:
                        print ('Fin de partie')
                        return None
            choix=choice(possibilite)
            return tuple_to_position(choix)

    if count>=3:
        last_hit=shooting_list[count-2]
        last_last_hit=shooting_list[count-3]

        if last_hit[0]==True:

            Case_last_hit=last_hit[1]
            Case_last_last_hit=last_last_hit[1]
            Haut=(Case_last_hit[0]-1,Case_last_hit[1])
            Bas=(Case_last_hit[0]+1,Case_last_hit[1])
            Droite=(Case_last_hit[0],Case_last_hit[1]+1)
            Gauche=(Case_last_hit[0],Case_last_hit[1]-1)

            if last_last_hit[0]==True: #Quand on enchaine 2 Hit on force le coomputer a tirer sur le même axe (Defaut : l'algo n'essaye d'aller que dans un sens)
                if Gauche==Case_last_last_hit and Playable_position(Droite[0],Droite[1],grid):
                    shooting_list.append(None,Droite)
                    return tuple_to_position(Droite)
                if Droite==Case_last_last_hit and Playable_position(Gauche[0],Gauche[1],grid):
                    shooting_list.append(None,Gauche)
                    return tuple_to_position(Gauche)
                if Haut==Case_last_last_hit and Playable_position(Bas[0],Bas[1],grid):
                    shooting_list.append(None,Bas)
                    return tuple_to_position(Bas)
                if Bas==Case_last_last_hit and Playable_position(Haut[0],Haut[1],grid):
                    shooting_list.append(None,Haut)
                    return tuple_to_position(Haut)
                else : #On abandonne le choix logique et on selectionne une position au hasard
                    possibilite=[]
                    for x in range (10):
                        for y in range (10):
                            Playable_position(x,y,grid)
                            if Playable_position(x,y,grid)==True :
                                possibilite.append((x,y))
                    if possibilite==[]:
                        print ('Fin de partie')
                        return None
                    else :
                        choix=choice(possibilite)
                        return tuple_to_position(choix)
            if last_last_hit[0]==False:

                 #Test pour savoir si les cases autours sont "jouables" (donc ou on n'a pas deja tiré et dans le terrain)

                if case_last_hit[0]==0 or (grid[possibilite["haut"]]=='Missed' or grid[possibilite["haut"]]=='Sunk' or grid[possibilite["haut"]]=='Touched' ):  #Test Haut de terrain
                    del possibilite["haut"]
                if case_last_hit[0]==9 or (grid[possibilite["bas"]]=='Missed' or grid[possibilite["bas"]]=='Sunk' or grid[possibilite["bas"]]=='Touched' ): #Test Bas de terrain
                    del possibilite["bas"]
                if case_last_hit[1]==0 or (grid[possibilite["gauche"]]=='Missed' or grid[possibilite["gauche"]]=='Sunk'or grid[possibilite["gauche"]]=='Touched' ): #Test Droite de terrain
                    del possibilite["gauche"]
                if case_last_hit[1]==9 or (grid[possibilite["droit"]]=='Missed' or grid[possibilite["droit"]]=='Sunk' or grid[possibilite["droit"]]=='Touched' ): #Test Gauche de terrain
                    del possibilite["droit"]

                choix=choice(list(possibilite.keys()))
                return (tuple_to_position(possibilite[choix]))

        if last_hit[0]==False: #On abandonne le choix logique et on selectionne une position au hasard
            possibilite=[]
            for x in range (10):
                for y in range (10):
                    if Playable_position(x,y,grid)==True :
                        possibilite.append((x,y))
            if possibilite==[]:
                print('Fin de partie')
                return None
            else :
                choix=choice(possibilite)
                return tuple_to_position(choix)

