
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
       
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, val):
        n = Node(val)
        if(self.head == None):
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
            
    def pop(self):
        if(self.head == None):
            raise Exception("Empty List")
        elif(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            item = self.tail.val
            self.tail = self.tail.prev
            
        return item

    def popleft(self):
        if(self.head == None):
            raise Exception("Empty List")
        elif(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            item = self.head.val
            self.head = self.head.next
            
        return item

    def insert_at_start(self, val):
        n = Node(val)
        if(self.head == None):
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        
            
        
            
            