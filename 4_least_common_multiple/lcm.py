# Use the fact that lcm * hcf = a*b
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
def gcd_euclid(a,b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b,a%b)

def lcm_fast(a,b):
    gcd= gcd_euclid(a,b)
    return ((a*b)//gcd)


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print( lcm_fast(a,b))
    # print(lcm_naive(a, b))

