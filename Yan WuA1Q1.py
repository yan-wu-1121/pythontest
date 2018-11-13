import pygame #imports pygame library  
import os #imports os library
import random #imports random library

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 40) #puts the display screen near the top left of the monitor screen
pygame.init() #auto initializes all pygame modules 

#info = pygame.display.Info() 
SIZE = (1000, 700) #variable for size 1000, 700 
Green = (0, 255, 0) #creates the colour green for RGB
White = (255, 255, 255) #creates the colour white for RGB
Black = (0, 0, 0) #creates the colour black for RGB
screen = pygame.display.set_mode(SIZE) #sets the window to 1000, 700
pygame.display.set_caption('Picture') #puts the window caption to picture

pygame.draw.rect(screen, Green, (0, 530, 1000, 530)) #draws the ground/grass

pygame.draw.rect(screen, White, (310, 530, 430, -220)) #draws the houses base shape
pygame.draw.rect(screen, Black, (310, 530, 430, -220), 2) #draws the houses base shape border

pygame.draw.polygon(screen, (225, 50, 0), [[775, 350], [740, 275], [310, 275], [275, 350]]) #draws the roof 
pygame.draw.polygon(screen, Black, [[775, 350], [740, 275], [310, 275], [275, 350]], 2) #draws the roof border

pygame.draw.polygon(screen, (80, 40, 0), [[775, 350], [650, 230], [530, 350]]) #draws the first roof triangle
pygame.draw.polygon(screen, Black, [[775, 350], [650, 230], [530, 350]], 2) #draws the first roof triangle border

pygame.draw.polygon(screen, White, [[750, 340], [650, 245], [555, 340]]) #draws the second roof triangle
pygame.draw.polygon(screen, Black, [[750, 340], [650, 245], [555, 340]], 2) #draws the second roof triangle border

pygame.draw.polygon(screen, (225, 50, 0), [[350, 220], [310, 220], [310, 275], [350, 275]]) #draws the chimney
pygame.draw.polygon(screen, Black, [[350, 220], [310, 220], [310, 275], [350, 275]], 2) #draws the chimney border

pygame.draw.line(screen, Black, (530, 350), (530, 530), 2) #draws the wall separating the porch thing from the house bulk thing

pygame.draw.rect(screen, (80, 40, 0), (475, 530, 55, -135))

pygame.display.flip()   
pygame.time.wait(12000)
pygame.quit()
