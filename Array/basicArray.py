from array import *


val = array('i',[1,2,3,4,5,6,7,8,9]) #print simple array 
for i in range (0,len(val)):
    print(val[i], end=" ")
    


for x in val:     #print array  self loop
    print(x, end=" , ")

print("\n")

print(val.typecode) #print typecode in python
print("\n")
val.reverse() # this is methord of revers string function 

for i in range(0,len(val)):  #print revers array 
    print(val[i], end=" , ")