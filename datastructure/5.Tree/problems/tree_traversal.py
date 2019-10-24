class Node:
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

    

    def insert(self, root, node):
        print(node.val) 
        if root is None: 
            root = node 
        else: 
            if root.val < node.val: 
                if root.right is None: 
                    root.right = node 
                else: 
                    self.insert(root.right, node) 
            else: 
                if root.left is None: 
                    root.left = node 
                else: 
                    self.insert(root.left, node)

    def display(self):
            lines, _, _, _ = self._display_aux()
            for line in lines:
                print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def pre_order(self, root):
        if root: 
            print(root.val) 
            self.pre_order(root.left) 
            self.pre_order(root.right)

    def post_order(self, root):
        if root: 
            self.post_order(root.left) 
            self.post_order(root.right)
            print(root.val) 

    def inorder(self, root): 
        if root: 
            self.inorder(root.left) 
            print(root.val) 
            self.inorder(root.right) 

r = Node(50) 
for i in [20, 30, 40, 70, 25, 80]:
    r.insert(r,Node(i))

r.pre_order(r)
r.display()

