user_data = {} #use a directory

print("Enter your data")
user_list = input().split()

for item in user_list:
    if item in user_data:
        user_data[item] = user_data[item] + 1
    else:
        user_data[item] = 1

print('Unique item(s) :')
for item in user_data:
    if user_data[item] == 1:
        print(item)
