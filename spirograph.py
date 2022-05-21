import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

for _ in range(73):
    tim.speed('fastest')
    tim.circle(100)
    tim.left(5)
    tim.pencolor(random_color())
    
        
# while True:
#     tim.forward(200)
#     tim.left(170)
#     if abs(tim.pos()) < 1:
#         break
# done()



