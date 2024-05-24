class Node:
    def __init__(self, data,prev=None, next=None):
        self.data = data
        self.next = None
        self.prev = None
        self.data = data
    def __str__(self):
        return str(self.data)
# node =Node(10)
# print(node.data)

#addLast(element),addFirst(element),addAt(index,element),removeLast(),removeFirst(),removeAt(index),get(index),isEmpty(),size(),Contains(element),indexOf(element),append(element)
class DLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
        self.__size += 1

    def __str__(self):
        l=[]
        trav = self.__head
        while trav is not None:
            l.append(str(trav.data))
            trav = trav.next    
        return '<---->'.join(l)
    
    def addFirst(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.next = self.__head
            self.__head.prev = newNode
            self.__head = newNode
        self.__size += 1

    def addAt(self,index,data):
        if index < 0 or index > self.__size():
            raise Exception("Invalid Index")
        if index == 0:
            self.addFirst(data) 
        elif index == self.__size():
            self.append(data)
        else:
            newNode = Node(data)
            trav = self.__head
            for i in range(index-1):
                trav = trav.next
            newNode.next = trav.next
            newNode.prev = trav
            trav.next = newNode
            self.__size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is Empty")
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
        self.__size -= 1

    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is Empty")
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.prev
        self.__size -= 1

    def removeAt(self,index):
        if index < 0 or index >= self.__size():
            raise Exception("Invalid Index")
        if index == 0:
            self.removeFirst()
        elif index == self.__size()-1:
            self.removeLast()
        else:
            trav = self.__head
            for i in range(index-1):
                trav = trav.next
            trav.next = trav.next.next
            self.__size -= 1

        def __iter__(self):
           self.__trav = self.__head
           return self
        
        def __next__(self):
            x=self.trav.data
            if(self.__trav is not None):
                self.__trav = self.__trav.next
            return x
        
        
            
print(DLL().size())
print(DLL().isEmpty())
l=DLL()
l.append(10)
l.append(20)
l.append(30)
l.append(50)
print(l.size())
print(l.isEmpty())
print(l)

