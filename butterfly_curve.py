import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.title("Butterfly Curve")
screen.setup(width=800, height=800)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1)

# Butterfly curve formula:
# r = e^(sin θ) - 2cos(4θ) + sin⁵((2θ-π)/24)
# x = r * cos(θ)
# y = r * sin(θ)

SCALE = 120
hue = 0.0
steps = 2000

t.penup()

for i in range(steps + 1):
    theta = i * (24 * math.pi / steps)

    # Butterfly curve formula
    r = (math.e ** math.sin(theta)
         - 2 * math.cos(4 * theta)
         + math.sin((2 * theta - math.pi) / 24) ** 5)

    x = SCALE * r * math.cos(theta)
    y = SCALE * r * math.sin(theta)

    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(color)
    hue = (hue + 0.0005) % 1.0

    if i == 0:
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

    if i % 200 == 0:
        screen.update()

# Glow effect — draw again slightly offset
t.penup()
hue = 0.5
t.pensize(1)

for i in range(steps + 1):
    theta = i * (24 * math.pi / steps)
    r = (math.e ** math.sin(theta)
         - 2 * math.cos(4 * theta)
         + math.sin((2 * theta - math.pi) / 24) ** 5)

    x = SCALE * r * math.cos(theta) + 1
    y = SCALE * r * math.sin(theta) + 1

    color = colorsys.hsv_to_rgb(hue, 0.5, 1.0)
    t.pencolor(color)
    hue = (hue + 0.0005) % 1.0

    if i == 0:
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

    if i % 200 == 0:
        screen.update()

screen.update()
turtle.done()
