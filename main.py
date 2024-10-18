import pygame
from pygame.locals import *
import time
import random

size = 45
    
class food:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("pic/khao.png").convert()
        self.parent_screen = parent_screen
        self.x = size*3
        self.y = size*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*size
        self.y = random.randint(1,19)*size


class Snake:
    def __init__(self, parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("pic/bl.png").convert()
        self.x = [size]*length
        self.y = [size]*length
        self.direction = "down"

   

    def increase_length(self):
        self.length += 1
        self.x.append(-1) 
        self.y.append(-1)
    

    def draw(self):
        self.parent_screen.fill((238,168,73))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"
    
    def move_left(self):
        self.direction = "left"
    
    def move_right(self):
        self.direction = "right"

    


    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "up":
            self.y[0] -= size
        if self.direction == "down":
            self.y[0] += size
        if self.direction == "left":
            self.x[0] -= size
        if self.direction == "right":
            self.x[0] += size 

        if self.x[0] < 0:
            self.x[0] = 900 - size
        elif self.x[0] >= 900:
            self.x[0] = 0
        if self.y[0] < 0:
            self.y[0] = 600 - size
        elif self.y[0] >= 600:
            self.y[0] = 0
        self.draw()

        



class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((900,600))
        self.surface.fill((111,255,51))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.food = food(self.surface)
        self.food.draw()

    def play(self):
        self.snake.walk()
        self.food.draw()

        for i in range(self.snake.length):
            if self.collision(self.snake.x[i], self.snake.y[i], self.food.x, self.food.y):
                self.snake.increase_length()
                self.food.move()
            

    def collision(self, x1,y1,x2,y2):
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 + size:
                return True
            return False


    def run(self):
        running = True
    
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False


            time.sleep(.3)
            self.play()

        


if __name__ == "__main__":
    game = Game()
    game.run()




