import csv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Завантаження перекладів із datatranslate.csv
def load_translations():
    """Завантажує переклади з datatranslate.csv у вигляді словника."""
    translations = {}
    file_name = 'templates/datatranslate.csv'  # Назва файлу з перекладами
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row['key'].strip().lower()
                translations[key] = {'uk': row['uk'].strip(), 'eng': row['eng'].strip()}
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено. Переконайтеся, що файл знаходиться у тій самій папці, що й скрипт.")
    except KeyError:
        print(f"Файл '{file_name}' має неправильний формат. Переконайтеся, що стовпці мають заголовки: key, uk, eng.")
    return translations

# Глобальний словник перекладів
TRANSLATIONS = load_translations()

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Привіт! Я бот-перекладач. Надішли слово, і я перекладу його з англійської на українську або навпаки."
    )

# Обробка текстових повідомлень
def translate(update: Update, context: CallbackContext) -> None:
    text = update.message.text.strip().lower()
    
    # Перевірка слова в словнику
    if text in TRANSLATIONS:
        uk_translation = TRANSLATIONS[text]['uk']
        eng_translation = TRANSLATIONS[text]['eng']
        response = f"Переклад:\nУкраїнською: {uk_translation}\nАнглійською: {eng_translation}"
    else:
        response = "Вибач, я не знаю цього слова. Спробуй інше."
    
    update.message.reply_text(response)

# Основна функція запуску бота
def main():
    # Замініть <YOUR_TOKEN> на токен вашого бота
    updater = Updater("7724574503:AAERQ3KHEhvLZq4n2jDlMpMfk3WPL8HG7nE")

    dispatcher = updater.dispatcher

    # Команда /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Обробка повідомлень
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
