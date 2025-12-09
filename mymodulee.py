import sqlite3

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

def delete_movie(kazakh_kino):
    name = input("Жойылатын фильм атауы: ").strip()
    if name in kazakh_kino:
        del kazakh_kino[name]
        print(f"🗑 {name} фильмі жойылды.")
    else:
        print("Ондай фильм табылмады.")

def search_movie(kazakh_kino):
    name = input("Ізделетін фильм атауы: ").strip()
    if name in kazakh_kino:
        print(f"{name}: {kazakh_kino[name]}")
    else:
        print("Ондай фильм табылмады.")

def show_all(kazakh_kino):
    if not kazakh_kino:
        print("База бос.")
        return
    print("\n{ Барлық фильмдер }")
    for name, rating in sorted(kazakh_kino.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {rating}")

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





def init_db():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        rating REAL
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        country_name TEXT,
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        genre TEXT,
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS languages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        lang TEXT,
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )""")
    conn.commit()
    conn.close()

def save_movie_to_db(name, rating, country, genre, lang):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO movies (name, rating) VALUES (?, ?)", (name, rating))
    cur.execute("SELECT id FROM movies WHERE name = ?", (name,))
    movie_id = cur.fetchone()[0]
    cur.execute("INSERT INTO countries (movie_id, country_name) VALUES (?, ?)", (movie_id, country))
    cur.execute("INSERT INTO genres (movie_id, genre) VALUES (?, ?)", (movie_id, genre))
    cur.execute("INSERT INTO languages (movie_id, lang) VALUES (?, ?)", (movie_id, lang))
    conn.commit()
    conn.close()

def show_all_from_db():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()

    print("\nФильмдерді сүзу үшін критерий таңдаңыз:")
    print("1. Ел")
    print("2. Рейтинг")
    print("3. Жанр")
    print("4. Тіл")
    print("5. Барлығы")

    choice = input("Таңдауыңыз: ").strip()

    query = """
    SELECT movies.name, movies.rating, 
           countries.country_name,
           genres.genre,
           languages.lang
    FROM movies
    LEFT JOIN countries ON movies.id = countries.movie_id
    LEFT JOIN genres ON movies.id = genres.movie_id
    LEFT JOIN languages ON movies.id = languages.movie_id
    """
    params = ()

    if choice == "1":
        country = input("Елді енгізіңіз: ").strip()
        query += " WHERE countries.country_name = ?"
        params = (country,)
    elif choice == "2":
        try:
            rating_min = float(input("Мин рейтинг: "))
            rating_max = float(input("Макс рейтинг: "))
            query += " WHERE movies.rating BETWEEN ? AND ?"
            params = (rating_min, rating_max)
        except ValueError:
            print("Рейтинг сан болуы керек!")
            return
    elif choice == "3":
        genre = input("Жанрды енгізіңіз: ").strip()
        query += " WHERE genres.genre = ?"
        params = (genre,)
    elif choice == "4":
        lang = input("Тілді енгізіңіз: ").strip()
        query += " WHERE languages.lang = ?"
        params = (lang,)
    elif choice == "5":
        pass
    else:
        print("Дұрыс таңдау енгізіңіз.")
        return

    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("Фильмдер табылмады.")
    else:
        print("\n{ Фильмдер }")
        for name, rating, country, genre, lang in rows:
            print(f"{name} | {rating} | {country} | {genre} | {lang}")
