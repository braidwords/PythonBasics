class Operation:
    def reverse_data(self, data):
        self.data = data
        print("reversed String is: %a" %(data[::-1]))


print("Enter your data")
data = str(input())
obj = Operation()
obj.reverse_data(data)

