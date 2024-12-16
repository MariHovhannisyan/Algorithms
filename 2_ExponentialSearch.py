def exponential_search(arr,target):
  if len(arr)==0:
    return 'the array is empty'
  if arr[0]==target:
    return 0
  prev=0
  hop=1
  while hop < len(arr) and arr[hop] < target:
    prev=hop
    hop*=2
    if prev>=len(arr):
      return "the element is not in the array"
  for i in range (prev,min(hop,len(arr))):
    if arr[i]==target:
      return i
  return "the element is not in the array"

arr=[2,4,6,8,10,12,14]
target=9
y=exponential_search(arr,target)
print(y)