# Creating Linked list
class Node:
    def __init__(self, val = None):
        self.val = val
        self.nextval = None
    
class LinkedList:
    def __init__(self):
        self.headval = None

    # for traversing
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.val)
            printval = printval.nextval
    
    # for insertion in the front
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
    # update the new nodes next value to headval
        NewNode.nextval = self.headval
        self.headval = NewNode

    # for insertion at the end
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    # inserting in between
    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print('The middle node is absent')
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # remove node
    def RemoveNode(self, RemoveKey):
        head = self.headval
        while head is not None:
            if head.val == RemoveKey:
                break
            prev = head
            head = head.nextval
        
        prev.nextval = head.nextval
        head = None


# creating linked list
list1 = LinkedList()
list1.headval = Node('Mon')
e2 = Node('Tues')
e3 = Node('Wed')

list1.headval.nextval = e2
e2.nextval = e3

# inserting value 
list1.AtBeginning('Sun')

# insterting value
list1.AtEnd('Thu')
list1.InBetween(list1.headval.nextval, 'Fri')

list1.RemoveNode('Fri')

if __name__ == '__main__':
    list1.listprint()