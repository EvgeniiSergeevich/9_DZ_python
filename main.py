import telebot
import model

bot = telebot.TeleBot("5888397915:AAFE6Y3eScQGDbeU4WLlT8z31wnSpkjFik8")


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "На столе лежит 117 конфет.\n" + 
                "Играют два игрока делая ход друг после друга.\n" +
                "За один ход можно забрать не более чем 28 конфет.\n"+
                "Все конфеты оппонента достаются сделавшему последний ход.\n" +
                "Для запуска напишите /start")


@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, 'На столе 117 конфет. Сколько конфет забираете?')
    
    bot.register_next_step_handler(message, process_digit_step)


def process_digit_step(message):
    digit = message.text
    if not digit.isdigit():
        msg = bot.reply_to(message, 'Вы ввели не цифры, введите пожалуйста цифры')
        return
    
    bot.send_message(message.chat.id, model.user_logic(message.text))
    bot.send_message(message.chat.id, model.won())
    if model.candies == 0:
        exit()
    bot.send_message(message.chat.id, model.bot_logic())
    bot.send_message(message.chat.id, model.won())
    if model.candies == 0:
        exit()
    bot.register_next_step_handler(message, process_digit_step)

@bot.message_handler(content_types = 'text')
def game(message):
    
    bot.register_next_step_handler(message, process_digit_step)
        

bot.infinity_polling()

# candies = model.candies
# while candies > 0:
#     print(model.user_logic(input(' ')))
#     print(model.won())
#     if model.candies == 0:
#         exit()
#     print(model.bot_logic())
#     print(model.won())
#     if model.candies == 0:
#         exit()