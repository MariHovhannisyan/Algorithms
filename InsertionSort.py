def insert(arr):
    n=len(arr)
    for i in range(1,n):
        k=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>k:
                arr[j+1]=arr[j]
            else:
                arr[j+1]=k
                break
        else:
            arr[0]=k
    return arr
a=[11,4,-2,51,-28,4,2,-3]
b=[5,7,-11,8,0,2,4,6]
print(insert(a))