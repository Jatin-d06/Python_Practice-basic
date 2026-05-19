x = 1
print(x == 1)
print(x == 2)

print(x != 1)
print(x != 2)
x = 4
print(x < 5 and x < 10 )
print(x > 5 or x > 10 )
print(x > 3 or x > 10 )
print(not(x > 3 or x > 10 ))

print()
x = 10 
y = 10.0

print( x is y ) # false cause y is float and x  not 

y = 20 
print(x is not y )