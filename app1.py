import math

def factorial(n):
    for i in range(1, n + 1):
        result = ((((1 + math.sqrt(5))/2)**(i-1)) - (((1- math.sqrt(5))/2)**(i - 1))) / math.sqrt(5) # algorithm of fabonacci series
        print(int(result), end=" , ")


n = int(input("Enter number of terms term: "))
factorial(n)