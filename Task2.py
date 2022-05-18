"""
Вам нужно написать функцию get_inductees
Функция get_inductees принимает 3 списка одинаковой длины.
В первом списке (names) — имена студентов, позволяющие их точно идентифицировать.
Во втором (birthday_years) — год рождения.
В третьем (genders) — пол студента.
Функция возвращает список с именами студентов мужского пола,
которые достигли или могут достигнуть 18 лет в 2021 году,
но при этом не старше 30 лет.
Cтуденты, по которым невозможно точно установить должны быть выведены отдельно.
"""
names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names, birthday_years, genders):
    corrupted_candidates = [1]
    suitable_canidates = []
    for k, v in enumerate(names):
        if not birthday_years[k] or not genders[k]:
            corrupted_candidates.append(names[k])
        elif birthday_years[k] >= 1991 and birthday_years[k] < 2004 and genders[k] == "Male":
            suitable_canidates.append(names[k])
    return suitable_canidates, corrupted_candidates


print(get_inductees(names, birthday_years, genders))
