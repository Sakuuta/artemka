import telebot
from telebot import types

bot = telebot.TeleBot("5869034757:AAEipkU0OojRHC8WXP4iwrK0Nxhva3ES7iQ")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'helo, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "hi":
        bot.send_message(message.chat.id, "и тебе привет", parse_mode='html')
    elif message.text == "Hi":
        bot.send_message(message.chat.id, "и тебе привет", parse_mode='html')
    elif message.text == "шутка":
        bot.send_message(message.chat.id, "women,hahahahah", parse_mode='html')
    elif message.text == "id":
        bot.send_message(
            message.chat.id, f"Твой ID:{message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open("mia.jpeg", 'rb')
        bot.send_photo(message.chat.id)


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "вау какое крутое фото")


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        "Посетить веб сайт", url="https://vk.com"))
    bot.send_message(message.chat.id, "летс гоу на ютуб", reply_markup=markup)


bot.polling(none_stop=True)
