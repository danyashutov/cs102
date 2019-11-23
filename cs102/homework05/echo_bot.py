import telebot

bot = telebot.TeleBot('996342875:AAGyJy_oiJe-DQuAeFADFOFIL_FVCw_9yG0')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
