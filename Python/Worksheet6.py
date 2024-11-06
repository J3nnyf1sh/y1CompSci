#Worksheet6
import math
from graphics import *

#-------------------------------------------------
#-------------------------------------------------

def fastFoodOrderPrice():
    price = float(input("Basic Price: "))
    total = price

    if price >= 20:
        total += 2.50

    print(f'The total price of your order is {total}')

#fastFoodOrderPrice()

#-------------------------------------------------
#-------------------------------------------------

def whatToDoToday():
    temp = float(input("Temperature today: "))

    if temp >= 25:
        print("Go for a swim in the sea")
    elif temp < 10:
        print("Watch a film at home")
    else:
        print("Go shopping in Gunwharf Quays")

#whatToDoToday()

#-------------------------------------------------
#-------------------------------------------------

def displaySquareRoots(start, end):
    for i in range(start, end):
        print(f'The square root of {i} is {math.sqrt(i)}')


def main():
    x = int(input("Start: "))
    y = int(input("End: "))

    displaySquareRoots(x, y + 1) 

#main()

#-------------------------------------------------
#-------------------------------------------------

def calculateGrade():
    mark = int(input("Enter mark: "))
    print(f"grade: {'FFFCCBBAAA'[mark]}")

#calculateGrade()

#-------------------------------------------------
#-------------------------------------------------

def clickToClose(win):
    win.getMouse()
    win.close()

def peasInAPod(): 
    peaNumber = int(input('How many peas: '))
    
    x = -50
    y = 50

    win = GraphWin(" ", (peaNumber * 100), 100)
    win.setBackground('white')
    
    for i in range(peaNumber):
        x += 100
        centre = Point(x, y)

        pea = Circle(centre, 50) 
        pea.setOutline('lime green')
        pea.setFill('lime green')

        pea.draw(win)

    clickToClose(win)

#peasInAPod()

#-------------------------------------------------
#-------------------------------------------------

def ticketPrice(age, km):
    price = 10 + (0.15 * km)

    if age <= 15 or age >= 60:
        price = price * 0.6

    print(f'The ticket price is £{round(price, 2)}')

def main1():
    km = float(input('How many km: '))
    age = int(input("Age: "))

    ticketPrice(age, km)

#main1()

#-------------------------------------------------
#-------------------------------------------------

def numberedSquare(n):
    x = 0

    for i in range(n):
        for j in range(n):
            number = (n + j) - x
            print(number, end=' ')

        x +=1
        print('')
        
        
def main2():
    n = int(input('number: '))
    
    numberedSquare(n)

#main2()

#-------------------------------------------------
#-------------------------------------------------



