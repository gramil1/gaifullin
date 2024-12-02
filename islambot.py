import telebot, os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я спортивный бот. Могу предоставить информацию о спорте. Напишите /help для списка доступных команд.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = (
        'Доступные команды:\n'
        '/start - Приветственное сообщение\n'
        '/help - Список команд\n'
        '/sportnews - Свежие новости спорта\n'
        '/records - Новые рекорды\n' 
    )
    await update.message.reply_text(help_message)

async def sport_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Здесь мы можем добавить функционал для получения свежих новостей спорта
    news = 'Последние спортивные новости: \nМатч завершился победой \nhttps://www.sports.ru/'
    await update.message.reply_text(news)
async def records(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news = 'Новые рекорды: \nНовые рекорд установлен \nhttps://reestrrekordov.ru/kak-pravilno-govorit-ustanavlivaem-ili-stavim-rekord/ '
    await update.message.reply_text(news)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TOKEN')).build()
    
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)
    sport_news_handler = CommandHandler('sportnews', sport_news)
    records_news_handler = CommandHandler('records',records)
    
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(sport_news_handler)
    application.add_handler(records_news_handler)
    
    print('Бот запущен...')
    application.run_polling()
