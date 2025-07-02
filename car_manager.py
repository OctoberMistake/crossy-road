from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.count = 0
        self.car_set = []
    
    def add_car(self):
        e = randint(1,6)
        if e == 1:
            self.count +=1
            i = self.count

            new_car = Turtle()
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.pu()
            new_car.shapesize(stretch_len=2.3, stretch_wid=1)
            new_car.left(180)
            y_position =  randint(-230, 230)
            new_car.teleport(470, y_position)
            self.car_set.append(new_car)    

    def move_cars(self, lv):
        for car in self.car_set:
            car.forward((STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (lv-1)))

    
#vas a crear n autos entre a y b sobre el eje y, 
# que estén a una distanciamayor a 20px
# sus características van a esta almacenadas en una lista
# 
# Esto se va a repetir cada intervalo de tiempo aleatorio

