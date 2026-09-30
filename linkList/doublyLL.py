class Node:
    def __init__(self, value =None):
        self.data = value
        self.prev = None
        self.next = None
        
class DoublyLL:
    def __init__(self):
        self.head = None
    
    def InsertAtEnd(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        t = self.head
        while(t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t
        
    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data, end=" ")
            t = t.next
        print(t.data)
        


obj = DoublyLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.printDLL()