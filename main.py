from typing_extensions import runtime
import pygame
import time

#------------------------------------------------------------------------------
displayWidth = 600                                                              #variables
displayHeight = 600
# background = (41,87,110)
clock = pygame.time.Clock()

running = True

pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Burger Time')

#-----------------------------chef walk-------------------------------------- move to class (study)
chefFront0 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\WalkFront\0.gif")
chefFront1 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\WalkFront\1.gif")

chefBack0 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\WalkBack\0.gif")
chefBack1 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\WalkBack\1.gif")

chefDead0 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\Dead\0.gif")
chefDead1 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\Dead\1.gif")

chefRight0 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\WalkRight\0.gif")
chefRight1 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\WalkRight\1.gif")

chefLeft0 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\WalkLeft\0.gif")
chefLeft1 = pygame.image.load(r"C:\Users\John Osias\Desktop\BurgerTime\Sprites\Chef\WalkLeft\1.gif")

chefX = 50
chefY = 450
chefImg = chefFront0

while running:
    clock.tick(60)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if chefImg != chefBack0:
            chefImg = chefBack0
            gameDisplay.blit(chefImg,(chefX,chefY))
        chefY-=1
    if keys[pygame.K_DOWN]:
        chefY+=2
        chefImg = chefFront0
    if keys[pygame.K_LEFT]:
        chefX-=2
        chefImg = chefLeft0
    if keys[pygame.K_RIGHT]:
        chefX+=2
        chefImg = chefRight0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting now....")
            running= False
        print(event)
        
    
    gameDisplay.blit(chefImg,(chefX,chefY))
    pygame.display.update()

pygame.quit()