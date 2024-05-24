#reverse in kth gap
def reverse_in_kth_gap(head, k):
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next
    curr = head
    while curr:
        next = curr.next
        curr.next = stack.pop()
        curr = next
        return head   
    
#test

#sort stack
def sort_stack(inputStack):
    sortedStack = []
    while inputStack:
        temp = inputStack.pop()
        while sortedStack and sortedStack[-1] > temp:
            inputStack.append(sortedStack.pop())
        sortedStack.append(temp)

    while sortedStack:
        inputStack.append(sortedStack.pop())

    return inputStack

#test
inputStack = [3, 5, 2, 1, 4]
print(sort_stack(inputStack))