# class Node:
#     def __init__(self, data,next = None):
#         self.__data = data
#         self.__next = next    

# class Stack:
#     def __init__(self):
#         self.__size=0
#         self.__head=None

#     def size(self)->int:
#         return self.__size
    
#     def isEmpty(self)->bool:
#         return (self.__size==0)
    
#     def push(self,val):
#         newNode=Node(val,self.__head)
#         head=newNode
#         self.__size+=1

#     def pop(self):
#         if self.isEmpty():
#             raise Exception("Stack is Empty")
#         else:
#             data=self.head.data
#             temp=self.head
#             self.head=self.head.next
#             del temp
#             self.__size-=1
#             return data

#     def top(self):
#         if self.isEmpty():
#             raise Exception("Stack is Empty")
#         else:
#             return self.head.data
        
#     def __str__(self):
#         st=[]
#         trav = self.__head
#         while trav is not None:
#             st.append(str(trav.data))
#             trav = trav.next
#         return '<---->'.join(st)
    
# #Test
# st=Stack()
# st.push(10)
# st.push(20)
# st.push(30)
# print(st)

class Node:
    def __init__(self, data, next=None):
        self.data = data  # Changed to public attribute
        self.next = next  # Changed to public attribute    

class Stack:
    def __init__(self):
        self.__size = 0
        self.__head = None

    def size(self) -> int:
        return self.__size
    
    def isEmpty(self) -> bool:
        return self.__size == 0
    
    def push(self, val):
        newNode = Node(val, self.__head)
        self.__head = newNode  # Corrected the reference to self.__head
        self.__size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            data = self.__head.data  # Corrected the reference to self.__head
            temp = self.__head
            self.__head = self.__head.next  # Corrected the reference to self.__head
            del temp
            self.__size -= 1
            return data

    def top(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            return self.__head.data  # Corrected the reference to self.__head
        
    def __str__(self):
        st = []
        trav = self.__head
        while trav is not None:
            st.append(str(trav.data))  # Corrected the reference to data
            trav = trav.next
        return '<---->'.join(st)
    
# Test
st = Stack()
st.push(10)
st.push(20)
st.push(30)
print(st)  # Output should be: 30<----20<----10
