# Binary togather of data and the methods
# Encapsulation:-1.state/field:-always private
                # 2. method/behaviour:-always public
                
# 1. Data Hiding
# 2. Data Abstraction
# 3. Data Encapsulation

class Person:
    def __init__(self, name, car):
        self.name = name # private
        self.__car = car # protected

        def getName(self):
            return self.name
        
        def setName(self, name):
            self.name = name
        
        def getCar(self):
            return self.__car
        
        def setCar(self, car):
            self.__car = car
   


   #Question:
            class Rectangle:
                def __init__(self, length, breadth):
                    self.length = length
                    self.breadth = breadth

            def getLength(self):
                    return self.__length
            def setLength(self, length):
                    self.__length = length

            def getBreadth(self):
                 return self.__breadth
            def setBreadth(self, breadth):
                    self.__breadth = breadth       
            def area(self):
                    return self.length * self.breadth
            def perimeter(self):
                    return 2*(self.length + self.breadth)
    