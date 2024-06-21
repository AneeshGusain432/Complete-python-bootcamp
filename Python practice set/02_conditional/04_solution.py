Bananacolor = "yellow"

if "green" in Bananacolor:
    print("Banana is unripe")
elif "yellow" in Bananacolor:
    print("Banana is ripe")
elif "brown" in Bananacolor:
    print("Banana is over ripe")

print()


# another solution

Fruit = "Banana"
Color = "Yellow"

if Fruit == "Banana":
    if Color == "Green":
        print("Unripe")
    if Color == "Yellow":
        print("Ripe")
    if Color == "Brown":
        print("OverRipe")
