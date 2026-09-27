from array import *

val = array('i',[10,20,30,40,50])
for i in range(0,len(val)):
    print(val[i], end=" ")

print("\nInsert and append values")
val.insert(1,60)
val.append(100)

for i in range(0,len(val)):
    print(val[i],end=" ")
    
print("\nReplace in array index[2]")
val[3]=500
for i in range(0,len(val)):
    print(val[i],end=" ")