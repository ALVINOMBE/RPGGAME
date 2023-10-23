print("Welcome to Home Made RPG")

while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    player_class = input("Enter your class (Mage, Melee, Range): ")
    clasees = str.lower(player_class)

    if name == " ":
        print("Character must contain a name.")
        continue

    if not age.isdigit():
        print("Age must be a number.")
        continue

    if clasees not in ["mage", "melee", "range"] or clasees == "":
        print("Invalid class. Please choose from Mage, Melee, or Range.")
        continue

    break

print("Character creation successful!\n")
print("Weapon")

if clasees == "mage":
    print("Pick a weapon")
    mageweaponchoose = input("Available weapons: (Fire staff, Curse staff, Wind staff): ")

elif clasees == "melee":
    print("Pick a weapon")
    meleeweaponchoose = input("Available weapons: (Sword, Axe, Mace): ")

elif clasees == "range":
    print("Pick a weapon")
    rangeweaponchoose = input("Available weapons: (Bow, Crossbow, Rifle): ")
else:
    print("Invalid class. No weapons available.")




