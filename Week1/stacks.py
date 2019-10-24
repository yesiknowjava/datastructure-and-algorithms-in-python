class StackClass:
    # Class takes in a list when initialized
    def __init__(self, stack):
        self.stack = stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()            
        else:
            return None

if __name__ == "__main__":    
    a = StackClass([1,2,3])

    print("Current Data before after pushing is {}".format(a.stack))
    print("Data popped is {}".format(a.pop()))    
    print("Current Data after pushing is {}".format(a.stack))

