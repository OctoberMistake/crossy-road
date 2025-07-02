from turtle import Turtle, Screen

def street():
    
    screen = Screen()
    screen.setup(width=900, height=600)
    screen.bgcolor("grey")
    screen.tracer(0)

    def stripes(segments, init_pos_x, init_pos_y, colour):
        road_stripes = Turtle()
        road_stripes.hideturtle()    
        road_stripes.color(colour)
        road_stripes.left(180)
        road_stripes.pensize(7)
        road_stripes.teleport(init_pos_x-15, init_pos_y)

        for i in range(0,segments):
            if i % 2 == 0:
                road_stripes.pd()
                road_stripes.forward(70)
            else:
                road_stripes.pu()
                road_stripes.forward(30)

    stripes(18, 450, 100, "yellow")
    stripes(18, 450, -100, "yellow")

    return screen
