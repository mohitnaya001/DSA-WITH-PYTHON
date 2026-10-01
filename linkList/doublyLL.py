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
        
    def insertAtBig(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp    
        
    def insertAtMid(self, value, x):
        t = self.head
        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        temp.prev = t
        if(t.next != None):
            t.next.prev = temp
        t.next = temp
       
    def DeleteDLL(self, value):
        if (self.head == None):
            print("DLL is empty")
            return
        t = self.head
        if(self.head.data == value):
            self.head = t.next
            self.head.prev = None
            return
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t =t.next
        if(t.data == value):
            t.prev.next = None                

    
    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data, end=" <--> ")
            t = t.next
        print(t.data)
        


obj = DoublyLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.insertAtMid(50,20)
obj.DeleteDLL(30)
obj.printDLL()