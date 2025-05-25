import pygame


class Piece:
    def __init__(self, circle:bool, x:int, y:int, width: int, height: int):
        image_path = "/home/chu/Code/tic-tac-toe-neat/tic_tac_toe/assets/"
        # image_path = "/Users/mba/Code/tic-tac-toe-neat/tic_tac_toe/assets/"
        image_path += "o3.png" if circle else "x.png"
        self.__image = pygame.image.load(image_path)
        self.__image = pygame.transform.scale(self.__image, ((width // 3), (height // 3)))
        
        self.__x = x
        self.__y = y

        self.__width = width
        self.__height = height
    

    def draw(self, window: pygame.Surface):
        window.blit(self.__image, (self.__width // 3 * self.__x, self.__height // 3 * self.__y))
