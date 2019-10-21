class Node:
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

root = Node(10)
root.left = Node(20)
root.left.left = Node(30)
root.left.right = Node(100)
root.right = Node(80)
root.right.left = Node(201)

def level(root):
    q = []
    if root:
        q.append(root)  
        counter = 0      
        while (len(q)):
            if counter == 0:
                print(q.pop(0).val)
                counter += 1
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            if q:
                root = q.pop(0)
            print(root.val)

           
    return q
level(root)






    

    