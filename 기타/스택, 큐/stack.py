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