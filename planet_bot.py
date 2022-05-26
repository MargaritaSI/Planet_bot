import logging  # для отображения ошибок модуль логирования
import ephem
import datetime
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)  # компонент отвечающий за коммун-ию с сервером Telegram импорт обработчик команд(под разные задачи)

import settings  #  импорт скрытых данных

logging.basicConfig(
    filename="bot.log", level=logging.INFO
)  # для создания файла с ошибками - файл и уровень важности

def greet_user(update, context):  # CommandHandler вызыв greet_user и переадает 2 арг.-update- то что пришло от телеграм
    # (старт, инфа от польз-ля), context(можем изнутри функции отдавать команды боту -отпр из функц сообщение др полз
    print("Called /start")
    update.message.reply_text(
        'Hi, user! Write Planet name in format: "/planet PlanetName"'
    )

def call_constellation(update, context):
    print("Called /planet") # не печатает нигде
    user_planet = update.message.text
    # try:  #тест работает ли функция с возвращением созвездия через команду /Planet - не работает

    intro, planet = user_planet.lower().split(maxsplit=2)

    pl_dic = {
        'Sun': ephem.Sun,
        'Mars': ephem.Mars,
        'Moon': ephem.Moon,
        'Mercury': ephem.Mercury,
        'Venus': ephem.Venus,
        'Jupiter': ephem.Jupiter,
        'Saturn': ephem.Saturn,
         'Uranus': ephem.Uranus,
         'Neptune': ephem.Neptune,
         'Pluto': ephem.Pluto,
    }

    planet = planet.capitalize()
    data_pl = datetime.date.today()
    print(data_pl)
    if planet in pl_dic:
        result_planet = pl_dic[planet](data_pl)
    const = ephem.constellation(result_planet)  # созвездие где будет находится марс в дату
    update.message.reply_text(f'Planet {planet} {data_pl} in the constellation: {const[1]}')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f'do you want speak about {user_text}?')


def main():  # Создаем бота и передаем ему ключ для авторизации на серверах Telegram #use_context еще нужен? + прокси
    mybot = Updater(
        settings.API_KEY,
        use_context=True,
    )
    dp = mybot.dispatcher  # mybot has an attribut dispatcher
    dp.add_handler(
        CommandHandler("start", greet_user)
    )  # добавляю/регистрирую у диспетчера обработчик реагирует на команду start и выз функцию приветсвие

    dp.add_handler(CommandHandler("planet", call_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # реаг тол на текст сообщ (Filters) функ-ей talk_to_me

    logging.info("Bot have been started")  # логируем в файл инфо о старте бота
    mybot.start_polling()  # Командуем боту начать ходить в Telegram за сообщениями (регулярные частные обращения)
    mybot.idle()  # Запускаем бота, он будет работать, пока мы его не остановим принудительно =бесконечный цикл


if __name__ == "__main__":
    main()  # бот стучится на сервер- Ctrl+C остановить бота
