import json



with open("harcosok.json", "r") as file:
    data = json.load(file)
    
    
print(data["harcosok"][1])
