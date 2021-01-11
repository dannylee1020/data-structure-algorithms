class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
        
    def insert(self, new_data):
        if self.data:
            if new_data < self.data:
                if self.left is None:
                    self.left = Node(new_data)
                else:
                    self.left.insert(new_data)
            elif new_data > self.data:
                if self.right is None:
                    self.right = Node(new_data)
                else:
                    self.right.insert(new_data)
        else:
            self.data = new_data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
    
    def findval(self, sval):
        if sval < self.data:
            if self.left is None:
                 print(f"{str(sval)} Not Found")
            else:
                self.left.findval(sval)
        elif sval > self.data:
            if self.right is None:
                print(f"{str(sval)} Not Found")
            else:
                self.right.findval(sval)
        else:
            print(f"{sval} is found")



root = Node(10)
root.insert(5)
root.insert(4)
root.insert(12)
root.insert(15)
root.print_tree()

root.findval(5)
root.findval(15)
root.findval(20)
root.findval(7)