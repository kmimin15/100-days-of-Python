#print specific caracters
# abc = 'abcdefghijklmnopqrstuvwxyz'
# print(abc[7] + abc[14] + abc[11] + abc[0])

#change integer to string, function len() accepts only string charcters
# num = len(str(12345))
# print(num)

#type analyzes the data type inside
# print(type(1234))
# print(type(3.1415))
# print(type(True))
# print(type("are you crazy"))

#bmi calculator
# height = 1.64
# weight = 94
# bmi = weight / (height ** 2)
# print(bmi)
# print(int(bmi))
# print(round(bmi))
# print(round(bmi, 2)) #normally used with money

#fstring
# score = 0
# height = 1.8
# is_winning = True
# print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")


#TIP CALCULATOR
print("Welcome to the tip calculator!")
total = float(input("What was the total of the bill? \n-$"))
tipPercent = int(input("How much tip would you like to give? 10, 12 or 15? \n-"))
people = int(input("How many people to split the bill? \n-"))
amount = (total + (total * (tipPercent/100))) / people
print(f"For a total of ${total} and a tip of {tipPercent}% divided by {people}, each must pay ${round(amount,2)}")
