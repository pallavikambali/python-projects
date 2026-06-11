import turtle, math, random, colorsys

S = turtle.Screen()
S.setup(800, 800); S.bgcolor("#000000"); S.title("Nebula Heart"); S.tracer(0)

hx = lambda t: 16 * math.sin(t)**3
hy = lambda t: 13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
PI2, SC = 2 * math.pi, 16

# Heart outline
o = turtle.Turtle(); o.hideturtle(); o.speed(0); o.pencolor("#ff0066"); o.penup()
pts = [(hx(k/200*PI2)*SC, hy(k/200*PI2)*SC) for k in range(201)]
o.goto(pts[0]); o.pendown()
[o.goto(x, y) for x, y in pts[1:]]; o.penup()

# Particles
P = []
for _ in range(400):
    p = turtle.Turtle(shape="circle"); p.speed(0); p.penup()
    t = random.uniform(0, PI2)
    p.goto(hx(t)*SC + random.gauss(0,5), hy(t)*SC + random.gauss(0,5))
    p._a, p._sp, p._sc, p._ph, p._sz = t, random.uniform(0.008,0.025), random.uniform(0,12), random.uniform(0,PI2), random.uniform(0.1,0.25)
    p.shapesize(p._sz); P.append(p)

# Animation
for f in range(800):
    pulse = 1 + 0.04 * math.sin(f * 0.04)
    for i, p in enumerate(P):
        p._a = (p._a + p._sp) % PI2
        t = p._a
        tx, ty = hx(t)*SC*pulse, hy(t)*SC*pulse
        dx, dy = -hy(t+0.01)+hy(t), hx(t+0.01)-hx(t)
        n = math.hypot(dx, dy) or 1
        s = p._sc * math.sin(f*0.03 + p._ph)
        p.goto(tx + dx/n*s, ty + dy/n*s)
        hue = ((f/800*0.5 + i/400*0.8 + p._ph/PI2) * 0.35 + 0.72) % 1
        p.color(*colorsys.hsv_to_rgb(hue, random.uniform(0.7,1), random.uniform(0.6,1)))
        p.shapesize(p._sz * random.uniform(0.8,1.2))
    S.update()

turtle.done()
