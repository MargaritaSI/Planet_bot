import logging # для отображения ошибок модуль логирования
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters  #компонент отвечающий за коммуникацию с сервером Telegram
# + импортируем обработчик команд(под разные задачи)

import settings  # импорт скрытых данных

logging.basicConfig(filename='bot.log', level=logging.INFO)  # для создания файла с ошибками - файл и уровень важности

PROXY = {'proxy_url': settings.PROXY_URL,     #  Настройки прокси-сервера - все запросы
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}  #бот будет переадресовывать через этот сервер с этими запросами
def greet_user(update, context): #CommandHandler вызывает greet_user и переадает 2 арг.-update- то что пришло от телеграм
# (старт, инфа от польз-ля), context(можем изнутри функции отдавать команды боту -отправить из функц сообщение
# др ползователю
    print('Вызван /start')
    #print(update)
    #print(1/0)
    update.message.reply_text('Hi, user!')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():  # Создаем бота и передаем ему ключ для авторизации на серверах Telegram #use_context еще нужен? + прокси
    mybot = Updater(
        settings.API_KEY,
        use_context=True,
        #request_kwargs=PROXY,
        )

    dp = mybot.dispatcher # mybot has an attribut dispatcher
    dp.add_handler(CommandHandler('start', greet_user))  # добавляю/регистрирую у диспетчера обработчик который
    # будет реагировать на команду start и вызывать функцию приветсвие
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # реаг тол на текстовые сообщения(Filters) функ-ей talk_to_me

    logging.info('Bot have been started') # логируем в файл инфо о старте бота
    mybot.start_polling()  # Командуем боту начать ходить в Telegram за сообщениями (регулярные частные обращения)
    mybot.idle()  # Запускаем бота, он будет работать, пока мы его не остановим принудительно =бесконечный цикл

if __name__ == '__main__':
    main() #бот стучится на сервер- Ctrl+C остановить бота


