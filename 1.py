import random
n = int(input("Введите колличество элементов массива: "))
arr = [0] * n 
for i in range(n):
    arr[i] = random.randint(-500, 500) + round(random.random(), 2)
maxx = arr[0]
for i in arr:
    if i > maxx:
        maxx = i 
indmax = arr.index(maxx) + 1 # max нельзя брат
for i in range(indmax, n):
    arr[i] = 0
print(arr)