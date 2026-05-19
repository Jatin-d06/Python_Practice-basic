#  break continue 

for i in range(10):
    if(i==5):
        break
    print(i)
print()
for i in range(10):
    if(i==7):
        continue
    print(i)
print()
''' error here '''
for i in range(10):
    if i>3 and i<7:
        break
        
        