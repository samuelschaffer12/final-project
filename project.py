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
car2 = Car("Leftie", 6,9,8,5,6)
car3 = Car("Rightie", 6,8,9,5,6)
car4 = Car("Balanced", 7,7,7,7,7)
car5 = Car("Excel", 7,5,6,9,7)