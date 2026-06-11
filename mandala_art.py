import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.title("Mandala Art")
screen.setup(width=800, height=800)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

hue = 0.0

for i in range(180):
    # Cycle through all colors
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(color)
    hue += 0.005

    # Draw each petal of the mandala
    for j in range(6):
        t.forward(150)
        t.right(60)
        t.forward(150)
        t.right(120)

    t.right(2)  # Rotate slightly each time to build the mandala

    # Every 30 steps draw inner ring
    if i % 30 == 0:
        screen.update()

screen.update()
turtle.done()
