import pygame as pg
import time
pg.init()

# Initialize the window
width = 600
height = 600
screen = pg.display.set_mode((width, height))
pg.display.update()
pg.display.set_caption("Snake Linked List")
pg.mouse.set_visible(True)

clock = pg.time.Clock()

snake_size = 10
snake_speed = 30

class Node:
    def __init__(self):
        self.next = None

class Snake:
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.dir_x = 0
        self.dir_y = 0

    def dir_change(self):
        if event.key == pg.K_LEFT:
            dir_x = -snake_size
            dir_y = 0
        elif event.key == pg.K_RIGHT:
            dir_x = snake_size
            dir_y = 0
        elif event.key == pg.K_UP:
            dir_x = 0
            dir_y = snake_size
        elif event.key == pg.K_DOWN:
            dir_x = 0
            dir_y = -snake_size
        return self

    def add_node(self):
        return self

    def eat(self):
        return self

# Game Loop
snake = Snake()
dead = False
while not dead:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            dead = True
        if event.type == pg.KEYDOWN:
            snake.dir_change()
    
    snake.x += snake.dir_x
    snake.y += snake.dir_y
    screen.fill((0,0,0))
    pg.draw.rect(screen, (255,255,255), pg.Rect(snake.x,snake.y,snake_size,snake_size))
    pg.display.update()

    

pg.quit()
quit()

