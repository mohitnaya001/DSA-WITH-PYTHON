class Dqueue:
    def __init__(self):
        self.items =[]
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def InserAtBig(self,value):
        self.items.insert(0,value)
    
    def DeleteAtBig(self):
        if(self.isEmpty()):
            print("Queue Is Empty")
        else:
            return self.items.pop(0)
        
    def InserAtEnd(self,value):
        self.items.append(value)
    
    def DeleteAtEnd(self):
        if(self.isEmpty()):
            print("Queue Is Empaty")
        else:
            return self.items.pop()
    
    
dq = Dqueue()
dq.InserAtBig(10)
dq.InserAtBig(20)
dq.InserAtEnd(50)
# print(dq.DeleteAtBig())
dq.InserAtBig(30)
print(dq.DeleteAtBig())