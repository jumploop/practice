"""
斐波那契数列
"""

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,b+a
    print()

fib(1000)