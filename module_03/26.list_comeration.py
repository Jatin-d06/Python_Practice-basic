# 21-05-2026
# 20 and 18 absent

# list comperihension 
'''
 syntax 
[ expression for item in iterable ]
 
 '''

row = []
for i in range(8):
    row.append("white_pawn")
print(row)


list = ["WHITE_PAWN" for i in range(8)]
print(list)
print()

square = [x**2 for x in range(10)]
print(square)
print()

two = [2**index for index in range(8)]
print(two)
print()

odd= [x for x in square if x % 2 != 0]
print(odd)
print()


list= [int(input("Enter elements : "))for i in range(int(input("enter int : ")))]
print(list)




