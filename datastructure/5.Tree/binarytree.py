class Node:
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)


# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 

r = Node(50) 
for i in [20, 30, 40, 70, 50, 25, 80]:
    insert(r,Node(i)) 

inorder(r)
 
       

            
