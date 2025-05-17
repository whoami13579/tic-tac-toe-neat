import pygame


class Board:
    def __init__(self):
        # self.image: pygame.Surface = pygame.image.load("/home/chu/Code/tic-tac-toe-neat/tic_tac_toe/assets/board.png")
        self.image = pygame.image.load("/Users/mba/Code/tic-tac-toe-neat/tic_tac_toe/assets/board.png")
    

    def draw(self, window: pygame.Surface):
        window.blit(self.image, (0, 0))
