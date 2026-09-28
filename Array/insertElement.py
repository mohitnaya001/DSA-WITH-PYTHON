from array import *

val = array('i',[10,20,30,40,50]) #print normal staring list 
for i in range(0,len(val)):
    print(val[i], end=" ")

print("\nInsert and append values") 
val.insert(1,60)        #for insert element in array (1,60) 1 is the index 60 is element of array
val.append(100)         #append add array on last index  

for i in range(0,len(val)):
    print(val[i],end=" ")
    
print("\nReplace in array index[2]")

val[3]=500              #replace the value of index in array. [3] of index is array and 500 element of array


for i in range(0,len(val)): #printthe value of change index 
    print(val[i],end=" ") 
    

    
print("\ncopy array")
copyArry =array(val.typecode,(x*2 for x in val)) # this is copy array program 
for i in range(0,len(copyArry)):
    print(copyArry[i], end=" ")
    

print('\n')
copyArry.pop(3)                     #pop is use for remove index array


copyArry.remove(120)                #remove use for remove element i array
for i in range(0,len(copyArry)):
    print(copyArry[i], end=" ")
    
print("\nSlicing Concept in array")
abc = val[::-1]                     #revers string using slicing concept
abc = val[1:4]                      #array slicing 
abc = val[1:-2]                             
for i in range(0, len(abc)):
    print(abc[i], end=" ")


