from array import *

arr =array('i',[10,20,30,40,50])

n = int(input("Enter a Number:")) # user input in array
for i in range(0,n):
    arr.append(int(input("Enter array list Number:")))
    
for x in arr:
    print(x, end=" ")

i = arr.index(50)   #find the index of element 
print("Index is:",i)