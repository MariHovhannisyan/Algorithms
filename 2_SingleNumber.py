'''numbers = [4, 4, 3, 3, 2]

result = 0 
for num in numbers:
    result ^= num  

print("XOR of all numbers:", result)
'''

numbers = [1, 1, 2, 2, 4, 5, 5, 6, 6, 7, 8, 8, 9, 11, 65, 65, 23]

result = 0
found_unique = [] 

for num in numbers:
    result ^= num  
    if numbers.count(result) % 2 != 0:
        found_unique.append(result) 
        result = 0

print("The unique numbers are:", found_unique)
