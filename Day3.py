#PIZZA PROGRAM
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L: \n-")
total = 0
if(size == "S"):
    total += 15
elif(size == "M"):
    total += 20
elif(size == "L"):
    total += 25
else:
    print("Invalid size")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n-")
if(pepperoni == "Y"):
    total += 2
else:
    total = total

extra_cheese = input("Do you want extra cheese on your pizza? Y or N: \n-")
if(extra_cheese == "Y"):
    total += 1
else:
    total = total

print(f"Your total is ${total}.")