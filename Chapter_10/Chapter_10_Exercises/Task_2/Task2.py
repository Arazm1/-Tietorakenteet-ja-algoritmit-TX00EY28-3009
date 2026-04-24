def fib(n):

    total = 0
    first_idx = 1
    second_idx = 1

    if n == 0:
        return 1
    
    if n == 1:
        return 1

    for i in range(2, n+1):
        total = first_idx + second_idx
        first_idx = second_idx
        second_idx = total
        

    return second_idx