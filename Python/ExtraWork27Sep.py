#projecteuler.net 

#problem 1 
def threeorfive():
    sum = 0

    for i in range(1, 100):
        if not i % 5 or not i % 3:
          sum += i

    print(sum)

#problem 2 
def fibonacciSeq():
    n = [1, 1]
    sum = 0

    while n[-1] <= 4000000:
      n.append(n[-1]+n[-2])
    for i in n:
        if not i%2:
            sum += i

    print(sum)

#problem 3
def largestPrimeFactor():
    n = 600851475143
    i = 2

    while i * i <= n:
        while n % i == 0:
            n = n/i
        i = i + 1

    print(n)


