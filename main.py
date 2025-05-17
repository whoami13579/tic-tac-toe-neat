import pygame
from tic_tac_toe import Game
import neat
import os
import pickle


WIDTH, HEIGHT = 600, 600

class TicTacToeGame:
    def __init__(self, width: int, height: int):
        self.__window = pygame.display.set_mode((width, height))
        self.__game = Game(self.__window, width, height)
    
    def testGame(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN and self.__game.getRun():
                    self.__game.addPiece()
            
            self.__game.draw()

        pygame.quit()


if __name__ == "__main__":
    ticTacToeGame = TicTacToeGame(WIDTH, HEIGHT)
    ticTacToeGame.testGame()
