def factorial(n):
    # Base case
    if n == 1:
        return 1
    
    # Common case
    return n * factorial(n-1)


#print(factorial(4))


def permutations(data, n=0):
    if n == len(data)-1:
        return data
    
    return [pattern + c for pattern in permutations(data, n+1) for c in data]

"""
permutations('123')
print(permutations('123'))
# or
permutations(('1', '2', '3'))
"""


print(permutations(('1', '2', '3')))




def fib(n):
    if n<2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)
    

def fib2(n, cache={0:1, 1:1}):
    if len(cache) <= n:
        cache[n] = fib(n-1, cache) + fib(n-2, cache)

    return cache[n]

from functools import cache

@cache
def fib3(n):
    if n<2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)