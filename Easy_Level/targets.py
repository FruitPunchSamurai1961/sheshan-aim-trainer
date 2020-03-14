import pygame
import random
from pygame.sprite import Sprite

"""This is the targets class which inherits from the Sprites class from pygame.sprite"""


class Target(Sprite):

    def __init__(self, screen):
        """create variables that will be used to draw the three circles"""
        super().__init__()
        self.screen = screen
        self.red_color = (225, 0, 0)
        self.white_color = (225, 225, 225)
        self.screen_rect = self.screen.get_rect()
        self.outer_radius = 5
        self.middle_radius = 3
        self.inner_radius = 1
        self.radius_speed_factor = 1
        self.time_limit = 31
        """X and Y positions of the three circles"""
        self.x = random.randint(50, self.screen_rect.right - 50)
        self.y = random.randint(50, self.screen_rect.bottom - 50)

        self.delay = 1

    def draw_target(self):
        """draw the target onto the screen"""
        outer_circle = pygame.draw.circle(self.screen, self.red_color, (self.x, self.y), self.outer_radius, 2)
        middle_circle = pygame.draw.circle(self.screen, self.white_color, (self.x, self.y), self.middle_radius, 2)
        inner_circle = pygame.draw.circle(self.screen, self.red_color, (self.x, self.y), self.inner_radius)

    def update(self):
        """update the movement of the target as time goes on"""
        self.draw_target()
        if self.time_limit > self.delay > 0:
            self.outer_radius += self.radius_speed_factor
            self.middle_radius += self.radius_speed_factor
            self.inner_radius += self.radius_speed_factor
            self.delay += 1
        elif self.delay == 31:
            self.delay = -30
        if self.delay < 0 and self.middle_radius > 2:
            self.outer_radius -= self.radius_speed_factor
            self.middle_radius -= self.radius_speed_factor
            self.inner_radius -= self.radius_speed_factor
            self.delay += 1
