dict = { 
    "cat" : "chat",
    "dog" : "chein",
    "horse" : "cheval"
}

words = ["cat","lion","horse"]

for word in words : 
    if word in dict: 
        print(f"{word} -> {dict[word]}")
    else: 
        print(f"----- {word} is not in dictionary -----")