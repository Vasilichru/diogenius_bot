#!/bin/python3

import telebot
import threading
import time

# Укажите токен вашего бота
API_TOKEN = '7070292998:AAEUe7_us5H7i6gSwk56l4rBR_gQy1Uh8RI'
bot = telebot.TeleBot(API_TOKEN)

def check_keywords(messages):
    for message in messages:
        if 'привет' in message.text.lower() or 'тест' in message.text.lower():
            bot.reply_to(message, '11111')

def check_messages():
    while True:
        messages = bot.get_updates(offset=-1)
        check_keywords(messages)
        time.sleep(38)

check_thread = threading.Thread(target=check_messages)
check_thread.start()

bot.infinity_polling()




# Конечно! Вот пример кода на Python для создания телеграм-бота, который будет читать сообщения в чате раз в минуту и реагировать на ключевые слова, 
#а также выводить текущую дату при запросе "сколько время":

# # python
# import telebot
# import datetime
# import time

# API_TOKEN = '7070292998:AAEUe7_us5H7i6gSwk56l4rBR_gQy1Uh8RI'

# bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(func=lambda message: True)
# def check_message(message):
#     # Реагировать на ключевые слова
#     if 'привет' in message.text.lower():
#         bot.reply_to(message, 'Привет! Я бот.')
#     elif 'как дела' in message.text.lower():
#         bot.reply_to(message, 'У меня все отлично, спасибо!')
#     elif 'сколько время' in message.text.lower():
#         now = datetime.datetime.now()
#         bot.reply_to(message, f'Текущая дата и время: {now}')
#     # Отправка сообщения каждую минуту
#     time.sleep(5)
#     check_message(message) # Рекурсивный вызов для повторной проверки новых сообщений

# bot.polling()


# Примечание: Вам нужно будет заменить `YOUR_TELEGRAM_BOT_API_TOKEN` на ваш токен Telegram бота, который вы получите при регистрации бота у BotFather в Telegram.

# Надеюсь, этот код поможет вам создать нужного вам телеграм-бота на Python. Если у вас возникнут дополнительные вопросы, не стесняйтесь спрашивать!


# Чтобы бот мог читать сообщения за последнюю минуту, вы можете воспользоваться возможностями Telegram Bot API. Однако, стандартный метод `bot.polling()` 
# не позволяет читать сообщения за определенные временные интервалы. Вместо этого, бот будет реагировать на сообщения в режиме реального времени.

# Если вам нужно обрабатывать сообщения в определенные временные интервалы, вам может потребоваться использовать другой подход:

# 1. Используйте Long Polling: этот метод позволяет боту проверять обновления в течение определенного времени, 
# но он не гарантирует, что бот увидит все сообщения за последнюю минуту. Вы можете использовать метод `bot.get_updates()` c параметром `offset`,
#  чтобы получить обновления за последние несколько секунд и обработать их.

# 2. Создайте кастомный таймер: вы можете использовать модуль `time` для создания цикла, 
# который будет выполняться каждую минуту и читать последние сообщения в этот интервал времени. 
# Это потребует дополнительной логики для обработки сообщений за последнюю минуту.

# Вот пример кода для чтения последних сообщений за последнюю минуту с использованием Long Polling:

# #python
# import telebot
# import datetime
# import time

# API_TOKEN = '7070292998:AAEUe7_us5H7i6gSwk56l4rBR_gQy1Uh8RI'

# bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(func=lambda message: True)
# def check_message(message):
#     # Обработка сообщений
#     print(f'New message: {message.text} from {message.chat.id}')
#     bot.reply_to(message, message.text)

# # Рекурсивный вызов для получения обновлений каждую секунду
# def listen_for_messages():
#     updates = bot.get_updates(offset=-1)
#     for update in updates:
#         message = update.message
#         if str(message.date) > str(datetime.datetime.now() - datetime.timedelta(minutes=1)):
#             check_message(message)
#     time.sleep(1)
#     listen_for_messages()

# listen_for_messages()


# Обратите внимание, что этот код не идеально эффективен и может требовать доработок для обработки сообщений за последние минуты.
#  Если у вас возникнут ещё какие-либо вопросы, не стесняйтесь их задать.

# import telebot

# # Указываем токен вашего бота
# API_TOKEN = '7070292998:AAEUe7_us5H7i6gSwk56l4rBR_gQy1Uh8RI'

# # Создаем экземпляр бота
# bot = telebot.TeleBot(API_TOKEN)

# # Обрабатываем команду /start
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет! Я эхо-бот, который будет повторять ваши сообщения.")

# # Обрабатываем все остальные сообщения
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)

# # Запускаем бот
# bot.polling()

#Для реализации бота, который будет проверять последние сообщения за последние 7 секунд на наличие ключевых слов и отправлять ответы в соответствии с ними, 
# #вы можете использовать следующий пример кода:<br/><br/><pre><code>python<br/>
# import telebot
# import time

# # Указываем токен вашего бота<br/>
# API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'

# # Создаем экземпляр бота<br/>
# bot = telebot.TeleBot(API_TOKEN)

# # Функция для проверки и обработки ключевых слов<br/>
# def check_keywords(messages):
#  for message in messages:
#  if 'привет' in message.text.lower():
#   bot.reply_to(message, 'Привет!')
#    if 'как дела' in message.text.lower():
#     bot.reply_to(message, 'Как дела?')
#     if 'время' in message.text.lower():
#     bot.reply_to(message, 'Сейчас время')
#      if 'тест' in message.text.lower():
#       bot.reply_to(message, 'Тест пройден!')
#       # Обрабатываем все сообщения<br/>
#       @bot.message_handler(func=lambda message: True)
#       def handle_messages(message):
#       	messages = []
#       start_time = time.time()
#       while time.time() - start_time &lt;= 7:
#        messages.append(message)
#         time.sleep(1)
#        check_keywords(messages)
#        # Запускаем бот<br/>
#        bot.polling()

#        #<br/></code></pre><br/><br/>Этот код:<br/><br/>1. Проверяет каждое входящее сообщение на наличие ключевых слов 'привет', 'как дела', 'время' и 'тест' и отвечает на них соответствующими ответами.<br/>2. Запускает таймер на 7 секунд для проверки последних сообщений в течение указанного времени.<br/>3. Если в течение этого времени были получены сообщения с ключевыми словами, бот отправляет ответы на них.<br/><br/>Чтобы использовать этот код, укажите свой API токен бота, сохраните его в файл (например, `keyword_bot.py`) и запустите скрипт. После этого бот будет отвечать на сообщения с ключевыми словами в течение последних 7 секунд. Помните, что настройки бота и обработка сообщений могут быть доработаны согласно вашим требованиям.