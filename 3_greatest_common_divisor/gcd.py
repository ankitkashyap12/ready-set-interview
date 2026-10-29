# calculate gcd(a,b) till b part becomes 0(base condition)
# make b as a%b
# and a as b
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_euclid(a,b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b,a%b)

if __name__ == "__main__":
    # print("Enter inputs : \n")
    # input =sys.stdin.read()
    n = input()
    a, b = map(int, n.split())
    # print("using naive : ",gcd_naive(a, b))
    # print("Using euclids : ",gcd_euclid(a,b))
    print(gcd_euclid(a,b))
