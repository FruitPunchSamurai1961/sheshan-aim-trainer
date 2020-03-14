import pygame
import sys
from options import Options
import easy_main as em
import medium_main as mm
import hard_main as hm


def draw_title(screen):
    screen_rect = screen.get_rect()
    my_font = pygame.font.Font('fonts/TarrgetRegular-WEOz.otf', 30)
    text_surface = my_font.render("Sheshan's Aim Training Game", True, (230, 230, 230))
    text_rect = text_surface.get_rect()
    gap_from_top = 50
    text_rect.center = (screen_rect.centerx, (screen_rect.top + gap_from_top))
    screen.blit(text_surface, text_rect)


def check_mouse_event(options, level):
    mouse_position = pygame.mouse.get_pos()
    easy_rect = options.easy_option_rect
    medium_rect = options.medium_option_rect
    hard_rect = options.hard_option_rect
    quit_rect = options.quit_option_rect
    start_rect = options.start_option_rect

    if easy_rect.x <= mouse_position[0] <= easy_rect.x + easy_rect.width and easy_rect.y <= mouse_position[
        1] <= easy_rect.y + easy_rect.height:
        level = 1
    elif medium_rect.x <= mouse_position[0] <= medium_rect.x + medium_rect.width and medium_rect.y <= mouse_position[
        1] <= medium_rect.y + medium_rect.height:
        level = 2
    elif hard_rect.x <= mouse_position[0] <= hard_rect.x + hard_rect.width and hard_rect.y <= mouse_position[
        1] <= hard_rect.y + hard_rect.height:
        level = 3
        return level
    if start_rect.x <= mouse_position[0] <= start_rect.x + start_rect.width and start_rect.y <= mouse_position[
        1] <= start_rect.y + start_rect.height:
        if level == 1:
            pygame.quit()
            em.run_game()
        elif level == 2:
            mm.run_game()
        elif level == 3:
            hm.run_game()
    elif quit_rect.x <= mouse_position[0] <= quit_rect.x + quit_rect.width and quit_rect.y <= mouse_position[
        1] <= quit_rect.y + quit_rect.height:
        sys.exit()
    return level


def run_game():
    pygame.init()
    pygame.font.init()
    screen_width = 850
    screen_height = 510
    screen = pygame.display.set_mode((screen_width, screen_height))
    options = Options(screen)
    pygame.display.set_caption("Selection Screen")
    background = pygame.image.load('images/Main-Screen-bg.jpg')
    level = 0
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_title(screen)
        options.load_options()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                level = check_mouse_event(options, level)
        options.choose_level(level)
        pygame.display.update()


run_game()
