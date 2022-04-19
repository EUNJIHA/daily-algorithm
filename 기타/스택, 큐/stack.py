class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        value = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            value = self.stack.pop()
        
        return value

    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True
    
    def peek(self):
        value = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            value = self.stack[-1]
        
        return value


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        value = None

        if self.isEmpty():
            print("Stack is Empty")
        else:
            value = self.head.data
            self.head = self.head.next
        
        return value

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def peek(self):
        value = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            value = self.head.data
        return value
