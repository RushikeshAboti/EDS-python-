import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

indices = np.where(array1 == search_value)[0]
print(indices)

count = np.count_nonzero(array1 == count_value)
print(count)

broadcasted = array1 + broadcast_value
print(broadcasted)

sorted = np.sort(array1)
print(sorted)
