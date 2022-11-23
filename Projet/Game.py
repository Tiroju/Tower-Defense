import pygame # importation de la librairie pygame
import Tours
import Interface
import sys # pour fermer correctement l'application
from pygame import mixer

#choix de la carte
carte = Interface.choix_carte()

# lancement des modules inclus dans pygame
pygame.init()

# création d'une fenêtre de 1250 par 625
screen = pygame.display.set_mode((1250,625))
pygame.display.set_caption("Tower Defense")

#Musique de fond
mixer.init()
mixer.music.load("Musique.mp3")
mixer.music.play(-1)

# chargement de l'image de fond en fonction de la carte choisie
fond = pygame.image.load("PNG/Carte"+str(carte)+".png")
fond = pygame.transform.scale(fond, (1250, 625))

font = pygame.font.Font('freesansbold.ttf', 20)
fontGame = pygame.font.Font("freesansbold.ttf", 150)
argent = 150
vie = 20

#Création des zones de construction et des vagues d'ennemis par rapport à la carte choisie
if carte == 1:
    listeEnnemis = [["soldat1","soldat2"],
               ["soldat1","soldat1","soldat1","soldat2","soldat2","soldat3"],
               ["soldat1","soldat1","soldat1","soldat1","soldat2","soldat2","soldat3","soldat3","tank1"],
               ["soldat3","soldat3","soldat2","soldat2","soldat2","soldat3","soldat3","tank1","tank1","tank1","tank2"],
               ["soldat3","soldat3","soldat2","soldat2","soldat2","soldat3","soldat3","tank1","tank1","tank1","tank2","tank2","tank2"]]
    build1 = Tours.Build(260,225,1)
    build2 = Tours.Build(235,480,2)
    build3 = Tours.Build(350,480,3)
    build4 = Tours.Build(505,170,4)
    build5 = Tours.Build(505,320,5)
    build6 = Tours.Build(705,250,6)
    build7 = Tours.Build(943,295,7)
    build8 = Tours.Build(943,50,8)
    build9 = Tours.Build(750,525,9)
elif carte == 2:
    listeEnnemis = [["soldat1","soldat2"],
               ["soldat1","soldat1","soldat1","soldat2","soldat2","soldat3"],
               ["soldat1","soldat1","soldat1","soldat1","soldat2","soldat2","soldat3","soldat3","tank1"],
               ["soldat3","soldat3","soldat2","soldat2","soldat2","soldat3","soldat3","tank1","tank1","tank1","tank2"],
               ["soldat3","soldat3","soldat2","soldat2","soldat2","soldat3","soldat3","tank1","tank1","tank1","tank2","tank2"],
               ["soldat3","soldat3","soldat2","soldat2","soldat2","soldat3","soldat3","tank1","tank1","tank1","tank2","tank2","tank2","tank2"]]
    build1 = Tours.Build(390,280,1)
    build2 = Tours.Build(50,280,2)
    build3 = Tours.Build(250,30,3)
    build4 = Tours.Build(430,30,4)
    build5 = Tours.Build(390,420,5)
    build6 = Tours.Build(655,320,6)
    build7 = Tours.Build(655,165,7)
    build8 = Tours.Build(1025,185,8)
    build9 = Tours.Build(925,320,9)
else:
    listeEnnemis = [["soldat1","soldat2"],
               ["soldat1","soldat1","soldat1","soldat2","soldat2","soldat3"],
               ["soldat1","soldat1","soldat1","soldat1","soldat2","soldat2","soldat3","soldat3","tank1"],
               ["soldat3","soldat3","soldat2","soldat2","soldat2","soldat3","soldat3","tank1","tank1","tank1","tank2"],
               ["soldat3","soldat3","soldat2","soldat2","soldat2","soldat3","soldat3","tank1","tank1","tank1","tank2","tank2"],
               ["soldat3","soldat3","soldat2","soldat2","soldat2","soldat3","soldat3","tank1","tank1","tank1","tank2","tank2","tank2","tank2"],
               ["soldat2","soldat3","soladt3","tank1","tank1","tank1","tank1","tank2","tank2","tank2","tank2","tank2","tank2"],
               ["tank1","tank1","tank1","tank1","tank1","tank1","tank1","tank2","tank2","tank2","tank2","tank2","tank2","tank2"]]
    build1 = Tours.Build(285,310,1)
    build2 = Tours.Build(285,150,2)
    build3 = Tours.Build(20,50,3)
    build4 = Tours.Build(20,400,4)
    build5 = Tours.Build(545,390,5)
    build6 = Tours.Build(600,180,6)
    build7 = Tours.Build(860,480,7)
    build8 = Tours.Build(920,220,8)
    build9 = Tours.Build(1100,380,9)
        
tous_morts = False
vague = []

towers = [0]*9

clock = pygame.time.Clock()
t_passe_vague = 30000

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    
    #Affichage des textes pour l'or et la vie à l'écran
    textOr = font.render("OR : " + str(argent), True, (255,255,255))
    screen.blit(textOr, (10, 10))
    
    textVie = font.render("VIE : " + str(vie), True, (255,255,255))
    screen.blit(textVie, (10, 30))
    
    t = clock.tick()
    
    
    t_passe_vague += t
    #Création de la vague s'il se sont écoulés 30 secondes depuis la dernière ou si tous les ennemis sont morts
    for ennemis in listeEnnemis:
        if t_passe_vague >= 30000 or tous_morts == True:
            vague = []
            for ennemi in ennemis:
                vague.append(Tours.Ennemi(carte,ennemi))
            del listeEnnemis[0]
            t_passe_vague = 0
            tous_morts = False
            
            
    
    #Affichage des zones de construction
    screen.blit(build1.image,[build1.x,build1.y])
    screen.blit(build1.num,[build1.x+15,build1.y+60])
    screen.blit(build2.image,[build2.x,build2.y])
    screen.blit(build2.num,[build2.x+15,build2.y+60])
    screen.blit(build3.image,[build3.x,build3.y])
    screen.blit(build3.num,[build3.x+15,build3.y+60])
    screen.blit(build4.image,[build4.x,build4.y])
    screen.blit(build4.num,[build4.x+15,build4.y+60])
    screen.blit(build5.image,[build5.x,build5.y])
    screen.blit(build5.num,[build5.x+15,build5.y+60])
    screen.blit(build6.image,[build6.x,build6.y])
    screen.blit(build6.num,[build6.x+15,build6.y+60])
    screen.blit(build7.image,[build7.x,build7.y])
    screen.blit(build7.num,[build7.x+15,build7.y+60])
    screen.blit(build8.image,[build8.x,build8.y])
    screen.blit(build8.num,[build8.x+15,build8.y+60])
    screen.blit(build9.image,[build9.x,build9.y])
    screen.blit(build9.num,[build9.x+15,build9.y+60])
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
            
        # gestion du clavier
        k = pygame.key.get_pressed()
        if k[pygame.K_a] and argent >= 40: # si la touche est appuyée
            if k[pygame.K_1] and build1.construire(): #Si la touche 1 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build1.x,build1.y,1,1)
                argent -= 40
                towers[0] = tour
            if k[pygame.K_2] and build2.construire(): #Si la touche 2 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build2.x,build2.y,1,2)
                argent -= 40
                towers[1] = tour
            if k[pygame.K_3] and build3.construire(): #Si la touche 3 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build3.x,build3.y,1,3)
                argent -= 40
                towers[2] = tour
            if k[pygame.K_4] and build4.construire(): #Si la touche 4 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build4.x,build4.y,1,4)
                argent -= 40
                towers[3] = tour
            if k[pygame.K_5] and build5.construire(): #Si la touche 5 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build5.x,build5.y,1,5)
                argent -= 40
                towers[4] = tour
            if k[pygame.K_6] and build6.construire(): #Si la touche 6 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build6.x,build6.y,1,6)
                argent -= 40
                towers[5] = tour
            if k[pygame.K_7] and build7.construire(): #Si la touche 7 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build7.x,build7.y,1,7)
                argent -= 40
                towers[6] = tour
            if k[pygame.K_8] and build8.construire(): #Si la touche 8 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build8.x,build8.y,1,8)
                argent -= 40
                towers[7] = tour
            if k[pygame.K_9] and build9.construire(): #Si la touche 9 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build9.x,build9.y,1,9)
                argent -= 40
                towers[8] = tour
                
        if k[pygame.K_z] and argent >= 60: # si la touche z est appuyée
            if k[pygame.K_1] and build1.construire(): #Si la touche 1 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build1.x,build1.y,2,1)
                argent -= 60
                towers[0] = tour
            if k[pygame.K_2] and build2.construire(): #Si la touche 2 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build2.x,build2.y,2,2)
                argent -= 60
                towers[1] = tour
            if k[pygame.K_3] and build3.construire(): #Si la touche 3 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build3.x,build3.y,2,3)
                argent -= 60
                towers[2] = tour
            if k[pygame.K_4] and build4.construire(): #Si la touche 4 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build4.x,build4.y,2,4)
                argent -= 60
                towers[3] = tour
            if k[pygame.K_5] and build5.construire(): #Si la touche 5 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build5.x,build5.y,2,5)
                argent -= 60
                towers[4] = tour
            if k[pygame.K_6] and build6.construire(): #Si la touche 6 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build6.x,build6.y,2,6)
                argent -= 60
                towers[5] = tour
            if k[pygame.K_7] and build7.construire(): #Si la touche 7 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build7.x,build7.y,2,7)
                argent -= 60
                towers[6] = tour
            if k[pygame.K_8] and build8.construire(): #Si la touche 8 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build8.x,build8.y,2,8)
                argent -= 60
                towers[7] = tour
            if k[pygame.K_9] and build9.construire(): #Si la touche 9 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build9.x,build9.y,2,9)
                argent -= 60
                towers[8] = tour
                
        if k[pygame.K_e] and argent >= 70: # si la touche e est appuyée
            if k[pygame.K_1] and build1.construire(): #Si la touche 1 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build1.x,build1.y,3,1)
                argent -= 70
                towers[0] = tour
            if k[pygame.K_2] and build2.construire(): #Si la touche 2 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build2.x,build2.y,3,2)
                argent -= 70
                towers[1] = tour
            if k[pygame.K_3] and build3.construire(): #Si la touche 3 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build3.x,build3.y,3,3)
                argent -= 70
                towers[2] = tour
            if k[pygame.K_4] and build4.construire(): #Si la touche 4 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build4.x,build4.y,3,4)
                argent -= 70
                towers[3] = tour
            if k[pygame.K_5] and build5.construire(): #Si la touche 5 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build5.x,build5.y,3,5)
                argent -= 70
                towers[4] = tour
            if k[pygame.K_6] and build6.construire(): #Si la touche 6 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build6.x,build6.y,3,6)
                argent -= 70
                towers[5] = tour
            if k[pygame.K_7] and build7.construire(): #Si la touche 7 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build7.x,build7.y,3,7)
                argent -= 70
                towers[6] = tour
            if k[pygame.K_8] and build8.construire(): #Si la touche 8 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build8.x,build8.y,3,8)
                argent -= 70
                towers[7] = tour
            if k[pygame.K_9] and build9.construire(): #Si la touche 9 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build9.x,build9.y,3,9)
                argent -= 70
                towers[8] = tour
                    
        if k[pygame.K_r] and argent >= 150: # si la touche r est appuyée
            if k[pygame.K_1] and build1.construire(): #Si la touche 1 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build1.x,build1.y,4,1)
                argent -= 150
                towers[0] = tour
            if k[pygame.K_2] and build2.construire(): #Si la touche 2 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build2.x,build2.y,4,2)
                argent -= 150
                towers[1] = tour
            if k[pygame.K_3] and build3.construire(): #Si la touche 3 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build3.x,build3.y,4,3)
                argent -= 150
                towers[2] = tour
            if k[pygame.K_4] and build4.construire(): #Si la touche 4 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build4.x,build4.y,4,4)
                argent -= 150
                towers[3] = tour
            if k[pygame.K_5] and build5.construire(): #Si la touche 5 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build5.x,build5.y,4,5)
                argent -= 150
                towers[4] = tour
            if k[pygame.K_6] and build6.construire(): #Si la touche 6 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build6.x,build6.y,4,6)
                argent -= 150
                towers[5] = tour
            if k[pygame.K_7] and build7.construire(): #Si la touche 7 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build7.x,build7.y,4,7)
                argent -= 150
                towers[6] = tour
            if k[pygame.K_8] and build8.construire(): #Si la touche 8 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build8.x,build8.y,4,8)
                argent -= 150
                towers[7] = tour
            if k[pygame.K_9] and build9.construire(): #Si la touche 9 est appuyée et qu'il n'y a pas déjà de tour sur cet emplacement
                tour = Tours.Tour(build9.x,build9.y,4,9)
                argent -= 150
                towers[8] = tour
    
    #Affichage des tours et leurs socles
    for tour in towers:
        if tour != 0:
            screen.blit(tour.image_socle,[tour.x,tour.y])
            screen.blit(tour.image_rot,[tour.x,tour.y])
    
    tous_morts = True
    for mob in vague:
        mob.avancer()
        if mob.collision(vague):
            screen.blit(mob.image,[mob.x, mob.y]) # appel de la fonction qui dessine les ennemis
        #Tir des tours après un certain temps selon leur type
        for tour in towers:
            if tour != 0:
                tour.t_tir += t
                if tour.num == 1:
                    if tour.t_tir >= 200:
                        if tour.zone(mob):
                            tour.tir(mob)
                            screen.blit(tour.image_tir,[tour.tir_x,tour.tir_y])
                            tour.t_tir = 0
                elif tour.num == 2:
                    if tour.t_tir >= 1000:
                        if tour.zone(mob):
                            tour.tir(mob)
                            screen.blit(tour.image_tir,[tour.tir_x,tour.tir_y])
                            tour.t_tir = 0
                elif tour.num == 3:
                    if tour.t_tir >= 1500:
                        if tour.zone(mob):
                            tour.tir(mob)
                            screen.blit(tour.image_tir,[tour.tir_x,tour.tir_y])
                            tour.t_tir = 0
                else:
                    if tour.t_tir >= 5000:
                        if tour.zone(mob):
                            tour.tir(mob)
                            screen.blit(tour.image_tir,[tour.tir_x,tour.tir_y])
                            tour.t_tir = 0
        if mob.mort():
            argent += mob.argent
        if mob.fin():
            vie -= mob.degats
        if mob.vivant:
            tous_morts = False
            
    if listeEnnemis == [] and tous_morts == True:
        textVictoire = fontGame.render("VICTOIRE", True, (0,0,255))
        screen.blit(textVictoire, (300, 300))
    if vie <= 0:
        textDefaite = fontGame.render("DEFAITE", True, (255,0,0))
        screen.blit(textDefaite, (300, 300))
    
    clock.tick(40)
    
    pygame.display.update() # pour ajouter tout changement à l'écran