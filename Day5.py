# #loops in lists
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:    #fruit is the single item on the list
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

#student scores
# students_scores = [87, 73, 95, 62, 100, 54, 89, 77, 81, 93, 68, 74, 59, 90, 85, 71, 66, 98, 80, 52]
# total_exam_score = sum(students_scores)
# print(f"1 = {total_exam_score}")
# total_exam_score = 0
# for score in students_scores:
#     total_exam_score += score
# print(f"2 = {total_exam_score}")

#student scores - finding the biggest grade
# students_scores = [87, 73, 95, 62, 100, 54, 89, 77, 81, 93, 68, 74, 59, 90, 85, 71, 66, 98, 80, 52]
# preScore = 0
# maxScore = 0
# for score in students_scores:
#     if(score >= maxScore):
#         maxScore = score
#         preScore = score
#     else:
#         preScore = score
# print(maxScore)
# print(max(students_scores))

#gauss problem
# maxNum = 0
# for num in range(1, 101):
#     maxNum += num
# print(maxNum)

#fizzbuzz code!
# for num in range(1,101):
#     if((num % 3) == 0 and (num % 5) == 0):
#         print('FizzBuzz')
#     elif((num % 3) == 0):
#         print('Fizz')
#     elif((num % 5) == 0):
#         print('Buzz')
#     else:
#         print(num)

#PASSWORD GENERATOR
import random

abc = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+"]

print("Welcome to the PyPassword Generator!")
password_list = []

charNumLet = int(input("How many letters would you like in your password?\n-"))
saveLetter = ""
for times in range(0,charNumLet): #aqui si es obligatorio pq el upper boundary no exclusivo
    saveLetter = abc[random.randint(0,len(abc)-1)] #a pesar de que el randint sea incluse en inicio y finalcomo uso un array es mejor usar de 0 a -1
    password_list.append(saveLetter)
# print(saveLetter)

charNumSym = int(input("How many symbols would you like?\n-"))
saveSymbol = ""
for times in range(0,charNumSym): #aqui si es obligatorio pq el upper boundary no exclusivo
    saveSymbol = symbols[random.randint(0,len(symbols)-1)]
    password_list.append(saveSymbol)
# print(saveSymbol)

charNumSNum = int(input("How many numbers would you like?\n-"))
saveNum = ""
for times in range(0,charNumSNum): #aqui si es obligatorio pq el upper boundary no exclusivo
    saveNum = numbers[random.randint(0,len(numbers)-1)]
    password_list.append(saveNum)
# print(saveNum)

print(password_list)

random.shuffle(password_list)
password = "".join(password_list)

print(f"Your password is: {password}")