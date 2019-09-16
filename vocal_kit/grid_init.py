import numpy as np
import random as rd
from copy import deepcopy as copy_list

def tuple_to_position(n): #marche
   return ((chr(n[0]+65) + str(n[1]+1)))

def position_to_tuple(n): #marche
   return((ord(n[0])-65,int(n[1:])-1))

def is_enough_space(position_initiale, direction, boat_length):
    """
    _ brief: this function looks if there is enough space to place a boat
    _ param position_initale: a tuple
    _ param direction: a string ("gauche", "haut"...)
    _ param boat_length: an integer
    _ return : a boolean
    """
    x,y = position_initiale
    if direction == "haut":
        return y-boat_length >= 0
    elif direction == "bas":
        return y+boat_length <= 9
    elif direction == "gauche":
        return x-boat_length >= 0
    elif direction == "droite":
        return x+boat_length <= 9


        
def list_points_boat(position_initiale, direction, boat_length): #On veut renvoyer la liste des points utilisés par les bateaux

    liste = [tuple_to_position(position_initiale)]    #On recupere une liste sous forme de chaine de caractères pour l'affichage
    position = position_initiale # On travaille avec les tuples
    i = 1

    while i < boat_length: #Tant qu'il reste des cases du bateau à ajouter

        i+=1 #On diminue à chaque fois la taille du bateau
        x,y = position #On recupere les positions
        
        if direction == "haut": #Pour chaque directions, on place petit à petit le bateau dans celle ci jusqu'à ce qu'il soit totalement placé
            position = (x, y-1)
        elif direction == "bas":
            position = (x, y+1)
        elif direction == "gauche":
            position = (x-1, y)
        elif direction == "droite":
            position = (x+1, y)
        
        liste.append(tuple_to_position(position)) # On ajoute les positions

    return liste

    
def generate_boat(grid, boats, boat_length, name):
    """
    _ brief: this function generates the grid and the boat dictionary (fot only one boat)
    _ param grid: numpy array
    _ param boats: dictionary
    _ boat_length: int
    _ param name: name of the boat
    _ return the grid and the dictionary boats updated
    """
    valide = False
    new_boats = boats

    while not valide : #Tant qu'on ne considere pas que le bateau est bien placé

        position_initiale = (rd.randint(0, 9), rd.randint(0, 9)) #On le place à un endroit au hasard
        direction = rd.choice(["haut", "bas", "gauche", "droite"]) #On choisit une direction de façon aléatoire

        if is_enough_space(position_initiale, direction, boat_length): #On vérifie si on peut placer le bateau dans la direction souhaitée
            list_points = list_points_boat(position_initiale, direction, boat_length) #On recupere la liste de l'emplacement bateau
            new_boats[name] =  {"pos" : list_points, 
                                "touch": [],
                                "is_sunk": False} #On definit un dictionnaire pour chaque bateau indiquant leurs positions, s'ils sont touchés et coulés
            new_grid = copy_list(grid)

            for new_point in list_points: #Pour chaque point du bateau

                x,y = position_to_tuple(new_point) #on recupere ses coordonnees

                if new_grid[x][y] == "Boat": #S'il y a déjà un bateau à l'emplacement souhaité, on annule le placement et on recommence
                    break
                new_grid[x][y] = "Boat"
            else:
                valide = True
                boats = new_boats
                grid = new_grid
    return grid, boats
    
def generate_random_grid_and_boats(boats_length = [2, 3, 3, 4, 5]):
    """
    _ brief: this function generates a random grid with boats (iterate for all the boats the previous function)
    _ param: list of the length of boats
    _ return: the grid and the dictionary of the boats
    """
    grid = np.empty((10,10), dtype=object)
    for i in range(10):
        for j in range(10):
            grid[i][j] = "Water" #Missed #Touched #Boat
    boats = {}
    indice = 0
    for boat_length in boats_length:
        indice +=1
        boat_name = "Boat "+str(indice)
        grid, boats = generate_boat(grid, boats, boat_length, name=boat_name)
    return grid, boats


