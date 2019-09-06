#This script is independet of lib or python version (tested on python 2.7 and 3.5)

import telegram
#token that can be generated talking with @BotFather on telegram
my_token = '633408515:AAHD8n5DevpI7pzofUPSccqCxwid3oFkKr'
chat_id = '-3200350938'
def send(msg, chat_id=chat_id, token=my_token):
	"""
	Send a mensage to a telegram user specified on chatId
	chat_id must be a number!
	"""
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)
	print('message sent.')

#send('Om')
