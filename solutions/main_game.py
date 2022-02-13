# import libraries
import pygame
import time
import random

snake_speed = 15

# window size
window_x = 650
window_y = 650

# set colors in game
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# initialize pygame library and font module
pygame.init()
pygame.font.init()

# create game window
pygame.display.set_caption('Sammie the Snake')
game_window = pygame.display.set_mode((window_x, window_y))
main_font = pygame.font.SysFont("comicsans", 15)

# set frames per second (FPS), this is basically a refresh/update timer
fps = pygame.time.Clock()

# define snake's starting position
snake_position = [100, 50]

# create snake's first body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

# set the fruit position
fruit_position = [random.randrange(1, ((window_x // 10) - 5)) * 10,
                  random.randrange(10, (window_y // 10)) * 10]
fruit_spawn = True

# set default snake direction to right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


# display player score
def show_score(game_font, score):
    # we need to create "invisible" surface to draw our text on, pygame doesn't allow drawing text directly on game
    score_surface = game_font.render('Score : ' + str(score), True, white)

    # then we'll write the text we want onto that "surface"
    game_window.blit(score_surface, (0, 10))


# game over function
def game_over(score):
    # we need to create "invisible" surface to draw our text on, pygame doesn't allow drawing text directly on game
    game_over_surface = main_font.render('Your Score is : ' + str(score), True, red)

    # display
    game_window.blit(game_over_surface, (window_x/3, window_y/2))
    pygame.display.flip()

    # after three seconds we will quit the program
    time.sleep(3)

    # shut down pygame library
    pygame.quit()

    # quit the program
    quit()


# main game function
while True:
    # handling key events (when user presses key)
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

    # in case two keys are pressed simultaneously, we only want Sammie to go in one direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # moving the snake, 0,0 in pygame is the upper left corner, so as you increase in y, you actually go DOWN
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # make the snake grow when it eats fruits, each fruit equals ten points. Fruit disappears after snake finds it
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    # make a new fruit
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    # draw the snake and the fruit
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # check if the game is over (snake goes off screen)
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over(score)
    elif snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over(score)

    # check if snake collided with itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over(score)

    # display score as you play
    show_score(main_font, score)

    # refresh game screen
    pygame.display.update()

    # set refresh rate
    fps.tick(snake_speed)
