# import libraries
import pygame
import time
import random

# how fast will our snake go? Feel free to adjust this number
# CHALLENGE: can you increase the speed of the snake as the score gets higher?
snake_speed = 5

# window size (x is width, y is height)
window_x = 650
window_y = 650

# set colors in game using RGB format, this is a common format for adding colors in code and worth looking up
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# initialize pygame library and font module
# some modules within pygame need to be initialized before you can use them, pygame itself, and its font module for example
pygame.init()
pygame.font.init()

# create game window (this uses the sizes you set above)
# feel free to play around with font types, check pygame documentation to see what other fonts are available
pygame.display.set_caption('BIT Snake Tutorial')
game_window = pygame.display.set_mode((window_x, window_y))
main_font = pygame.font.SysFont("comicsans", 15)

# set frames per second (FPS), this is basically a refresh/update timer
fps = pygame.time.Clock()

# define snake's starting position
snake_position = [0, 0]

# create snake's first body, think of this as series of pixels/squares
snake_body = [[0, 0],
              [0, 0],
              [0, 0],
              [0, 0]]

# set the fruit spawning positions
fruit_position = [random.randrange(1, ((window_x // 10) - 5)) * 10,
                  random.randrange(10, (window_y // 10)) * 10]
fruit_spawn = True

# set default snake direction to right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


# display player score on the screen
def show_score():
    pass


# game over function
def game_over():
    # render the player's final score with some game over text

    # this method will update the screen to show your game over message
    pygame.display.flip()

    # set a time for the game to wait before shutting off
    time.sleep()

    # turn off pygame
    pygame.quit()

    # turn off the program completely
    quit()


# main game function
while True:
    # handling key events (when user presses key). It may be useful to consult pygame's documentation on key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # consider, if two keys are pressed simultaneously, snake should only go in one direction. How could we achieve this?

    # once you have set the direction, we need to move the snake
    # 0,0 in pygame is the upper left corner, so as you increase in y, you actually go DOWN
    if direction == 'UP':
        pass
    if direction == 'DOWN':
        pass
    if direction == 'LEFT':
        pass
    if direction == 'RIGHT':
        pass

    # make the snake grow when it eats fruits, each fruit equals ten points. Fruit disappears after snake finds it
    # when the snake finds a fruit, we need to increase the length of the snake
    # if it hasn't found a fruit, it needs to adjust its position
    # remember that the snake's body positions are pixels, each with a specific location, each held in a list.

    # make a new fruit
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    # draw the snake and the fruit
    # hint: research pygame documentation for the .Rect() method
    for pos in snake_body:
        pass

    # Snake ends two ways, you go off screen, or you collide with yourself.
    # we need a function or some code to check to see if either of those conditions are true before continuing the game

    # display score as user plays
    show_score()

    # refresh game screen
    pygame.display.update()

    # set refresh rate
    fps.tick(snake_speed)
