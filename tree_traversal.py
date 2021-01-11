# implementing different types of tree traversal algorithms

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    # insert Node
    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
            else:
                self.val = val
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()


    # inorder traversal
    # left -> root -> right
    def in_order_traversal(self, root):
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.val)
            res = res + self.in_order_traversal(root.right)
        return res
    
    # pre_order traversal
    # root -> left -> right
    def pre_order_traversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
        return res
    
    # post_order traversal
    # left -> right -> root
    def post_order_traversal(self, root):
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.val)
        return res




root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# print(root.print_tree())
print(root.in_order_traversal(root))
print(root.pre_order_traversal(root))
print(root.post_order_traversal(root))
