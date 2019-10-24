class QueueClass:
    # Class takes in a list when initialized
    def __init__(self, queue):
        self.queue = queue

    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)            
        else:
            return None

if __name__ == "__main__":    
    a = QueueClass([1,2,3])
    a.push(5)
    a.push(10)
    print("Current Data before pushing is {}".format(a.queue))
    print("Data popped is {}".format(a.pop()))    
    print("Current Data after pushing is {}".format(a.queue))