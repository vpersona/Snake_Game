import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
        # create an x and y pos
        #draw a square
    
    def draw_fruit(self):
        #create a rectangle and draw it
        fruit_rect=pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(120,160,130),fruit_rect)

class SNAKE():
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(6,10),Vector2(7,10)]
    def draw_snake(self):
        for block in self.body:
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            #create a rect and draw a rect
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(180,100,120),block_rect)  


pygame.init()

#Display Surface/Screen
cell_size=40
cell_number=20
screen=pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
#FPS limit
clock=pygame.time.Clock()
snake=SNAKE()
fruit = FRUIT()
while True:
    #Draw all elements
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color(175,200,75))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)

