import turtle
import random
import colorsys
import math
import time

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.title("Fireworks")
screen.setup(width=800, height=800)
screen.tracer(0)

# ── Firework particle ─────────────────────────────────────────────────────────
class Particle:
    def __init__(self, x, y, color):
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.shapesize(0.3)
        self.t.penup()
        self.t.color(color)
        self.t.goto(x, y)

        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 8)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = 1.0         # Starts full, fades to 0
        self.fade = random.uniform(0.02, 0.05)

    def update(self):
        self.vy -= 0.15         # Gravity pulls particles down
        x = self.t.xcor() + self.vx
        y = self.t.ycor() + self.vy
        self.t.goto(x, y)
        self.life -= self.fade
        self.vx *= 0.97         # Slow down over time
        return self.life > 0    # Returns False when dead

    def destroy(self):
        self.t.hideturtle()
        self.t.clear()

# ── Launch rocket trail ───────────────────────────────────────────────────────
def launch_rocket(x):
    rocket = turtle.Turtle()
    rocket.shape("circle")
    rocket.shapesize(0.4)
    rocket.penup()
    rocket.color("white")
    rocket.goto(x, -380)

    # Rocket flies upward
    target_y = random.randint(50, 300)
    while rocket.ycor() < target_y:
        rocket.sety(rocket.ycor() + 12)
        screen.update()

    rocket.hideturtle()
    return rocket.xcor(), rocket.ycor()

# ── Explode firework ──────────────────────────────────────────────────────────
def explode(x, y):
    hue = random.random()
    particles = []

    # Create 60 particles in all directions
    for _ in range(60):
        r, g, b = colorsys.hsv_to_rgb(hue + random.uniform(-0.05, 0.05), 1.0, 1.0)
        color = (r, g, b)
        particles.append(Particle(x, y, color))

    # Animate particles until all fade out
    while particles:
        alive = []
        for p in particles:
            if p.update():
                alive.append(p)
            else:
                p.destroy()
        particles = alive
        screen.update()

# ── Stars background ──────────────────────────────────────────────────────────
def draw_stars():
    stars = turtle.Turtle()
    stars.hideturtle()
    stars.penup()
    stars.color("white")
    for _ in range(150):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        stars.goto(x, y)
        stars.dot(random.choice([1, 2]))

draw_stars()

# ── Main loop — launch 15 fireworks ──────────────────────────────────────────
for _ in range(15):
    x = random.randint(-300, 300)
    ex, ey = launch_rocket(x)
    explode(ex, ey)
    time.sleep(0.3)

turtle.done()
