first_house = {'red': ['room', 'kitchen', 'bathroom'],
               'blue': ['garage', 'bedroom']}

second_house = {'red': ['living room', 'bathroom'],
                'blue': ['garage', 'bedroom', 'kitchen']}
houses = [first_house, second_house]

# print(houses)


number = 1
for house in houses:
    # print('house items', house.items())
    for colour, rooms in house.items():
        print('Colour', colour)
        print('Rooms', rooms)

# numbers += 1
