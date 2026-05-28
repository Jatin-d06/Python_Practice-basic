# dict = {
#     "name" : " ",
#     "score" : ()
# }

school = {}
while True : 
    name = input("Enter name : ")
    if name == "":
        break 
    score = int(input(f"Enter {name}'s score : "))
    if score not in range(1,11):
        break
    if name in school : 
        school[name] += (score, )
    else : 
        school[name] = (score, )
print(school)


for name , score in school.items(): 
    sum = 0 
    for s in score: 
        sum += s 
    print(name,sum)