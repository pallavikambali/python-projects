import turtle
import math
import random
import colorsys

# ── Heart curve parametric formula ──────────────────────────────────────────
# These two functions define the shape of a heart using math
# 't' is an angle from 0 to 2*pi that traces the full heart shape
def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return (13 * math.cos(t)
            - 5  * math.cos(2 * t)
            - 2  * math.cos(3 * t)
            -      math.cos(4 * t))

# ── Setup ────────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.setup(width=800, height=800)   # 800x800 window
screen.bgcolor("#000000")             # Black background
screen.title("Nebula Heart")
screen.tracer(0)                      # Turn off auto-drawing (we update manually)

SCALE      = 16    # Makes the heart bigger on screen
SWARM_SIZE = 400   # Number of glowing particles
FRAMES     = 800   # How many animation frames to run

# ── Build particles ──────────────────────────────────────────────────────────
particles = []

for i in range(SWARM_SIZE):
    p = turtle.Turtle(shape="circle")  # Each particle is a small circle
    p.speed(0)                         # Fastest drawing speed
    p.penup()                          # Don't draw lines when moving
    p.shapesize(0.15)                  # Start very small

    # Place each particle somewhere on the heart curve
    t = random.uniform(0, 2 * math.pi)          # Random position on heart
    scatter = random.gauss(0, 10)               # Random spread amount
    hx = heart_x(t) * SCALE + random.gauss(0, scatter * 0.5)  # X with blur
    hy = heart_y(t) * SCALE + random.gauss(0, scatter * 0.5)  # Y with blur

    p.goto(hx, hy)  # Move particle to starting position

    # Save unique properties for each particle
    p._angle   = t                               # Where on the heart it is
    p._speed   = random.uniform(0.008, 0.025)   # How fast it orbits
    p._scatter = random.uniform(0, 12)          # How far it drifts from curve
    p._phase   = random.uniform(0, 2 * math.pi) # Offset for color cycling
    p._size    = random.uniform(0.10, 0.25)     # Its size

    p.shapesize(p._size)
    particles.append(p)  # Add to our list

# ── Draw faint heart outline ─────────────────────────────────────────────────
outline = turtle.Turtle()
outline.hideturtle()          # Hide the turtle arrow
outline.speed(0)
outline.penup()
outline.pencolor("#ff0066")   # Pink/magenta color

# Draw the heart shape by connecting 200 points along the curve
steps = 200
for k in range(steps + 1):
    t = (k / steps) * 2 * math.pi   # Evenly spaced angles
    ox = heart_x(t) * SCALE
    oy = heart_y(t) * SCALE
    if k == 0:
        outline.goto(ox, oy)
        outline.pendown()            # Start drawing
    else:
        outline.goto(ox, oy)         # Connect the dots

outline.penup()

# ── Animation loop ────────────────────────────────────────────────────────────
for frame in range(FRAMES):

    # Pulse effect: heart slowly grows and shrinks like a heartbeat
    pulse = 1.0 + 0.04 * math.sin(frame * 0.04)

    for i, p in enumerate(particles):

        # Move each particle forward along the heart curve
        p._angle += p._speed
        if p._angle > 2 * math.pi:
            p._angle -= 2 * math.pi  # Wrap around when it completes a loop

        t = p._angle

        # Calculate the target position on the heart (with pulse)
        target_x = heart_x(t) * SCALE * pulse
        target_y = heart_y(t) * SCALE * pulse

        # Calculate perpendicular direction to drift off the curve (nebula effect)
        dx = -heart_y(t + 0.01) + heart_y(t)
        dy =  heart_x(t + 0.01) - heart_x(t)
        length = math.hypot(dx, dy) or 1
        dx, dy = dx / length, dy / length  # Normalize to unit vector

        # Drift amount oscillates over time giving a breathing nebula look
        scatter_amt = p._scatter * math.sin(frame * 0.03 + p._phase)
        nx = target_x + dx * scatter_amt
        ny = target_y + dy * scatter_amt

        p.goto(nx, ny)  # Move particle to new position

        # Calculate color: cycles through pink/purple nebula hues over time
        hue = (frame / FRAMES * 0.5 + i / SWARM_SIZE * 0.8 + p._phase / (2 * math.pi)) % 1.0
        hue = (hue * 0.35 + 0.72) % 1.0   # Lock hue to pink-purple range
        sat = random.uniform(0.7, 1.0)     # High saturation = vivid colors
        val = random.uniform(0.6, 1.0)     # Brightness varies slightly
        r, g, b = colorsys.hsv_to_rgb(hue, sat, val)
        p.color(r, g, b)

        # Twinkle: randomly resize each particle slightly every frame
        twinkle = p._size * random.uniform(0.8, 1.2)
        p.shapesize(twinkle)

    screen.update()  # Refresh the screen once per frame

# ── Keep window open ──────────────────────────────────────────────────────────
turtle.done()
