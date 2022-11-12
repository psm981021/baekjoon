#https://www.acmicpc.net/problem/2407

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n, m = map(int, input().split())


from fractions import Fraction
print(Fraction(factorial(n), (factorial(m)*factorial(n-m))))