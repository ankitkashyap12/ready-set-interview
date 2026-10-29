# We can rewrite the relation F(n+1) = F(n) + F(n-1) as below
# F(n-1)    = F(n+1)  -  F(n)

# Similarly,
# F(n-2)    = F(n)    -  F(n-1)
# .          .           .
# .          .             .
# .          .             .
# F(0)      = F(2)    -  F(1)
# -------------------------------

# Adding all the equations, on left side, we have 
# F(0) + F(1) + … F(n-1) which is S(n-1).
# Therefore, 
# S(n-1) = F(n+1) – F(1) 
# S(n-1) = F(n+1) – 1 
# S(n) = F(n+2) – 1 —-(1)
# In order to find S(n), simply calculate the (n+2)’th Fibonacci number and subtract 1 from the result.
# F(n) can be evaluated in O(log n) time
# The goal in this problem is to find the last digit of a sum of the first 𝑛 Fibonacci numbers.
import sys
import math

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def getNthFib(n):
    # phi = (1 + math.sqrt(5)) / 2
    fib=[]
    fib.append(0)
    fib.append(1)
    n=n%60
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]
 
    # return round(pow(phi, n) / math.sqrt(5))

def sumLastDigitFib(n):
    n+=2
    return (getNthFib(n)%10-1%10)%10

if __name__ == '__main__':
    input = input()
    n = int(input)
    # print(fibonacci_sum_naive(n))
    # print("using faster method : ",sumLastDigitFib(n))
    print(sumLastDigitFib(n))
