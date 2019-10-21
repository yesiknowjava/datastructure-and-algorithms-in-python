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


def make_array(root, binary_array=[]): 
    if root.left is None: 
        return insert(root.left, node)  
    if root.right is None: 
        return insert(root.right, node) 



binary_tree = Node(50) 
for i in [20, 30, 40, 70, 50, 25, 80]:
    insert(binary_tree,Node(i))

binary_array = make_array(root, [])


       

            
