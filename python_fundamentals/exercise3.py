print("What is your name?")

user_name = input()

print("Hello, {}".format(user_name))


secret_password = "please"
print("What's the password?")
password_attempt = input()
correct_or_not = (password_attempt == secret_password)
print("That's {}!".format(correct_or_not))
print("How many cookies have been eaten?")
eaten = input()
remaining_cookies = 12 - int(eaten)
print("There are {} cookies left.".format(remaining_cookies))

my_number = 5

if my_number < 4:
    print("Hello")
    print("How are you?")

if my_number > 4:
    print("Hi there")
    print("How are you?")

your_number = input()

if int(your_number) > 5:
    print("This line will run if the user enters a number greater than 5")

print("This line always runs")

x = input()
y = input()

if int(x) > int(y):
    print("x is greater than y!")
elif x < y:
    print("x is less than y!")
else:
    print("x equals y!")
