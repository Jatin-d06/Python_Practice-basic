# Write a program to print numbers from 1 to 50 in this pattern
# [1, 2, Fiz, 4, Buzz, Fiz, 7, 8, Fiz, Buzz, 11, Fiz, 13, 14, FizBuzz, 16....50]
count = 0 
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0 :
        print("fizz")
    elif i % 5 == 0 :
        print("buzz")
    else :
        print(i)
        count+=1

print(count)
