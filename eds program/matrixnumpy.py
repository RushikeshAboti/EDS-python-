import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])

print("Addition (A + B):")
a = matrix_a + matrix_b
print(a)
print("Subtraction (A - B):")
b = matrix_a - matrix_b 
print(b)
print("Element-wise Multiplication (A * B):")
m = matrix_a*matrix_b 
print(m)
print("A dot B:")
d = np.dot(matrix_a,matrix_b) 
print(d)
print("Transpose of A:")
t = np.transpose(matrix_a)
print(t)