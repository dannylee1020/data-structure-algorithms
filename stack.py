class stack():
    def __init__(self):
        self.stack = []
    # Push into stack
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]

    # Pop from stack
    def remove(self):
        if len(self.stack) <= 0:
            return ('No element in stack')
        else:
            return self.stack.pop()


Astack = stack()
Astack.add('Mon')
Astack.add('Tues')
Astack.add('Wed')
# print(Astack.peek())
Astack.add('Thu')
Astack.add('Fri')
# print(Astack.peek())
print(Astack.remove())
print(Astack.remove())



# if __name__ == '__main__':
