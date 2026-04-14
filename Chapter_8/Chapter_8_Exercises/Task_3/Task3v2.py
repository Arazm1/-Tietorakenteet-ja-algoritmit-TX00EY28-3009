def binary_search_iterative(array, value):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        
        midpoint = start + (end - start) // 2

        if array[midpoint] == value:
            return midpoint
        
        # 4. If the value is smaller, throw away the right half
        if value < array[midpoint]:
            end = midpoint - 1
            
        # 5. If the value is bigger, throw away the left half
        elif value > array[midpoint]:
            start = midpoint + 1
            
    return None

print(binary_search_iterative([1, 2, 3, 4, 5], 5))