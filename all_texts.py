import pygame
from initializations import money
pygame.init()

action_text = pygame.font.Font("fonts/font.ttf", 30)

hello_text = pygame.font.Font("fonts/font.ttf", 40).render("Добро пожаловать в покер!", True, (130, 31, 31))

start_text = action_text.render("Начать игру", True, (0, 0, 0))
start_text_rect = start_text.get_rect(topleft=(475, 400))

action_text_2 = pygame.font.Font("fonts/font.ttf", 20)

check_text = action_text_2.render("Check", True, (85, 89, 107))
pass_text = action_text_2.render('  Pass', True, (85, 89, 107))
raize_text = action_text_2.render('Raize', True, (85, 89, 107))
bank_text = action_text_2.render('VA-Bank', True, (85, 89, 107))

exit_label = pygame.font.Font("fonts/font.ttf", 40).render((f"Выигрыш составляет:" if money>=0 else f"Вы проиграли:"), True, (130, 31, 31))
money_label = pygame.font.Font("fonts/font.ttf", 40).render((f"{money}" if money>=0 else f"{money*-1:^75}"), True, (130, 31, 31))
restart_label = pygame.font.Font("fonts/font.ttf", 30).render("Играть заново", True, (0, 0, 0))
restart_label_rect = restart_label.get_rect(topleft=(475, 350))
