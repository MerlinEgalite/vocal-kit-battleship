#!/usr/bin/env python3
import numpy as np
from vocal_kit.grid_init import *
from vocal_kit.grid_update import *
from tkinter import *


class Interface(Frame):
    
    """Fenetre de jeu"""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=550, height=550, **kwargs)
        self.pack(fill="both")

        #Création des différents widgets

        #Grille de jeu
        self.cadre = Canvas(self, width=550, height=550, background='#88D')
        self.tableau = np.zeros((11,11))

        for i in range(1,11):
            #On cree les coordonnees
            self.tableau[i,0] = self.cadre.create_text(50*i+25,25,text = chr(i+64))
            self.tableau[0,i] = self.cadre.create_text(25,50*i+25,text = str(i))
            for j in range(1,11):
                self.tableau[i,j] = self.cadre.create_rectangle(50*i,50*j,50*(i+1),50*(j+1))


        #On place la grille de jeu en bas vis-a-vis des autres widgets
        self.cadre.pack(side="bottom")
        self.cadre.bind('<Button-1>', lambda event: self.actualisation_on_click())

        #Input
        self.entree = Entry(self, textvariable=str, width=30)
        self.entree.pack()
        self.entree.bind('<Return>', lambda event: self.actual())


        #Bouton d'actualisation du plateau
        self.bouton_actualisation = Button(self, text="Je joue", command=self.actual)
        self.bouton_actualisation.pack(side="left")


        #Bouton d'affichage de la position des bateaux:
        self.trichement = True
        self.bouton_triche = Button(self, text="Je veux tricher", command=self.triche)
        self.bouton_triche.pack(side="right")


        #Position des bateaux
        self.grid, self.boats = generate_random_grid_and_boats()

        #Nombre de vie du joueur
        self.life = 5

        #Texte de ce que le joueur a joué
        self.text = Label(self,text="Prêt à jouer ?")
        self.text.pack()

        #Dictionnaire des couleurs affichées
        self.color_triche = {"Boat": "pink", "Touched": "#222", "Missed": "#22D", "Water": "#88D", "Sunk": "#D22"}
        self.color_reglo = {"Boat": "#88D", "Touched": "#222", "Missed": "#22D", "Water": "#88D", "Sunk": "#D22"}


    def actualisation_on_click(self):
        x = self.winfo_pointerx() - self.winfo_rootx()
        y = self.winfo_pointery() - self.winfo_rooty()
        x =  x//50 - 1
        y =  y//50 - 2
        self.position = tuple_to_position((x,y))
        self.boats, self.grid, self.life, self.text["text"] = grid_update_player(self.position, self.boats, self.grid,
                                                                                 self.life)

        for i in range(1, 11):
            for j in range(1, 11):
                if not self.trichement:
                    self.tableau[i, j] = self.cadre.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1),
                                                                     fill=self.color_triche[self.grid[i-1,j-1]])
                else:
                    self.tableau[i, j] = self.cadre.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1),
                                                                     fill=self.color_reglo[self.grid[i - 1, j - 1]])


    def actual(self):

        """ Actualisation des tirs réalisés"""
        self.position = self.entree.get()
        self.boats,self.grid, self.life, self.text["text"] = grid_update_player(self.position,self.boats,self.grid, self.life)
        self.entree.delete(0, 'end')

        for i in range(1, 11):
            for j in range(1, 11):
                if not self.trichement:
                    self.tableau[i, j] = self.cadre.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1),
                                                                     fill=self.color_triche[self.grid[i-1,j-1]])
                else:
                    self.tableau[i, j] = self.cadre.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1),
                                                                     fill=self.color_reglo[self.grid[i - 1, j - 1]])


    def triche(self):
        """Fonction qui affiche la position des bateaux"""
        if self.trichement:
            self.bouton_triche["text"] = "J'arrête de tricher"
            for i in range(1,11):
                for j in range(1,11):
                    self.tableau[i,j] = self.cadre.create_rectangle(50*i,50*j,50*(i+1),50*(j+1),fill=self.color_triche[self.grid[i-1,j-1]])
        else:
            self.bouton_triche["text"] = "Je veux tricher"
            for i in range(1,11):
                for j in range(1,11):
                    self.tableau[i,j] = self.cadre.create_rectangle(50*i,50*j,50*(i+1),50*(j+1),fill=self.color_reglo[self.grid[i-1,j-1]])
        self.trichement = not self.trichement



fenetre = Tk()
inter = Interface(fenetre)
inter.mainloop()
