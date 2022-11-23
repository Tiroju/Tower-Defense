# Tower-Defense

Objectif : Un jeu Tower Defense avec plusieurs cartes, tours et ennemis. Choix de la carte possible avec une interface.

MVP : Un jeu Tower Defense qui fonctionne même avec quelques problèmes et des fonctionnalités en moins que l'objectif final.
      Le joueur peut choisir le placement des tours sur des zones prédédfinies en utilisant de l'argent qu'il obtient en éliminant les ennemis et l'aarrivée d'un             ennemi au bout du chemin fait perdre de la vie au joueur.

Objectifs intermédiaires :
- Commencer par une carte simple (ligne droite et un virage) avec 1 ou 2 tours fixes et un type ennemi qui suit le chemin
                             
- Faire le placement des tours selon l'envie du joueur
                            
- Rajouter des cartes, tours et ennemis
                            
- Faire le système de coeurs du joueur et d'or (lâché par l'ennemi) qui permet d'acheter les tours
                            
- Faire l'interface de choix de carte

Structures de données : Classes, listes
                            
Fonctions :
- construire : Permet de construire une tour sur un emplacement dédié
- zone : Pour savoir si un ennemi entre dans la zone d'attaque de la tour
- tir : Si un ennemi est dans la zone, alors la tour tire lui inflige des dégâts
- rot : Pour faire tourner les sprites sans problème
- avancer : Pour faire avancer l'ennemi sur le chemin
- mort : Pour savoir si un ennemi est mort, donc s'il n'a plus de PV
- fin : Si l'ennemi arrive jusqu'à la fin du chemin alors le joueur perd un coeur et l'ennemi disparait
- collision : Pour créer des collisions entre les ennemis et éviter qu'ils s'empilent les uns sur les autres
