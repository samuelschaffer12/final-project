import math
import time
import pygame


class Car:
    def __init__(self, name, speed, turn_left, turn_right, acceleration, distance):
        self.name = name
        self.speed = speed
        self.turn_left = turn_left
        self.turn_right = turn_right
        self.acceleration = acceleration
        self.distance = distance
car1 = Car("SpeedDemon", 9,5,5,8,7)
car2 = Car("Lefty", 6,9,8,5,6)
car3 = Car("Righty", 6,8,9,5,6)
car4 = Car("Balanced", 7,7,7,7,7)
car5 = Car("Excel", 7,5,6,9,7)

#all of the pygame functions were looked up as I wasn't very familiar with the external tool
pygame.init()

width, height = 1000,700
screen_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw your track here!")
white = (255,255,255)
black = (0,0,0)
def track_drawing_function():
    playing_game = True
    is_mouse_being_pressed = False
    track_points_pressed = []
    while playing_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return track_points_pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_mouse_being_pressed = True
                track_points_pressed.append(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                is_mouse_being_pressed = False
            elif event.type == pygame.MOUSEMOTION and is_mouse_being_pressed:
                track_points_pressed.append(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    track_points_pressed =[]
                elif event.key == pygame.K_RETURN:
                    return track_points_pressed
        screen_display.fill(white)

        if len(track_points_pressed) >= 1:
            pygame.draw.lines(screen_display,black,True,track_points_pressed,5)
        pygame.display.update()
track = track_drawing_function()
print("Tracking points: ", track)
pygame.quit


#next will be calculating time

