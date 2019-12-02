"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    Journal = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [4,5,4,2,3]},
    {'school_class': '5a', 'scores': [5,3,2,5,4]},
    {'school_class': '5b', 'scores': [2,5,3,5,5]},
    ]

    school_score_sum = 0
    school_score_count = 0

    for school_class in Journal:
        class_score = school_class['scores']
        class_num = school_class['school_class']
        # цикл ниже можно заменить на меньшую конструкцию:
        # class_sum = sum(class_score)
        # class_count = count(class_score)
        # school_score_sum += class_sum
        # school_score_count += class_count
        for score in class_score:
            school_score_sum  += score
            school_score_count += 1
    
        # здесь соответственно с учетом новых переменных получится
        # school_class_score_avg = class_sum/class_count
        school_class_score_avg = sum(class_score) / len(class_score)
        print(f"Cредний балл для класса {class_num}: {school_class_score_avg}")

    school_score_avg = school_score_sum / school_score_count
    print(f"Cредний балл по всей школе {school_score_avg}")

    
if __name__ == "__main__":
    main()
