def heapify(arr,n,i):
  largest = i
  left = 2*i +1
  right = 2*i +2

  if left < n and arr[largest] < arr[left]:
    largest = left
  if right < n and arr[largest] < arr[right]:
    largest = right

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr,n,largest)

def sort(arr):
  n = len(arr)

  for i in range(n//2,-1,-1):
    heapify(arr,n,i)

  print(arr)
  for i in range(n-1,0,-1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr,i,0)


arr = [-8,6,0,11,4,-6,1,3,4,-3]
sort(arr)
print(arr)
