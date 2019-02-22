class Person:
    def __init__(self, fname, lname, x=0, y=0):
        self.first_name = fname
        self.last_name = lname
        self.x_position = 0
        self.y_position = 0

    def __str__(self):
        return "Person object:{}".format(self.full_name())

    def introduce(self):
        return "Hello, my name is {}".format(self.first_name)

    def meet(self, other_name):
        return "Hello {}, my name is {}".format(other_name, self.first_name)

    def full_name(self):
        return "{}{}".format(self.first_name, self.last_name)


janelle = Person("Janelle", "Doe")
dora = Person("Dora", "Lora")

print(janelle.first_name)
print(janelle.last_name)


class Recipe:
    def __init__(self, title, description, mins, veg):
        self.title = title
        self.description = description
        self.time_in_minutes = mins
        self.vegetarian = veg
        self.votes = 0


breakfast = Recipe("oatmeal", "a healthy breakfast", 15, True)

print(breakfast.votes)

breakfast.votes += 1

print(breakfast.votes)
