# Write a Program to Count Numbers of Digits in this String
# Input: string = "U r a a n S 0 f t s k i l l 1 s 1234"
# Output: Total number of Digits = 6

string = input("Enter string : ")
count = 0
for i in string: 
    if i >= '0'and i <= '9':
        count +=1

print(count)

