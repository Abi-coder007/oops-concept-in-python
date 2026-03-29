class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):   # overriding the parent method
        print("Dog barks")

a = Animal()
a.sound()

d = Dog()
d.sound()


'''

o/p
Animals make sound
Dog barks
'''