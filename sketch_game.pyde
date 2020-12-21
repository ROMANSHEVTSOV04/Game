x = random (0, 10)
y = random (0, 6)
s = second()
def setup():
    size (1200, 800)
def draw():
    background (0)
    rect(100*x, 100*y, 100, 100)
    t = second()
    if (t > s+1):
        background (255 ,0 ,0)
        stroke(255,255,255)
        textSize(48)
        text("Y O U    L O S E", 430, 400)
        noLoop()
def mousePressed():
    if (mouseButton == LEFT and 100*x < mouseX < 100*x+100 and 100*y < mouseY < 100*y+100):
        fill (255, 204, 0)
