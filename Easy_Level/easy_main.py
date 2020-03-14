import pygame
from pygame.sprite import Group
import sys
import random
from targets import Target


def update_time(total_time):
    """This updates the time to make sure that the game ends once the timer is up"""
    total_time -= 1
    return total_time


def create_target(targets, screen, limit_of_targets):
    """Using the sprites class, we made a group which add all of the target class instances"""
    wait_time = random.random()  # this is here to make sure that all of the targets don't appear at the same time
    if len(targets) < limit_of_targets and wait_time < 0.1:
        new_target = Target(screen)
        targets.add(new_target)


def show_targets(targets):
    """for the targets in the group, we need to draw them onto the screen after creating them"""
    for target in targets:
        target.update()


def delete_targets(targets):
    """Need to get rid of the targets which the player missed, so it doesn't eat up space"""
    for target in targets.copy():
        if target.inner_radius == 1:
            targets.remove(target)


def check_mouse_position(targets, num_of_targets_destroyed):
    """Need this in order to see if the player hit the targets and if they did, we need to get rid of them"""
    mouse_position = pygame.mouse.get_pos()
    for target in targets.copy():
        if target.x - target.outer_radius <= mouse_position[0] <= (
                target.x + (target.outer_radius * 2)) and target.y - target.outer_radius <= mouse_position[1] <= (
                target.y + (target.outer_radius * 2)):
            targets.remove(target)
            num_of_targets_destroyed += 1
    return num_of_targets_destroyed  # return this, so we can print out the accuracy of the player


def run_game():
    """The main function for the easy level"""
    pygame.init()
    clock = pygame.time.Clock()
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    targets = Group()
    limit_of_targets = 5
    num_of_targets_destroyed = 0
    num_of_mouse_presses = 0
    background = pygame.image.load('Images/easy-grid.png')
    time_allowed = 30
    frames_per_second = 18
    total_time = time_allowed * frames_per_second
    accuracy = 0
    print("You have " + str(time_allowed) + " seconds to destroy as many targets as possible") # This is what they
    # player will see, so they know how much time they have
    game_on = True
    while game_on:
        clock.tick(frames_per_second)
        total_time = update_time(total_time)
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        create_target(targets, screen, limit_of_targets)
        show_targets(targets)
        delete_targets(targets)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                num_of_mouse_presses += 1
                num_of_targets_destroyed = check_mouse_position(targets, num_of_targets_destroyed)
                if num_of_mouse_presses > 0:
                    accuracy = num_of_targets_destroyed / num_of_mouse_presses
        if total_time == 0:
            game_on = False
            print("Your accuracy is: " + str((accuracy * 100))[:2] + " %")
        pygame.display.update()
