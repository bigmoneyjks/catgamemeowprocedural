from images import *

cat_attributes = {
    "intelligence": 3,
    "energy": 20,
    "weight": 4,
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name of cat: ")
colour = input("Enter the colour of your cat: ")

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Feed cat 4. Make them sleep 5. Show stats: ")

    if option == '1' and cat_attributes["energy"] >= 3:
        print("Your cat decices to sprint around the room")
        cat_attributes["energy"] -= 3
        cat_attributes["weight"] -= 0.2
    elif option == '2' and cat_attributes["energy"] >= 7:
        print("Your cat reads a novel whilst lifting a dumbell")
        cat_attributes["energy"] -= 7
        cat_attributes["weight"] += 0.3
        cat_attributes["intelligence"] += 0.3
    elif option == "3":
        print("Your cat eats a 3 course exotic meal")
        cat_attributes["energy"] += 4
        cat_attributes["weight"] += 0.1
    elif option == "4":
        print("Your cat curls up and snores loudly")
        cat_attributes["energy"] += 10
    elif option == "5":
        print(cat_attributes)

# 
    if cat_attributes['energy'] <= 0:
        print("Your cat has passed out since they were so tired")
        sleeping()
        cat_attributes["energy"] = 15
    elif cat_attributes["weight"] >= 8:
        print("Your cat has died from being too fat")
        grave()
        break
    elif cat_attributes["weight"] <= 1:
        print("Your cat as died from being too malnourished")
        grave()
        break
    