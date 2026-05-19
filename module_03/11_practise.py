number = [1,2,3,4,5]
# print(len(number))

# del number[-1]
# print(number)

x = int(input("Enter a number : "))
size = len(number)
mid = size // 2

number[mid] = x

print(number)
