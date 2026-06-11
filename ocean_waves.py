import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("#0a0a2e")
screen.title("Ocean Waves")
screen.setup(width=800, height=600)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# Stars in the sky
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.color("white")
import random
for _ in range(100):
    x = random.randint(-400, 400)
    y = random.randint(50, 290)
    stars.goto(x, y)
    stars.dot(random.choice([1, 2]))

# Moon
moon = turtle.Turtle()
moon.hideturtle()
moon.penup()
moon.goto(280, 220)
moon.dot(50, "#fffde7")
moon.goto(295, 228)
moon.dot(42, "#0a0a2e")  # Crescent cutout

# Wave layers — each with different color, speed, amplitude
wave_layers = [
    {"y": -80,  "amp": 30, "freq": 0.03, "speed": 0.04, "color": (0.0,  0.3, 0.7)},
    {"y": -120, "amp": 25, "freq": 0.04, "speed": 0.06, "color": (0.0,  0.4, 0.8)},
    {"y": -160, "amp": 20, "freq": 0.05, "speed": 0.05, "color": (0.0,  0.5, 0.9)},
    {"y": -200, "amp": 18, "freq": 0.06, "speed": 0.07, "color": (0.1,  0.6, 1.0)},
    {"y": -240, "amp": 15, "freq": 0.07, "speed": 0.08, "color": (0.2,  0.7, 1.0)},
]

offset = 0.0

# Draw ocean floor
floor = turtle.Turtle()
floor.hideturtle()
floor.penup()
floor.goto(-400, -300)
floor.color("#001133")
floor.begin_fill()
floor.goto(400, -300)
floor.goto(400, -270)
floor.goto(-400, -270)
floor.end_fill()

# ── Animation loop ─────────────────────────────────────────────────────────
for frame in range(600):
    t.clear()
    offset += 0.05

    for layer in wave_layers:
        t.penup()
        t.pencolor(layer["color"])
        t.pensize(2)

        # Draw wave line
        first = True
        for x in range(-400, 401, 4):
            y = (layer["y"]
                 + layer["amp"] * math.sin(layer["freq"] * x + offset * layer["speed"] * 20))
            if first:
                t.goto(x, y)
                t.pendown()
                first = False
            else:
                t.goto(x, y)

        # Fill below the wave
        t.goto(400, -300)
        t.goto(-400, -300)
        t.penup()

    # Reflection of moon on water
    t.penup()
    t.pencolor("#fffde7")
    t.pensize(1)
    for i in range(5):
        rx = 270 + math.sin(frame * 0.1 + i) * 5
        ry = -90 - i * 15
        t.goto(rx, ry)
        t.pendown()
        t.goto(rx + 20, ry)
        t.penup()

    screen.update()

turtle.done()
