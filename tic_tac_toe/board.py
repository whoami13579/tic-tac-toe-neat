import pygame


class Board:
    def __init__(self):
        self.__image = pygame.image.load("/home/chu/Code/tic-tac-toe-neat/tic_tac_toe/assets/board.png")
        # self.__image = pygame.image.load("/Users/mba/Code/tic-tac-toe-neat/tic_tac_toe/assets/board.png")
    

    def draw(self, window: pygame.Surface):
        window.blit(self.__image, (0, 0))
