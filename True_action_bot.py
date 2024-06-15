import telebot
from telebot import types
import datetime
import random

API_TOKEN = "MYAPI"
bot = telebot.TeleBot(API_TOKEN)

true = ['Как часто ты унижаешь старших?', 'Есть ли у тебя какие-то страхи или фобии?', 'Как ты представляешь идеальный день?', 'Где бы ты спрятал контрабандные талоны на бензин?',  'Сколько бы людей ты довел до истерики, если бы не было последствий?', 'Как бы ты отпраздновал полное восстановление человека после болезни туберкулезом?', 'Что бы ты делал, если бы перед тобой стоял твой воображаемый друг вместе с бочкой нитроглицерина?', 'У тебя есть тайные фанаты?', 'Ты бы съел торт с кусочками апельсина?', 'Если бы тебе дали возможность отправиться в прошлое, какой период ты бы выбрал(а) и почему?']
action = ['Напиши игру пинг-понг', 'Разукрась обои в своей комнате', 'Удали все игры с компьютера', 'Спроси у своей учительницы, выполнила ли она домашнее заданее от Тайлера',  'Сбрей 90% волос на теле', 'Сделай себе прическу "кроп"', 'Помой рот с мылом', 'Выпей чай с солью', 'Напиши друзьям (братве), что ограбил магазин, попроси укрыться у них', 'Постирай носки вручную']

@bot.message_handler(func=lambda message: True)
def log_message(message):
    print(
        f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
        f"новое сообщение от: {message.chat.last_name} {message.chat.first_name} aka @{message.chat.username},"
        f"текст: {message.text}"
    )
    return telebot.ContinueHandling()

@bot.message_handler(commands=['start'])
def send_question(message):
    bot.send_message(message.chat.id, f"{message.chat.username}, правда(/true) или действие(/action)?")

@bot.message_handler(commands=["true"])
def send_question_t(message):
    bot.reply_to(message, get_question_t())
    bot.send_message(message.chat.id, f"{message.chat.username}, правда(/true) или действие(/action)?")
def get_question_t():
    index = random.randint(0, len(true)-1)
    random_true = true[index]
    return random_true

@bot.message_handler(commands=["action"])
def send_question_a(message):
    bot.reply_to(message, get_question_a())
    bot.send_message(message.chat.id, f"{message.chat.username}, правда(/true) или действие(/action)?")
def get_question_a():
    index = random.randint(0, len(action)-1)
    random_action = action[index]
    return random_action

print("Игра началась!")
bot.infinity_polling()
