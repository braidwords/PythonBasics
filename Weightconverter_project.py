weight = input("Enter your weight: ")
weight_unit = input("Choose the unit:(P)ounds or (K)ilograms: ")
if weight_unit.upper() == 'K':
    weight = float(weight) * 2.205
    print(f"You are {weight} pounds")
else:
    weight = float(weight) / 2.205
    print(f"You are {weight} kilos")

print("Conversion finished")
