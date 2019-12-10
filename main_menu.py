import pygame
from pygame.locals import KEYDOWN
from game import game_flow
import os

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Connect 4')

def menu():
    '''display main menu'''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_flow()


def main():
	menu()

if __name__ == '__main__':
    main()