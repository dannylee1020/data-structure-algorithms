class queue():
    def __init__(self):
        self.queue = []
    # adding to queue
    def addtoq(self, data):
        if data is not None:
            self.queue.insert(0, data)
            return True
        else:
            return False
    def size(self):
        return len(self.queue)

    # remove from queue
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return ('No element in queue')

    
Q = queue()
Q.addtoq('Mon')
Q.addtoq('Tues')
Q.addtoq('Wed')
print(Q.size())
print(Q.remove())
print(Q.remove())