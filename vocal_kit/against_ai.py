#!/usr/bin/env python3
import numpy as np
from grid_init import *
from grid_update import *
from tkinter import *
import random as rd


class Interface(Frame):

    """Fenetre de jeu"""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=1150, height=550, **kwargs)
        self.pack(fill="both")

        #Création des différents widgets

        #Grille de jeu
        self.cadre = Canvas(self, width=1150, height=550, background='#88D')
        self.tableau = np.zeros((11,11))
        self.tableau2 = np.zeros((11,11))

        for i in range(1,11):
            #On cree les coordonnees
            self.tableau[i,0] = self.cadre.create_text(50*i+25,25,text = chr(i+64))
            self.tableau[0,i] = self.cadre.create_text(25,50*i+25,text = str(i))
            for j in range(1,11):
                self.tableau[i,j] = self.cadre.create_rectangle(50*i,50*j,50*(i+1),50*(j+1))

        for i in range(1,11):
            #On cree les coordonnees
            self.tableau2[i,0] = self.cadre.create_text(600+50*i+25,25,text = chr(i+64))
            self.tableau2[0,i] = self.cadre.create_text(625,50*i+25,text = str(i))
            for j in range(1,11):
                self.tableau2[i,j] = self.cadre.create_rectangle(600+50*i,50*j,600+50*(i+1),50*(j+1))


        #On place la grille de jeu en bas vis-a-vis des autres widgets
        self.cadre.pack(side="bottom")
        self.cadre.bind('<Button-1>', lambda event: self.actualisation_on_click())

        #Input
        self.entree = Entry(self, textvariable=str, width=30)
        self.entree.pack()
        self.entree.bind('<Return>', lambda event: self.actual_player())

        #Bouton d'actualisation du plateau pour le joueur
        self.bouton_actualisation = Button(self, text="Je joue", command=self.actual_player)
        self.bouton_actualisation.pack(side="left")


        #Bouton d'affichage de la position des bateaux:
        self.trichement = True
        self.bouton_triche = Button(self, text="Je veux tricher", command=self.triche)
        self.bouton_triche.pack(side="right")

        #Position des bateaux
        self.grid_ai, self.boats_ai = generate_random_grid_and_boats()
        self.grid_player, self.boats_player = generate_random_grid_and_boats()

        #Nombre de vie du joueur
        self.life_ai = 5
        self.life_player = 5
        
        #Texte de ce que le joueur a joué
        self.text = Label(self,text="Prêt à jouer ?")
        self.text.pack()

        #Dictionnaire des couleurs affichées
        self.color_visible = {"Boat": "pink", "Touched": "#222", "Missed": "#22D", "Water": "#88D", "Sunk": "#D22"}
        self.color_cache   = {"Boat": "#88D", "Touched": "#222", "Missed": "#22D", "Water": "#88D", "Sunk": "#D22"}
        
        #Affichage des bateaux du joueur
        for i in range(1, 11):
            for j in range(1, 11):
                self.tableau2[i, j] = self.cadre.create_rectangle(600 + 50 * i, 50 * j, 600 + 50 * (i + 1), 50 * (j + 1),
                                                                     fill=self.color_visible[self.grid_player[i-1,j-1]])


    def actualisation_on_click(self):
        x = self.winfo_pointerx() - self.winfo_rootx()
        y = self.winfo_pointery() - self.winfo_rooty()
        x =  x//50 - 1
        y =  y//50 - 2
        
        self.position = tuple_to_position((x,y))
        print(self.position)
        self.boats_ai, self.grid_ai, self.life_ai, self.text["text"] = grid_update_player(self.position, self.boats_ai, self.grid_ai, self.life_ai)
        
        for i in range(1, 11):
            for j in range(1, 11):
                if not self.trichement:
                    self.tableau[i, j] = self.cadre.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1),
                                                                     fill=self.color_visible[self.grid_ai[i-1,j-1]])
                else:
                    self.tableau[i, j] = self.cadre.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1),
                                                                     fill=self.color_cache[self.grid_ai[i - 1, j - 1]])
    
        self.actual_ai()
        
        
    def actual_player(self):

        """ Actualisation des tirs réalisés"""
        self.position = self.entree.get()
        self.boats_ai,self.grid_ai, self.life_ai, self.text["text"] = grid_update_player(self.position,self.boats_ai,self.grid_ai, self.life_ai)
        self.entree.delete(0, 'end')

        for i in range(1, 11):
            for j in range(1, 11):
                if not self.trichement:
                    self.tableau[i, j] = self.cadre.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill=self.color_visible[self.grid_ai[i-1,j-1]])
                else:
                    self.tableau[i, j] = self.cadre.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill=self.color_cache[self.grid_ai[i - 1, j - 1]])
        self.actual_ai()
        
    def actual_ai(self):

        """ Actualisation des tirs réalisés par l'ai"""
        self.position = (rd.randint(0, 9), rd.randint(0, 9))
        self.position = tuple_to_position(self.position)
        self.boats_player,self.grid_player, self.life_player, self.text["text"] = grid_update_player(self.position,self.boats_player,self.grid_player, self.life_player)
        self.entree.delete(0, 'end')
        
        for i in range(1, 11):
            for j in range(1, 11):
                self.tableau2[i, j] = self.cadre.create_rectangle(600 + 50 * i, 50 * j, 600 + 50 * (i + 1), 50 * (j + 1),
                                                                     fill=self.color_visible[self.grid_player[i-1,j-1]])
        if self.life_ai == 0:
            self.text["text"] = "VICTORY !!!"
        elif self.life_player == 0:
            self.text["text"] = "YOU LOSE..."

    def triche(self):
        """Fonction qui affiche la position des bateaux"""
        if self.trichement:
            self.bouton_triche["text"] = "J'arrête de tricher"
            for i in range(1,11):
                for j in range(1,11):
                    self.tableau[i,j] = self.cadre.create_rectangle(50*i,50*j,50*(i+1),50*(j+1),fill=self.color_visible[self.grid_ai[i-1,j-1]])
        else:
            self.bouton_triche["text"] = "Je veux tricher"
            for i in range(1,11):
                for j in range(1,11):
                    self.tableau[i,j] = self.cadre.create_rectangle(50*i,50*j,50*(i+1),50*(j+1),fill=self.color_cache[self.grid_ai[i-1,j-1]])
        self.trichement = not self.trichement


fenetre = Tk()
inter = Interface(fenetre)
inter.mainloop()
