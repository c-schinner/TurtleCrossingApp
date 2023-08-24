from turtle import Turtle

ROAD_LINES = [
    -225, -175, -125, -75, -25, 25, 75, 125, 175, 225
]


class RoadLines(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.up()
        self.hideturtle()

    def draw_lines(self):
        self.goto(-300, 250)
        self.down()
        self.forward(600)
        self.up()
        self.goto(-300, -250)
        self.down()
        self.forward(600)

    # This needs to be fixed... figure out how to get the road_lines list to work with the 'for loop'
    def road_lines(self):
        for _ in ROAD_LINES:
            for i in range(0, 31):
                self.down()
                self.forward(20)
                self.up()
                self.forward(20)


