import pygame
from time import time as timer

back = (200, 255, 255)
win_widht = 600
win_height = 500
window = display.set_mode((win_height, win_widht))
window.fill(back)

game = True
clock = time.Clock()

while game:

    for event in event.get():
        if e.type == pygame.QUIT:
            game = False
    
    display.update
    clock.tick(60)