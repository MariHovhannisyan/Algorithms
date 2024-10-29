def bubble(list):
  for i in range(len(list)):
    for j in range(0,len(list)-i-1):
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
  return list
a = [31,2,5,-7,-4,1,2,3,10,1,-4]
print(bubble(a))