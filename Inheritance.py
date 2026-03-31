# class animal:
#     def sound(self):
#         print("animal makes sound")
#
# class dog(animal):
#     def bark(self):
#         print("dogs barks")
#
#
# d = dog()
# d.sound()
# d.bark()


'''
o/p
animal makes sound
dogs barks
'''



class Tree:
    def type(self):
        print("tupes of trees")

class branch(Tree):
    def colour(self):
        print("brown")

class leaves(Tree):
    def colour(self):
        print("green")

b = branch()
b.colour()
l = leaves()
l.colour()

'''
o/p
brown
green
'''