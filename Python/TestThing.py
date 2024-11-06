from graphics import *

def clickToClose(win):
    win.getMouse()
    win.close()

def drawStickFigure2(win):
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    arm1 = Line(Point(200, 90), Point(160, 100))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 100))
    arm2.draw(win)
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)


    #.undraw()

def idk(win):
    #stickfigure
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(60, 90), Point(140, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(70, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(130, 170))
    leg2.draw(win)

    #eyes
    center = Point(90,60)
    eyeleft =  Circle(center,5)
    eyeleft.draw(win)

    center = Point(110,60)
    eyeright =  Circle(center,5)
    eyeright.draw(win)


    eyeLidLeft = Line(Point(85,60),Point(95,60))
    eyeLidLeft.draw(win)
    eyeLidRight = Line(Point(105,60),Point(115,60))
    eyeLidRight.draw(win)

    #duvet
    tl = Point(55,85)
    br = Point(145,175)
    duvet = Rectangle(tl,br)
    colour = "light blue"
    duvet.setFill(colour)
    duvet.draw(win)

    #snore 
    for click in range(1,6):
        snore = "sn"
        snoreText = Text(Point(200,30), f'{snore + ( click * "z")}')
        snoreText.draw(win)
        win.getMouse()
        snoreText.undraw()

    eyeLidLeft.undraw()
    eyeLidRight.undraw()
    duvet.undraw()
        
    win.getMouse()

def main():
    win = GraphWin("Stick figure", 300, 200)
    win.setBackground("white")

    idk(win)
    clickToClose(win)

main()