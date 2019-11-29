"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def string_comparison(str1, str2):
        s1 = str1
        s2 = str2
        if type(s1) != str or type(s2) != str:
            return 0
        elif s1 == s2:
            return 1
        elif s1 != s2 and len(s1) > len(s2):
            return 2
        elif s1 != s2 and s2 == 'learn':
            return 3
    

    print(string_comparison(100, 'learn'))
    print(string_comparison('learn', 'learn'))
    print(string_comparison('learn python', 'python'))
    print(string_comparison('Igor', 'learn'))
    
if __name__ == "__main__":
    main()
