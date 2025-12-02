#print function, to show something in the console
#print("Hello World")
#print("Hello" + " this is " + 'Kevin \n')

#input function, to have data entry to the console
#input("What's your name \n-")

#Execute a question, and then prints the answer with the print statment and the strings you've placed to introduce the answer
#print('Hello, I am ' + input('Whats is your name and how old are you? \n-') + ' years old \n')

#variables
#name = input('What is your name? \n-')
#print('Hello ' + name + ' nice to meet you.')

#len() gives you the number of chacacters in interger, to change it into string use the function str()
#print('Your name has ' + str(len(name)) + ' characters\n')

#username = input('What is your name \n-')
#length = 'Your name has ' + str(len(username)) + ' characters'
#print(length)


#BAND NAME GENERATOR
print('Welcome to the Bnad Name Generator.')
city = input('What is the name of the city you grew up in? \n- ')
pet = input("What's your pet name? \n- ")
bandname = city + " " + pet
print('Your band name could be ' + bandname)
