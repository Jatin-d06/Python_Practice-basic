def my_fun(my_list_1):
    print(f"print #1{my_list_1} ")
    print(f"print #2{my_list_2} ")
    # my_list_1 = [0,1]
    del my_list_1[0] 
    print(f"print #1{my_list_1} ")
    print(f"print #2{my_list_2} ")

my_list_2 = [2,3]
my_fun(my_list_2)
print(f"print #2{my_list_2} ")