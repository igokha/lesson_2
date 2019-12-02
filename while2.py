"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
Question_Answer = [
    # формат словаря по условию задания должен быть "Как дела": "Хорошо!", "Что делаешь?": "Программирую"
    # метки "question" и "answer" не нужны
    # в будущем это сильно упросит код функции ask_user_dict()
    # проверку на вхождение вопроса в словарь можно будет сделать условием: if user_question in Question_Answer.keys()
    {"question" : "Как дела?", "answer" : "Хорошо!"},
    {"question" : "Что делаешь?", "answer" : "Программирую"}, 
    {"question" : "Какая погода?", "answer" : "Солнечно"}, 
    {"question" : "Куда уезжаешь?", "answer" : "В США"}
]

def ask_user_dict():
    answer = ''
    while True:
        User_question = input('Введите вопрос: ').capitalize()
        for q in Question_Answer:
            question = q["question"]
            if User_question == question:
                answer = q["answer"]
                print(answer)
                break
               
        if answer == '':
            print("Неверный вопрос")
        else:
            break
    
if __name__ == "__main__":
    ask_user_dict()
