arr = list(map(int, input().split()))
key = int(input())
found_index = -1


for i in range(len(arr)):
	if arr[i] == key:
		found_index = i
		break

if found_index == -1:
	print("Not found")
else:
	print(found_index)
