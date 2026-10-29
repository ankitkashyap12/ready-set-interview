# Trick here is to not store nth term, instead store last digit of nth term
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
# faster one
def get_fibonacci_last_digit(n):
    fib= []
    fib.append(0%10)
    fib.append(1%10)
    for indx in range(2,n+1):
        fib.append((fib[indx-1]+fib[indx-2])%10)

    return fib[n]

if __name__ == '__main__':
    n = input()
    # n = int(input("enter n: "))
    print(get_fibonacci_last_digit(int(n)))
    # print("Last digit of " ,n," is :",get_fibonacci_last_digit(n))

