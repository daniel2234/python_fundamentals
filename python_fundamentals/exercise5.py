distance = 0
energy = 0

while distance < 20:
    if energy < 0:
        print("You can not run!")
        print("You must rest and eat")
    print("Would you like to walk or run?")
    input_change = input()
    if input_change == 'walk':
        distance += 1
        energy += 1
        print("Distance from home is {}km".format(distance))
    elif input_change == 'run':
        distance += 5
        energy -= 1
        print("Distance from home is {}km".format(distance))
    elif input_change == 'go home':
        break
    else:
        print("Anything else that, you gain no distance.")
