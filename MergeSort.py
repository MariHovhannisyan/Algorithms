def merge(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        merge(left_arr)
        merge(right_arr)

        i = 0 # left_arr index
        j = 0 # right_arr index
        k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1 
            else:
                arr[k] = right_arr [j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr [i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr [j]
            j += 1
            k += 1

arr=[-5,0,-11,3,2,19,23,-7,0,6]
merge(arr)
print(arr)