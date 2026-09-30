class node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next
        
class singliyLL:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = node(value)
        if (self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp   
            
    def insertAtbag(self,value):
        temp = node(value)
        temp.next = self.head
        self.head = temp  
    
    def inserAtMid(self,value,x):
        temp = node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
            
    def deleteLL(self,value):
        t1 = self.head
        pev = t1
        if(t1.data == value):
            self.head = t1.next       
        while(t1.next != None):
            if(t1.data == value):
                pev.next = t1.next
                break
            else:
                pev =t1
                t1 = t1.next

        if(t1.data == value):
            pev.next = None 
            
            
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)
            
obj = singliyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(40)
obj.insertAtEnd(30)
obj.insertAtbag(50)
obj.inserAtMid(20,10)
obj.deleteLL(30)
obj.printLL()
          