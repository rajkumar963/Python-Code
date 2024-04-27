# Method of three types:-
# 1. Instance Method
# 2. Static Method
# 3. Class Method

######################################################################

# Class method:
# class Person:
#     Country="India"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#         @staticmethod
#         def Disco():
#             print("I love disco and EDM")

#     @classmethod
#     def gaming(cls):
#          print("I love to india football and cricket:",cls.Country)
#          print("I am a gaming player!! I love to play games")
         
# Person.gaming()
# per=Person("Hanuman", 20)
# per.gaming()

# Person.Disco()
# per1=Person.Disco()

###########################################################################

# class std:
#     exam_given=[ ]
#     def __init__(self, id):
#         self.book = [ ]
#         self.college = "IIT"
#         self.roll = id

# std1=std(102)
# std2=std(103)
# std1.exam_given.append("JEE")
# std2.exam_given.append("NEET")
# std1.book.append("atomic habbit")
# std2.book.append("GATE")

# std1.college="NIT"
# print(std1.roll)
# print( std2.roll)
# print(std1.exam_given)
# print( std2.exam_given)
# print(std1.college)
# print( std2.college)
# print(std1.book)
# print( std2.book)

####################################################################

# class employe:
#     holidays=["sunday","monday","tuesday"]
#     def __init__(self, name, id, salary):
        
#         self.name = name
#         self.id = id
#         self.salary = salary

#     def get_tax(self):
#        return 0.2*self.salary
    
#     @classmethod 
#     def get_holidays(cls):
#         return cls.holidays

# emp1=employe("ramesh", 101, 10000)
# emp2=employe("suresh", 102, 20000)
# print(emp1.get_tax())
# print(emp2.get_tax())
# employe.get_holidays()
# print(emp1.get_holidays())
# print(emp2.get_holidays())


########################################################################

#make point class use this method distance from origin, distance (point), isequal (point), cross product, rotate point, dot product
# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def distance_to_origin(self):
#         return (self.x**2 + self.y**2)**0.5
    
#     def isequal(self, a):
#         return self.x==a.x and self.y==a.y
    
#     def cross_product(self,a):
#         return self.x*a.y - self.y*a.x
    
#     def dot_product(self,a):
#         return self.x*a.x + self.y*a.y
    
#     def unit_vector(self):
#         return point(self.x/((self.x**2 + self.y**2)**0.5), self.y/((self.x**2 + self.y**2)**0.5))
    
#     def point_point(self):
#         return point(self.x, self.y)

    
# pt=point(4,3)
# pt1=point(2,4)
# print(pt.unit_vector())
# print(pt.point_point())


# print(pt.dot_product(pt))
    
# pt=point(7,6)
# pt=point(5,6)
# print(pt.cross_product(pt1))

# pt=point(2,4)
# pt=point(2,4)
# print(pt.isequal(pt1))

# pt=point(2,3)
# print(pt.distance_to_origin())

    
#######################################################################

# make matrix class use this method add, sub, mul, div, str

# class Matrix:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self, a):
#         return Matrix(self.x+a.x, self.y+a.y)
#     def sub(self, a):
#         return Matrix(self.x-a.x, self.y-a.y)
#     def mul(self, a):
#         return Matrix(self.x*a.x, self.y*a.y)
#     def truediv(self, a):
#         return Matrix(self.x/a.x, self.y/a.y)
#     def __str__(self):
#         return "("+str(self.x)+","+str(self.y)+")"  
    
# matrix = Matrix(2, 3)
# matrix1 = Matrix(4, 3)
# result = matrix.mul(matrix1)
# print(result)

############################################################################

#make student class use this method name, roll, age, marks, college, address, attendance    
class student: 
    def __init__(self, name, roll, age, marks, college, address, attendance):
        self.name = name
        self.roll = roll
        self.age = age
        self.marks = marks
        self.college = college
        self.address = address
        self.attendance = attendance

st1 = student("suresh", 101, 20, 80, "NIT", "pune", 80)
st2 = student("ramesh", 102, 21, 90, "VNIT", "pune", 90)
st3 = student("kiran", 103, 20, 70, "IIT", "pune", 70)     

print(st1.name, st1.roll, st1.age, st1.marks, st1.college, st1.address, st1.attendance)
print(st2.name, st2.roll, st2.age, st2.marks, st2.college, st2.address, st2.attendance)
print(st3.name, st3.roll, st3.age, st3.marks, st3.college, st3.address, st3.attendance)


################################################################################

#