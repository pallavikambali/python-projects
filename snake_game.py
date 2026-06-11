import turtle
import random
import time

# ── Setup ────────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("#1a1a2e")
screen.setup(width=600, height=600)
screen.tracer(0)

# ── Snake Head ───────────────────────────────────────────────────────────────
head = turtle.Turtle()
head.shape("square")
head.color("#00ff88")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# ── Food ─────────────────────────────────────────────────────────────────────
food = turtle.Turtle()
food.shape("circle")
food.color("#ff4757")
food.penup()
food.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)

# ── Score Display ─────────────────────────────────────────────────────────────
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(0, 270)
score = 0
high_score = 0
score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 14, "bold"))

# ── Snake Body Segments ───────────────────────────────────────────────────────
segments = []

# ── Controls ──────────────────────────────────────────────────────────────────
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
# WASD controls too
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# ── Move Function ─────────────────────────────────────────────────────────────
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# ── Game Over ─────────────────────────────────────────────────────────────────
def game_over():
    global score, segments

    # Clear segments
    for seg in segments:
        seg.goto(1000, 1000)
    segments.clear()

    # Reset head
    head.goto(0, 0)
    head.direction = "Stop"

    # Show game over message
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.color("#ff4757")
    msg.goto(0, 20)
    msg.write("GAME OVER!", align="center", font=("Arial", 28, "bold"))
    msg.goto(0, -20)
    msg.color("white")
    msg.write("Press any arrow key to restart", align="center", font=("Arial", 14, "normal"))

    screen.update()
    time.sleep(2)
    msg.clear()

# ── Main Game Loop ────────────────────────────────────────────────────────────
while True:
    screen.update()

    # Move body segments (from tail to neck)
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move first segment to head's old position
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # ── Wall collision ────────────────────────────────────────────────────────
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        if score > high_score:
            high_score = score
        score = 0
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 14, "bold"))
        game_over()

    # ── Food collision ────────────────────────────────────────────────────────
    if head.distance(food) < 15:
        # Move food to new random position
        food.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)

        # Add new body segment
        seg = turtle.Turtle()
        seg.shape("square")
        seg.color("#00ccff")
        seg.penup()
        segments.append(seg)

        # Update score
        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 14, "bold"))

    # ── Self collision ────────────────────────────────────────────────────────
    for seg in segments:
        if seg.distance(head) < 10:
            if score > high_score:
                high_score = score
            score = 0
            score_display.clear()
            score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 14, "bold"))
            game_over()

    time.sleep(0.12)  # Game speed — lower = faster
