#practice lecture 2

def areaofrectangle():
    length = float(input("What is the length of the rectangle? "))
    width =  float(input("What is the width of the rectangle? "))
    area = width*length 
    print("the area of the rectangle is", area)

def areaofrectangleagain():
    x1 = float(input("what is x1? "))
    y1 = float(input("what is y1? "))
    x2 = float(input("what is x2? "))
    y2 = float(input("what is y2? "))
    height = y2 - y1
    length = x2 - x1

    area = length*height
    print("the area is", area)

import math

def distanceBetweenPoints():
    x1 = float(input("what is x1? "))
    y1 = float(input("what is y1? "))

    x2 = float(input("what is x2? "))
    y2 = float(input("what is y2? "))

    dx = x2 - x1
    dy = y2 - y1

    dxsq = dx * dx
    dysq = dy * dy
    
    added = dxsq + dysq

    distance = math.sqrt(added)

    print(distance)


#worksheet

def speedCalculator():
    distance = float(input("What is the distance in km? "))
    duration = float(input("what is the duration in hours? "))

    speed = distance/duration

    print('the speed is', speed)

def circumferenceOfCircle():
    radius = float(input("what is the radius of the circle in cm? "))

    circumference = math.pi * radius * 2
    print(circumference)

def areaOfCircle():
    radius = float(input("what is the radius of the circle in cm? "))

    area = math.pi * (radius ** 2)
    print(area)

def costOfPizza():
    radius = float(input('what is the radius of the pizza in cm? '))
    area = math.pi * (radius ** 2)
    price = area * 0.035
    print("the pizza is £" + str(round(price, 2)))

def slopeOfLine():
    x1 = float(input("What is x1? "))
    y1 = float(input("What is y1? "))
    x2 = float(input("What is x2? "))
    y2 = float(input("What is y2? "))

    gradient = (y2-y1)/(x2-x1)

    print(gradient)

def travelStatistics():
    avgspeed = float(input("what is the average speed in km/h? "))
    duration = float(input('What is the duration of the car journey in hours? '))

    distance = avgspeed*duration
    fuelEfficiency = 5

    fuel = distance/5
    print("fuel used:", fuel ,"litres")

def sumOfSquares():

    #empty list 
    squares = []

    n = int(input('What is n? '))

    n = int(n) + 1

    sum = 0

    #adds to the empty list, e.g. n = 4, n = 4 + 1. so i is 1,2,3,4 and numbers get added by append to the empty list
    for i in range(1, n):
        squares.append(i)


    #len() returns the number of items in an object. so if the list is [2,5,4,3], len(list) returns 4, because there are 4 items.
    for x in range(len(squares)):
        sum = sum + (squares[x]**2)

    print(sum)

def averageofNumbers():
    n = int(input("how many numbers would you like to input? "))
    sum = 0

    for i in range(n):
        x = int(input("enter a number: "))
        sum = sum + x 

    average = sum/n

    print(average)
    
def fibonacci():
    n = int(input("Which nth term are you looking for? "))
    x = [0, 1]

    for i in range(n-1):
        x.append(x[-1]+x[-2])
    
    print(x)
    print(x[-1])

def selectCoins():
    pence = int(input("Enter amount in pence: "))

    twopound = pence//200
    print('£2 =', twopound)
    pence = pence%200

    onepound = pence//100
    print('£1 =', onepound)
    pence = pence%100

    fiftyp = pence//50
    print('50p =', fiftyp)
    pence = pence%50

    twentyp = pence//20
    print('20p =', twentyp)
    pence = pence%20

    tenp = pence//10
    print('10p =', tenp)
    pence = pence%10

    fivep = pence//5
    print('5p =', fivep)
    pence = pence%5

    twop = pence//2
    print('2p =', twop)
    pence = pence%2

    onep = pence
    print('1p =', onep)


selectCoins()









    


def hypotenuse():
    b = float(input("What is the length of the first short side of the right angle triangle? "))
    c = float(input("What is the length of the second short side of the right angle triangle? "))

    a = math.sqrt((b**2)+(c**2))
    print("the hypotenuse length is", a)






#for loop is for a know number of repeats/loops, while is for unknown number fo loops until its done
#square brackets is index