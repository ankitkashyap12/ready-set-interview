#  Compute the last digit of sum of fibonacci element squared
# F1^2+..Fn^2 = Fn*Fn+1
# so need to calculate (Fn*Fn+1)%10 which is equivalent to (Fn%10 *Fn+1%10)%10( by property of modulo)
# Can use Pisano period to know last digit of each Fn
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def getPisanoPeriod(m):
    prev = 0
    curr =1
    for i in range(1,m*m):
        prev,curr = curr,(prev+curr)%m

        if prev==0 and curr==1:
            return i+1

def getFib(n):
    fib= []
    fib.append(0)
    fib.append(1)
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    # print("fib is ",fib[n])
    return fib[n]

def getFibSumSquaredLastDigit(n):
    #  period = getPisanoPeriod(n)
     n_ = n%60
    #  period_n_plus1= getPisanoPeriod(n+1)
     n_plus1=(n+1)%60
    #  print("period is ",n)
     return (getFib(n_)%10*getFib(n_plus1)%10)%10


if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_squares_naive(n))
    print(getFibSumSquaredLastDigit(n))
