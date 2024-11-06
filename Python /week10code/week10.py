from graphics import *
from time import *
from Utilities import *
from Car import * 

##### PROGRAM
def main():
    win = GraphWin('', 800, 500)
    cars = []

    for i in range(0, 200, 10):
        car = Car((10*i), (10*i), (15*i), (7*i), (3*i), "blue", win)
        car.buildCar()
        cars.append(car)

    # bmw = Car(100, 130, 150, 70, 30, "blue", win)
    # bmw.buildCar()
    # ford = Car(10, 13, 10, 7, 4, "red", win)
    # ford.buildCar()

    # buildCar(topLeftX, topLeftY, widthCarTop, heightCarTop, diff, 'blue', win, car)
    win.getMouse()
    for j in range(1000):
        sleep(.01)
        # bmw.move(2, 0)
        # ford.move(.5, .5)
        flag = True
        for car in cars:
            if flag:
                car.move(j+1, 0)
            else:
                car.move(j-1, 0)
                flag = not flag
    win.getMouse()


main()