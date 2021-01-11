class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
    # adding data element
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
    # printing elements
    def listprint(self, node):
        while node is not None:
            print(node.data)
            node = node.next
    
    # inserting into the list
    def insert(self, prev_node, NewVal):
        # checking first value
        NewNode = Node(NewVal)
        if prev_node is None:
            return 
        # link new node and prev node
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        
    # appending element at the end
    def append(self, NewVal):
        NewNode = Node(NewVal)
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return 


dlist = doubly_linked_list()
dlist.push(8)
dlist.push(10)
dlist.push(12)
dlist.insert(dlist.head.next,62)
dlist.append(50)

dlist.listprint(dlist.head)
