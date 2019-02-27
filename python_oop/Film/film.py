class Film:
    library = []
    next_id = 1

    def __init__(self, title, genre, rating):
        """Initiated title, genre, rating, and id that increase everytime a new film is added"""
        self.title = title
        self.genre = genre
        self.rating = rating
        self.id = Film.next_id
        Film.next_id += 1

    def __str__(self):
        return "Object ID: {}, Title: {}, Genre: {}, Rating: {}".format(self.id, self.title, self.genre, self.rating)

    @classmethod
    def create(self, title, genre, rating):
        film = Film(title, genre, rating)
        self.library.append(film)
        return film

    @classmethod
    def all(self):
        return self.library

    @classmethod
    def find(self, id):
        for film in self.library:
            if film.id == id:
                return film
        return None

    @classmethod
    def find_by(self, attr, val):
        for film in self.library:
            if attr == 'title':
                if film.title == val:
                    return film
            elif attr == 'genre':
                if film.genre == val:
                    return film
            elif attr == 'rating':
                if film.rating == val:
                    return film
        return None

    @classmethod
    def delete_all(self):
        self.library = []
        return self.library

    def delete(self):
        self.library.remove(self)
        return self

    def update(self, attr, val):
        if attr == 'title':
            self.title = val
        elif attr == 'genre':
            self.genre = val
        elif attr == 'rating':
            self.rating = val

        return val


book_one = Film.create('IT', 'Horror', 4)
book_two = Film.create('Modern Romance', 'Comedy', 5)
book_three = Film.create('Javascript: The Hard Parts', 'Programming', 5)
print(book_one)
print(book_two)
print(book_three)
print(Film.all())
print(Film.find(1))
print(Film.find_by('title', 'Modern Romance'))
# print(Film.delete_all())
print(Film.all())
# print(Film.delete(book_one))
print(Film.update(book_one, 'title', 'Modern Roance'))
print(book_one)
