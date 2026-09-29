from numpy import *

val = array([10,20,30,40,50])

val = linspace(10,20,6) # creating array by using linspace (10(starting array: 20(last value array): 6(partision on array)))

val= arange(10,30,2)  # creating array by using arange (10(starting array: 20 last value in array: 2(this is diffrence is array))

for x in val:
    print(x, end=" ")

two = array([[10,20,40],[40,50,60]])
print(two)

print("\n")

three = array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three)