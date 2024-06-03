import pygame, sys, random
from pygame.math import Vector2

#Creating a Snake 

class SNAKE():
    def __init__(self):
        # Initializing the snake body, direction, and new block flag
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(0,0)
        self.new_block=False

        # Loading snake head images

        self.head_up=pygame.image.load('graphics/head-up.png').convert_alpha()
        self.head_down=pygame.image.load('graphics/head-down.png').convert_alpha()
        self.head_right=pygame.image.load('graphics/head-right.png').convert_alpha()
        self.head_left=pygame.image.load('graphics/head-left.png').convert_alpha()

        # Loading snake tail images

        self.tail_up=pygame.image.load('graphics/tail-up.png').convert_alpha()
        self.tail_down=pygame.image.load('graphics/tail-down.png').convert_alpha()
        self.tail_right=pygame.image.load('graphics/tail-right.png').convert_alpha()
        self.tail_left=pygame.image.load('graphics/tail-left.png').convert_alpha()

        # Loading snake body images

        self.body_vertical=pygame.image.load('graphics/body-vertical.png').convert_alpha()
        self.body_horizontal=pygame.image.load('graphics/body-horizontal.png').convert_alpha()

        self.body_tr=pygame.image.load('graphics/body-tr.png').convert_alpha()
        self.body_tl=pygame.image.load('graphics/body-tl.png').convert_alpha()
        self.body_br=pygame.image.load('graphics/body-br.png').convert_alpha()
        self.body_bl=pygame.image.load('graphics/body-bl.png').convert_alpha()
        
        # Loading snake crunch sound

        self.crunch_sound=pygame.mixer.Sound('sound/eating-sound-effect.mp3')
        

    def draw_snake(self):

        # Update head and tail graphics before drawing

        self.update_head_graphics()
        self.update_tail_graphics()

        #Draw each block of snake's body

        for index,block in enumerate(self.body):
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            #direction of head

            if index==0:
                screen.blit(self.head,block_rect)

            #direction of the tail

            elif index==len(self.body) -1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index+1]-block
                next_block=self.body[index-1]-block
                if previous_block.x ==next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y==next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                #Corners of snake
                else:
                    if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                        screen.blit(self.body_tl,block_rect)

                    elif previous_block.x==-1 and next_block.y==1 or previous_block.y==1 and next_block.x==-1:
                        screen.blit(self.body_bl,block_rect)
            
                    elif previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                        screen.blit(self.body_tr,block_rect)
            
                    elif previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x==1:
                        screen.blit(self.body_br,block_rect)
            
        

    def update_head_graphics(self):

        #update snake's head based on his direction

        head_relation=self.body[1] - self.body[0]
        
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation==Vector2(-1,0): self.head=self.head_right
        elif head_relation==Vector2(0,1): self.head=self.head_up
        elif head_relation==Vector2(0,-1): self.head=self.head_down

    def update_tail_graphics(self):

        #update snake's tail based on his direction

        tail_relation=self.body[-2] - self.body[-1]
        
        if tail_relation == Vector2(1,0): self.tail = self.tail_right
        elif tail_relation==Vector2(-1,0): self.tail=self.tail_left
        elif tail_relation==Vector2(0,1): self.tail=self.tail_down
        elif tail_relation==Vector2(0,-1): self.tail=self.tail_up

    def move_snake (self):

        if self.new_block==True: #adding a naew block to snake's body after eating a fruit
            body_copy=self.body[:] 
            body_copy.insert(0,body_copy[0] + self.direction) 
            self.body=body_copy[:]
            self.new_block=False
        else:
            body_copy=self.body[:-1] #creating a copy of the snakes body 
            body_copy.insert(0,body_copy[0] + self.direction) 
            self.body=body_copy[:]


    def add_block(self):
        #set flag to add a new block

        self.new_block=True

    def play_crunch_sound(self):
        #play crunch sound

        self.crunch_sound.play()
    
    def reset(self):
        #Reset snake to initial state 
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(0,0)

#Creating a fruit that will be showing on random cells ot the game screen

class FRUIT:
    def __init__(self):
        #initialize fruit position
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
        # create an x and y pos
        
    
    def draw_fruit(self):
        #create a rectangle and draw it
        fruit_rect=pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        
        

    def randomize(self):
        # randomize fruit position
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)

# Creating the Main class to manage game logic
class MAIN():

    def  __init__(self):
        self.snake = SNAKE()
        self.fruit=FRUIT()
        

    def update(self):
        # Update snake movement and check for collisions or failures
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
      

    def draw_elements(self):
        # Draw game elements (grass, fruit, snake, score)
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
       

    def check_collision(self):
        #check if snake eats the fruit
        if self.fruit.pos==self.snake.body[0]:
            
            #reposition the fruit and add another block to the snake
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

            #ensure the new fruit position desn't overlap with snake

            for block in self.snake.body[1:]:
                if block==self.fruit.pos:
                    self.fruit.randomize()

    def check_fail(self):
        #check if snake is outside the screen 

        if not 0<=self.snake.body[0].x <= cell_number-1 or not 0<=self.snake.body[0].y <= cell_number-1:
            self.game_over()
      
        #check if snake hits itself

        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                
                self.game_over()
                
    
    def game_over(self):
        #Reset the game if snake fails
        self.snake.reset()
    
    def draw_grass(self):
        #Draw the grass pattern
        grass_color=(128, 197, 75)
        for row in range(cell_number):
            if row%2==0:
                for col in range(cell_number):
                    if col%2==0:
                        grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col%2!=0:
                        grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    def draw_score(self):
        #Draw the current score on screen

        score_text=str(len(self.snake.body)-3)
        score_surface=game_font.render(score_text,True,(56,74,12))
        score_x=int(cell_size*cell_number - 60)
        score_y=int(cell_number*cell_size - 40)

        score_rect=score_surface.get_rect(center = (score_x,score_y))
        

        apple_rect=apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect=pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width+score_rect.width + 6,apple_rect.height +6)

        pygame.draw.rect(screen,(164,209,61),bg_rect)
        screen.blit(apple,apple_rect)
        screen.blit(score_surface,score_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)



pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

pygame.mixer.music.load('sound/background-music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#Display Surface/Screen
cell_size=40
cell_number=20
screen=pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))


#FPS limit
clock=pygame.time.Clock()

apple=pygame.image.load('graphics/apple.png').convert_alpha()
game_font=pygame.font.Font('fonts/Pixeled.ttf',25)



SCREEN_UPDATE= pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game=MAIN()

while True:
    # Get the current position of the mouse
    mouse_pos=pygame.mouse.get_pos()

    #Draw all elements
    for event in pygame.event.get():
        # Check if the user has requested to quit the game
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #check if it's time to update the screen
        if event.type==SCREEN_UPDATE:
            main_game.update()
        #check for key press to control snake's movement
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                #prevent snake from reversing direction
                if main_game.snake.direction.y !=1:
                    main_game.snake.direction=Vector2(0,-1)
                #prevent snake from reversing direction
            if event.key==pygame.K_DOWN:
                if main_game.snake.direction.y !=-1:
                    main_game.snake.direction=Vector2(0,1)
                #prevent snake from reversing direction
            if event.key==pygame.K_RIGHT:
                if main_game.snake.direction.x !=-1:
                    main_game.snake.direction=Vector2(1,0)
                #prevent snake from reversing direction
            if event.key==pygame.K_LEFT:
                if main_game.snake.direction.x !=1:
                    main_game.snake.direction=Vector2(-1,0)
                    
        


    screen.fill((175,200,75))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

