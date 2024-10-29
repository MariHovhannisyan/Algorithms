
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr

arr = [15, -17, 18, 8, 12, -6]
selection_sort(arr)
print(arr)


