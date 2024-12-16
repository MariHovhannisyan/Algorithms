import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n)) 
    prev = 0 

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1 

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i  

    return -1 


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  
target = 14
result = jump_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
