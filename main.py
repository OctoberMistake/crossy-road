import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import street

screen = street.street()
##Termina el formato de la calle

tim = Player()
lv = Scoreboard()
traffic = CarManager()

lv.lv_print()

screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    screen.onclick(tim.walk)    

    traffic.add_car()
    traffic.move_cars(lv.lv)

    for car in traffic.car_set:
        if car.distance(tim) < 20:
            tim.hited()
            y = tim.pos()[1]
            lv.game_over(0, y)
    
    if tim.pos()[1] > 230:
        lv.update_lv()
        tim.rst()


        



    

