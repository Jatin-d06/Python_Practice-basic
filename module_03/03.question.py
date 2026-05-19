'''Write a program that reads a sequence of numbers and counts how many 
numbers are even and how many are odd. The program terminates when zero is 
entered.'''

while True:
    x = int(input("Enter input : "))
    count = 0
    even = 0
    odd = 0 

    while count < x:
        if x == 0 :
            break
        elif count % 2 == 0 :
            even += 1 
        else:
            odd += 1 
        count+=1

    print(f"The total count is : {count}")
    print(f"The total even is : {even}")
    print(f"The total odds is : {odd}")
    print()