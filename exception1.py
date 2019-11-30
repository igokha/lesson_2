"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
# исправить соответственно задаче while2
Question_Answer = [
    {"question" : "Как дела?", "answer" : "Хорошо!"},
    {"question" : "Что делаешь?", "answer" : "Программирую"}, 
    {"question" : "Какая погода?", "answer" : "Солнечно"}, 
    {"question" : "Куда уезжаешь?", "answer" : "В США"}
]

def ask_user_dict():
        answer = ''
        while True:
            try:
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
            except KeyboardInterrupt:
                print('\n'"Пока!")
                break
            
if __name__ == "__main__":
    ask_user_dict()