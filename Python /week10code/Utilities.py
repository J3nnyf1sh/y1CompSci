from graphics import *   

class Utilities: #### CORE FUNCTIONS TO BE USED IN CAR

    @staticmethod
    def drawRectangle(win, tl, br, colour):
        rectangle = Rectangle(tl, br)
        rectangle.setFill(colour)
        rectangle.draw(win)
        return rectangle

    @staticmethod
    def drawCircle(win, center, radius, colour):
        circle = Circle(center, radius)
        circle.setFill(colour)
        circle.draw(win)
        return circle
