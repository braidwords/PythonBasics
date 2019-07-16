class Cat:
    def __init__(self, cat_name, color):
        self.cat_name = cat_name
        self.color = color
        print("Details received.")
    def add_data(self):
        census = []
        census.append(self.cat_name)
        census.append(self.color)
        print(census)

class Attributes(Cat):
    def other_data(self, weight, eyes_color):
        self.weight = weight
        self.eyes_color = eyes_color
        if self.weight <= 30:
            print("Your cat need to put on weight. Make her eat something good.")
        elif self.weight >= 45:
            print("Your cat needs to loose weight!")
        else:
            print("Congratulations! You have a healthy cat")


print("Enter the name of your cat: ")
cat_name = str(input())
print("Enter the color: ")
color = str(input())
fluffy = Attributes(cat_name, color)
fluffy. add_data()
print("Enter the weight of your cat: ")
weight = int(input())
print("Enter the color of your cat's eyes: ")
eyes_color = str(input())
fluffy.other_data(weight, eyes_color)

