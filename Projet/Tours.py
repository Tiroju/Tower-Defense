import pygame  # necessaire pour charger les images et les sons
import math


class Build(): # classe pour créer les zones pour construire les tours
    def __init__(self,x:int,y:int,num:int):
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
            
            

class Tour(pygame.sprite.Sprite): # classe pour créer les tours
    def __init__(self,x:int,y:int,num:int,build:int):
        self.x = x
        self.y = y
        self.num = num
        self.build = build
        self.sens = "G"
        self.image = pygame.image.load("PNG/Tours/Tour"+str(num)+".png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image_socle = pygame.image.load("PNG/Socle_tour"+str(num)+".png")
        self.image_socle = pygame.transform.scale(self.image_socle, (80, 80))
        self.angle = 0
        self.change_angle = 0
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
        self.image_rot = self.image
        self.rect = self.image_rot.get_rect(center=(32,32))
        
    def zone(self,ennemi:object)->bool:
        """
        Fonction qui permet de savoir si un ennemi se trouve à portée de la tour.
        Renvoie True si un ennemi l'est.
        """
        if (math.fabs(self.y - ennemi.y) < 150) and (math.fabs(self.x - ennemi.x) < 150):
            return True
        
    def tir(self,ennemi:object):
        """
        Fonction qui permet à la tour de tirer et ainsi d'infliger des dégâts à l'ennemi.
        Permet également de gérer les animations de tir et de recharge pour chaque tour.
        """
        #Calculs pour trouver l'angle nécessaire afin de tourner la tour
        dx = ennemi.x - self.x
        dy = ennemi.y - self.y
        rads = math.atan2(-dy,dx)
        rads %= 2*math.pi
        degs = math.degrees(rads)
        self.change_angle = 360 - degs
        self.rot()
        
        if self.num == 1:
            if self.sens == "G":
                self.tir_x = self.x + 17
                self.sens = "D"
            else:
                self.tir_x = self.x - 17
                self.sens = "G"
        elif self.num == 2:
            if self.sens == "G":
                self.tir_x += 17
                self.sens = "D"
                self.image = pygame.image.load("PNG/Tours/Tour2.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            else:
                self.tir_x -= 17
                self.sens = "G"
                self.image = pygame.image.load("PNG/Tours/Tour2_vide.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
        elif self.num == 3:
            if self.sens == "G":
                self.tir_x += 17
                self.sens = "D"
                self.image = pygame.image.load("PNG/Tours/Tour3.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            else:
                self.tir_x -= 17
                self.sens = "G"
                self.image = pygame.image.load("PNG/Tours/Tour3_vide.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            if self.sens == "G":
                self.sens = "D"
                self.image = pygame.image.load("PNG/Tours/Tour4_vide.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
            else:
                self.sens = "G"
                self.image = pygame.image.load("PNG/Tours/Tour4.png")
                self.image = pygame.transform.scale(self.image, (80, 80))
        ennemi.vie -= self.degats
        
    def rot(self):
        """
        Fonction qui permet de tourner le sprite de la tour sans qu'elle soit déformée ou que son centre ne change.
        """
        self.image_rot = pygame.transform.rotate(self.image,self.angle)
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.image_rot.get_rect(center=self.rect.center)
        
        
class Ennemi(): # classe pour créer les tours
    def __init__(self,carte:int,mob:str):
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
            self.vie = 7
            self.vitesse = 1
            self.degats = 1
            self.argent = 5
        elif mob == "soldat2":
            self.vie = 5
            self.vitesse = 2
            self.degats = 1
            self.argent = 5
        elif mob == "soldat3":
            self.vie = 12
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
            self.vitesse = 0.5
            self.degats = 10
            self.argent = 200
        
    def avancer(self):
        """
        Fonction qui permet aux ennemis d'avancer selon un parcours prédéfini pour chacune des cartes.
        """
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
                
    def mort(self)->bool:
        """
        Fonction qui permet de savoir si un ennemi est mort, c'est-à-dire s'il n'a plus de PV.
        Renvoie True si l'ennemi est mort.
        """
        if self.vie <= 0 and self.y < 800:
            self.x = 1400
            self.y = 800
            self.vivant = False
            return True
        
    def fin(self)->bool:
        """
        Fonction qui permet de savoir si un ennemi est arrivé à la fin de son parcours.
        Si c'est le cas, enlève de la vie au joueur et renvoie True, sinon renvoie False
        """
        if self.carte == 1 and (self.x == 1250 or self.x == 1251) and self.y == 420:
            self.x = 1400
            self.y = 800
            self.vivant = False
            return True
        elif self.carte == 2 and (self.x == 1250 or self.x == 1252) and self.y == 70:
            self.x = 1400
            self.y = 800
            self.vivant = False
            return True
        elif self.carte== 3 and (self.x == 975 or self.x == 976) and self.y == 600:
            self.x = 1400
            self.y = 800
            self.vivant = False
            return True
        return False
    
    def collision(self,vague:list)->bool:
        """
        Fonction qui fait avancer l'ennemi seulement s'il n'y en n'a pas déjà un devant, sinon fait avancer celui qui est devant.
        Renvoie True s'il y a collision entre 2 ennemis.
        """
        for mob in vague:
            if (math.fabs(self.y - mob.y) < 50) and (math.fabs(self.x - mob.x) < 50):
                if self.y > mob.y or self.x > mob.x:
                    self.avancer()
                else:
                    mob.avancer()
                return True
        
