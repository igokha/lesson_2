"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
# исправить соответственно задаче while2
Question_Answer = {
    "Как дела?" : "Хорошо!",
    "Что делаешь?" : "Программирую", 
    "Какая погода?" : "Солнечно", 
    "Куда уезжаешь?" : "В США"
}

def ask_user_dict():
        while True:
            try:
                User_question = input('Введите вопрос: ').capitalize()
                if User_question in Question_Answer.keys():
                    answer = Question_Answer.get(User_question)
                    print(answer)
                    break
                else:
                    print("Неверный вопрос")
            except KeyboardInterrupt:
                print('\n'"Пока!")
                break
            
if __name__ == "__main__":
    ask_user_dict()