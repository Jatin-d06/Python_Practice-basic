dict = { 
    "cat" : "chat",
    "dog" : "chein",
    "horse" : "cheval"
}
print(dict)
print()

dict2 = dict.copy()
print(dict2)
print()

dict["cat"] = "lock"
print(dict)
print()


dict["camel"] = "badal"
print(dict)
print()

del dict ["cat"]
print(dict)
print()

dict.popitem()
print(dict)


del dict["dog"]
print(dict)
print(len(dict))

dict.clear()
print(len(dict))
print(dict)

# del dict
# print(len(dict))
# print(dict)



