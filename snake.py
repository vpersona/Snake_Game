import pygame, sys, random
from pygame.math import Vector2

#Creating a fruit that will be showing on random cells ot the game screen

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
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,(120,160,130),fruit_rect)
        

    def randomize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)

#Creating a Snake 

class SNAKE():
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.new_block=False

        self.head_up=pygame.image.load('graphics/head-up.png').convert_alpha()
        self.head_down=pygame.image.load('graphics/head-down.png').convert_alpha()
        self.head_right=pygame.image.load('graphics/head-right.png').convert_alpha()
        self.head_left=pygame.image.load('graphics/head-left.png').convert_alpha()

        self.tail_up=pygame.image.load('graphics/tail-up.png').convert_alpha()
        self.tail_down=pygame.image.load('graphics/tail-down.png').convert_alpha()
        self.tail_right=pygame.image.load('graphics/tail-right.png').convert_alpha()
        self.tail_left=pygame.image.load('graphics/tail-left.png').convert_alpha()

        self.body_vertical=pygame.image.load('graphics/body-vertical.png').convert_alpha()
        self.body_horizontal=pygame.image.load('graphics/body-horizontal.png').convert_alpha()

        self.body_tr=pygame.image.load('graphics/body-tr.png').convert_alpha()
        self.body_tl=pygame.image.load('graphics/body-tl.png').convert_alpha()
        self.body_br=pygame.image.load('graphics/body-br.png').convert_alpha()
        self.body_bl=pygame.image.load('graphics/body-bl.png').convert_alpha()

    def draw_snake(self):

        self.update_head_graphics()

        for index,block in enumerate(self.body):
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            #direction of head

            if index==0:
                screen.blit(self.head_right,block_rect)

            else:
                pygame.draw.rect(screen,(180,100,120),block_rect)
        # for block in self.body:
        #     x_pos=int(block.x*cell_size)
        #     y_pos=int(block.y*cell_size)
        #     #create a rect and draw a rect
        #     block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)
        #     pygame.draw.rect(screen,(180,100,120),block_rect)  

    def update_head_graphics(self):
        head_relation=self.body[1] - self.body[0]
        if head_relation == Vector2(1,0):
            self.head = self.head_left

    def move_snake (self):

        if self.new_block==True: #adding a naew block to snake's bosy after eating a fruit
            body_copy=self.body[:] 
            body_copy.insert(0,body_copy[0] + self.direction) 
            self.body=body_copy[:]
            self.new_block=False
        else:
            body_copy=self.body[:-1] #creating a copy of the snakes body 
            body_copy.insert(0,body_copy[0] + self.direction) #direction --> player input
            self.body=body_copy[:]


    def add_block(self):
        self.new_block=True

class MAIN():

    def  __init__(self):
        self.snake = SNAKE()
        self.fruit=FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):

        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
            
            #reposition the fruit and add another block to the snake
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        #check if snake is outside the screen 

        if not 0<=self.snake.body[0].x <= cell_number-1 or not 0<=self.snake.body[0].y <= cell_number-1:
            self.game_over()
      
        #check if snake hits itself

        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()

#Display Surface/Screen
cell_size=40
cell_number=20
screen=pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))

#FPS limit
clock=pygame.time.Clock()

apple=pygame.image.load('graphics/apple.png').convert_alpha()


SCREEN_UPDATE= pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game=MAIN()

while True:
    #Draw all elements
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==SCREEN_UPDATE:
            main_game.update()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if main_game.snake.direction.y !=1:
                    main_game.snake.direction=Vector2(0,-1)

            if event.key==pygame.K_DOWN:
                if main_game.snake.direction.y !=-1:
                    main_game.snake.direction=Vector2(0,1)

            if event.key==pygame.K_RIGHT:
                if main_game.snake.direction.x !=-1:
                    main_game.snake.direction=Vector2(1,0)

            if event.key==pygame.K_LEFT:
                if main_game.snake.direction.x !=1:
                    main_game.snake.direction=Vector2(-1,0)



    screen.fill(pygame.Color(175,200,75))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

