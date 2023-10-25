#Типа покер
import pygame
from initializations import *
from functions import *
from all_texts import *

pygame.init()

clock = pygame.time.Clock()

counter = 0
first_start = True
gameplay=False
run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    if not gameplay and first_start:
        screen.blit(hello_text, (280, 200))
        screen.blit(start_text, start_text_rect)
        pygame.display.update()
        first_start = False



    mouse = pygame.mouse.get_pos()
    if not gameplay and start_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        gameplay=True
        Update_All_Cards()
        Open_Five_Cards(1)
        Open_Five_Cards(2)
        Open_Five_Cards(3)
        counter+=1
        print(counter)


    if gameplay:
        where_touch(mouse)
        draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    clock.tick(10)
