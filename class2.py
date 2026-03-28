class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

# Creating object
s1 = Student("Abishek", 90)

# Calling method
s1.display()

'''
o/p
Name: Abishek
Marks: 90
'''