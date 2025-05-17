import pygame
from tic_tac_toe import Game
import neat
import os
import pickle


WIDTH, HEIGHT = 600, 600

class TicTacToeGame:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game = Game(self.window, WIDTH, HEIGHT)
    
    def testGame(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN and self.game.getRun():
                    self.game.addPiece()
            
            self.game.draw()

        pygame.quit()


if __name__ == "__main__":
    ticTacToeGame = TicTacToeGame(WIDTH, HEIGHT)
    ticTacToeGame.testGame()
