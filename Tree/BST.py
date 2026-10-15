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
        
def get_successor(root):
    root = root.right
    while( root != None and root.left != None ):
        root = root.left
    return root
    

def delete(root,value):
    if(root == None):
        return root
    if(root.data > value):
        root.left = delete(root.left, value)
    elif(root.data < value):
        root.right = delete(root.right, value)
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right,succ.data)
    return root
     
def Inorder(root):
    if(root != None):
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)   

            
root = Insert(None,20)
root = Insert(root,15)
root = Insert(root,30)
root = Insert(root,40)
root = Insert(root,12)
root = Insert(root,18)
root = Insert(root,25)
root = Insert(root,50)

Inorder(root)
print("\n")
# search(root, 5)
# search(root, 100)
delete(root,30)
print("\n")
Inorder(root)
