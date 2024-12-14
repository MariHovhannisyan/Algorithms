def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [76, 39, 92, 19, 71, 43, 58]
target = int(input("Target="))
result = linear_search(arr, target)

if result != -1:
    print(str(target) + "   index=" + str(result)) 
else:
    print("not found")