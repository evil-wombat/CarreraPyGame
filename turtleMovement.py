import pygame, sys
from pygame.locals import * # de pygame.locals importamos todo (para tener los atributos keys)
import random

class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0):
        
        isCustome = random.randint (0,4)
        self.custome = pygame.image.load("images/{}.png".format (self.__customes [isCustome]))
        
        self.position = [x, y]
        self.name = ""

class Game():
    def __init__ (self):
        self.__screen = pygame.display.set_mode ((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption ("Carrera de bichos")
        
        self.runner = Runner (320, 240)
    
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        # Mover hacia arriba runner
                        self.runner.position[1] -= 5
                    elif event.key == K_DOWN:
                        # Mover hacia abajo runner
                        self.runner.position [1] += 5
                    elif event.key == K_LEFT:
                        # Mover hacia la izq runer
                        self.runner.position [0] -= 5
                    elif event.key == K_RIGHT:
                        # Mover runner hacia dcha
                        self.runner.position [0] += 5
                    else:
                        pass
            
            self.__screen.blit (self.__background, (0, 0))
            self.__screen.blit (self.runner.custome, self.runner.position)
            
            pygame.display.flip()
            
print ('my name is {}'.format (__name__))

if __name__ == '__main__':
    game = Game ()
    pygame.init()
    game.start ()
                            