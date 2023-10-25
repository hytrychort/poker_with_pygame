import pygame
from initializations import *
from all_texts import *

RESTART = False
INFO = False


def Update_All_Cards(count_opponents = 4):
    global cards, card_1, card_2, images_of_five_cards, five_cards
    cards = list_cards.copy()
    buff_card_1 = choice(list(cards.keys()))
    card_1 = (buff_card_1, cards[f"{buff_card_1}"])
    del cards[f'{card_1[0]}']
    buff_card_2 = choice(list(cards.keys()))
    card_2 = (buff_card_2, cards[f"{buff_card_2}"])
    del cards[f'{card_2[0]}']


    for opponent in range(count_opponents):
        for i in range(2):
            card_bot_buff = choice(list(cards.keys()))
            card_bot = (card_bot_buff, cards[f"{card_bot_buff}"])
            cards_of_opponents[opponent][i] = card_bot     #Обновление карт противников

    for i in range(5):
        card_on_table_buff = choice(list(cards.keys()))
        card_on_table = (card_on_table_buff, cards[f"{card_on_table_buff}"])
        del cards[f"{card_on_table[0]}"]
        five_cards[f""] = card_on_table
        five_cards[f"{i}"] = card_on_table     #Обновление пяти карт на столе


    images_of_five_cards = list_five_cards.copy()


def Draw_five_Cards(count_open_cards = 0):
    if count_open_cards == 1:
        for i in range(3):
            images_of_five_cards[i] = five_cards[f"{list(five_cards.keys())[i]}"]   #Подмена картинки рубашки на карту

    elif count_open_cards == 2 or count_open_cards == 3:
        images_of_five_cards[count_open_cards + 1] = five_cards[count_open_cards + 1]
    print(type(images_of_five_cards[0][1]) == type(rubashka))
    for i in range(1, 6):
        screen.blit(images_of_five_cards[i - 1][1], (300 + (i * 85), 270))

def Info(mouse):
    global INFO
    if INFO:
        #screen.fill((224, 224, 224))
        screen.blit(info_card, (88, 5))
        pygame.display.update()


def Pass():
    pass


def Close(mouse):
    global RESTART
    if RESTART:
       screen.blit(background, (0, 0))
       screen.blit(exit_label, exit_label.get_rect(topleft=(350, 170)))
       screen.blit(money_label, money_label.get_rect(topleft=(600 - (len(str(money)) * 17), 250)))
       screen.blit(restart_label, restart_label_rect)
       if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
           Update_All_Cards()
           RESTART = False


def where_touch(mouse):
    global RESTART, INFO
    if pygame.mouse.get_pressed()[0] and info.get_rect(topleft=(15, 15)).collidepoint(mouse):
        INFO = True
    elif pygame.mouse.get_pressed()[0] and info.get_rect(topleft=(15, 15)).collidepoint(mouse) == False:
        INFO = False
    if pygame.mouse.get_pressed()[0] and check_text.get_rect().collidepoint(mouse):
        pass
    elif pygame.mouse.get_pressed()[0] and close_button.get_rect(topleft=(1150, 15)).collidepoint(mouse):
        RESTART = True
    elif pygame.mouse.get_pressed()[0] and raize_text.get_rect().collidepoint(mouse):
        pass
    else:
        return True


def Opponents(opponents):
    for opponent in range(len(opponents) - 1, -1, -1):
        if opponents[opponent]:
            if opponent == 0 or opponent == 1:
                screen.blit(rubashka, koord_cards_opponents[opponent])
                screen.blit(rubashka, (koord_cards_opponents[opponent][0] + 80, koord_cards_opponents[opponent][1]))
            else:
                screen.blit(rubashka_r, koord_cards_opponents[opponent])
                screen.blit(rubashka_r, (koord_cards_opponents[opponent][0], koord_cards_opponents[opponent][1] + 80))


def Combinations(five_cards = None, cards = None):
    array_cards = []
    for i in range(5): array_cards.append(list(five_cards.keys())[i][:list(five_cards.keys())[i].find('_')])
    for i in range(2): array_cards.append(cards[i][:cards[i].find('_')])
    slovar_cards = {}
    for i in array_cards:
        if i not in slovar_cards:
            slovar_cards[f'{i}'] = array_cards.count(i)
    print(slovar_cards)

            

def draw():
    global card_1, card_2, five_cards
    mouse = pygame.mouse.get_pos()
    screen.blit(info, (15, 15))
    screen.blit(close_button, (1150, 15))
    screen.blit(card_1[1], (520, 460))
    screen.blit(card_2[1], (600, 460))
    pygame.draw.rect(screen, 'Blue', pass_button, border_radius=10)
    pygame.draw.rect(screen, 'Orange', check_button, border_radius=10)
    pygame.draw.rect(screen, 'Red', raize_or_VABank_button, border_radius=10)
    screen.blit(pass_text, (pass_button.x + 35, pass_button.y + 10))
    screen.blit(check_text, (check_button.x + 35, check_button.y + 10))
    screen.blit(raize_text, (raize_or_VABank_button.x + 35, raize_or_VABank_button.y + 10))
    Opponents(active_bots)
    Draw_five_Cards(1)
    Close(mouse)
    Info(mouse)
    Combinations(five_cards, (card_1, card_2))
    pygame.display.update()
