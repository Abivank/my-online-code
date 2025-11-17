def add_movie(kazakh_kino):
    name = input("Фильм атауы: ").strip()
    if not name:
        print("Атау бос болмауы керек.")
        return
    try:
        rating = float(input("Бағасы (0–10): "))
        if 0 <= rating <= 10:
            kazakh_kino[name] = rating
            print(f"{name} фильмі қосылды!")
        else:
            print("Рейтинг 0–10 аралығында болуы керек.")
    except ValueError:
        print("Сан енгізіңіз!")

def show_all(kazakh_kino):
    if not kazakh_kino:
        print("База бос.")
        return
    print("\n{ Барлық фильмдер }")
    for name, rating in sorted(kazakh_kino.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {rating}")

def search_movie(kazakh_kino):
    name = input("Ізделетін фильм атауы: ").strip()
    if name in kazakh_kino:
        print(f"{name}: {kazakh_kino[name]}")
    else:
        print("Ондай фильм табылмады.")

def delete_movie(kazakh_kino):
    name = input("Жойылатын фильм атауы: ").strip()
    if name in kazakh_kino:
        del kazakh_kino[name]
        print(f"🗑 {name} фильмі жойылды.")
    else:
        print("Ондай фильм табылмады.")

def save_to_file(filename, kazakh_kino):
    with open(filename, "w", encoding="utf-8") as f:
        for name, rating in kazakh_kino.items():
            f.write(f"{name};{rating}\n")

def load_from_file(filename):
    kazakh_kino = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                name, rating = line.strip().split(";")
                kazakh_kino[name] = float(rating)
    except FileNotFoundError:
        pass
    return kazakh_kino
class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def info(self):
        return f"{self.name}: {self.rating}"

class AnimatedMovie(Movie):
    def __init__(self, name, rating, studio):
        super().__init__(name, rating)
        self.studio = studio

    def info(self):
        return f"{self.name} ({self.studio}): {self.rating}"

class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def delete_movie(self, db, name):
        if name in db:
            del db[name]
            return True
        return False
