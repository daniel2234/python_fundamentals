from datetime import datetime


class Cat:
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return "{} eats {} at {}".format(self.name, self.preferred_food, self.meal_time)

    def eats_at(self):
        d = datetime.strptime("{}".format(self.meal_time), "%H")
        self.meal_time = d.strftime("%I:%M %p")

    def meow(self):
        return "My name is {} and I eat {} at {}".format(self.name, self.preferred_food, self.meal_time.lstrip('0'))


felix = Cat('Felix', 'tuna', 15)
tobias = Cat('Tobias', 'sardines', 12)

# print(felix)
print(felix.eats_at())
print(felix.meow())
