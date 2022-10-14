import random 
a = int(input("Введите колличество элементов массива 1: "))
b = int(input("Введите колличество элементов массива 1: "))
A = [0] * a
B = [0] * b
ans = []
for i in range(a):
    A[i] = random.randint(-10, 0)
for i in range(b):
    B[i] = random.randint(-10, 0)
for a in A:
    if a in B and a not in ans:
        ans.append(a)
for i in ans:
    print(i, end=" ")
