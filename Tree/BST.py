class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
def Insert(root, value):
    if (root == None):
        return Node(value)
    if(root.data == value):
        return root
    if(root.data < value):
        root.right = Insert(root.right, value)
    else:
        root.left = Insert(root.left, value)
    return root
    
def search(root, value):
    if(root == None):
        print("element Not Found", end="\n")
        return
    if(root.data == value):
        print("Element Found ")
        return
    if(root.data < value):
        search(root.right, value)
    else:
        search(root.left, value)
     
def Inorder(root):
    if(root != None):
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)   

            
root = Insert(None,20)
root = Insert(root,15)
root = Insert(root,26)
root = Insert(root,5)
root = Insert(root,10)
root = Insert(root,30)

Inorder(root)
print("\n")
search(root, 5)
search(root, 100)