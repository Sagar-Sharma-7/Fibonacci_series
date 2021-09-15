# Fibonacci series
## **What is Fibonacci Series?**
 > The Fibonacci Series of Sequence is the series of numbers:
 >> <div align="center">  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... </div>

>>> The next number is found by adding up the two numbers before it:
>>> * the 2 is found by adding the two numbers before it (1 + 1),
>>> * the 3 is found by adding the two numbers before it (1 + 3),
>>> * the 5 is (2 + 3),
>>> * and so on!

## The two different ways to get fibonacci series:
1. 
```py 
import math

def factorial(n):
    for i in range(1, n + 1):
        result = ((((1 + math.sqrt(5))/2)**(i-1)) - (((1- math.sqrt(5))/2)**(i - 1))) / math.sqrt(5)
        print(int(result), end=" , ")


n = int(input("Enter number of terms term: "))
factorial(n)
```

----
2. 
```py
def fibonacci(n):
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(1, n):
        third = first + second
        print(third)
        first, second = second, third

n = int(input("Enter nth term: "))
fibonacci(n)
```