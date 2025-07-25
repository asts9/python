names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
namesWith_O = [item for item in names if len(item) >5]
print(namesWith_O)
namesWith_O = [item for item in names if "o" in item and len(item)>6]
