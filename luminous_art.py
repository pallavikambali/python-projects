import turtle
import colorsys

def draw_luminous_art():
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Luminous Fractal Art")
    screen.setup(width=1000, height=1000)

    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(5)
    t.hideturtle()

    petals = 120
    hue = 0.6

    for i in range(400):
        color = colorsys.hsv_to_rgb(hue, 0.9, 1)
        t.pencolor(color)
        hue += 0.002

        t.penup()
        t.goto(0, 0)
        t.setheading(i * 15)
        t.pendown()
        t.forward(i * 0.8)
        t.right(45)
        t.forward(i * 0.4)
        t.right(90)
        t.forward(i * 0.4)

    turtle.update()
    turtle.done()

draw_luminous_art()
