import pygame
import sys

pygame.init()
size_block = 100
margin = 15
width = heigth = size_block*3 + margin*4

size_window = (width,heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("")

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
mas = [[0]*3 for i in range(3)]
query = 0 # 1 2 3 4 5 6 7
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            





