class House:
    house = []

    @classmethod
    def total_square_feet(cls):
        total = 0
        for room in cls.house:
            total += room.square_feet()
        total = sum(total)
        return total


class Room:
    pass

    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length

    def square_feet(self):
        return self.width * self.length


kitchen = Room('kitchen', 10, 15)
bathroom = Room('kitchen', 10, 15)
closet = Room('kitchen', 10, 15)


House.house.append(kitchen)
House.house.append(bathroom)
House.house.append(closet)
