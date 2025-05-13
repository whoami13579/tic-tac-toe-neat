import pygame


class Board:
    def __init__(self):
        self.image: pygame.Surface = pygame.image.load("/home/chu/Code/tic-tac-toe-neat/tic_tac_toe/assets/board.png")
    

    def draw(self, window: pygame.Surface):
        image: pygame.Surface = self.image
        window.blit(image, (0, 0))
