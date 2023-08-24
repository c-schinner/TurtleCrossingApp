from turtle import Turtle
import random


COLORS = ['red', 'orange', 'yellow', 'blue', 'purple', 'black']
STARTING_POS = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # create a method to randomly generate cars and have them move continuously across the screen
    def create_car(self):
        random_chance = random.randint(1, 15)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.up()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y = random.choice(STARTING_POS)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

