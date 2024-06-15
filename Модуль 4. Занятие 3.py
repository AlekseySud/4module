import telebot
from telebot import types
import datetime
import random

API_TOKEN = "MYAPI"
bot = telebot.TeleBot(API_TOKEN)

greetings = {"ПРИВЕТ", "ЗДРАВСТВУЙ", "ДОБРЫЙ ДЕНЬ"}
new_words = [
    "Селфи - это Слово происходит от английского возвратного суффикса -self, означающего отношение к себе и аналогичного русскому суффиксу «-сь» в словах: «моюсь», «возвращаюсь» и других. Они, в свою очередь, ни что иное, как сокращение от слова «себя», то есть «мою себя», «возвращаю себя» и так далее.",
    "Репост - Одна из функций абсолютно всех соцсетей — это возможность делать репосты сообщений, то есть размещать чужой пост (публикацию, сообщение) на своей странице, разумеется, со ссылкой на источник, которая прописывается автоматически, либо прислать ссылку на чужой пост адресно кому-то из своих подписчиков"
]
hobbys = ["Внештатный журналист или блогер (ведение своего блога)", "Домашнее рукоделие (можно продавать в интернете или на ярмарках)", "Украшение и изготовление тортов на заказ Распродажи и аукционы", "Фотографирование (свадьба, дети, фриланс)", "Плотницкие работы", "Графический дизайн", "Создание видео и выкладывание на ютуб (с монетизацией)"]
usefuls = ["Развеселите другого", "Пропустите или помогите кому-то в очереди", "Поделитесь с соседями","Поговорите с одиноким человеком на вечеринке","Скажите человеку на улице о потере вещи","Откажитесь от пакета и пластикового стакана","Помогите что-либо донести","Напишите тому, кому давно хотели","Угостите кого-нибудь","Сделайте комплимент незнакомцу"]
ideas = ["Защитный чехол для пилы.","Простой нож для отрыва наждачной бумаги.","Резьбовое соединение в пластиковой трубе.","Лёгкий способ стравить воздух с радиатора отопления.","Железный карандаш.","Цепь из пластиковой трубы.","Плетение металлической сетки.","Крепление для горячего клея.","Способ подбить ламинатную доску, не разбирая весь пол."]

@bot.message_handler(func=lambda message: True)
def log_message(message):
    print(
        f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
        f"новое сообщение от: {message.chat.last_name} {message.chat.first_name} aka @{message.chat.username},"
        f"текст: {message.text}"
    )
    return telebot.ContinueHandling()


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Добро пожаловать в бота, {message.chat.username}!")


# Обрабатывает приветствие пользователя
@bot.message_handler(func=lambda message: greetings.issuperset({message.text.upper()}))
def send_greetings(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}!")


# Отвечает на запрос про значение случайного слова
@bot.message_handler(commands=["new_word"])
def send_new_word(message):
    bot.reply_to(message, get_new_word())

@bot.message_handler(commands=["new_hobby"])
def send_new_hobby(message):
    bot.reply_to(message, get_new_hobby())
def get_new_hobby():
    index = random.randint(0, len(hobbys)-1)
    random_hobby = hobbys[index]
    return random_hobby

@bot.message_handler(commands=["new_usefulThing"])
def send_new_usefulThing(message):
    bot.reply_to(message, get_new_usefulThing())
def get_new_usefulThing():
    index = random.randint(0, len(usefuls)-1)
    random_useful = usefuls[index]
    return random_useful

@bot.message_handler(commands=["new_handmadeIdea"])
def send_new_handmadeIdea(message):
    bot.reply_to(message, get_new_handmadeIdea())
def get_new_handmadeIdea():
    index = random.randint(0, len(ideas)-1)
    random_idea = ideas[index]
    return random_idea


def get_new_word():
    index = random.randint(0, len(new_words) - 1)
    random_word = new_words[index]
    return random_word


print("Бот запущен!")
bot.infinity_polling()
