#Типа покер
import pygame
from initializations import five_cards
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
    mouse = pygame.mouse.get_pos()

    if not gameplay and first_start:
        screen.blit(hello_text, (280, 200))
        screen.blit(start_text, start_text_rect)
        pygame.display.update()
        if start_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            first_start = False
            gameplay = True
            Update_All_Cards()
            print(five_cards)
            Hho_win(4, five_cards)
            print(Combinations(Mass_to_combinations([('6_b', 0), ('4_p', 0), ('2_p', 0), ('3_b', 0), ('5_ch', 0)], (('1_k', 0), ('10_p', 0)))))


    if gameplay:
        where_touch(mouse)
        draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    clock.tick(10)
