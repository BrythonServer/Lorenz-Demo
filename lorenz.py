from ggame.asset import Color
from ggame.mathapp import MathApp
from ggame.point import Point
from ggame.timer import Timer

s = 10
b = 8/3
r = 28

x = -1
y = -1
z = 0
D = 0.015

ITERATIONS = 1000
count = 0

def pointcolor(z):
    return Color((255-(z+50)*255//100)*0x10000 + (z+50)*255//100, 1.0)

def tick(t):
    global x, y, z
    global count
    if count < ITERATIONS:
        x += D*s*(y - x)
        y += D*(x*(r - z) - y)
        z += D*(x*y - b*z)
        Point((x,y), size=4, color=pointcolor(z))
        count += 1
        if count == ITERATIONS:
            print(f"Finished {ITERATIONS} iterations!")

TIMER = Timer()
TIMER.callEvery(D, tick)
MathApp(8).run()
