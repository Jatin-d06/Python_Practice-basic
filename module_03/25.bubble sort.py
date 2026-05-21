my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # this condition store true at the start so that while begans to start then if swap occur it true 
while swapped:
    swapped = False # it make the condition false when iterator iterate through all value and it ends it 
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)