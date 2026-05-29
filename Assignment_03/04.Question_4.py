# Write a Program to Count Numbers of Digits in this String
# Input: string = "MindCoders password2 is : 1234"
# Output: Total number of Digits = 5
string = input("Enter string : ")
count = 0
for i in string: 
    if i >= '0'and i <= '9':
        count +=1

print(count)

