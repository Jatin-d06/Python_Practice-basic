# 7. ⁠Write a program to create 2 variables, initialize them with integer values, Print the difference of both variables

var_1 = int(input("Enter a number : "))
var_2 = int(input("Enter another number : "))

if var_1 > var_2 :
    result = var_1 - var_2 
elif var_2 > var_1:
    result = var_2 - var_1
else : 
    result = 0

print(result)