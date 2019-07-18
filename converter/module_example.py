from converter import converters

print("""Choose option to enter your weight: 
 1. Weight in KG
 2. Weight in Pounds""")
user_input = input()
if user_input == '1':
    print("Enter your weight: ")
    weight = int(input())
    converters.kg_to_pounds(weight)
else:
    print("Enter your weight: ")
    weight = int(input())
    converters.pounds_to_kg(weight)
