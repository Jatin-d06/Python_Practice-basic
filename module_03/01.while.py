# loops, strt with while loop 
largest_number = -99999999

number = int(input("Enter a number or type -1 to stop: "))

while number != -1:
    if number > largest_number :
        largest_number = number 
    number = int(input("Enter a number type -1 to stop: "))

print(f"The largest number is {largest_number}") 