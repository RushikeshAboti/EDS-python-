import math
num=int(input())
if num<10:
	print(num**2)
elif num<100:
	print(f"{math.sqrt(num):.2f}")
elif num<1000:
	print(f"{math.cbrt(num):.2f}")
else :
	print("Invalid")