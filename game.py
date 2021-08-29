import pygame
from random import randint

from pygame.draw import rect
# from enum import Enum

from package.constants import width, height, title, bwidth, bheight, screenfill, fps
from package.vector import Vector
from package.snake import Snake
from package.food import Food


# setup 
pygame.init()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

def gameloop():
	
	game_over = False
	game_exit = False

	clock = pygame.time.Clock()

	snake = Snake(Vector(randint(0, bwidth - 1), randint(0, bheight - 1)))
	food = Food()


	while not game_over :

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				game_over = True

			if event.type == pygame.KEYDOWN:
				snake.turn(event.key)

		snake.update()
		win.fill(screenfill)

		# checking for food to be eaten

		if snake.head == food:
			snake.eat()
			food = Food()

		food.draw(win)
		snake.draw(win)

		pygame.display.update()
		clock.tick(fps)

gameloop()

pygame.quit()
quit()