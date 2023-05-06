# jeudelavie-python
Projet d'informatique très classique dans le supérieur. Le jeu de la vie est un jeu de simulation dans lequel des cellules se développent et meurent en fonction de leur environnement. Le jeu se joue sur une grille carrée, où chaque case peut être soit vide, soit occupée par une cellule vivante. 

Le jeu de la vie est un jeu de simulation dans lequel des cellules se développent et meurent en fonction de leur environnement. Le jeu se joue sur une grille carrée, où chaque case peut être soit vide, soit occupée par une cellule vivante. 

Les règles du jeu sont les suivantes :
- Si une cellule a deux ou trois voisines vivantes, elle reste en vie. 
- Si une cellule a moins de deux voisines vivantes, elle meurt d'isolement. 
- Si une cellule a plus de trois voisines vivantes, elle meurt de surpopulation. 
- Si une case vide a exactement trois voisines vivantes, une nouvelle cellule naît dans cette case. Le jeu se joue en itérations, chaque itération étant un tour complet du jeu. 
À chaque itération, chaque cellule est examinée pour déterminer si elle doit vivre ou mourir. Les cellules naissantes sont également ajoutées à la grille. 


Création du tableau et notion de vie de cellules

Nous avons commencé par créer un tableau de dimensions variables, même si c’est une fonctionnalité avancée du jeu, pour dimensionner tout le code avec des configurations différentes.
Nous avons choisi de représenter les cellules vivantes par des cases à 1, et les mortes par des cases à 0.
Pour ne pas figer les parties et les renouveller à chaque fois, on a cherché une randomisation des états des cellules au 1er tour. Le module random nous a donné une fonction randint que l’on borne entre 0 et 1.
Evolution des cellules
C’était la partie la plus complexe. Nous avons développé l’évolution pour une itération, afin de comparer le tableau des cellules après 1 tour et vérifier nos résultats.
Cellules voisines
Sur papier on a traduit la notion de cellules voisines en algorithmique depuis le tableau : on a trouvé une formule générale
 
Mais certaines cellules aux bords ou 1ère/dernières lignes du tableau étaient hors index quand on leur soustrayait 1 par exemple, nous avions des erreurs.
Vu que l’on parcourt le tableau par colonne dans les lignes, on a essayé de différencier et rassembler les cas d’erreurs par limite, c’est-à-dire toutes les cases de la 1ère ligne, toutes celles de la 1ère colonne, idem avec les dernières, et les cas particuliers des cases dans les bords du tableau, qui avaient encore moins de voisines. Une fois les cas étudiés, toutes les autres cases avaient 8 voisines, comme on voit sur le dessin. 
 
Calcul du nombre de cellules voisines vivantes
Puisque nos cellules vivantes valent 1, les mortes 0, une somme des éléments nous donne uniquement le nombre de cellules vivantes.
Donc une fois bien ciblé les cellules voisines d’une même cellule, il suffit de faire leur somme pour trouver le nombre de cellules vivantes.
 
On a essayé un match case, mais Python 3.0 n’est pas compatible, et c’est compliqué de mettre plusieurs variables en différenciateurs.
Donc on a choisi plusieurs if et elsif pour tout cerner.
La variable voisviv est la somme des 1 des cellules voisines de chaque cellule.

Comparaison aux règles du jeu
Avec le nombre de voisines vivantes, il ne reste que l’état initial de chaque cellule pour donner leur état au prochain tour.
C’était simple, il suffit de différencier les cas, et plutôt que de multiplier les if, par exemple si 1 cellule vivante a 2 ou 3 voisines vivantes, elle survit, nous faisons la logique inverse de la tuer en la mettant à 0 si elle en a + ou -
 
Pour ne pas modifier la grille initiale dans le programme, on crée une grille temporaire copie qui elle sera modifiée dans la fonction
  
Fin de la 1ère évolution et tests du fonctionnement
Avec ces 2 notions de cellules voisines et de règles, nous codons un 1er tour complet. En sortie nous devrions avoir une liste avec les bonnes valeurs de 0 et 1 selon les cellules mortes et nées.
A présent nous pouvions vérifier notre code, en affichant la liste post-évolution de notre programme.
Pour pouvoir vérifier plus simplement, on a fixé une grille test, et sur Excel on a représenté graphiquement ses valeurs, et celles attendues en fin du 1er tour théoriquement.  

Mais la grille en sortie de notre code était fausse, pour comprendre pourquoi on a mis des affichages au différentes étapes de notre fonction d’évolution voisins() : l’erreur pouvait venir d’une mauvaise sélection des cellules voisines, d’un mauvais compte, ou alors d’une mauvaise application des règles.

Les print de localisation des cases, « haut gauche », puis « haut », « haut droite », « colonne gauche », reste, « colonne droite », […] jusqu’à « bas droite » à grille[3][5] la dernière cellule du tableau, nous ont montré qu’il n’y avait pas d’erreurs dans le choix des cellules voisines.

Comparaison des valeurs de cellules voisines.
  
Nous avons bien vérifié que l’indentation ne mettait pas notre écriture des nouvelles valeurs de cellules en boucle, mais non, pourtant l’erreur ne pouvait venir que d’un changement de valeurs de la grille entre son tour 0 et les suivants.
En affichant l’évolution de la grille de base et de celle copiée après l’évolution de chaque cellule, nous nous sommes rendus compte qu’elle prenaient les mêmes valeurs : en fait le grilletemp = grille fait que les 2 variables pointent vers un même objet, en écrivant de nouvelles valeurs dans la copie on modifiait aussi la grille de départ, et on faussait les résultats.
 
Nous avions besoin de figer la copie de la grille en début de fonction, donc nous avons utilisé la fonction deepcopy() du module copy.
Cela a marché, on peut voir que la grille initiale reste figée, et la 2nde liste évolue à partir du calcul des cellules voisines depuis la grille figée au tour 0.
 


  
Affichage
Repère et carrés noirs
Maintenant que la logique de jeu est programmée, peu importe les valeurs de cellules, on veut une fonction qui prend des valeurs à 1 d’un tableau et les met dans un graphique représentés par des carrés noirs.
 
La subtilité est que notre tableau se remplit par le « haut » en axe Y descendant comme sur un tableur, alors que dans les coordonnées d’un repère l’origine est en bas.
Paramétrage du repère
Nous avons mis du temps à paramétrer l’affichage du quadrillage, et à enlever les « labels » sur les axes. 
 
Voilà nos paramètres pour obtenir une grille de jeu nette 
 
 
 
Programme principal et fin de la programmation
Maintenant que nous affichions n’importe quel tableau en bon graphique de jeu de la vie, nous devons programmer l’interactivité du jeu.

On demande au joueur/joueuse de choisir les dimensions de la grille, et le nombre d’itérations de jeu.
 
On ajoute un compte en deepcopy des cellules vivantes en début de partie et à la fin.
 
On affiche la grille et les cellules au début après leur choix aléatoire, puis en fin de chaque tour.
 
Il faut simplement faire attention à transformer les int en str pour les afficher dans du print, et les str en int pour calculer les nombres récupérés des input.
 
Conclusion
Le programme est fonctionnel, modulable, nous avons des fonctionnalités avancées.
On pourrait l’améliorer au niveau graphique, par exemple en apprenant à faire des animations entre les tours lorsqu’une cellule naît/meurt.
