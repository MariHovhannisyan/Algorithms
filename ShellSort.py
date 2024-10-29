def shell_sort(arr):
    gap=len(arr)//2
    if len(arr)==1:
        return arr

    while gap>=1:
        for i in range(gap,len(arr)):
            c=arr[i]
            j=i
            while j>=gap and arr[j-gap]>c:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=c
        gap//=2
    return arr

arr=[8,-6,4,2,6,3,0,3,1,-6]    
shell_sort(arr)
print(arr)




