class StudentData:
    def __init__(self, name, marks, marks1):
        self.name = name
        self.marks = marks
        self.marks1 = marks1

    def marks_cal(self):
        result = (self.marks + self.marks1)
        return result


print("Enter the name")
name = str(input())
print("Enter your marks for Maths: ")
marks = int(input())
print("Enter your marks for Chemistry: ")
marks1 = int(input())
data = StudentData(name, marks, marks1)
print("Your marks are: %d" %(data.marks_cal()))
