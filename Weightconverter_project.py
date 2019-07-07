weight = input("Enter your weight: ")
weight_unit = input("Choose the unit:(P)ounds or (K)ilograms: ")
if weight_unit == 'K':
    weight = float(weight) * 2.76
    print(weight)
else:
    weight = float(weight) / 2.76
    print(weight)

print("Conversion finished")
