dict = { 
    "cat" : "chat",
    "dog" : "chein",
    "horse" : "cheval"
}
dict = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for key, value in dict.items():
    print(f"{key} -> {value}")

print(dict.items())
print(dict.values())
print(dict.keys())

dict2 = dict.copy()
print(dict2)