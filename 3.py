array = [int(a) for a in input("Введите массив: ").split()]
delta = int(input("Введите delta: "))
minel = array[0]
for i in array:
    if minel > i:
        minel = i 
count = 0
for i in array:
    if i - minel == delta:
        count += 1
print(count)