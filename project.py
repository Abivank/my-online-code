from mymodolee import add_movie, delete_movie, search_movie, show_all, save_to_file, load_from_file

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

while True:
    print("\n{ Фильмдер рейтингі жүйесі }")
    print("1. Фильм қосу")
    print("2. Фильмдерді көру")
    print("3. Фильм іздеу")
    print("4. Фильм жою")
    print("5. Сақтау және шығу")

    choice = input("Таңдауыңыз: ")

    if choice == "1":
        add_movie(kazakh_kino)
    elif choice == "2":
        show_all(kazakh_kino)
    elif choice == "3":
        search_movie(kazakh_kino)
    elif choice == "4":
        delete_movie(kazakh_kino)
    elif choice == "5":
        save_to_file("kazakh_kino.txt", kazakh_kino)
        print("Мәліметтер сақталды. Бағдарлама аяқталды.")
        break
    else:
        print(" Дұрыс таңдау енгізіңіз.")
