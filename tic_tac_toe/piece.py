import pygame


class Piece:
    def __init__(self, circle:bool, x:int, y:int, width: int, height: int):
        # image_path = "/home/chu/Code/tic-tac-toe-neat/tic_tac_toe/assets/"
        image_path = "/Users/mba/Code/tic-tac-toe-neat/tic_tac_toe/assets/"
        image_path += "o.png" if circle else "x.png"
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, ((width // 3), (height // 3)))
        
        self.x = x
        self.y = y

        self.width = width
        self.height = height
    

    def draw(self, window: pygame.Surface):
        window.blit(self.image, (self.width // 3 * self.x, self.height // 3 * self.y))
