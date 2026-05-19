# 9. ⁠Write a program to create 2 variables, initialize them with integer values, Print the division of both variables

var_1 = int(input("Enter a number : "))
var_2 = int(input("Enter another number : "))

if var_2 == 0 :
    print('''Error occured "can't divide by zero" ''')
else:
    print(var_1 / var_2)