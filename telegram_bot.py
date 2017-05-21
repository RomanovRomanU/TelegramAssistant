import telebot
from constants import bot_token, help_string, error_string
from data_scraping import find_tickets
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['help', 'start'])
def handle_command(command):
    bot.send_message(command.chat.id, help_string)


@bot.message_handler(content_types=['text'])
def handle_text(message): 
    station_from, station_till, date = message.text.split(',')
    print(station_from,station_till,date)
    search_result = find_tickets(station_from, station_till, date)
    for result in search_result:
        anwser = ''
        anwser+= 'Номер поезда: '+result['train_number']+'\n'
        anwser += result['date'].split('Прибытие')[0] + '\n'
        anwser += 'Прибытие' + result['date'].split('Прибытие')[1] + '\n'
        anwser += 'Время пребывания: ' + result['duration'] + '\n'
        anwser += 'Места:\n'
        for place in result['places'].split('Выбрать')[:-1]:
            anwser += place.strip() + '\n'
        bot.send_message(message.chat.id, anwser)



# Имя чата message.chat.id

bot.polling(timeout=20)
