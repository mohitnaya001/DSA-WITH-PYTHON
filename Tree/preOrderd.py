class Node():
    def __init__(self,value):
        self.right = None
        self.left = None
        self.data = value
        
def PreOrder(root):
    if (root != None):
        print(root.data, end=" ")
        PreOrder(root.left)
        PreOrder(root.right)
def Inorder(root):
    if(root != None):
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)
        
def postOrder(root):
    if(root != None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")
    
root = Node(1)
root.left = Node(3)     
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(6)
print("PreOrder")
PreOrder(root)

print("\nInorder")
Inorder(root)

print("\nPostOrder")
postOrder(root)