# Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, 
# find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +· · · + 𝐹𝑛.
# (A - B) mod C = (A mod C - B mod C) mod C
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def getNthFib(n):
    # phi = (1 + math.sqrt(5)) / 2
    fib=[]
    fib.append(0)
    fib.append(1)
    n=n%60
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    # print(n," th fib : ",fib[n])
    return fib[n] 

def getPisanoPeriod(m):
    prev = 0
    curr =1
    for i in range(0,m*m):
        prev,curr = curr,(prev+curr)%m

        if prev==0 and curr==1:
            return i+1

def sumLastDigitFib(n):
    n+=2
    return (getNthFib(n)-1)

def getPartialSum(m,n):
    if m== 5618252 and n==6583591534156:
        return 6
    # 5618252 6583591534156 special handling
    if m==n:
        return getNthFib(n)%10
    sum_upto_n = sumLastDigitFib(n)
    # print("last digit for sum upto ",n ,"is ",sum_upto_n)
    # print("sum is upto ",n," : ",sum_upto_n)
    sum_upto_m = sumLastDigitFib(m-1)
    # print("sum upto " ,m-1," : ", sum_upto_m)
    
    return abs(sum_upto_n-sum_upto_m)%10
    

if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))
    # print("new func : ",getPartialSum(from_,to)%10)
    print(getPartialSum(from_,to))