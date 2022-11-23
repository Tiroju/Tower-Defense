import pygame 
import sys 
  
def choix_carte():
    """
    Fonction qui permet d'afficher l'interface de choix de carte
    """
    
    # lancement des modules inclus dans pygame
    pygame.init() 
      
    # création d'une fenêtre de 1250 par 625
    screen = pygame.display.set_mode((1250,625))
    pygame.display.set_caption("Tower Defense")

    #Couleur claire du boutton
    color_light = (170,170,170) 
      
    #Couleur sombre du boutton
    color_dark = (100,100,100) 
      
    #Garde la largeur de l'écran dans une variable
    width = screen.get_width() 

    #Garde la hauteur de l'écran dans une variable
    height = screen.get_height() 
      
    #Création du texte pour le boutton
    smallfont = pygame.font.SysFont('Corbel',35) 
    text1 = smallfont.render('Carte 1' , True , (255,255,255))
    text2 = smallfont.render('Carte 2' , True , (255,255,255))
    text3 = smallfont.render('Carte 3' , True , (255,255,255))

    fontTitre = pygame.font.SysFont('Corbel',75) 
    textTitre = fontTitre.render("CALL OF DEFENSE" , True , (0,0,0))
      
    while True: 
          
        for ev in pygame.event.get(): 
              
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                  
            #Vérifie si un boutton de souris est cliqué 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                  
                #Si on appuie sur le boutton alors on lance le jeu
                if width/2-100 <= mouse[0] <= width/2+40 and height/2+75 <= mouse[1] <= height/2+115:
                    carte = 1
                    pygame.quit()
                    return carte
                    
                if width/2-100 <= mouse[0] <= width/2+40 and height/2+140 <= mouse[1] <= height/2+180:
                    carte = 2
                    pygame.quit()
                    return carte
                
                if width/2-100 <= mouse[0] <= width/2+40 and height/2+205 <= mouse[1] <= height/2+245:
                    carte = 3
                    pygame.quit()
                    return carte
                      
        #Remplit l'écran en blanc
        screen.fill((255,255,255)) 
        
        #Garde les coordonnées (x,y) du curseur de la souris
        mouse = pygame.mouse.get_pos() 
          
        #Si la souris passe sur le bouton il devient plus clair
        if width/2-100 <= mouse[0] <= width/2+40 and height/2+75 <= mouse[1] <= height/2+115: 
            pygame.draw.rect(screen,color_light,[width/2-100,height/2+75,140,40]) 
              
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-100,height/2+75,140,40])
            
        if width/2-100 <= mouse[0] <= width/2+40 and height/2+140 <= mouse[1] <= height/2+180: 
            pygame.draw.rect(screen,color_light,[width/2-100,height/2+140,140,40]) 
              
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-100,height/2+140,140,40])
            
        if width/2-100 <= mouse[0] <= width/2+40 and height/2+205 <= mouse[1] <= height/2+245: 
            pygame.draw.rect(screen,color_light,[width/2-100,height/2+205,140,40]) 
              
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-100,height/2+205,140,40]) 
          
        #Afficher le texte sur le boutton
        screen.blit(text1 , (width/2-77,height/2+80))
        screen.blit(text2 , (width/2-77,height/2+145))
        screen.blit(text3 , (width/2-77,height/2+210))
        
        #Afficher le nom du jeu
        screen.blit(textTitre, (330,150))
        
        #Afficher les barres bleues sur les côtés de l'écran
        pygame.draw.rect(screen,(0,149,182),[0,0,75,625])
        pygame.draw.rect(screen,(0,149,182),[1175,0,75,625]) 
        
        pygame.display.update() 
