import pygame

"""This class is for all the buttons that will be on the screen"""


class Options:
    def __init__(self, screen):
        self.screen = screen
        option_width = 100
        option_height = 100
        self.screen_rect = self.screen.get_rect()
        """this defines all we need for the medium button"""
        self.medium_option = pygame.image.load('images/medium.png')
        self.medium_option_rect = self.medium_option.get_rect()
        self.medium_option_rect.x = self.screen_rect.centerx - 100
        self.medium_option_rect.y = self.screen_rect.centery - 100
        """this defines all we need for the easy button"""
        self.easy_option = pygame.image.load('images/easy.png')
        self.easy_option_rect = self.easy_option.get_rect()
        self.easy_option_rect.x = self.medium_option_rect.x - 200
        self.easy_option_rect.y = self.medium_option_rect.y
        """this defines all we need for the hard button"""
        self.hard_option = pygame.image.load('images/hard.png')
        self.hard_option_rect = self.hard_option.get_rect()
        self.hard_option_rect.x = self.medium_option_rect.x + 250
        self.hard_option_rect.y = self.medium_option_rect.y - 85
        """this defines all we need for the quit button"""
        self.quit_option = pygame.transform.scale(pygame.image.load('images/Quit.png'), (option_width, option_height))
        self.quit_option_rect = self.quit_option.get_rect()
        self.quit_option_rect.x = self.screen_rect.right - 100
        self.quit_option_rect.y = self.screen_rect.bottom - 100
        """this defines all we need for the start button"""
        self.start_option = pygame.transform.scale(pygame.image.load('images/Start.png'), (option_width, option_height))
        self.start_option_rect = self.start_option.get_rect()
        self.start_option_rect.y = self.screen_rect.bottom - 100

    def load_options(self):
        """This will load all the buttons onto the screen"""
        self.screen.blit(self.medium_option, (self.medium_option_rect.x, self.medium_option_rect.y))

        self.screen.blit(self.easy_option, (self.easy_option_rect.x, self.easy_option_rect.y))

        self.screen.blit(self.hard_option, (self.hard_option_rect.x, self.hard_option_rect.y))

        self.screen.blit(self.quit_option, (self.quit_option_rect.x, self.quit_option_rect.y))

        self.screen.blit(self.start_option, (self.start_option_rect.x, self.start_option_rect.y))

    def choose_level(self, level):
        """This is what will allow the screen to be changed depending on what the user selects"""
        if level == 1:
            easy_option_outer_rect = pygame.draw.rect(self.screen, (0, 225, 0), self.easy_option_rect, 2)
        elif level == 2:
            medium_option_outer_rect = pygame.draw.rect(self.screen, (225, 0, 0), self.medium_option_rect, 2)
        elif level == 3:
            hard_option_outer_rect = pygame.draw.rect(self.screen, (0, 0, 250), self.hard_option_rect, 2)
