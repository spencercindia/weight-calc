print("Welcome to weight converter!")

weight = input("Please enter your weight: ")

type = input("Enter K for kilograms, or L for Lbs: ")

#type variable call doesn't work... any letter calls first func
if type == "l" or "L":
    weight = (float(weight) / 2.2046)
    print(weight)
elif type == "k" or "K":
    weight = (float(weight) * 2.2046)
    print(weight)
else: print("Sorry, I didn't understand your input :/")
print("Done")
