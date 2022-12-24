import telebot


bot = telebot.TeleBot("5888397915:AAFE6Y3eScQGDbeU4WLlT8z31wnSpkjFik8")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "На столе лежит 117 конфет.\n" + 
                "Играют два игрока делая ход друг после друга.\n" +
                "За один ход можно забрать не более чем 28 конфет.\n"+
                "Все конфеты оппонента достаются сделавшему последний ход.")




bot.infinity_polling()