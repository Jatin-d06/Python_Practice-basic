# #  weather 

# temps = [[0.0 for h in range(24) ] for d in range(31)]
# for element in temps: 
#     print(element)
# print()
# print()
# print()
# print()
# print()
# temp1 = 30
# temp2 = 32
# count = 0

# for days in temps : 
#     if count == 0 : 
#         days[11] = temp1
#         count = 1
#     else: 
#         days[11] = temp2 
#         count = 0


# total = 0 
# average = 0

# for day in temps : # taking a perticular day
#     total += day[11]
# average = total/31

# for day in temps :
#     print([day])

# print(average)
# print(total)


# highest = 0 

# for day in temps :
#     for temp in day: 
#         if temp > highest:
#             highest = temp 

# print(highest)

# hot_days = 0 
# for day in temps : 
#     if day[11] == 32:
#         hot_days += 1

# print(hot_days)


# x as rooms 
# z as floor 
# y as  building

rooms = [[[False for x in range(3)]for z in range(2)]for y in range(4)]
for room in rooms:
    print(room)

vac =  0 
for vac in range(3):
    if not rooms[1][1][vac]:
        vac +=1

print(vac)