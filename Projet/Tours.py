import pygame  # necessaire pour charger les images et les sons
import math


class Build(): # classe pour créer les zones pour construire les tours
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.constr = False
        self.num = pygame.image.load("PNG/maths/"+str(num)+".png")
        self.num = pygame.transform.scale(self.num, (50, 50))
        self.image = pygame.image.load("PNG/Build.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        
            
    def construire(self):
        """
        Fonction qui permet la construction d'une tour sur cette zone seulement s'il n'y a pas déjà une tour dessus.
        Renvoie True s'il n'y a pas de tour et False s'il y a déjà une tour.
        """
        if self.constr == False:
            self.constr = True
            return True
        return False
            
            

class Tour(): # classe pour créer les tours
    def __init__(self,x,y,num,build):
        self.x = x
        self.y = y
        self.num = num
        self.build = build
        self.sens = "G"
        self.image = pygame.image.load("PNG/Tours/Tour"+str(num)+"H.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image_socle = pygame.image.load("PNG/Socle_tour"+str(num)+".png")
        self.image_socle = pygame.transform.scale(self.image_socle, (80, 80))
        if num == 1:
            self.tir_x = x - 2
            self.tir_y = y - 35
            self.degats = 1
            self.t_tir = 200
            self.image_tir = pygame.image.load("PNG/Bonus/Tir_tour1.png")
            self.image_tir = pygame.transform.scale(self.image_tir, (65, 65))
        elif num == 2:
            self.tir_x = x - 2
            self.tir_y = y - 35
            self.degats = 3
            self.t_tir = 1000
            self.image_tir = pygame.image.load("PNG/Bonus/Roquette_mini.png")
            self.image_tir = pygame.transform.scale(self.image_tir, (65, 65))
        elif num == 3:
            self.tir_x = x - 2
            self.tir_y = y - 35
            self.degats = 5
            self.t_tir = 1500
            self.image_tir = pygame.image.load("PNG/Bonus/Roquette_mini.png")
            self.image_tir = pygame.transform.scale(self.image_tir, (65, 65))
        else:
            self.tir_x = x + 8
            self.tir_y = y - 35
            self.degats = 10
            self.t_tir = 5000
            self.image_tir = pygame.image.load("PNG/Bonus/Roquette.png")
            self.image_tir = pygame.transform.scale(self.image_tir, (65, 65))
        
    def zone(self,ennemi):
        if (math.fabs(self.y - ennemi.y) < 150) and (math.fabs(self.x - ennemi.x) < 150):
            return True
        
    def tir(self,ennemi):
        if self.num == 1:
            if self.sens == "G":
                self.tir_x += 17
                self.sens = "D"
            else:
                self.tir_x -= 17
                self.sens = "G"
        elif self.num == 2:
            if self.sens == "G":
                self.tir_x += 17
                self.sens = "D"
                self.image = pygame.image.load("PNG/Tours/Tour2H.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            else:
                self.tir_x -= 17
                self.sens = "G"
                self.image = pygame.image.load("PNG/Tours/Tour2_videH.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
        elif self.num == 3:
            if self.sens == "G":
                self.tir_x += 17
                self.sens = "D"
                self.image = pygame.image.load("PNG/Tours/Tour3H.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            else:
                self.tir_x -= 17
                self.sens = "G"
                self.image = pygame.image.load("PNG/Tours/Tour3_videH.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            if self.sens == "G":
                self.sens = "D"
                self.image = pygame.image.load("PNG/Tours/Tour4_videH.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            else:
                self.sens = "G"
                self.image = pygame.image.load("PNG/Tours/Tour4H.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
        ennemi.vie -= self.degats
        
        
class Ennemi():
    def __init__(self, carte,mob):
        self.mob = mob
        self.carte = carte
        self.vivant = True
        if carte == 1:
            self.x = 115
            self.y = 600
            
        elif carte == 2:
            self.x = 0
            self.y = 150
            
        else:
            self.x = 150
            self.y = 0
            
        if mob == "soldat1":
            self.vie = 15
            self.vitesse = 1.25
            self.degats = 1
            self.argent = 5
        elif mob == "soldat2":
            self.vie = 10
            self.vitesse = 2
            self.degats = 1
            self.argent = 5
        elif mob == "soldat3":
            self.vie = 20
            self.vitesse = 1
            self.degats = 2
            self.argent = 10
        elif mob == "tank1":
            self.vie = 50
            self.vitesse = 0.5
            self.degats = 4
            self.argent = 50
        elif mob == "tank2":
            self.vie = 100
            self.vitesse = 0.25
            self.degats = 10
            self.argent = 200
        
    def avancer(self):
        if self.carte == 1:
            if self.y > 350 and self.x == 115:
                self.y = self.y - self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"H.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.x < 390 and self.y == 350:
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.y > 60 and (self.x == 390 or self.x == 391):
                self.y = self.y - self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"H.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.x < 825 and self.y == 60:
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.y < 420 and self.x == 825:
                self.y = self.y + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"B.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.x < 1251 and self.y == 420:
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
                
        elif self.carte == 2:
            if self.x < 520 and self.y == 150:
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.y < 435 and self.x == 520:
                self.y = self.y + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"B.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.x < 800 and (self.y == 435 or self.y == 436):
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.y > 70 and self.x == 800:
                self.y = self.y - self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"H.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.x < 1251 and self.y == 70:
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
                
        else:
            if self.y < 450 and self.x == 150:
                self.y = self.y + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"B.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.x < 410 and self.y == 450:
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.y > 60 and self.x == 410:
                self.y = self.y - self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"H.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.x < 800 and self.y == 60:
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.y < 350 and self.x == 800:
                self.y = self.y + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"B.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.x < 975 and self.y == 350:
                self.x = self.x + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"D.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif self.y < 601 and (self.x == 975 or self.x == 976):
                self.y = self.y + self.vitesse
                self.image = pygame.image.load("PNG/Ennemis/"+self.mob+"B.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
                
    def mort(self):
        if self.vie <= 0 and self.y < 800:
            self.x = 1400
            self.y = 800
            self.vivant = False
            return True
        
    def fin(self):
        if self.carte == 1 and (self.x == 1250 or self.x == 1251) and self.y == 420:
            self.x = 1400
            self.y = 800
            return True
        elif self.carte == 2 and self.x == 1250 and self.y == 70:
            self.x = 1400
            self.y = 800
            return True
        elif self.carte== 3 and (self.x == 975 or self.x == 976) and self.y == 600:
            self.x = 1400
            self.y = 800
            return True
        return False
            

    """       
    def attack(self,para):
        if (math.fabs(self.y - para.y) < 40) and (math.fabs(self.x - para.x) < 40):
            return True
    """
        
