import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("#050505")
screen.setup(width=800, height=800)
screen.tracer(5)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(1)

def draw_fractal(size, depth, hue):
    if depth == 0:
        return
    t.pencolor(colorsys.hsv_to_rgb(hue, 0.7, 1))
    for _ in range(3):
        t.forward(size)
        draw_fractal(size / 2, depth - 1, hue + 0.05)
        t.backward(size)
        t.right(120)

t.penup()
t.goto(0, 0)
t.pendown()

hue = 0.0
for i in range(12):
    t.right(30)
    draw_fractal(150, 4, hue)
    hue += 0.08
    screen.update()

screen.update()
turtle.done()