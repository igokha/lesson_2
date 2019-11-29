"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

Planets = ['Mars', 'Jupiter', 'Saturn', 'Uranus']

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
def planet_state(bot, update):
    user_text = update.message.text.split()
    if user_text[1].capitalize() == Planets[0]:
        planet = ephem.Mars()
        pl = planet.compute()
        const = ephem.constellation(planet)
        update.message.reply_text(const)
    elif user_text[1].capitalize() == Planets[1]:
        planet = ephem.Jupiter()
        pl = planet.compute()
        const = ephem.constellation(planet)
        update.message.reply_text(const)
    elif user_text[1].capitalize() == Planets[2]:
        planet = ephem.Saturn()
        pl = planet.compute()
        const = ephem.constellation(planet)
        update.message.reply_text(const)
    elif user_text[1].capitalize() == Planets[3]:
        planet = ephem.Uranus()
        pl = planet.compute()
        const = ephem.constellation(planet)
        update.message.reply_text(const)
    else:
        update.message.reply_text("Неверное название планеты! Выберите одну из следующих: {}".format(Planets))

def main():
    mybot = Updater("837091703:AAG6jwMqsXfPetSbs9C0jvrTit_AUWOdvlA")
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_state))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
