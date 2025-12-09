from mymodolee import *
import numpy as np
import matplotlib.pyplot as plt

kazakh_kino = {
    "Байдың баласы": 8.5,
    "Бизнес по-казахски": 7.8,
    "Қыз Жібек": 9.2,
    "Анаға апарар жол": 8.0,
    "Тақиялы періште": 7.5,
    "Жаужүрек мың бала": 8.7,
    "Көшпенділер": 8.3,
    "Біздің ауылдың қызы": 7.9,
    "Бекзат": 8.6,
    "Райхан": 8.1
}

kazakh_kino.update(load_from_file("kazakh_kino.txt"))

def show_graph():
    names = list(kazakh_kino.keys())
    ratings = np.array(list(kazakh_kino.values()))
    plt.figure(figsize=(10,5))
    plt.plot(names, ratings, marker='o', color='blue')
    plt.title("Қазақ фильмдерінің рейтингтері")
    plt.xlabel("Фильм атауы")
    plt.ylabel("Рейтинг")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

init_db()

while True:
    print("\n{ Фильмдер рейтингі жүйесі }")
    print("1. Фильм қосу")
    print("2. Фильмдерді көру")
    print("3. Фильм іздеу")
    print("4. Фильм жою")
    print("5. График көрсету")
    print("6. Сақтау және шығу")

    choice = input("Таңдауыңыз: ")

    if choice == "1":
        add_movie(kazakh_kino)
        name = input("Фильм атауы : ")
        rating = float(input("Рейтинг: "))
        country = input("Ел: ")
        genre = input("Жанр: ")
        lang = input("Қай тілде көрсетіледі: ")
        save_movie_to_db(name, rating, country, genre, lang)

    elif choice == "2":
        show_all_from_db()  # <-- енді сүзгілеу қосылды

    elif choice == "3":
        search_movie(kazakh_kino)
    elif choice == "4":
        delete_movie(kazakh_kino)
    elif choice == "5":
        show_graph()
    elif choice == "6":
        save_to_file("kazakh_kino.txt", kazakh_kino)
        print("Мәліметтер сақталды. Бағдарлама аяқталды.")
        break
    else:
        print("Дұрыс таңдау енгізіңіз.")
