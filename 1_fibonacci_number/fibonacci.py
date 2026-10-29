
# Different ways to calculate nth term of fibonacci
# 1.Recursion - Not efficient
# 2. Dynamic Programming
# 3. DP with space optimization(Instead of array, keep track of last two only)
# 4.Using power of the matrix {{1, 1}, {1, 0}}) 
# This is another O(n) which relies on the fact that if we n times multiply the 
# matrix M = {{1,1},{1,0}} to itself 
# (in other words calculate power(M, n)), then we get the (n+1)th Fibonacci number as the element
#  at row  and column (0, 0) in the resultant matrix.
# 5.Fn = {[(√5 + 1)/2] ^ n} / √5 (Phi)
# Reference : https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/ 


from datetime import date, datetime
import timeit
from typing import List
def calc_fib(n):
    
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]
n = int(input())

# st = timeit.default_timer()
# print(calc_fib(n))
# sto = timeit.default_timer()
# t = sto-st
# print("time taken for n= ",n," wiht naive is ",t )

# print("Calling efficient method now ")
# start = datetime.now()
print(calc_fib_fast(n))
# print("time taken for n= ",n," with fast algo  is ",datetime.now() - start )
