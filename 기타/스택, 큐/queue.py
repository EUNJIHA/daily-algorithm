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