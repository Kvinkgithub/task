a = [
    [1, 2, 3],
    [4, 5, 6]
]

total = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        total += a[i][j]
print(f"Сумма всех элементов: {total}")

max_item = a[0][0]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > max_item:
            max_item = a[i][j]
print(f"Максимальный элемент: {max_item}")

count = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] % 2 == 0:
            count += 1
print(f"Четных чисел: {count}")
