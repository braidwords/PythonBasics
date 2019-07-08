numbers = [23, 20, 2, 45, 67, 87]
small = numbers[0]
for x in numbers:
    if x < small:
        small = x
print(small)
