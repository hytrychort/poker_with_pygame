import pygame
from random import choice

pygame.init()

screen = pygame.display.set_mode((1200, 700))
background = pygame.image.load('images/background1.png').convert_alpha()
pygame.display.set_caption("Покер")
pygame.display.set_icon(pygame.image.load("images/icon.png").convert_alpha())

list_robot = [pygame.image.load(f'images/хз/хз{i}.png').convert_alpha() for i in range(1, 15)]
count_in_list_robot = 0


list_cards = {}
for i in range(1, 14):
    for j in ['k', 'b', 'ch', 'p']:
        list_cards[f"{i}_{j}"] = pygame.image.load(f'images/yellow_cards/{i}_{j}.png').convert_alpha()
cards=list_cards.copy()


rubashka = pygame.image.load('images/yellow_cards/back.png').convert_alpha()
rubashka_r = pygame.image.load('images/yellow_cards/back_r.png').convert_alpha()
shesterna = pygame.image.load('images/шестерня.png').convert_alpha()
info = pygame.image.load('images/info.png').convert_alpha()
info_card = pygame.image.load('images/info_card.jpg').convert_alpha()
close = pygame.image.load('images/close.png').convert_alpha()

background = pygame.image.load('images/bg.png').convert_alpha()

close_button = pygame.image.load('images/close.png').convert_alpha()
pass_button = pygame.Rect(350, 550, 153, 60)
check_button = pygame.Rect(515, 550, 153, 60)
raize_or_VABank_button = pygame.Rect(680, 550, 153, 60)

cards_of_opponents = [[[], []], [[], []], [[], []], [[], []]]
koord_cards_opponents = [(350, 70), (700, 70), (110, 270), (1000, 270)]

active_bots = [True, True, True, True]


five_cards = []
list_five_cards = {f'{i}':rubashka for i in range(5)}
images_of_five_cards = list_five_cards.copy()

money = 0