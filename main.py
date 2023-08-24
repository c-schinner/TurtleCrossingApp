from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
from road_lines import RoadLines
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('grey')
screen.title("Turtle Crossing")
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
outline = RoadLines()
outline.draw_lines()
cars = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_back, "Down")


game_is_on = True

while game_is_on:
    time.sleep(.01)
    screen.update()

    # Have cars randomly generate on the y-axis, from -250 - 250
    cars.create_car()
    cars.move_cars()

    # Detect when the player hits a car and give the "Game Over" message at: 0, 0
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Have turtle level up when it reaches the finish line at the top, increase cars speed at each new level
    if player.ycor() > 270:
        player.reset_turtle()
        scoreboard.level_up()
        cars.level_up()

screen.exitonclick()
