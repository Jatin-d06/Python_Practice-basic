var = 2 
print(var) # 2

def return_var():
    global var 
    var = 5 
    return var

print(return_var()) # 5
print(var)