import telebot
from keep_alive import keep_alive

keep_alive()

# Замените на ваш токен
TOKEN = '7518212120:AAEL2Bqji3U2GQJTk6iLFeFPV_fs_oX7Jps'
# Замените на ID администратора (можно получить, написав /start админу)
ADMIN_ID = '7888746600'

bot = telebot.TeleBot(TOKEN)

# Словарь для хранения сообщений от пользователей
user_messages = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Что-бы выложить свой товар / услугу в наш канал напиши здесь. Укажи: свой username (@username), название товара / услуги, цену, немного описания и можешь прикрепить от 1 до 3-х фото. \n\nПри публикации мы укажем твои контакты.\n\nТелеграм канал: @bestshop_russ\n\nСписок всех команд: /commands")

@bot.message_handler(commands=['commands'])
def send_welcome(message):
    bot.reply_to(message, "/rules - список всех правил публикации.\n\n/help - помощь в публикации\n\n/listadm - список администрации.")
    
@bot.message_handler(commands=['rules'])
def send_rules(message):
    rules_text = "Правила публикации:\n\n1) в вашем объявлении не должно быть матов, оскорблений, рекламы.\n\n2) фотографии не должны содержать порнографию или злобный характер.\n\n3) объявления с рекламой не принимаются."
    bot.reply_to(message, rules_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Для публикации вашего объявления нужно:\n\n1) фотографии. До 3-х штук.\n\n2) минимальное описание до 5 предложений.\n\n3) наименование."
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['listadm'])
def list_admins(message):
    admin_list = "Главный администратор который смотрит ваши объявления - @mainadminnn."  # Замените на имя пользователя администратора
    bot.reply_to(message, admin_list)

@bot.message_handler(func=lambda message: True)
def forward_message_to_admin(message):
    # Пересылаем все сообщения от пользователей админу
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)


bot.polling(none_stop=True)