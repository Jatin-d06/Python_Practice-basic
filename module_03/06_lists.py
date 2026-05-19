# numbers = [1,2,3,4,5]

# print(numbers)
# print(type(numbers))



number = [1,2,3,4,5]

print(f"first element :{number[0]} ")
print(f"second element :{number[1]} ")
print(f"third element :{number[2]} ")
print(f"four element :{number[3]} ")
print(f"five element :{number[4]} ")
print()
number[3]  = 999
print(f"first element :{number[0]} ")
print(f"second element :{number[1]} ")
print(f"third element :{number[2]} ")
print(f"four element :{number[3]} ")
print(f"five element :{number[4]} ")


number[4] = number[3]
print(number)