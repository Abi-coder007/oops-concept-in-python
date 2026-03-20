#  Constructor __init__
#
# class car:
#     def __init__(self,brand,style,color,look):
#         self.brand = brand
#         self.style = style
#         self.color = color
#         self.look = look
#
#
# c1 = car("Rolls Royce","mass","white","Zebra")
# c2 = car("dogoe","mass","Black","Black horse")
#
# print(c1.brand,c1.style,c1.color,c1.look)
# print(c2.brand,c2.style,c2.color,c2.look)
#
# '''
# o/p
# Rolls Royce mass white Zebra
# dogoe mass Black Black horse
#
# '''

class Car:
    def __init__(self, brand):
        self.brand = brand   # THIS object's brand

c1 = Car("Toyota")
c2 = Car("Honda")

print(c1.brand)  # Toyota  — c1 has its own data
print(c2.brand)  # Honda   — c2 has its own data


'''
o/p
Toyota
Honda

'''
