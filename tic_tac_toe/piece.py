import pygame


class Piece:
    def __init__(self, circle:bool, x:int, y:int):
        image_path: str = "/home/chu/Code/tic-tac-toe-neat/tic_tac_toe/assets/"
        image_path += "o.png" if circle else "x.png"
        self.image:pygame.surface = pygame.image.load(image_path).convert()
        
        self.x: int = x
        self.y: int = y
    

    def draw(self, window: pygame.Surface):
        image:pygame.Surface = self.image
        window.blit(image, (0, 0))
