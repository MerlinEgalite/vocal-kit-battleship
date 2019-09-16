
from grid_init import generate_random_grid_and_boats, tuple_to_position, position_to_tuple

def grid_update_player(position, boats, grid, life=5):
    """
    _ brief: this function returns all the variables after the machine or the player has played
    _ param position: (string) position where the player want to play
    _ param boats: (dictionary)
    _ param grid: (numpy array)
    _ param shooting_list: (list) list of the place where the computer has already played
    _ param life: (int) number of boats not sunk 5 initially
    _ return the boats dictionary and the grid updated after the player's shot, the life updated and the text to return
    """
    print("You played", position, end=" : ")
    x, y = position_to_tuple(position) #we collect the coords of the position given in entry
    text_returned = 'in the water'      #initialize the to return at the end
    for boat in boats:      #we loop into the dictionary boats
        boat = boats[boat]
        if position in boat["pos"]:         #if position is a position taken by a boat
            if not position in boat["touch"]:       #and the boat has not already been touched at this position
                boat["touch"].append(position)      #then we add this position to the touched position
                is_sunk = len(boat["pos"]) == len(boat["touch"])        #if the lenght of the two lists position and touched are the same is_sunk = True
                if is_sunk:
                    text_returned = 'a boat has been sunk'
                    life -= 1       #when a boat is sunk the life of the player decreases until it reaches 0
                    for point_sunk in boat["pos"]:      #updates the grid when the boat is sunk
                        x,y = position_to_tuple(point_sunk)
                        grid[x,y] = 'Sunk'
                else:
                    text_returned = 'a boat has been touched'
                    grid[x,y] = 'Touched'
                boat["is_sunk"] = is_sunk
                
            else:
                text_returned = 'the boat has already been touched'
    if text_returned == 'in the water':
        grid[x,y] = 'Missed'
    print(text_returned)        #the vocal kit displays the sentence
    return (boats, grid, life, text_returned)       #return the variable updated after
