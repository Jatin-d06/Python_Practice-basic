# Write a program to find the count for the occurrence of 's' or 'S' character in a string
# Input: "MindCoders"
# Output: 3

string = input("Enter a string : ")
count = 0


for i in string: 
    if i == "s" or i == "S":
        count += 1
print(count)