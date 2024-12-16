def interpolation_search(arr,target):
  if len(arr)==0:
    return 'the array is empty'
  pos = 0 + ((target - arr[0]) * (len(arr)-1)) // (arr[-1] - arr[0])
      
  if arr[pos] == target:
            return pos
  elif arr[pos] < target:
            low = pos + 1
  else:
            high = pos - 1

  return 'there is no such element'
    

arr=[2,4,6,8,10,12,14]
target=9
y=interpolation_search(arr,target)
print(y)