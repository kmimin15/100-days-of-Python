#randomization and importing modules
import random
# import Day4Help # you can add your own modules within the same location
# print(Day4Help.myFavoriteNumber) #extracted from the module

# random_integer = random.randint(1,10) #gives you all the integers between those nombers incluiding their limits
# print(random_integer)

#random number 0 to 1
# random_number_0to1 = random.random()
# print(random_number_0to1)

#random number including limits with floats
# random_float = random.uniform(1, 10)
# print(random_float)

#HEADS OF TAILS
# option = random.randint(1,10)
# if(option <= 5):
#     print("Heads")
# else:
#     print("Tails")

#Lists go from 0 (first item) and so on.
statesOfAmerica = ["Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
    ]

# print(statesOfAmerica[0])
# print(statesOfAmerica[4])
# print(statesOfAmerica[9])
# print(statesOfAmerica[24])
# print(statesOfAmerica[49])
# print(statesOfAmerica[-1]) # last
# print(statesOfAmerica[-2]) # before the last

# statesOfAmerica.extend(["Angelaland, Kevinland"]) #extend the list later
# # print(f"{statesOfAmerica} \n")

# #choose a random item from a list
# print("Your random choise is : " + random.choice(statesOfAmerica)) #option 1
# stateRam = random.randint(0,len(statesOfAmerica)-1) #create the upper bound len(statesOfAmerica)-1, it has a minus because it counts from 1... lists begin with 0
# print(f"Your random choise is : {statesOfAmerica[stateRam]}")


#list within lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Blackberries"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]