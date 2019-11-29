"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = input('What age are you? ')

    def age_status(age):
        age = int(age)
        status = ['child', 'pupil', 'student', 'adult']
        if age < 0:
            raise ValueError('Age could not be less then 0')
        elif age >= 0 and age < 7:
            return status[0]
        elif age >= 7 and age < 18:
            return status[1]
        elif age >= 18 and age < 25:
            return status[2]
        else:
            return status[3]

    status = age_status(age)
    print(status)

if __name__ == "__main__":
    main()
