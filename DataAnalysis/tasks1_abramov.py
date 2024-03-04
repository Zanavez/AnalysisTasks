def lecture_task():
    import pandas as pd

    music = [
        ["Каникулы на Марсе", "Дедушка"],
        ["Asper X", "Смерть Луны"],
        ["Bling-Bang-Bang-Born", "Creepy Nuts"],
        ["Guren No Yumiya", "Linked Horizon"],
        ["Bury the Light", "Casey Edwards"]
    ]

    entries = ["artist", "track"]

    playlist = pd.DataFrame(data=music, columns=entries)
    print(playlist)


def task1():
    try:
        welcome_input = input("Добро пожаловать! Введите своё имя для продолжения: ")
        print(f"Привет, {welcome_input}!")
    except Exception:
        print("Возникла ошибка при обработке данных!")


def task2():
    try:
        age = int(input("Введите свой возраст: "))
        if age >= 18:
            print("Доступ разрешён!")
        elif 14 <= age < 18:
            print("Доступ ограничен!")
        elif 0 <= age < 14:
            print("Доступ ограничен!")
        else:
            print("Ошибка! Недопустимый возраст!")
    except Exception:
        print("Ошибка! Проверьте правильность введённых данных!")


def task3():
    text = input("Введите текст: ")
    count = int(input("Введите количество повторений: "))
    print((text + "\n") * count)


def task4():
    text = input("Введите текст: ")
    count = int(input("Введите количество повторений: "))
    i = 0
    while i < count:
        print(text)
        i += 1


def task5():
    def print_fio(name, surname, patronymic):
        print(name[0] + surname[0] + patronymic[0])

    print_fio("Абрамов", "Александр", "Александрович")


def task6():
    import pandas as pd
    data = {'col 1': ['Я', 'Python', 'Буду'],
            'col 2': ['люблю', 'мой', 'стараться'],
            'col 3': ['анализ', 'лучший', 'хорошо'],
            'col 4': ['данных', 'друг', 'учиться']
            }

    df = pd.DataFrame(data)
    print(df)


lecture_task()
print()
task1()
print()
task2()
print()
task3()
print()
task4()
print()
task5()
print()
task6()
