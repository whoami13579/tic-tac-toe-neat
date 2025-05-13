import pygame
from tic_tac_toe import Game
import neat
import os
import pickle

class TicTacToeGame:
    def __init__(self, window: pygame.Surface, width: int, height: int):
        self.game: Game = Game()
        self.window: pygame.Surface = window
        self.width: int = width
        self.height: int = height


width, height = 600, 600
window = pygame.display.set_mode((width, height))
game = Game(window, width, height)
game.draw()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    game.draw()

pygame.quit()