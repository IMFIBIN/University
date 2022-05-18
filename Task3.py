"""
Функция find_athlets принимает 3 списка с именами студентов.
В первом списке (know_english) — список тех, кто хорошо владеет английским языком.
Второй (sportsmen) — содержит имена тех, кто увлекается спортом.
Tретий (more_than_20_years) — предоставляет информацию о тех, кто старше 20 лет.
Функция возвращает список имен студентов, которые подходят под все три критерия.
Пример входных данных приведен ниже.
"""

know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


def find_athlets(know_english, sportsmen, more_than_20_years) :
    all_candidates = []
    top_candidates = []
    for i in know_english :
        if i in sportsmen :
            if i in more_than_20_years :
                top_candidates.append(i)
    print(top_candidates)


find_athlets(know_english, sportsmen, more_than_20_years)
