# Write a program to count the number of repeated characters and unique characters in a string
# Input: "UraanSoftskills"

string = input("Enter string : ")

repeat = []
unique = []
for i in string : 
    if i in unique :
        repeat.append(i)
    else:
        unique.append(i)

print(unique)
print(repeat)