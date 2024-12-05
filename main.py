import telebot
from telebot import types
from deep_translator import GoogleTranslator
from Loat_token import loat_token




def main():

    bot = telebot.TeleBot(loat_token())
    target_language = 'en'

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(
            message.chat.id,
            "Привіт! Я бот-перекладач. Надішліть мені текст, і я перекладу його англійською мовою. "
            "Щоб змінити мову перекладу, скористайтеся командою /language."
        )

    @bot.message_handler(commands=['language'])
    def choose_language(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add("Англійська (en)", "Німецька (de)", "Французька (fr)", "Іспанська (es)")
        bot.send_message(message.chat.id, "Оберіть мову для перекладу:", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text in ["Англійська (en)", "Німецька (de)", "Французька (fr)", "Іспанська (es)"])
    def set_language(message):
        global target_language
        language_codes = {
            "Англійська (en)": "en",
            "Німецька (de)": "de",
            "Французька (fr)": "fr",
            "Іспанська (es)": "es"
        }
        target_language = language_codes[message.text]
        bot.send_message(message.chat.id, f"Мову перекладу змінено на {message.text.split(' ')[0]}.")

    @bot.message_handler(content_types=['text'])
    def translate_message(message):
        try:
            translated_text = GoogleTranslator(source='auto', target=target_language).translate(message.text)
            bot.send_message(message.chat.id, f"Переклад: {translated_text}")
        except Exception as e:
            bot.send_message(message.chat.id, "Вибачте, сталася помилка при перекладі. 😔")
            print(f"Помилка: {e}")

    print("Бот працює...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()