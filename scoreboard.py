from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.teleport(-420, 250)
        self.color("white")
        
        #values
        self.lv = 1
    
    def lv_print(self):
        self.write(f"Level: {self.lv}", font=FONT)

    def update_lv(self):
        self.lv += 1
        self.clear()
        self.lv_print()

    def game_over(self, x, y):
        self.teleport(x+15, y+15)
        self.write("👻", font = FONT)
        self.teleport(0,0)
        self.write("GAME OVER", font=FONT, align="center")

        