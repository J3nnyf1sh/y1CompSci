from graphics import *

def clickToClose(win):
    win.getMouse()
    win.close()

def drawStickFigure(win):

    head = Circle(Point(100, 60), 20)
    head.draw(win)

    eye1centre = Point(90, 60)
    eye1 = Circle(eye1centre, 5)
    eye1.draw(win)

    eye2centre = Point(110, 60)
    eye2 = Circle(eye2centre, 5)
    eye2.draw(win)

    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)

    arms = Line(Point(60, 90), Point(140, 90))
    arms.draw(win)

    pompom1centre = Point(52, 90)
    pompom1 = Circle(pompom1centre, 8)
    pompom1.setFill('red')
    pompom1.draw(win)

    pompom2centre = Point(148, 90)
    pompom2 = Circle(pompom2centre, 8)
    pompom2.setFill('red')
    pompom2.draw(win)

    leg1 = Line(Point(100, 120), Point(70, 170))
    leg1.draw(win)

    leg2 = Line(Point(100, 120), Point(130, 170))
    leg2.draw(win)

    text = Text(Point(200,50), "punch me!")
    text.draw(win)

    for punch in range(10):
        win.getMouse()
        text.undraw()
        for punch in range(0,9):
            text = "ow"
            text = Text(Point(200,100), f'{(punch * "o") + text}')
            text.draw(win)
            win.getMouse()
            text.undraw()

        blackeye = Circle(eye1centre, 5)
        blackeye.setFill('black')
        blackeye.draw(win)

        text = Text(Point(200,50), "OK, enough!")
        text.draw(win)

def main():
    win = GraphWin("Stick figure", 300, 200)
    win.setBackground("white")

    drawStickFigure(win)
    clickToClose(win)

main()