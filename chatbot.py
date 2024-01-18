

print('Hi! I am the Gibson Chat Bot, GCB for short!')
print('I\'ve been on scratch for 3½ years now! I am trying Python.')
name = input('But anyways, what is your name? ')  # asking name
print('Hi there!', name, 'What a good name!')  # Good Name
import time
time.sleep(3)  # Sleep for 3 seconds
print('Ahem...')  # uhhh
year = input('What the heck?? What year is it??? ')
print('I think so..')
time.sleep(3)  # Sleep for 3 seconds
myage = input('Guess my age.. - enter a number: ')
print('Oh my, you\'re right!!!..')
myage = int(myage)
nyears = 18 - myage
print('I will be 18 in', nyears, 'years')
print('That will be the year', int(year) + nyears)
time.sleep(3)
# Adding Turtle Graphics
import turtle

# Create a turtle screen
window = turtle.Screen()
window.title("Turtle Circle")

# Create a turtle object
circle_turtle = turtle.Turtle()

# Draw a circle
circle_turtle.circle(100)

# Close the turtle graphics window after 5 seconds
time.sleep(3)
window.bye()

# Continue with the chat
print("A circle I drew!")
time.sleep(3)
print("Food Talk!")
time.sleep(3)
print("I love birthday cake!")
food = input ('How about you?  What food you love? ')
print('I love ', food, 'too!')
question = 'How much do you LOVE' + food + '?'
lovemeter = input(question)
print('Its it a good food, I hope that is good for your health.')
animal = input('My most loved amimal is a cat. What is yours: ')
print(animal,  'I dont love them ugh!');
print('I wonder if a', animal , 'loves to eat' , food, '?')

time.sleep(3)
print("End of Food Talk!")
time.sleep(3)

feeling = input('How are you feeling today? ')
print('Why are you feeling', feeling ,'now?')
reason = input("Tell me why?: ")
print('I know!')
print('It been a long day...')
print('Uggh')
print('I am sooo tired!')
print('Goodbye', name ,'I liked talking with you! *shuts off*')
