import turtle
import time
import math

screen = turtle.Screen()
screen.bgcolor("#1a1a2e")
screen.title("Analog Clock")
screen.setup(width=800, height=800)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

def draw_hand(angle, length, color, width):
    t.penup()
    t.goto(0, 0)
    t.setheading(90 - angle)
    t.pensize(width)
    t.pencolor(color)
    t.pendown()
    t.forward(length)
    t.penup()

def draw_clock_face():
    # Outer circle
    t.penup()
    t.goto(0, -210)
    t.pendown()
    t.pencolor("#e0e0e0")
    t.pensize(3)
    t.circle(210)

    # Inner circle
    t.penup()
    t.goto(0, -195)
    t.pendown()
    t.pencolor("#4444aa")
    t.pensize(1)
    t.circle(195)

    # Hour markers
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = 185 * math.sin(angle)
        y1 = 185 * math.cos(angle)
        x2 = 200 * math.sin(angle)
        y2 = 200 * math.cos(angle)
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.pencolor("#ffffff")
        t.pensize(3)
        t.goto(x2, y2)

    # Minute markers
    for i in range(60):
        angle = math.radians(i * 6)
        x1 = 190 * math.sin(angle)
        y1 = 190 * math.cos(angle)
        x2 = 200 * math.sin(angle)
        y2 = 200 * math.cos(angle)
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.pencolor("#aaaaaa")
        t.pensize(1)
        t.goto(x2, y2)

    # Hour numbers
    t.penup()
    for i in range(1, 13):
        angle = math.radians(i * 30)
        x = 160 * math.sin(angle)
        y = 160 * math.cos(angle) - 10
        t.goto(x, y)
        t.pencolor("#ffffff")
        t.write(str(i), align="center", font=("Arial", 14, "bold"))

    # Center dot
    t.goto(0, 0)
    t.dot(10, "#ff4757")

# ── Main loop ─────────────────────────────────────────────────────────────────
while True:
    t.clear()
    draw_clock_face()

    # Get current time
    now = time.localtime()
    hrs  = now.tm_hour % 12
    mins = now.tm_min
    secs = now.tm_sec

    # Calculate angles
    sec_angle  = secs * 6
    min_angle  = mins * 6 + secs * 0.1
    hour_angle = hrs * 30 + mins * 0.5

    # Draw hands
    draw_hand(hour_angle, 110, "#ffffff", 6)   # Hour hand
    draw_hand(min_angle,  150, "#00ff88", 4)   # Minute hand
    draw_hand(sec_angle,  170, "#ff4757", 2)   # Second hand

    # Center dot on top
    t.penup()
    t.goto(0, 0)
    t.dot(8, "#ff4757")

    # Date and time text
    t.goto(0, -250)
    t.pencolor("#aaaaaa")
    t.write(time.strftime("%A, %d %B %Y"), align="center", font=("Arial", 12, "normal"))

    screen.update()
    time.sleep(1)
