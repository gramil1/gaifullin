import random, string, telebot, os
from telebot import types 
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


def generate_password(length=12):
    """Генерирует безопасный пароль."""
    # Используем более широкий набор символов
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@bot.message_handler(commands=['password'])
def generate_password_command(message):
    """Обработчик команды /password."""
    try:
        length = int(message.text.split()[1])  #  Попытка получить длину из аргументов
        if length <= 0:
           raise ValueError("Длина пароля должна быть положительным числом")
        password = generate_password(length)
        bot.reply_to(message, f"Ваш безопасный пароль: {password}")
    except (ValueError, IndexError):
      bot.reply_to(message, "Ошибка! Используйте команду в формате /password <длина пароля>\nНапример: `/password 16` для пароля длиной 16 символов")



# Запускаем бота
bot.polling(none_stop=True)
