# Tower-Defense

Objectif : Un jeu Tower Defense avec plusieurs cartes, tours et ennemis et des compétences comme faire apparaitre des soldats pour bloquer les ennemis ou lancer des bombardements.

MVP : Un jeu Tower Defense qui fonctionne même avec quelques problèmes et des fonctionnalités en moins que l'objectif final.
      Le joueur peut choisir le placement des tours sur des zones prédédfinies en utilisant de l'argent qu'il obtient en éliminant les ennemis et l'aarrivée d'un             ennemi au bout du chemin fait perdre de la vie au joueur.

Objectifs intermédiaires :
- Commencer par une carte simple (ligne droite et un virage) avec 1 ou 2 tours fixes et un type ennemi qui suit le chemin
                             
- Faire le placement des tours selon l'envie du joueur
                            
- Rajouter des cartes, tours et ennemis
                            
- Faire le système de coeurs du joueur et d'or (lâché par l'ennemi) qui permet d'acheter les tours
                            
- Créer les compétences

Structures de données : Classes, listes
                            
Fonctions (liste non exhaustive):
- avance : Pour faire avancer l'ennemi sur le chemin
- zone : Pour savoir si un ennemi entre dans la zone d'attaque de la tour
- tir : Si l'ennemi est dans la zone, alors la tour tire
- degats : Si l'ennemi est touché, il perd des PV
- mort : Si l'ennemi n'a plus de PV il meurt et donne de l'or au joueur
- fin : Si l'ennemi arrive jusqu'à la fin du chemin alors le joueur perd un coeur et l'ennemi disparait
              
