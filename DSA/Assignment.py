# class DynamicArray:
#     def _init_(self, initial_capacity=10, resize_factor=1.5):
#         self.array = [0] * initial_capacity
#         self.capacity = initial_capacity
#         self.size = 0
#         self.resize_factor = resize_factor

#     def resize(self):
#         new_capacity = int(self.capacity * self.resize_factor)
#         new_array = [0] * new_capacity
#         for i in range(self.size):
#             new_array[i] = self.array[i]
#         self.array = new_array
#         self.capacity = new_capacity

#     def insert_at(self, index, value):
#         if index > self.size:
#             print("Index out of range")
#             return
#         if self.size == self.capacity:
#             self.resize()
#         for i in range(self.size, index, -1):
#             self.array[i] = self.array[i - 1]
#         self.array[index] = value
#         self.size += 1

#     def delete_at(self, index):
#         if index >= self.size:
#             print("Index out of range")
#             return
#         for i in range(index, self.size - 1):
#             self.array[i] = self.array[i + 1]
#         self.size -= 1

#     def get_size(self):
#         return self.size

#     def is_empty(self):
#         return self.size == 0

#     def rotate_right(self, k):
#         if self.size == 0:
#             return
#         k %= self.size
#         temp = self.array[-k:] + self.array[:-k]
#         self.array[:self.size] = temp

#     def reverse(self):
#         self.array[:self.size] = self.array[:self.size][::-1]

#     def append(self, value):
#         if self.size == self.capacity:
#             self.resize()
#         self.array[self.size] = value
#         self.size += 1

#     def prepend(self, value):
#         self.insert_at(0, value)

#     @staticmethod
#     def merge(a, b):
#         result = DynamicArray(a.size + b.size)
#         for i in range(a.size):
#             result.append(a.array[i])
#         for i in range(b.size):
#             result.append(b.array[i])
#         return result

#     @staticmethod
#     def interleave(a, b):
#         new_size = a.size + b.size
#         result = DynamicArray(new_size)
#         min_size = min(a.size, b.size)
#         for i in range(min_size):
#             result.append(a.array[i])
#             result.append(b.array[i])
#         for i in range(min_size, a.size):
#             result.append(a.array[i])
#         for i in range(min_size, b.size):
#             result.append(b.array[i])
#         return result

#     def middle_element(self):
#         if self.size == 0:
#             print("Array is empty")
#             return -1
#         return self.array[self.size // 2]

#     def index_of(self, value):
#         for i in range(self.size):
#             if self.array[i] == value:
#                 return i
#         return -1

#     def split_at(self, index):
#         if index > self.size:
#             print("Index out of range")
#             return None, None
#         first = DynamicArray(index)
#         second = DynamicArray(self.size - index)
#         for i in range(index):
#             first.append(self.array[i])
#         for i in range(index, self.size):
#             second.append(self.array[i])
#         return first, second

#     def set_resize_factor(self, factor):
#         if factor <= 1.0:
#             print("Resize factor must be greater than 1.0")
#             return
#         self.resize_factor = factor


# # Testing the DynamicArray class
# if _name_ == "_main_":
#     arr = DynamicArray()

#     arr.append(1)
#     arr.append(2)
#     arr.append(3)
#     arr.prepend(0)

#     print("Array after appending and prepending: ", end="")
#     for i in range(arr.get_size()):
#         print(arr.middle_element(), end=" ")
#     print()

#     arr.insert_at(2, 10)
#     print("Array after inserting 10 at index 2: ", end="")
#     for i in range(arr.get_size()):
#         print(arr.middle_element(), end=" ")
#     print()

#     arr.delete_at(2)
#     print("Array after deleting element at index 2: ", end="")
#     for i in range(arr.get_size()):
#         print(arr.middle_element(), end=" ")
#     print()

#     arr.rotate_right(2)
#     print("Array after rotating right by 2: ", end="")
#     for i in range(arr.get_size()):
#         print(arr.middle_element(), end=" ")
#     print()

#     arr.reverse()
#     print("Array after reversing: ", end="")
#     for i in range(arr.get_size()):
#         print(arr.middle_element(), end=" ")
#     print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.listSize = 0

    def __del__(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node

    def insert_at(self, index, value):
        if index > self.listSize:
            print("Index out of range")
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = None
            curr = self.head
            for i in range(index):
                prev = curr
                curr = curr.next
            new_node.next = curr
            prev.next = new_node
        self.listSize += 1

    def delete_at(self, index):
        if index >= self.listSize:
            print("Index out of range")
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
        else:
            prev = None
            for i in range(index):
                prev = temp
                temp = temp.next
            prev.next = temp.next
        del temp
        self.listSize -= 1

    def get_size(self):
        return self.listSize

    def is_empty(self):
        return self.listSize == 0

    def rotate_right(self, k):
        if self.listSize == 0:
            return
        k = k % self.listSize
        if k == 0:
            return

        old_tail = self.head
        new_tail = self.head
        new_head = self.head

        for i in range(self.listSize - 1):
            old_tail = old_tail.next
        for i in range(self.listSize - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        old_tail.next = self.head
        new_tail.next = None
        self.head = new_head

    def reverse(self):
        prev = None
        curr = self.head
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.listSize += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.listSize += 1

    @staticmethod
    def merge(a, b):
        result = SinglyLinkedList()
        temp = a.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        temp = b.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    @staticmethod
    def interleave(a, b):
        result = SinglyLinkedList()
        temp_a = a.head
        temp_b = b.head
        while temp_a or temp_b:
            if temp_a:
                result.append(temp_a.data)
                temp_a = temp_a.next
            if temp_b:
                result.append(temp_b.data)
                temp_b = temp_b.next
        return result

    def middle_element(self):
        if self.listSize == 0:
            print("List is empty")
            return -1
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def index_of(self, value):
        temp = self.head
        for i in range(self.listSize):
            if temp.data == value:
                return i
            temp = temp.next
        return -1

    def split_at(self, index):
        if index > self.listSize:
            print("Index out of range")
            return None, None
        first = SinglyLinkedList()
        second = SinglyLinkedList()
        temp = self.head
        for i in range(index):
            first.append(temp.data)
            temp = temp.next
        while temp:
            second.append(temp.data)
            temp = temp.next
        return first, second

    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("null")

# Testing the SinglyLinkedList class
if _name_ == "_main_":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.prepend(0)
    sll.print_list()

    sll.insert_at(2, 10)
    print("After inserting 10 at index 2: ", end="")
    sll.print_list()

    sll.delete_at(2)
    print("After deleting element at index 2: ", end="")
    sll.print_list()

    sll.rotate_right(2)
    print("After rotating right by 2: ", end="")
    sll.print_list()

    sll.reverse()
    print("After reversing: ", end="")
    sll.print_list()

    list1 = SinglyLinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = SinglyLinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    merged_list = SinglyLinkedList.merge(list1, list2)
    print("Merged list: ", end="")
    merged_list.print_list()

    interleaved_list = SinglyLinkedList.interleave(list1, list2)
    print("Interleaved list: ", end="")
    interleaved_list.print_list()

    print(f"Middle element of the list: {sll.middle_element()}")

    print(f"Index of element 3: {sll.index_of(3)}")

    first_half, second_half = sll.split_at(2)
    print("First half: ", end="")
    first_half.print_list()
    print("Second half: ", end="")