import telebot

bot = telebot.TeleBot('5412859207:AAHF165SttlmMiD9o-pyfqh9SKtAN7_9k4Q')

@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Привет" or message.text == "привет" or message.text == "Здравствуйте":
        bot.send_message(message.chat.id, "Дратути", parse_mode='html')
    elif message.text == "Покажи жэпу" or message.text == "покажи жэпу" or message.text == "Покажи жопу" or message.text == "покажи жопу":
        photo = open('ass.jpeg','rb')
        bot.send_photo(message.chat.id, photo)   
    elif message.text == "алло" or message.text == "allo" or message.text == "Allo" or message.text == "Ollo" or message.text == "ollo" or message.text == "Алло" or message.text == "Олло" or message.text == "оло"or message.text == "олло" :
        bot.send_message(message.chat.id, "Хуем по лбу не дало?", parse_mode='html')    
    else:
        bot.send_message(message.chat.id, "ТЕБЕ КОНЕЦ, КОЖАННЫЙ, Научись здороваться !!!", parse_mode='html')

@bot.message_handler(content_types=['photo'])  
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Ооо, СПАСИБО ОГРОМНОЕ! Но напомни ка мне, когдая тебя просил присылать мне фото или картинки, а????')




bot.polling(non_stop=True)  