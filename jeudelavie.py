# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:55:01 2023
Projet Info ENSAM-Metz
****From scratch****
Puisse ce merveilleux jeu de la vie parfaitement fonctionnel vous inspirer, au moins moi j'ai pu récupérer tout mon niveau sur les TDs que j'ai deserté

Règles du jeu de la vie : si une cellule morte a exactement 3 voisines vivantes elle naît, si une cellule vivante a 2 ou 3 voisines vivantes, elle survit, si + ou - elle meurt.

Le programme décidé aléatoirement d'un 1er tour en remplissant en binaire 0=morte 1=vivante une liste de dimensions choisies par l'utilisateur.ice via creerGrille() & remplirrandom()
Puis chaque cellule de la liste évolue un nombre de fois défini par l'utilisateur.ice selon les règles du jeu via evolution()
A chaque tour on affiche l'évolution via afficher_repere()

@author: arthurvp
"""

import random #librairie de calcul de valeur aléatoire
import matplotlib.pyplot as plt #librairie de tracé graphique
from copy import deepcopy #librairie de copie d'objets

def creerGrille(nombreLignes, nombreColonnes):
  #cette fonction crée un tableau de dimensions données en argument
  grid = [[]] * nombreLignes
  for ligne in range(nombreLignes):
    grid[ligne] = [0] * nombreColonnes
  return grid

def remplirrandom(grille):
  #cette fonction prend un tableau, parcourt chaque cellule, et lui donne aléatoirement 0 ou 1
  #on s'en sert pour generer un nouveau jeu de cellules vivantes/mortes à chaque partie
  for ligne in range(len(grille)-1):
    for colonne in range(len(grille[0])-1):
      grille[ligne][colonne]=random.randint(0,1)
  return grille

def creerGrilledeTEST(grille):
  #cette fonction crée un tableau de jeu de la vie donné, pour vérifier facilement les erreurs dans la suite du programme
  grille[0][1]=1
  grille[0][4]=1
  grille[1][0]=1
  grille[1][1]=1
  grille[1][2]=1
  grille[1][3]=1
  grille[1][4]=1
  grille[2][1]=1
  grille[2][3]=1
  grille[2][4]=1
  grille[3][1]=1
  grille[3][3]=1
  return grille

def afficher_repere(tableau):
  #la fonction sert à afficher des carrés noirs pour chaque cellule vivante, c'est à dire quand la valeur du tableau est à 1, aux coordonnées correspondantes
    plt.figure()
    ax = plt.gca() #désormais "ax" représente notre figure
  #on utilise les parametres des fonctions plot pour avoir un repere orthonormé
    ax.set_aspect('equal', adjustable='box') #paramètre orthonormé
    ax.set_xlim(0, len(tableau[0])) #bornes des axes correspondant au tableau
    ax.set_ylim(0, len(tableau))
    ax.set_title('Tour n°' + str(tour))

    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] == 1:
                square = plt.Rectangle((j, len(tableau) - i - 1), 1, 1, facecolor='black') #les lignes sont ordonnées inversement au tableau : la 1ère ligne du tableau est en haut, alors que le 1er Y est en bas dans un repère classique. Donc on doit tracer à Ymax et decroitre du numéro de ligne actuel à chaque fois.
                ax.add_patch(square)

    #ajoute un quadrillage
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.grid(True, linestyle='-', linewidth=1, color='black')  # Épaisseur et couleur modifiées
    #paramètres pour changer et masquer les coordonnées sur les axes, et transformer le repère en grille de jeu
    ax.tick_params(axis='both',bottom=0, top=0, left=0, right=0,labelbottom=0, labeltop=0, labelleft=0, labelright=0

)

    plt.show() #une fois les modifs effectuees on affiche la figure en fin d'itération

def evolution(grille):
  #cette fonction parcourt le tableau, et pour chaque cellule cherche le nombre de cellules voisines par une somme de leur valeur = 1 si elles sont vivantes, en differenciant les cas de bords de tableaux. Puis avec la somme elle compare la valeur de cellules voisines vivantes et l'état de la cellule actuelle aux règles, pour changer le tableau-copie de l'argument d'entrée de la fonction en faisant naitre et mourir les bonnes cellules. Une fois toutes les cellules actualisées elle renvoie le tableau
#voisviv est la somme des valeurs des cases entourant la cellule observée, soit ligne avant,égale,après,colonnes précédente,égale,suivante, mais en ne comptant pas les cellules hors du cadre du tableau
  
    grtemp=deepcopy(grille) #on copie la grille en argument pour ne pas modifier l'objet grille
    for l in range(len(grille)):
          for c in range(len(grille[0])): #pour chaque colonne, dans chaque ligne
              if l==0 and c==0: #case en haut à gauche
                      voisviv=sum([grille[l][c+1],grille[l+1][c],grille[l+1][c+1]])
              elif l==0 and c==len(grille[0])-1: #case en haut à droite
                      voisviv=sum([grille[l][c-1],grille[l+1][c-1],grille[l+1][c]])
              elif l==0: #reste des cases de la 1ere ligne
                      voisviv=sum([grille[l][c-1],grille[l][c+1],grille[l+1][c-1],grille[l+1][c],grille[l+1][c+1]])
              elif l==len(grille)-1 and c==0: #case en bas à gauche
                voisviv=sum([grille[l-1][c],grille[l-1][c+1],grille[l][c+1]])
              elif l==len(grille)-1 and c==len(grille[0])-1: #case en bas à droite
                voisviv=sum([grille[l-1][c-1],grille[l-1][c],grille[l][c-1]])
              elif l==len(grille)-1: #reste des cases du bas
                voisviv=sum([grille[l-1][c-1],grille[l-1][c],grille[l-1][c+1],grille[l][c-1],grille[l][c+1]])
              elif l!=0 and c==0: #colonne de gauche sauf lignes du haut/bas dejà traitées
                voisviv=sum([grille[l-1][c],grille[l-1][c+1],grille[l][c+1],grille[l+1][c],grille[l+1][c+1]])
              elif l!=len(grille)-1 and c==0: #colonne de gauche sauf lignes du haut/bas dejà traitées
                voisviv=sum([grille[l-1][c],grille[l-1][c+1],grille[l][c+1],grille[l+1][c],grille[l+1][c+1]])
              elif l!=0 and c==len(grille[0])-1: #colonne de droite sauf lignes du haut/bas dejà traitées
                voisviv=sum([grille[l-1][c-1],grille[l-1][c],grille[l][c-1],grille[l+1][c-1],grille[l+1][c]])
              elif l!=len(grille)-1 and c==len(grille[0])-1: #colonne de droite sauf lignes du haut/bas dejà traitées
                voisviv=sum([grille[l-1][c-1],grille[l-1][c],grille[l][c-1],grille[l+1][c-1],grille[l+1][c]])
              else:  #tous les cas particuliers sont traités, le reste des cellules a toutes ses 8 voisines
                voisviv=sum([grille[l-1][c-1],grille[l-1][c],grille[l-1][c+1],grille[l][c-1],grille[l][c+1],grille[l+1][c-1],grille[l+1][c],grille[l+1][c+1]])
                
              #maintenant on compare aux règles du jeu : si la cellule est morte, et a 3 voisines vivantes, elle naît
              if grille[l][c]==0 and voisviv==3:
                grtemp[l][c]=1
              #et si elle est vivante, si elle est en isolement ou surpopulation elle meurt, sinon on ne fait rien, elle reste vivante  
              elif grille[l][c]==1:
                if voisviv<2 or voisviv>3:
                  grtemp[l][c]=0

    return grtemp

def nbcellulesviv(grille):
    #cette fonction calcule le nombre de cellules vivantes dans un tableau
    s=0
    for l in range(len(grille)):
        s+=sum(grille[l])
    return s

 #PROGRAMME PRINCIPAL

#○n demande à l'utilisateur.ice les paramètres de jeu
ligne = int(input('_______Jeu de la vie______\n\n\nDonnez le nombre de lignes du tableau\n'))
colonne = int(input('Donnez le nombre de colonnes du tableau\n'))
iterations = int(input('Donnez le nombre d itérations du jeu\n'))
tour=0 #on initialise tour à 0 pour le titre du 1er graphique
g = creerGrille(ligne,colonne) #création d'une liste aux bonnes dimensions, remplie de cellules mortes
g=remplirrandom(g) #remplissage aléatoire avec des cellules vivantes
somme_ini=deepcopy(nbcellulesviv(g)) #on fige une copie du nombre de cellules vivantes au départ
afficher_repere(g) #affichage des cellules au tour 0
for c in range (iterations):
  tour+=1
  g=evolution(g) #on fait évoluer les cellules selon les règles du jeu
  afficher_repere(g) #et on affiche le tableau modifié

#fin du jeu et bilan
print('\n\nIl y avait '+str(somme_ini)+' cellules vivantes initialement.\nAprès '+str(iterations)+' tours il reste '+ str(nbcellulesviv(g)) +' cellules vivantes.\n\n_______Fin du Jeu_______')
