#width = diametre of cookies
#rectangle = diametre * n

import math

def biscuitCutting():

    #Asks the user to enter the number of biscuits to be cut from the mixture
    n = float(input("How many biscuits would you like to be cut from the mixture? "))
    
    #Asks user for radius of each biscuit in cm
    r = float(input("What is the radius of each biscuit in cm? "))

    #output 1 
    width = r*2
    print("The width of the bescuit mixture is", width, "cm")

    #output 2 
    length = width*n
    print("The length of the biscuit mixture is", length, "cm")

    BMarea = width*length
    Barea = n * (math.pi * (r ** 2))
    spare = BMarea - Barea
    print("The amount of spare mixture is", spare, "cm^2")

    

biscuitCutting()


