from pygame import *
from time import time as timer

back = (200, 255, 255)
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
clock = time.Clock()
racket1 = Player()
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update
    clock.tick(60)