x = random (0, 10)
y = random (0, 6)
s = second()
menu = True
game = False
loose = False
win = False

def setup():
    size (1200, 800)
    
def draw():
    global menu, game,start, loose, win
    background (0)
    
    if menu == True:
        background (0,205,0)
        stroke(255,255,255)
        textSize(48)
        text("PRESS SHIFT FOR START", 330, 400)
        
    if game == True:
        background (0)
        rect(100*x, 100*y, 100, 100)
        
        t = second()
        if (t > s+3):
            game = False
            loose = True
            start = False
            menu = False
    
    if loose == True:
        background (255 ,0 ,0)
        stroke(255,255,255)
        textSize(48)
        text("Y O U    L O S E", 430, 400)
        
    if win == True:
        background (255 ,0 ,0)
        stroke(255,255,255)
        textSize(48)
        text("Y O U    W I N", 430, 400)
        
#мышка
def mousePressed():
    global menu, game, loose
    if (mouseButton == LEFT and 100*x < mouseX < 100*x+100 and 100*y < mouseY < 100*y+100):
        fill (255, 204, 0)
        win = True
        loose = False
        
#клавиатура
def keyReleased():
    global menu, game, loose
    if key == ' ' and menu == True:
        game = True
    if key == ' ' and loose == True:
        exit()
