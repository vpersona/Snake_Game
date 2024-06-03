# Snake Game

This is a classic Snake game implemented using Pygame. The player controls a snake that grows in length as it eats fruits that appear on the screen. The game ends if the snake collides with itself or the boundaries of the game window.

## 1. Features
* **Snake Movement:** The snake can move in four directions: up, down, left, and right.
* **Fruit Eating:** When the snake eats a fruit, it grows in length and a sound effect is played.
* **Score Tracking:** The player's score is displayed on the screen, which increases as the snake eats more fruits.
* **Grass Background:** The game features a patterned grass background.

## 2. Getting Started
**Prerequisites**

* Python 3.x
* Pygame library 

**Installation**

I. Clone the repository:

```
git clone https://github.com/vpersona/Snake_Game.git
cd Snake_Game
```
II. Install the Pygame library:

```
pip install pygame
```

## 3.Running the Game
Run the game script:
```
python main.py
```

## 4. Game Controls
Arrow Keys: Use the arrow keys to change the direction of the snake.
* Up: Move the snake up.
* Down: Move the snake down.
* Left: Move the snake left.
* Right: Move the snake right.

## 4. Code Overview
### Snake Class 

The **SNAKE class** is responsible for managing the snake's behavior, including movement, growth, and drawing the snake on the screen.
```python
class SNAKE():
    def __init__(self):
        # Initializing the snake body, direction, and new block flag
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        # Loading snake head, tail, and body images
        # ...

        # Loading crunch sound
        self.crunch_sound = pygame.mixer.Sound('sound/eating-sound-effect.mp3')
```
    def draw_snake(self):
        # Update head and tail graphics before drawing
        self.update_head_graphics()
        self.update_tail_graphics()

        # Draw each block of the snake's body
        # ...

    def update_head_graphics(self):
        # Update head graphic based on direction
        # ...

    def update_tail_graphics(self):
        # Update tail graphic based on direction
        # ...

    def move_snake(self):
        # Move the snake and add new block if needed
        # ...

    def add_block(self):
        # Set flag to add a new block
        self.new_block = True

    def play_crunch_sound(self):
        # Play crunch sound
        self.crunch_sound.play()
    
    def reset(self):
        # Reset snake to initial state
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
### Fruit Class
The **FRUIT class** handles the creation and positioning of the fruit that the snake eats.

```python
class FRUIT:
    def __init__(self):
        # Initialize fruit position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
```
    def draw_fruit(self):
        # Draw the fruit on the screen
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        
    def randomize(self):
        # Randomize fruit position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

### Main Class
The **MAIN class** manages the overall game logic, including updating game states, drawing elements, checking for collisions, and handling game over scenarios.

```python
class MAIN():
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
```
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
        # Check if snake eats the fruit
        if self.fruit.pos == self.snake.body[0]:
            # Reposition the fruit and add another block to the snake
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

            # Ensure the new fruit position does not overlap with the snake
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

    def check_fail(self):
        # Check if snake is outside the screen
        if not 0 <= self.snake.body[0].x <= cell_number - 1 or not 0 <= self.snake.body[0].y <= cell_number - 1:
            self.game_over()
      
        # Check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    def game_over(self):
        # Reset the game if snake fails
        self.snake.reset()
    
    def draw_grass(self):
        # Draw the grass pattern on the screen
        grass_color = (128, 197, 75)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        # Draw the current score on the screen
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_number * cell_size - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
## 5. Credits
**Graphics:** All graphics used in the game (snake head, body, tail, fruit) are custom made and stored in the graphics directory.

**Sound Effects:** The crunch sound effect played when the snake eats a fruit is stored in the sound directory.

**Fonts:** The game uses a pixelated font stored in the fonts directory.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Enjoy the game! 	