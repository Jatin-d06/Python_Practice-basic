blocks = int(input("ENter no of blocks : "))

height = 0 
layer = 0 

while layer <= blocks : 
    height += 1
    blocks -=1 
    layer += 1

print(f'''
    height : {height}
    blocks : {blocks}
    layer : {layer}
''')