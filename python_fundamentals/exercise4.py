print('Enter a new number')
enter_number = int(input())

if enter_number < 100:
    print("That's a big number")
elif enter_number > 100:
    print("hwy not dream a little bigger")

print('Enter your age')
enter_age = int(input())

print("{}".format(29 - enter_age))
if(enter_age > 105):
    print("I'm not sure I believe you")

# 3 Save your name as a string into a variable, then ask the user to enter their name. If the two names match, print "We have the same name!".
same_name = 'daniel'
print('Enter your name')
name = input()

if name == same_name:
    print("We have the same name!")


# 4 Pick a number and save it in a variable called secret_number. Ask the user to enter a number. If they enter the secret number, print "You win!". If they are off by 1, print "So close!". Otherwise, print "Try again".
