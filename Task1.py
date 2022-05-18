"""
У каждого кандидата есть результаты сданных экзаменов по математике, русскому и информатике.
Соответственно, у каждого потенциального студента есть сумма баллов по этим экзаменам.
Также есть дополнительные (extra_scores) баллы: за волонтерство, участие в олимпиадах и другие активности.
Вам нужно отобрать 5 человек, у которых суммарный балл выше, чем у других.
В случае, если не получается однозначно определить 5 человек
(например, 2 человека набрали одинаковое СУММАРНОЕ количество баллов и претендуют на 5 место в списке,
стоит их ранжировать по "профильным" дисциплинам - "информатике" и "математике").
"""

candidates = [
    {"name" : "Vasya", "scores" : {"math" : 58, "russian_language" : 62, "computer_science" : 95}, "extra_scores" : 0},
    {"name" : "Fedya", "scores" : {"math" : 33, "russian_language" : 85, "computer_science" : 71}, "extra_scores" : 2},
    {"name" : "Petya", "scores" : {"math" : 92, "russian_language" : 33, "computer_science" : 82}, "extra_scores" : 1},
    {"name" : "Gosha", "scores" : {"math" : 48, "russian_language" : 50, "computer_science" : 68}, "extra_scores" : 0},
    {"name" : "Masha", "scores" : {"math" : 98, "russian_language" : 48, "computer_science" : 92}, "extra_scores" : 3},
    {"name" : "Maxim", "scores" : {"math" : 84, "russian_language" : 75, "computer_science" : 61}, "extra_scores" : 0},
]


def sum_balls(student) :
    return student['scores']['math'] + student['scores']['russian_language'] + student['scores']['computer_science'] + \
           student['extra_scores']


def main(candidates) :
    for k, v in enumerate(candidates) :
        candidates[k]['sum'] = sum_balls(v)
    candidates = sorted(candidates, key=lambda x : x['sum'], reverse=True)
    for i in candidates :
        print(i)


if __name__ == '__main__' :
    main(candidates)
