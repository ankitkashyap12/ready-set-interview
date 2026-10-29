# In this problem, your goal is to compute 𝐹𝑛 modulo 𝑚, where 𝑛 may be really huge: up to 1014. 
# For such values of 𝑛, an algorithm looping for 𝑛 iterations will not fit into one second for sure. 
# Therefore we need to avoid such a loop

# Both these sequences are periodic! For 𝑚 = 2, the period
# is 011 and has length 3, while for 𝑚 = 3 the period is 01120221 and has length 8. 
# Therefore, to compute, say, 𝐹2015 mod 3 we just need to find the remainder of 2015 when 
# divided by 8. Since 2015 = 251 · 8 + 7, we conclude that 𝐹2015 mod 3 = 𝐹7 mod 3 = 1.
# This is true in general: for any integer 𝑚 ≥ 2, the sequence 𝐹𝑛 mod 𝑚 is periodic. 
# The period alway starts with 01 and is known as Pisano period.
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
def getPisanoPeriod(m):
    prev = 0
    curr =1
    for i in range(0,m*m):
        prev,curr = curr,(prev+curr)%m

        if prev==0 and curr==1:
            return i+1

def getFib(n):
    # print("calculating fib for ",n)
    fib= []
    fib.append(0)
    fib.append(1)
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    # print("fib is ",fib[n])
    return fib[n]

def getFibModulo(n,m):
     period = getPisanoPeriod(m)
    #  print("Period is : ", period)
     n = n%period
    #  print("new n is ",n)
    #  print("",2%4)
     return getFib(n)%m

if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(getFibModulo(n,m))
    # print(get_fibonacci_huge_naive(n, m))
