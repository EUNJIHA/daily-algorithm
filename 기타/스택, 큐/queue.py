class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        value = None
        
        if self.isEmpty():
            print("Queue is Empty")
        else:
            # return self.queue.pop(0)
            value = self.queue[0]
            self.queue = self.queue[1:]
        
        return value
    
    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue():
    def __init__(self): # FIXME: 이 부분이 다름
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        value = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            value = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None

        return value


